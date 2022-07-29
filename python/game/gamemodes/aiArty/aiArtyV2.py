#aiArty.py v2.0 (for conquest) beta
#By worldlife

import host
import bf2
import log
import math, random, types

from ArtyManager import ArtyManager
from SatManager import SatManager
from PlayerTracker import PlayerTracker
from AirdropManager import AirdropManager
from timer import timer
from artySettings import g_debug
from artySettings import *#G_ARTY_SETTINGS, G_SAT_SETTINGS, G_AI_SETTINGS
from exceptionoutput import *

#global
aiCommander = None

def init(enableCPArtyEvent=True):
	#host.registerGameStatusHandler(gameStatusChanged)
	#global g_debug
	#g_debug = 1
	if g_debug: 
		log.init()
		print "aiArtyV2.py initialized"
	global aiCommander
	if not aiCommander:
		aiCommander = AiCommander(G_AI_SETTINGS, G_ARTY_SETTINGS, G_SAT_SETTINGS, G_AIRDROP_SETTINGS, enableCPArtyEvent)
	else:
		aiCommander.enableCPArtyEvent = enableCPArtyEvent

def deinit():
	#host.unregisterGameStatusHandler(gameStatusChanged)
	global aiCommander
	aiCommander.deinit()
	#aiCommander = None
	if g_debug: 
		log.deinit()
		print "aiArtyV2.py deinitialized"

class EventInfo:
	def __init__(self, type, position):
		self.type = type
		self.position = position
		self.time = host.timer_getWallTime()
		
	def __eq__(self, other):
		return self.__class__==other.__class__ and self.type==other.type and abs(self.position[0]-other.position[0])<0.1 and abs(self.position[1]-other.position[1])<0.1 and abs(self.position[2]-other.position[2])<0.1

class ObjectInfo:
	def __init__(self, type, position, objref):
		self.type = type
		self.position = position
		self.objref = objref
		
class AiCommander:
	def __init__(self, aiSettings, artySettings, satSettings, airdropSettings, enableCPArtyEvent=True):
		self.settings = aiSettings
		self.artySettings = artySettings
		self.satSettings = satSettings
		self.airdropSettings = airdropSettings
		self.WEIGHT_KERNEL = (
			aiSettings[OBJECT_ENEMY_IDLE],
			aiSettings[OBJECT_ENEMY_SOLDIER],
			aiSettings[OBJECT_ENEMY_LIGHTARMOUR],
			aiSettings[OBJECT_ENEMY_HEAVYARMOUR],
			aiSettings[OBJECT_ENEMY_UNKNOWN],
			aiSettings[OBJECT_FRIENDLY_SOLDIER],
			aiSettings[OBJECT_FRIENDLY_LIGHTARMOUR],
			aiSettings[OBJECT_FRIENDLY_HEAVYARMOUR],
			aiSettings[OBJECT_FRIENDLY_UNKNOWN],
			aiSettings[EVENT_CPSTATUSCHANGE_NEUTRALIZE][0],
			aiSettings[EVENT_CPSTATUSCHANGE_TOP][0],
			aiSettings[EVENT_C4_OPERATING][0],
			aiSettings[EVENT_C4_PLACED][0],
			aiSettings[EVENT_C4_PLACED_PROTECT][0],
		)
		self.artyManager = None
		self.playerTracker = None
		self.satManager = None
		self.airdropManager = None
		self.team1_hasCommander = False
		self.team2_hasCommander = False
		#self.team1_artyWeightTable = {}#{artillery position : weightList}
		#self.team2_artyWeightTable = {}
		self.team1_eventList = []#{artillery position : weightList}
		self.team2_eventList = []
		self.controlPoints = []
		self.loopTimer = None
		self.isAIGame = host.sgl_getIsAIGame() #or not self.settings["ONLY_IN_AIGAME"] #host.sgl_getIsAIGame() may not be accurate
		self.enableCPArtyEvent = enableCPArtyEvent
		host.registerGameStatusHandler(self.gameStatusChanged)
		if g_debug: 
			print "AiCommander initialized!"
		
	def gameStart(self):
		#self.isLocalGame = self.isLocal()
		if g_debug: log.output("aiArty:gameStart")
		# self.isAIGame = False
		# for player in bf2.playerManager.getPlayers():
			# if g_debug: log.output("player: %s" % player.getName())
			# if player.isAIPlayer():
				# self.isAIGame = True
				# break
		#self.isAIGame = self.isAIGame or not self.settings["ONLY_IN_AIGAME"]
		if not (self.isAIGame or not self.settings["ONLY_IN_AIGAME"]): return
		host.registerHandler('RemoteCommand', self.onRemoteCommand)
		if self.enableCPArtyEvent: host.registerHandler('ControlPointChangedOwner', self.onCPStatusChange)
		self.artyManager = ArtyManager(self.artySettings)
		self.artyManager.disableArty(1)#disable artillery at start
		self.artyManager.disableArty(2)
		self.playerTracker = PlayerTracker()
		self.satManager = SatManager(self.satSettings, self.playerTracker)
		self.airdropManager = AirdropManager(self.airdropSettings)
		self.controlPoints = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
		if not self.loopTimer: 
			self.loopTimer = timer.loop(self.settings["LOOP_INTERVAL"], self.loopScan)
			if g_debug: log.output("AiCommander: loopTimer registered!")
		
	def gameEnd(self):
		if g_debug: log.output("aiArty:gameStart")
		self.artyManager = None
		if self.playerTracker:
			self.playerTracker.deinit()
			self.playerTracker = None
		self.satManager = None
		self.airdropManager = None
		self.team1_eventList = []
		self.team2_eventList = []
		self.controlPoints = []
		if self.loopTimer :
			self.loopTimer.abort()
			self.loopTimer = None
			
	def deinit(self): #python doc discourages using __del__()?
		host.unregisterGameStatusHandler(self.gameStatusChanged)
		if g_debug: 
			print "AiCommander deinitialized!"
	
	def gameStatusChanged(self, status):
		if status == bf2.GameStatus.Playing:
			self.gameStart()				
		elif status == bf2.GameStatus.EndGame:
			self.gameEnd()	
	
	#loopTimer function
	def loopScan(self):
		try:
			if g_debug: log.output("loopScan...")
			self.renewCommanderState()
			#team1
			if not self.team1_hasCommander: 
				pos = self.findPosForArty(1)
				if pos:
					self.artyManager.startArtyAt(1, pos)
			#team2
			if not self.team2_hasCommander: 
				pos = self.findPosForArty(2)
				if pos:
					self.artyManager.startArtyAt(2, pos)
		except:
			ExceptionOutput()
	
	
	#scan all player positions/cp state and find the best place to throw artillery			
	def findPosForArty(self, team):
		if g_debug: log.output("findPosForArty: team%s " % team)
		if not self.artyManager.isAvailable(team): return
		else:
			weightTable = {}#(team==1) and self.team1_artyWeightTable or self.team2_artyWeightTable
			eventList = (team==1) and self.team1_eventList or self.team2_eventList
			objectInfoList = []
			
			#if satellite available, first scan to get enemy positions
			if self.satManager.isAvailable(team):
				lastScanResult = self.satManager.getLastScanResult(team).copy()
				if not self.satManager.startSatScan(team): return
				scanResult = self.satManager.getLastScanResult(team)
				#add idle enemy objects to objectInfoList
				self.getIdleObjectsFromScan(lastScanResult, scanResult, objectInfoList)
				#add enemy objects to objectInfoList/weightTable
				for index in scanResult:
					if scanResult[index][1] > self.settings["VEHICLE_SPEED_THRESHOLD"]:#speed threshold
						continue
					else: 
						#add position to weight table
						weightTable[scanResult[index][0]] = [0] * len(self.WEIGHT_KERNEL) 
						#add object info
						objName = scanResult[index][2].templateName
						vehicleType = OBJECT_ENEMY_UNKNOWN
						if VEHICLETYPE_CONVERT.get(objName):
							dummyType = VEHICLETYPE_CONVERT[objName]
							if dummyType == OBJECT_SKIP: continue
							else: vehicleType = ENEMYTYPE_CONVERT[dummyType]
						objectInfoList.append(ObjectInfo(vehicleType, scanResult[index][0], scanResult[index][2]))
			
			#prepare event position's weight table
			for eventInfo in eventList:
				#add position to weight table
				if g_debug: log.output("event: %s " % eventInfo.type)
				weightTable[eventInfo.position] = [0] * len(self.WEIGHT_KERNEL) 
				#calc event weight
				decay = (host.timer_getWallTime()-eventInfo.time)/self.settings[eventInfo.type][1]
				if g_debug: log.output("event decay: %s " % decay)
				if decay<1: weightTable[eventInfo.position][eventInfo.type] += 1 - decay
			
			#add friendly objects to objectInfoList
			for p in bf2.playerManager.getPlayers():
				if p.getTeam() == team:
					#note that multiple person may occupy the same vehicle -- this counts as multiple vehicles
					v = p.getVehicle()
					if v:
						v = self.getRootParent(v)
						vehicleType = OBJECT_ENEMY_UNKNOWN
						objName = v.templateName
						if VEHICLETYPE_CONVERT.get(objName):
							dummyType = VEHICLETYPE_CONVERT[objName]
							if dummyType == OBJECT_SKIP: continue
							else: vehicleType = FRIENDLYTYPE_CONVERT[dummyType]
						objectInfoList.append(ObjectInfo(vehicleType, v.getPosition(), v))
			
			#calc position weight
			for artyPos in weightTable:
				for objInfo in objectInfoList:
					roughDist = self.getRoughDistance(objInfo.position, artyPos) 
					if roughDist > self.settings["ARTY_ROUGHDIST_THRESHOLD"]:
						continue
					else:
						#calculate distance to cps
						weightModifier = 1
						# find closest CP
						closestCP = None
						closestCPdist = 9999
						for obj in self.controlPoints:
							if obj.cp_getParam('team') != team and obj.cp_getParam('team') != 0: continue #do not count enemy cps
							distanceTo = self.getVectorDistance(objInfo.position, obj.getPosition())
							if closestCP == None or distanceTo < closestCPdist:
								closestCP = obj
								closestCPdist = distanceTo
						if closestCP :
							threshold = float(closestCP.getTemplateProperty('radius')) * self.settings["OBJECT_INCP_DIST_THRESHOLD_RADIUS_MODIFIER"]
							if closestCPdist < threshold:
								weightModifier *= 1 + (self.settings["OBJECT_INCP_WEIGHT_MODIFIER_MAX"]-1) * closestCPdist / threshold
						weightTable[artyPos][objInfo.type] += weightModifier
			if g_debug:
				log.output("weightTable: %s" % weightTable)
			#find artillery position according to weight
			pos = self.findMaxArtyWeightPos(team, weightTable)
			if pos:#ready for artillery, delete previous events
				#clear event list
				#weightTable.clear()
				eventList[:] = []
			#return
			return pos
	
	def getIdleObjectsFromScan(self, prevScan, scan, objectInfoList):
		objPosTable = {}
		for index in scan:
			objPosTable[scan[index][2]] = scan[index][0]
		for index in prevScan:
			if objPosTable.get(prevScan[index][2]):
				pos = objPosTable[prevScan[index][2]]
				if self.getRoughDistance(pos,prevScan[index][0]) < self.settings["OBJECT_IDLE_DIST_THRESHOLD"]:
					objectInfoList.append(ObjectInfo(OBJECT_ENEMY_IDLE, pos, prevScan[index][2]))
	
	def findMaxArtyWeightPos(self, team, weightTable):
		#weightTable = (team==1) and self.team1_artyWeightTable or self.team2_artyWeightTable
		eventList = (team==1) and self.team1_eventList or self.team2_eventList
		maxWeight = 0	
		maxWeightPos = None	
		for pos in weightTable:
			weight = 0
			#position/event weights
			weights = weightTable[pos]
			if len(weights) == len(self.WEIGHT_KERNEL): weight += self.vec_dot_tuple(tuple(weights), self.WEIGHT_KERNEL)
			#random weights
			weight += self.settings["WEIGHT_RANDOM"]*(random.random()-0.5)
			#compare
			if weight > maxWeight:
				maxWeight = weight	
				maxWeightPos = pos
				
		if maxWeight > self.settings["ARTY_WEIGHT_THRESHOLD"] : return maxWeightPos
		else: return None
			
			
	def vec_dot_tuple(self, a, b):
		result = 0
		for x,y in zip(a,b):
			result += x*y
		return result

	def renewCommanderState(self):
		self.team1_hasCommander = (bf2.playerManager.getCommander(1) != None)
		self.team2_hasCommander = (bf2.playerManager.getCommander(2) != None)
	
	def eventNotify(self, team, event, reactOnTime=False):
		if g_debug: log.output("New event %s send to team %s" % (event, team))
		eventList = (team==1) and self.team1_eventList or self.team2_eventList
		eventList.append(event)
		if reactOnTime: self.loopScan()
		
	def eventDelete(self, team, event):
		eventList = (team==1) and self.team1_eventList or self.team2_eventList
		i=0
		while i<len(eventList):
			if event==eventList[i]:
				eventList.remove(eventList[i])
			else:
				i+=1
		#self.loopScan()
	
	#rcon commands
	def onRemoteCommand(self, playerid_or_socket, cmd):
		cmd = cmd.strip()
		if g_debug: log.output("Player %s Sending rcon command: %s" % (playerid_or_socket, cmd))

		# Is this a non-interactive client?
		if len(cmd) > 0 and cmd[0] == '\x02':
			cmd = cmd[1:]
			#interactive = False

		spacepos = cmd.find(' ')
		if spacepos == -1: spacepos=len(cmd)
		subcmd = cmd[0:spacepos]

		if type(playerid_or_socket) == types.IntType:
			playerid = playerid_or_socket
			#from sandbox
			if playerid == -1: #fix for local servers
				playerid = 255
		else:
			#socket = playerid_or_socket
			return
		
		player = bf2.playerManager.getPlayerByIndex(playerid)
		if (subcmd == "supplydrop"):
			soldier = player.getDefaultVehicle()
			if (soldier): self.airdropManager.startSupplydrop(player.getTeam(), soldier.getPosition())
		elif (subcmd == "vehicledrop"):
			soldier = player.getDefaultVehicle()
			if (soldier): self.airdropManager.startVehicledrop(player.getTeam(), soldier.getPosition())
	
	#cp taken, may trigger(for conquest mode)
	#note that this triggers after the cp is taken(different from gpm_cq.py)--------------
	def onCPStatusChange(self, cp, top):
		try:
			if g_debug: log.output("onCPStatusChange: %s %s" % (cp.templateName,top))
			if g_debug: log.output("onCPStatusChange: cp.cp_getParam('team')=%s cp.cp_getParam('flag')=%s" % (cp.cp_getParam('team'),cp.cp_getParam('flag')))
			if cp.cp_getParam('team') != 0:
				#if g_debug: log.output("cp.cp_getParam('team') != 0")
				if top:
					# regained flag, do nothing
					pass			
				else:
					# neutralize
					'''if cp.cp_getParam('team') == 1:
						atkTeam = 2
					else:
						atkTeam = 1	'''
					if g_debug: log.output("neutralize")
					atkTeam = cp.cp_getParam('team')
					'''if atkTeam == 1: hascommander = self.team1_hasCommander
					else: hascommander = self.team2_hasCommander
					if not hascommander and random.random()<self.settings["RANDOM_ARTY"]: 
						if g_debug: log.output("startArty!")
						self.artyManager.startArtyAt(atkTeam, cp.getPosition())#spawnArtyAt(atkTeam, cp.getPosition(), ARTY_BURSTSIZE)'''
					self.eventNotify(atkTeam, EventInfo(EVENT_CPSTATUSCHANGE_NEUTRALIZE, cp.getPosition()))
			else:
				#if g_debug: log.output("cp.cp_getParam('team') == 0")
				if top:
					# capture
					if cp.cp_getParam('flag') == 1:
						atkTeam = 2
					else:
						atkTeam = 1				
					'''if random.random()<self.settings["RANDOM_ARTY"]: 
						if g_debug: log.output("startArty!")
						self.artyManager.startArtyAt(atkTeam, cp.getPosition())#spawnArtyAt(atkTeam, cp.getPosition(), ARTY_BURSTSIZE)'''
					self.eventNotify(atkTeam, EventInfo(EVENT_CPSTATUSCHANGE_TOP, cp.getPosition()))
			if g_debug: log.output("onCPStatusChangeEnd")
		except:
			ExceptionOutput()
		
	# get distance between two positions
	def getVectorDistance(self, pos1, pos2):
		diffVec = [0.0, 0.0, 0.0]
		diffVec[0] = math.fabs(pos1[0] - pos2[0])
		diffVec[1] = math.fabs(pos1[1] - pos2[1])
		diffVec[2] = math.fabs(pos1[2] - pos2[2])
		 
		return math.sqrt(diffVec[0] * diffVec[0] + diffVec[1] * diffVec[1] + diffVec[2] * diffVec[2])
	
	#faster calculation
	def getRoughDistance(self, pos1, pos2):
		return math.fabs(pos1[0] - pos2[0]) + math.fabs(pos1[1] - pos2[1]) + math.fabs(pos1[2] - pos2[2])	
	
	def getRootParent(self, obj):
		parent = obj.getParent()
		
		if parent == None:
			return obj
			
		return self.getRootParent(parent)
	
	def isLocal(self):
		internet = int(host.rcon_invoke("sv.internet"))
		if internet:
			return False
		else:
			return True
