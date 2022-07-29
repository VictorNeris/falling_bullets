# rush v1.1.1 Beta

#This script is modified based on dice's original gpm_cq.py, the conquest mode script. You are free to use it in any mod.
#If you want to modify and release it, just add your name to the MODIFIER_MAP with the version.
#Credits:
#Credit to http://www.bf2tech.org/
#Thanks for the excellent bf2 python docs.I learned a lot!
#Credit to Omnicide_Final
#Thanks for the convenient timer.once class and loop class.It helps a lot!
#Credit to alpha project
#Thanks for the BF2Object.py that helps me to spawn vehicles!

'''
MODIFIER_MAP = {
	"V1.0.0 beta" : "worldlife",
	"V1.1.0 beta" : "worldlife",
	"V1.1.1 beta" : "worldlife",
	#add modifier names to this list
}
'''

TAKEOVERTYPE_CAPTURE = 1
TAKEOVERTYPE_NEUTRALIZE = 2

SCORE_CAPTURE = 2
SCORE_NEUTRALIZE = 2
SCORE_CAPTUREASSIST = 1
SCORE_NEUTRALIZEASSIST = 1
SCORE_DEFEND = 1

#constants
#from BF2Object.py alpha_project
FIND_TARGET_DELAY = 0.2 #time delay between addTargetVehicle() and linkTargetVehicle()
TARGET_SPAWN_HEIGHT = 10000.0 #spawn the targets high up in the air at first
#######
TIME_RETRY = 0.5
C4_PLACE_DELAY = 8
C4_DISARM_DELAY = 8 #currently, those two should be the same
C4_DETONATE_DELAY = 40
TARGETNAME_A = 'target_aircontroltower_mec_sp_A'
TARGETNAME_B = 'target_aircontroltower_mec_sp_B'
C4OBJECTNAME = 'c4_explosives_bigpack_pco2'
#TARGETNAME_A = 'ats_hj8'
#TARGETNAME_B = 'ats_tow'
DUMMYTARGETNAME_A = 'target_aircontroltower_mec_dummyA'#not used yet
DUMMYTARGETNAME_B = 'target_aircontroltower_mec_dummyB'#not used yet
TRIGGER_RADIUS = 5

#rush scores
SCORE_DESTROYTARGET = 30
SCORE_DESTROYFRIENDLYTARGET = -50
SCORE_PLACEC4 = 5
SCORE_DISARMC4 = 20

Top = 0
Middle = 1
Bottom = 2

import host
import bf2
import math
from game.scoringCommon import addScore, RPL
from bf2 import g_debug
from exceptionoutput import *
import logfile
from game.rcons import *
from game.messages import *
settings = [] # currently no use
debugtimer = None
g_controlPoints = [] # cache, as this map won't change

#debug
g_echooutput = 0

class Rush:
	def __init__(self, settings):
		self.gameState = 0#0:pregame,1:ingame,2:notready
		self.targetSequence = []
		self.targetSpawner = []
		self.currentTarget = 1
		self.defenseTeam = 1
		self.attackTeam = 2
		self.Adestroyed = False
		self.Bdestroyed = False
		self.targetCheckTimer = None
	
	#get methods
	def getTargets(self):
		return self.targetSequence
	
	def getDefenseTeam(self):
		return self.defenseTeam
		
	def getAttackTeam(self):
		return self.attackTeam
	
	def getCurrentTarget(self):
		return self.currentTarget
	
	#set methods
	def setGameState(self, state):
		if state >= 0 and state <= 2:	
			self.gameState = state
	
	#judge methods
	def getCurrentTargetsDown(self):
		return self.Adestroyed and self.Bdestroyed
	
	#ingame methods
	def gameSetting(self, cps):
		host.rcon_invoke("run objects/weapons/projectile/c4_explosives_bigpack/" + C4OBJECTNAME +".con")#make sure the name matches
		tmpSequence = []
		#determine defenseTeam
		for obj in cps:
			if obj.cp_getParam('unableToChangeTeam') != 1:
				self.defenseTeam = obj.cp_getParam('team')
				if self.defenseTeam == 1: self.attackTeam = 2
				else: self.attackTeam = 1
		for obj in cps:
			if obj.cp_getParam('team') != self.defenseTeam or obj.cp_getParam('unableToChangeTeam'): continue
			obj.targetVehicle = None #this links to the target VehicleObject
			tmpSequence.append(obj)
		self.targetSequence = tmpSequence[:]
		for obj in tmpSequence:
			#arrange target sequence
			try:
				index = int(obj.cp_getParam('timeToGetControl'))
				if self.targetSequence[index * 2 - 2] != obj:
					if int(self.targetSequence[index * 2 - 2].cp_getParam('timeToGetControl')) != index:
						self.targetSequence[index * 2 - 2] = obj
					else: self.targetSequence[index * 2 - 1] = obj
			except:
				if g_debug: print "index error!Check the map and fix this!"
		#maybe will change data structure later
		if g_debug: 
			print "tmpSequence:"
			for obj in tmpSequence:
				print obj.templateName		
			print "targetSequence:"	
			for obj in self.targetSequence:
				print obj.templateName
		#adjust targetSequence by objectspawners
		objspws = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ObjectSpawner')
		cpnames = []
		for cp in self.targetSequence:
			cpnames.append(cp.templateName)
		for obj in objspws:
			if obj.templateName[-8:] == '_targetA' or obj.templateName[-8:] == '_targetB':
				self.targetSpawner.append(obj)
		for obj in objspws:
			if obj.templateName[-8:] == '_targetA':
				self.addObjectOnTeam(DUMMYTARGETNAME_A, obj.getPosition(), obj.getRotation(), 0)#prevent vehicles disturbing target spawn
				cpname = obj.templateName[:-8]
				i = 0
				try:
					i = cpnames.index(cpname)
				except:
					if g_debug: print "Name error!Check the map and fix this!Current object:" + obj.templateName[:-8]
				if (i/2)*2 != i :
					self.targetSequence[i],	self.targetSequence[i-1] = self.targetSequence[i-1], self.targetSequence[i]#swap a and b
					cpnames[i], cpnames[i-1] = cpnames[i-1], cpnames[i]
					self.targetSpawner[i-1] = obj
				else: self.targetSpawner[i] = obj
			elif obj.templateName[-8:] == '_targetB': 
				self.addObjectOnTeam(DUMMYTARGETNAME_B, obj.getPosition(), obj.getRotation(), 0)#prevent vehicles disturbing target spawn
				cpname = obj.templateName[:-8]
				i = cpnames.index(cpname)
				if (i/2)*2 == i :
					self.targetSequence[i],	self.targetSequence[i+1] = self.targetSequence[i+1], self.targetSequence[i]#swap a and b
					cpnames[i], cpnames[i+1] = cpnames[i+1], cpnames[i]
					self.targetSpawner[i+1] = obj
				else: self.targetSpawner[i] = obj
		self.c4setting()
		#check timer
		#self.targetCheckTimer = loop(1, self.targetCheck)
		if g_debug: 	
			print "targetSequenceAfterAdjust:"	
			for obj in self.targetSequence:
				print obj.templateName
			print "targetSpawner:"
			for obj in self.targetSpawner:
				print obj.templateName
		self.gameState = 2
	
	def c4setting(self):
		host.rcon_invoke('ObjectTemplate.active ' + C4OBJECTNAME)
		hp = float(host.rcon_invoke('ObjectTemplate.armor.hitPoints'))
		host.rcon_invoke('ObjectTemplate.armor.hpLostWhileCriticalDamage %s' % (hp/C4_DETONATE_DELAY))
	
	def getCurrentTargetObjectA(self):
		return self.targetSequence[self.currentTarget*2-2].targetVehicle
	
	def getCurrentTargetObjectB(self):
		return self.targetSequence[self.currentTarget*2-1].targetVehicle
		
	def toNextTarget(self):
		#if g_echooutput: host.rcon_invoke("echo debugtryToNextTarget")
		'''if g_debug: 
			if self.getCurrentTargetObjectA():
				print self.getCurrentTargetObjectA().templateName + " state %s" % self.getCurrentTargetObjectA().getIsWreck()
			if self.getCurrentTargetObjectB():
				print self.getCurrentTargetObjectB().templateName + " state %s" % self.getCurrentTargetObjectB().getIsWreck()'''
		if self.gameState != 1: 
			#timer.once(TIME_RETRY, self.toNextTarget)
			return
		#if (not self.getCurrentTargetObjectA().isValid() or self.getCurrentTargetObjectA().getIsWreck()) and (not self.getCurrentTargetObjectB().isValid() or self.getCurrentTargetObjectB().getIsWreck()):
		if self.targetSequence[self.currentTarget*2-2].cp_getParam('team') == self.getAttackTeam() and self.targetSequence[self.currentTarget*2-1].cp_getParam('team') == self.getAttackTeam():
			host.rcon_invoke("echo debugtoNextTarget")
			if self.currentTarget*2 >= len(self.targetSequence):
				host.rcon_invoke("game.sayAll \"All targets destroyed!Round is ending...\"")
				self.gameState = 2
				bf2.gameLogic.setTickets(self.defenseTeam, 1)#set defenseTeam's ticket to min
				timer.once(3, host.sgl_endGame, self.attackTeam, 3)
			else:
				host.rcon_invoke("game.sayAll \"Current targets down!Moving to next targets!\"")
				for player in bf2.playerManager.getPlayers():
					if player.getTeam() == rushData.getAttackTeam():
						MSG_teammoveon(player)
				self.currentTarget += 1
				#self.addTargetVehicle()
				#need to use linkTargetVehicle() after some time
				self.Adestroyed =False
				self.Bdestroyed =False
				timer.once(FIND_TARGET_DELAY, self.linkTargetVehicle)
		else:
			#timer.once(TIME_RETRY, self.toNextTarget)
			pass
	'''def addTargetVehicle(self):
		#spawnposA = (0.0, TARGET_SPAWN_HEIGHT, 0.0)
		#spawnposB = (0.0, TARGET_SPAWN_HEIGHT/2, 0.0)
		#self.addObjectOnTeam(TARGETNAME_A, spawnposA, (90.0, 0.0, 0.0), 0)
		#self.addObjectOnTeam(TARGETNAME_B, spawnposB, (90.0, 0.0, 0.0), 0)
		spawnposA = self.targetSequence[self.currentTarget*2-2].getPosition()
		spawnposA = (spawnposA[0], spawnposA[1] + 0, spawnposA[2])
		spawnposB = self.targetSequence[self.currentTarget*2-1].getPosition()
		spawnposB = (spawnposB[0], spawnposB[1] + 0, spawnposB[2])
		self.addObjectOnCp(TARGETNAME_A, self.targetSequence[self.currentTarget*2-2], spawnposA, (90.0, 0.0, 0.0))
		self.addObjectOnCp(TARGETNAME_B, self.targetSequence[self.currentTarget*2-1], spawnposB, (90.0, 0.0, 0.0))
		self.gameState = 2'''
		
	def linkTargetVehicle(self):
		host.rcon_invoke("echo debuglinkTargetVehicle")
		pcos = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.PlayerControlObject')
		Afound = False
		Bfound = False
		for obj in pcos:
			if not obj.isValid() or obj.getIsWreck(): continue
			if obj.templateName == TARGETNAME_A:
					obj.c4object = None 
					obj.c4placeplayer = None
					obj.playerEnterAt = 0.0 #sets when player start operate the c4
					obj.occupyingPlayer = None
					obj.destroyed = False #do not work when bugs occurs
					self.targetSequence[self.currentTarget*2-2].targetVehicle = obj
					#obj.setPosition(self.targetSequence[self.currentTarget*2-2].getPosition())
					'''isHemi = int(self.targetSequence[self.currentTarget*2-2].cp_getParam('isHemisphere'))
					if isHemi != 0:
						id = bf2.triggerManager.createHemiSphericalTrigger(obj, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))
					else:
						id = bf2.triggerManager.createRadiusTrigger(obj, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))			'''								
					id = bf2.triggerManager.createHemiSphericalTrigger(obj, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))#ONLY USE HEMI TRIGGER
					obj.triggerId = id
					Afound = True
					host.rcon_invoke("echo debuglinkTargetVehicleA")
			if obj.templateName == TARGETNAME_B:
					obj.c4object = None 
					obj.c4placeplayer = None
					obj.playerEnterAt = 0.0
					obj.occupyingPlayer = None
					obj.destroyed = False #do not work when bugs occurs
					self.targetSequence[self.currentTarget*2-1].targetVehicle = obj
					'''isHemi = int(self.targetSequence[self.currentTarget*2-1].cp_getParam('isHemisphere'))
					if isHemi != 0:
						id = bf2.triggerManager.createHemiSphericalTrigger(obj, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))
					else:
						id = bf2.triggerManager.createRadiusTrigger(obj, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))		'''	
					id = bf2.triggerManager.createHemiSphericalTrigger(obj, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))#ONLY USE HEMI TRIGGER
					obj.triggerId = id
					#obj.setPosition(self.targetSequence[self.currentTarget*2-1].getPosition())
					Bfound = True
					host.rcon_invoke("echo debuglinkTargetVehicleB")
		'''id = bf2.triggerManager.createHemiSphericalTrigger(self.targetSequence[self.currentTarget*2-2].targetVehicle, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))#ONLY USE HEMI TRIGGER
		self.targetSequence[self.currentTarget*2-2].targetVehicle.triggerId = id
		id = bf2.triggerManager.createHemiSphericalTrigger(self.targetSequence[self.currentTarget*2-1].targetVehicle, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))#ONLY USE HEMI TRIGGER
		self.targetSequence[self.currentTarget*2-1].targetVehicle.triggerId = id'''

		#debug
		for obj in self.targetSequence:
			#host.rcon_invoke("echo linkTargetVehicledebugA" + obj.templateName )
			if obj.targetVehicle == None:
				host.rcon_invoke("echo \"DEBUG:No spawning target vehicle on " + obj.templateName + "\"")
			else: host.rcon_invoke("echo \"DEBUG:target vehicle on " + obj.templateName + " is " + obj.targetVehicle.templateName + "\"")
		if g_debug: 
			print "A:" + host.rcon_invoke("Object.listObjectsofTemplate " +TARGETNAME_A)
			print "B:" + host.rcon_invoke("Object.listObjectsofTemplate " +TARGETNAME_B)				
		self.gameState = 1
		#if not (Afound and Bfound): timer.once(TIME_RETRY, self.linkTargetVehicle)
	
	def addC4OnTargetVehicle(self, currentPlayer, targetVehicle):
		if targetVehicle.c4object == None and targetVehicle.occupyingPlayer == currentPlayer and currentPlayer.getTeam() == self.attackTeam and abs(host.timer_getWallTime() - targetVehicle.playerEnterAt - C4_PLACE_DELAY) <=0.1:
			spawnpos = (TARGET_SPAWN_HEIGHT * 0.6, TARGET_SPAWN_HEIGHT * 1.2, TARGET_SPAWN_HEIGHT * 0.6)
			self.addObjectOnTeam(C4OBJECTNAME, spawnpos, (90.0, 0.0, 0.0), 0)
			timer.once(FIND_TARGET_DELAY, self.linkC4ToTargetVehicle, targetVehicle)

	def linkC4ToTargetVehicle(self, targetVehicle):
		host.rcon_invoke("echo debuglinkC4")
		c4found = False
		pcos = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.PlayerControlObject')
		if targetVehicle.c4object != None or not targetVehicle.occupyingPlayer: return
		for obj in pcos:
			if not obj.isValid() or obj.getIsWreck(): continue
			#host.rcon_invoke("echo "+ "%s" % self.getRoughDistance(obj.getPosition(), (0.0, TARGET_SPAWN_HEIGHT * 1.2, 0.0)))
			if obj.templateName == C4OBJECTNAME:# and self.getRoughDistance(obj.getPosition(), (0.0, TARGET_SPAWN_HEIGHT * 1.2, 0.0)) < 1:
				if not hasattr(obj, 'hasLink') or obj.hasLink == False: obj.hasLink = True
				else: continue
				host.rcon_invoke("echo debuglinkC4Success")
				c4found = True
				targetVehicle.c4object = obj				
				targetVehicle.c4placeplayer = targetVehicle.occupyingPlayer
				#player score
				addScore(targetVehicle.c4placeplayer, SCORE_PLACEC4, RPL)
				targetpos = targetVehicle.getPosition()
				c4pos = (targetpos[0] - 0.0, targetpos[1] + 1.64, targetpos[2] + 0.0)
				obj.setPosition(c4pos)
				#timer.once(1, obj.setPosition, c4pos)
				#if g_debug: 
				#	print obj.getPosition()
				host.rcon_invoke("game.sayAll \"Bomb placed on target " + targetVehicle.templateName[-1] + " by player " + targetVehicle.c4placeplayer.getName() + " !\"")
				MSG_bombplace(targetVehicle.c4placeplayer)
				#targetVehicle.occupyingPlayer = None
				#break
		if not c4found: timer.once(TIME_RETRY, self.linkC4ToTargetVehicle, targetVehicle)
	
	def disarmC4OnTargetVehicle(self, currentPlayer, targetVehicle):
		host.rcon_invoke("echo debugdisarmC4")
		if not targetVehicle.destroyed and targetVehicle.occupyingPlayer == currentPlayer and currentPlayer.getTeam() == self.defenseTeam and targetVehicle.c4object != None and abs(host.timer_getWallTime() - targetVehicle.playerEnterAt - C4_DISARM_DELAY) <=0.1:
			host.rcon_invoke("echo debugdisarmC4Success")
			#if hasattr(targetVehicle.c4object, 'hasLink') and targetVehicle.c4object.hasLink == True: targetVehicle.c4object.hasLink = False
			MSG_bombdisarm(currentPlayer)
			targetVehicle.c4object.setPosition((TARGET_SPAWN_HEIGHT * 0.6, TARGET_SPAWN_HEIGHT * 1.5, TARGET_SPAWN_HEIGHT * 0.6))
			targetVehicle.c4object = None
			#player score
			addScore(currentPlayer, SCORE_DISARMC4, RPL)
			host.rcon_invoke("game.sayAll \"Bomb on target " + targetVehicle.templateName[-1] + " disarmed by player" + currentPlayer.getName() + " !\"")
			MSG_placerbombdisarmed(targetVehicle.c4placeplayer)
			#targetVehicle.c4placeplayer = None
			
	#message methods
	def c4PlaceProcess25(self, currentPlayer, targetVehicle):
		if targetVehicle.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetVehicle.playerEnterAt - C4_PLACE_DELAY * 0.25) <= 0.1:
			MSG_c4Process25(currentPlayer)
			
	def c4PlaceProcess50(self, currentPlayer, targetVehicle):
		if targetVehicle.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetVehicle.playerEnterAt - C4_PLACE_DELAY * 0.5) <= 0.1:
			MSG_c4Process50(currentPlayer)
			
	def c4PlaceProcess75(self, currentPlayer, targetVehicle):
		if targetVehicle.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetVehicle.playerEnterAt - C4_PLACE_DELAY * 0.75) <= 0.1:
			MSG_c4Process75(currentPlayer)
			
	def c4DisarmProcess25(self, currentPlayer, targetVehicle):
		if targetVehicle.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetVehicle.playerEnterAt - C4_DISARM_DELAY * 0.25) <= 0.1:
			MSG_c4Process25(currentPlayer)
			
	def c4DisarmProcess50(self, currentPlayer, targetVehicle):
		if targetVehicle.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetVehicle.playerEnterAt - C4_DISARM_DELAY * 0.5) <= 0.1:
			MSG_c4Process50(currentPlayer)
			
	def c4DisarmProcess75(self, currentPlayer, targetVehicle):
		if targetVehicle.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetVehicle.playerEnterAt - C4_DISARM_DELAY * 0.75) <= 0.1:
			MSG_c4Process75(currentPlayer)
			
	#assist methods
	def getEngineIds(self, templateName):
		rawIds = host.rcon_invoke("Object.listObjectsofTemplate " +templateName)	
		rawIds = rawIds.split("\n")
		#if g_debug: print rawIds
		objectIds = []
		
		for rawId in rawIds:
			if len(rawId) == 0:
				continue
			id = rawId.split(" ")
			id = id[3]
			objectIds.append(id)
		#if g_debug: print str(type(objectIds[0]))
		if g_debug: print templateName + "\'s objectId is " + objectIds[0]
		return objectIds
		
	def getControlPointId(self, cp):
		host.rcon_invoke("ObjectTemplate.activeSafe ControlPoint " + cp.templateName)
		cpId = host.rcon_invoke("ObjectTemplate.controlPointId").split("\n")[0]
		#if g_debug: print str(type(cpId))
		if g_debug: print cp.templateName + "\'s cpId is " + cpId
		return cpId #note:cpId is a string
	
	'''def addObjectOnCp(self, templateName, cp, position, rotation):
		host.rcon_invoke("echo debugaddObjectOnCp" + cp.templateName)
		spawnerName = "bf2obj_" + templateName + "_target%s" % self.currentTarget
		spawnerCmds = [
				
			"ObjectTemplate.create ObjectSpawner " + spawnerName,
			"ObjectTemplate.activeSafe ObjectSpawner " + spawnerName,
			"ObjectTemplate.isNotSaveable 1",
			"ObjectTemplate.hasMobilePhysics 0",
			"ObjectTemplate.setObjectTemplate 0 " + templateName,
			"ObjectTemplate.minSpawnDelay 9999",
			"ObjectTemplate.maxSpawnDelay 9999",
			"ObjectTemplate.maxNrOfObjectSpawned 1"
		]
		createCmds = [

			"Object.create " + spawnerName,
			"Object.absolutePosition %s/%s/%s" % position,
			"Object.rotation %s/%s/%s" % rotation
			#"Object.setControlPointId " + self.getControlPointId(cp),
			#"Object.layer %s" % self.currentTarget
			#"Object.delete"
		]
		cmds = spawnerCmds + createCmds
		if g_debug: print cmds
		for cmd in cmds:
			host.rcon_invoke(cmd)	'''
			
	def addObjectOnTeam(self, templateName, position, rotation, team):
		spawnerName = "bf2obj_" + templateName
		
		spawnerCmds = [
				
			"ObjectTemplate.create ObjectSpawner " + spawnerName,
			"ObjectTemplate.activeSafe ObjectSpawner " + spawnerName,
			"ObjectTemplate.isNotSaveable 1",
			"ObjectTemplate.hasMobilePhysics 0",
			"ObjectTemplate.setObjectTemplate %d " % team + templateName,
			"ObjectTemplate.team %d" % team,
			"ObjectTemplate.teamOnVehicle 1"
			"ObjectTemplate.maxNrOfObjectSpawned 1"
		]
		#newpos = (position[0], position[1]+0.5, position[2])
		createCmds = [

			"Object.create " + spawnerName,
			"Object.absolutePosition %s/%s/%s" % position,
			"Object.rotation %s/%s/%s" % rotation,
			"Object.team %d" % team,
			#"Object.setVisibleTeam %d" % team,
			"Object.delete"
		]
		
		cmds = spawnerCmds + createCmds
	
		for cmd in cmds:
			host.rcon_invoke(cmd)
		#host.rcon_invoke('echo addObjectOnTeam')
		
	def getVectorDistance(pos1, pos2):
		diffVec = [0.0, 0.0, 0.0]
		diffVec[0] = math.fabs(pos1[0] - pos2[0])
		diffVec[1] = math.fabs(pos1[1] - pos2[1])
		diffVec[2] = math.fabs(pos1[2] - pos2[2])
	 
		return math.sqrt(diffVec[0] * diffVec[0] + diffVec[1] * diffVec[1] + diffVec[2] * diffVec[2])
	
	def getRoughDistance(pos1, pos2):
		diffVec = [0.0, 0.0, 0.0]
		diffVec[0] = math.fabs(pos1[0] - pos2[0])
		diffVec[1] = math.fabs(pos1[1] - pos2[1])
		diffVec[2] = math.fabs(pos1[2] - pos2[2])
	 
		return diffVec[0] + diffVec[1] + diffVec[2]	
		
rushData = None
	
def init():
	# events hook
	#global rushData
	host.registerGameStatusHandler(onGameStatusChanged)
	if host.sgl_getIsAIGame() == 1:
		host.sh_setEnableCommander(1)
	else:
		host.sh_setEnableCommander(0)
	#rushData = Rush(settings)	
	host.registerHandler('TimeLimitReached', onTimeLimitReached, 1)	
	global g_debug
	g_debug = 1
	if g_debug: 
		logfile.init()
		registerRConCommand('output', rcon_debugoutput)
		registerRConCommand('disableoutput', rcon_debugdisableoutput)
		print "rush.py initialized"
		
		
		
def deinit():
	bf2.triggerManager.destroyAllTriggers()
	global g_controlPoints
	g_controlPoints = []
	#global rushData
	#rushData = None
	host.unregisterGameStatusHandler(onGameStatusChanged)
	if g_debug: 
		logfile.deinit()
		print "rush.py uninitialized"


def onGameStatusChanged(status):

	global g_controlPoints
	global rushData
	global debugtimer
	if status == bf2.GameStatus.Playing: 
		host.rcon_invoke('echo gamestatusplaying')

		# add control point triggers
		rushData = Rush(settings)
		g_controlPoints = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
		for obj in g_controlPoints:
			radius = float(obj.getTemplateProperty('radius'))
			isHemi = int(obj.cp_getParam('isHemisphere'))
			if isHemi != 0:
				id = bf2.triggerManager.createHemiSphericalTrigger(obj, onCPTrigger, '<<PCO>>', radius, (1, 2, 3))
			else:
				id = bf2.triggerManager.createRadiusTrigger(obj, onCPTrigger, '<<PCO>>', radius, (1, 2, 3))			
			obj.triggerId = id
			obj.lastAttackingTeam = 0
			if obj.cp_getParam('team') > 0:
				obj.flagPosition = Top
			else:
				obj.flagPosition = Bottom
				
		rushData.gameSetting(g_controlPoints)
		#rushData.addTargetVehicle()
		timer.once(FIND_TARGET_DELAY, rushData.linkTargetVehicle)
		host.registerHandler('ControlPointChangedOwner', onCPStatusChange)
		
		debugtimer = loop(1, targetCheck)
		# setup ticket system
		ticketsTeam1 = calcStartTickets(bf2.gameLogic.getDefaultTickets(1))
		ticketsTeam2 = calcStartTickets(bf2.gameLogic.getDefaultTickets(2))
		
		bf2.gameLogic.setTickets(1, ticketsTeam1)
		bf2.gameLogic.setTickets(2, ticketsTeam2)
		
		bf2.gameLogic.setTickets(rushData.getDefenseTeam(), 9999)#set defenseTeam's ticket to max
		
		bf2.gameLogic.setTicketState(1, 0)
		bf2.gameLogic.setTicketState(2, 0)

		bf2.gameLogic.setTicketLimit(1, 1, 0)
		bf2.gameLogic.setTicketLimit(2, 1, 0)
		bf2.gameLogic.setTicketLimit(1, 2, 10)
		bf2.gameLogic.setTicketLimit(2, 2, 10)
		bf2.gameLogic.setTicketLimit(1, 3, int(ticketsTeam1*0.1))
		bf2.gameLogic.setTicketLimit(2, 3, int(ticketsTeam2*0.1))
		bf2.gameLogic.setTicketLimit(1, 4, int(ticketsTeam1*0.2))
		bf2.gameLogic.setTicketLimit(2, 4, int(ticketsTeam1*0.2))
		
		host.registerHandler('TicketLimitReached', onTicketLimitReached)
		updateTicketLoss()

		# player events
		host.registerHandler('PlayerDeath', onPlayerDeathCQ)
		host.registerHandler('PlayerKilled', onPlayerKilledCQ)
		host.registerHandler('PlayerRevived', onPlayerRevived)
		host.registerHandler('PlayerSpawn', onPlayerSpawn)
		host.registerHandler('EnterVehicle', onEnterVehicle)
		host.registerHandler('ExitVehicle', onExitVehicle)
		
		host.registerHandler('VehicleDestroyed', onVehicleDestroyedRush)#for switching targets
		host.registerHandler('PlayerDeath', onPlayerDeathRush)
		host.registerHandler('PlayerKilled', onPlayerKilledRush)
		host.registerHandler('PlayerRevived', onPlayerRevivedRush)
		host.registerHandler('PlayerSpawn', onPlayerSpawnRush)
		host.registerHandler('EnterVehicle', onEnterVehicleRush)
		host.registerHandler('ExitVehicle', onExitVehicleRush)#for placing and disarming c4
		
		if g_debug: print "Conquest gamemode initialized."
	else:
		bf2.triggerManager.destroyAllTriggers()
		g_controlPoints = []
		rushData = None



def calcStartTickets(mapDefaultTickets):
	return int(mapDefaultTickets * (bf2.serverSettings.getTicketRatio() / 100.0))
	
	
	
def onTimeLimitReached(value):
	team1tickets = bf2.gameLogic.getTickets(1)
	team2tickets = bf2.gameLogic.getTickets(2)
	
	winner = 0
	victoryType = 0
	if team1tickets > team2tickets:
		winner = 1
		victoryType = 3
	elif team2tickets > team1tickets:
		winner = 2
		victoryType = 3
	

	host.sgl_endGame(winner, victoryType)



# update ticket system
def updateTicketLoss():
	areaValueTeam1 = 0
	areaValueTeam2 = 0
	totalAreaValue = 0
	numCpsTeam0 = 0
	numCpsTeam1 = 0
	numCpsTeam2 = 0
	
	# calculate control point area value for each team
	for obj in g_controlPoints:
		team = obj.cp_getParam('team')
		if team == 1:
			#areaValueTeam1 += obj.cp_getParam('areaValue', team)
			totalAreaValue += areaValueTeam1
			numCpsTeam1 += 1
		elif team == 2:
			#areaValueTeam2 += obj.cp_getParam('areaValue', team)
			totalAreaValue += areaValueTeam2
			numCpsTeam2 += 1
		else:
			numCpsTeam0 += 1
			totalAreaValue += 0
		
	# check if a team has no control points
	if numCpsTeam1 == 0 or numCpsTeam2 == 0:
		if numCpsTeam1 == 0:
			losingTeam = 1
			winningTeam = 2
		else:
			losingTeam = 2
			winningTeam = 1
		
		# check if there is anyone alive
		foundLivingPlayer = False
		for p in bf2.playerManager.getPlayers():
			if p.getTeam() == losingTeam and p.isAlive():
				foundLivingPlayer = True
				break
				
		if not foundLivingPlayer:

			# drop tickets
			ticketLossPerSecond = bf2.gameLogic.getDefaultTicketLossAtEndPerMin()
			bf2.gameLogic.setTicketChangePerSecond(losingTeam, -ticketLossPerSecond)
			bf2.gameLogic.setTicketChangePerSecond(winningTeam, 0)
			
			return

	
	# update ticket loss
	team1AreaOverweight = areaValueTeam1 - areaValueTeam2
	percentualOverweight = 1.0
	if totalAreaValue != 0:
		percentualOverweight = abs(team1AreaOverweight / totalAreaValue)
	
	ticketLossPerSecTeam1 = calcTicketLossForTeam(1, areaValueTeam2, -team1AreaOverweight)
	ticketLossPerSecTeam2 = calcTicketLossForTeam(2, areaValueTeam1, team1AreaOverweight)
	bf2.gameLogic.setTicketChangePerSecond(1, -ticketLossPerSecTeam1)
	bf2.gameLogic.setTicketChangePerSecond(2, -ticketLossPerSecTeam2)


	
# actual ticket loss calculation function
def calcTicketLossForTeam(team, otherTeamAreaValue, otherTeamAreaOverweight):
	if otherTeamAreaValue >= 100 and otherTeamAreaOverweight > 0:
		ticketLossPerSecond = (bf2.gameLogic.getDefaultTicketLossPerMin(team) / 60.0) * (otherTeamAreaOverweight / 100.0)
		return ticketLossPerSecond
	else:
		return 0


	
DOWNWARDS = -1
UPWARDS = 1	

# called when tickets reach a predetermined limit (negativ value means that the tickets have become less than the limit)
def onTicketLimitReached(team, limitId):
	if (limitId == -1):
		if (team == 1):
			winner = 2
		
		elif (team == 2):
			winner = 1
		
		bf2.gameLogic.setTicketState(1, 0)
		bf2.gameLogic.setTicketState(2, 0)
	
		host.sgl_endGame(winner, 3)		

	# update ticket state
	else:
		updateTicketWarning(team, limitId)

	

# called when the ticket state should be updated (for triggering messages and sounds based on tickets left)
def updateTicketWarning(team, limitId):

	oldTicketState = bf2.gameLogic.getTicketState(team)
	newTicketState = 0
	
	if (oldTicketState >= 10):
		newTicketState = 10		

	if (limitId == -2):
		newTicketState = 10
	
	elif (limitId == 2):
		newTicketState = 0		

	elif (limitId == -3):
		newTicketState += 2

	elif (limitId == -4):
		newTicketState += 1

	if (oldTicketState != newTicketState):
		bf2.gameLogic.setTicketState(team, newTicketState)
		
	
	
# called when someone enters or exits cp radius
def onCPTrigger(triggerId, cp, vehicle, enter, userData):
	if not cp.isValid(): return
	
	if vehicle and vehicle.getParent(): return
	
	if cp in rushData.getTargets():	calcTakeOverChangePerSecondRush(cp)
	
	# can this cp be captured at all?
	if cp.cp_getParam('unableToChangeTeam') != 0:
		return					
		
	playersInVehicle = None	
	if vehicle:
		playersInVehicle = vehicle.getOccupyingPlayers()
	
	if enter:
		for p in playersInVehicle:
			cp = getOccupyingCP(p)
			if cp != None:
				if not p.getIsInsideCP():
					#if g_debug: print "Resetting enterPctAt for player ", p.getName()
					p.enterCpAt = host.timer_getWallTime()
	
	if vehicle:	
		for p in playersInVehicle:
			# only count first player in a vehicle
			if p == playersInVehicle[0]:  
				#if g_debug: print p.index, " is in radius. v=", vehicle.templateName
				p.setIsInsideCP(enter)	
			else:
				p.setIsInsideCP(0)
				if enter == 1:
					bf2.gameLogic.sendHudEvent(p, 66, 49) #66 = HEEnableHelpMessage, 49 = VHMExitToCaptureFlag;	
	
	#if int(cp.cp_getParam('timeToGetControl')) < rushData.getCurrentTarget(): calcTakeOverChangePerSecond(cp)
	#calcTakeOverChangePerSecondRush(cp)
	
def calcTakeOverChangePerSecondRush(cp):
	#if g_echooutput: host.rcon_invoke("echo debugcalcTakeOverChangePerSecondRush")
	if rushData.gameState != 1 or not cp.targetVehicle: return 
	if cp in rushData.getTargets():
		if int(cp.cp_getParam('timeToGetControl')) == rushData.getCurrentTarget():
			#if g_echooutput: host.rcon_invoke("echo debugCurrentTarget")
			if rushData.getCurrentTargetsDown():
				if g_echooutput: host.rcon_invoke("echo debugCurrentTargetsDown")
				if cp.cp_getParam('team') == 0:
					if g_echooutput: host.rcon_invoke("echo debugcalcTakeOverChangePerSecondRushAttackTeamGetFlag")
					cp.cp_setParam('flag', rushData.getAttackTeam())
					cp.cp_setParam('takeOverChangePerSecond', 999)
				elif cp.cp_getParam('team') == rushData.getDefenseTeam():
					if g_echooutput: host.rcon_invoke("echo debugcalcTakeOverChangePerSecondRushDefenseTeamLostFlag")
					cp.cp_setParam('takeOverChangePerSecond', -999)
			elif (cp.targetVehicle == rushData.getCurrentTargetObjectA() and rushData.Adestroyed) or (cp.targetVehicle == rushData.getCurrentTargetObjectB() and rushData.Bdestroyed) and cp.cp_getParam('team') == rushData.getDefenseTeam():
				if g_echooutput: host.rcon_invoke("echo debugcalcTakeOverChangePerSecondRushDefenseTeamLostFlag2")
				cp.cp_setParam('takeOverChangePerSecond', -999)
		'''elif int(cp.cp_getParam('timeToGetControl')) < rushData.getCurrentTarget():
			if cp.cp_getParam('team') == 0:
				host.rcon_invoke("echo debugcalcTakeOverChangePerSecondRushAttackTeamGetFlagLate")
				cp.cp_setParam('flag', rushData.getAttackTeam())
				cp.cp_setParam('takeOverChangePerSecond', 999)
			elif cp.cp_getParam('team') == rushData.getDefenseTeam():
				host.rcon_invoke("echo debugcalcTakeOverChangePerSecondRushDefenseTeamLostFlagLate")
				cp.cp_setParam('takeOverChangePerSecond', -999)'''
	
def calcTakeOverChangePerSecond(cp):

	# count people in radius
	team1Occupants = 0
	team2Occupants = 0

	pcos = bf2.triggerManager.getObjects(cp.triggerId)
	for o in pcos:
		if not o: continue # you can get None in the result tuple when the host can't figure out what object left the trigger
		if o.getParent(): continue # getOccupyingPlayers returns all players downwards in the hierarchy, so dont count them twice
		occupyingPlayers = o.getOccupyingPlayers()
		for p in occupyingPlayers:
			if p.getTeam() == rushData.getDefenseTeam(): continue
			# only count first player in a vehicle
			if p != occupyingPlayers[0]: 
				continue
				
			if p.isAlive() and not p.isManDown():
				
				if not p.killed:
					if p.getTeam() == 1:
						team1Occupants += 1
					elif p.getTeam() == 2:
						team2Occupants += 1


	# determine who is taking control
	team1OverWeight = team1Occupants - team2Occupants
	attackOverWeight = 0

	if team1OverWeight > 0:
		attackingTeam = 1
	elif team1OverWeight < 0:
		attackingTeam = 2
	else:
		attackingTeam = 0

	
	if team1Occupants == 0 and team2Occupants == 0:

		# nobody here, slowly go back to owning team
		if cp.cp_getParam('team') == 0:
			attackOverWeight = -0.5
		else:
			attackOverWeight = 0.5
			
		timeToChangeControl = cp.cp_getParam('timeToLoseControl')

	else:

		# raise flag if already ours, or at bottom and neutral. Otherwise lower first.
		if cp.cp_getParam('flag') == attackingTeam or (cp.flagPosition == Bottom and cp.cp_getParam('team') == 0):

			# our flag, raise
			attackOverWeight = abs(team1OverWeight)
			timeToChangeControl = cp.cp_getParam('timeToGetControl')
		else:

			# other team raised flag, lower first
			attackOverWeight = - abs(team1OverWeight)
			timeToChangeControl = cp.cp_getParam('timeToLoseControl')


	if cp.cp_getParam('onlyTakeableByTeam') != 0 and cp.cp_getParam('onlyTakeableByTeam') != attackingTeam:
		return


	# flag can only be changed when at bottom
	if cp.flagPosition == Bottom:
		cp.cp_setParam('flag', attackingTeam)


	# calculate flag raising/lowering speed
	if timeToChangeControl > 0:
		takeOverChangePerSecond = 1.0 * attackOverWeight / timeToChangeControl
	else:
		takeOverChangePerSecond = 0.0

	if (cp.flagPosition == Top and takeOverChangePerSecond > 0) or (cp.flagPosition == Bottom and takeOverChangePerSecond < 0):
		takeOverChangePerSecond = 0.0

	if abs(takeOverChangePerSecond) > 0:
		cp.flagPosition = Middle
				
	cp.cp_setParam('takeOverChangePerSecond', takeOverChangePerSecond)

			
	
# called when a control point flag reached top or bottom
def onCPStatusChange(cp, top):

	playerId = -1
	takeoverType = -1
	newTeam = -1
	scoringTeam = -1
	
	if top:	cp.flagPosition = Top
	else:   cp.flagPosition = Bottom
	
	# determine capture / neutralize / defend
	if cp.cp_getParam('team') != 0:

		if top:
			# regained flag, do nothing
			pass
			
		else:
			# neutralize
			newTeam = 0
			if cp.cp_getParam('team') == 1:
				scoringTeam = 2
			else:
				scoringTeam = 1
			cp.cp_setParam('flag', 0)#newly add	
			takeoverType = TAKEOVERTYPE_NEUTRALIZE

	else:

		if top:
			# capture
			newTeam = cp.cp_getParam('flag')
			scoringTeam = newTeam
			takeoverType = TAKEOVERTYPE_CAPTURE

		else:
			# hit bottom, but still neutral
			pass

	
	# scoring
	if takeoverType > 0:
		pcos = bf2.triggerManager.getObjects(cp.triggerId)
	
		# count number of players
		scoringPlayers = []
		firstPlayers = []
		for o in pcos:
			if o.getParent(): continue

			occupyingPlayers = o.getOccupyingPlayers()
			for p in occupyingPlayers:
			
				# only count first player in a vehicle
				if p != occupyingPlayers[0]: 
					continue
					
				if p.isAlive() and not p.isManDown() and p.getTeam() == scoringTeam:
					if len(firstPlayers) == 0 or p.enterCpAt < firstPlayers[0].enterCpAt:
						firstPlayers = [p]
					elif p.enterCpAt == firstPlayers[0].enterCpAt:
						firstPlayers += [p]
					
					if not p in scoringPlayers:
						scoringPlayers += [p]
	
		# deal score
		for p in scoringPlayers:
			oldScore = p.score.score;
			if takeoverType == TAKEOVERTYPE_CAPTURE:
				if p in firstPlayers:
					p.score.cpCaptures += 1
					addScore(p, SCORE_CAPTURE, RPL)
					bf2.gameLogic.sendGameEvent(p, 12, 0) #12 = Conquest, 0 = Capture
					playerId = p.index
				else:
					p.score.cpAssists += 1
					addScore(p, SCORE_CAPTUREASSIST, RPL)
					bf2.gameLogic.sendGameEvent(p, 12, 2) #12 = Conquest, 2 = Assist


			elif takeoverType == TAKEOVERTYPE_NEUTRALIZE:
				if p in firstPlayers:
					p.score.cpNeutralizes += 1
					addScore(p, SCORE_NEUTRALIZE, RPL)
					bf2.gameLogic.sendGameEvent(p, 12, 3) #12 = Conquest, 3 = Neutralize
				else:
					p.score.cpNeutralizeAssists += 1
					addScore(p, SCORE_NEUTRALIZEASSIST, RPL)
					bf2.gameLogic.sendGameEvent(p, 12, 4) #12 = Conquest, 4 = Neutralize assist
					
				

	# immediate ticket loss for opposite team
	enemyTicketLossInstant = cp.cp_getParam('enemyTicketLossWhenCaptured')
	if enemyTicketLossInstant > 0 and newTeam > 0:
		
		if newTeam == 1:
			punishedTeam = 2
		elif newTeam == 2:
			punishedTeam = 1
		
		tickets = bf2.gameLogic.getTickets(punishedTeam)
		tickets -= enemyTicketLossInstant
		bf2.gameLogic.setTickets(punishedTeam, tickets)
	
	
	# update control point	
	cp.cp_setParam('playerId', playerId) #always set player first
	if newTeam != -1 and cp.cp_getParam('team') != newTeam:
		cp.cp_setParam('team', newTeam)
	onCPTrigger(cp.triggerId, cp, 0, 0, 0)
	updateTicketLoss()

				
				
def onPlayerDeathCQ(victim, vehicle):		

	# punish team with one ticket
	if victim != None:
		team = victim.getTeam()
		teamTickets = bf2.gameLogic.getTickets(team)
		teamTickets -= 1
		bf2.gameLogic.setTickets(team, teamTickets)

	# check if it was the last player
	foundLivingPlayer = False
	for p in bf2.playerManager.getPlayers():
		if p != victim and p.getTeam() == victim.getTeam() and p.isAlive():
			foundLivingPlayer = True
	
	if not foundLivingPlayer:
		updateTicketLoss()
	


def onPlayerKilledCQ(victim, attacker, weapon, assists, object):
	if not victim: 
		return
	
	victim.killed = True
	
	# update flag takeover status if victim was in a CP radius
	cp = getOccupyingCP(victim)
	if cp != None:
		onCPTrigger(-1, cp, victim.getVehicle(), False, None)

		# give defend score if killing enemy within cp radius
		if attacker != None and attacker.getTeam() != victim.getTeam()\
		   and cp.cp_getParam('unableToChangeTeam') == 0 and cp.cp_getParam('onlyTakeableByTeam') == 0:
		
			if cp != None and cp.cp_getParam('team') == attacker.getTeam():
				attacker.score.cpDefends += 1
				addScore(attacker, SCORE_DEFEND, RPL)
				bf2.gameLogic.sendGameEvent(attacker, 12, 1) #12 = Conquest, 1 = Defend
			
			
			
def onPlayerRevived(victim, attacker):

	# update flag takeover status if victim was in a CP radius
	victim.killed = False
	
	cp = getOccupyingCP(victim)
	if cp != None:
		onCPTrigger(-1, cp, victim.getVehicle(), True, None)
	
	
	
def onPlayerSpawn(player, soldier):
	player.killed = False
	
	
	
def onEnterVehicle(player, vehicle, freeSoldier = False):
	player.setIsInsideCP(False)
	cp = getOccupyingCP(player)
	if cp != None:
		onCPTrigger(-1, cp, vehicle, False, None)
		updateCaptureStatus(vehicle) 


def onExitVehicle(player, vehicle):

	# update flag takeover status if player in a CP radius
	
	if g_debug: print "Player exiting ", player.getName()
	cp = getOccupyingCP(player)

	# can this cp be captured at all?
	player.setIsInsideCP(cp != None and cp.cp_getParam('unableToChangeTeam') == 0)

	updateCaptureStatus(vehicle)
		

#Update cp capture status on players in vehicle
def updateCaptureStatus(vehicle):	

	rootVehicle = bf2.objectManager.getRootParent(vehicle)
	playersInVehicle = rootVehicle.getOccupyingPlayers()
	
	# set the player in the topmost pco as inside - others outside
	for p in playersInVehicle:
		if g_debug: print "Players in vehicle ", p.getName()
		cp = getOccupyingCP(p)
		p.setIsInsideCP(cp != None and cp.cp_getParam('unableToChangeTeam') == 0 and p == playersInVehicle[0])
		
		
# find cp that player is occupying, if any		
def getOccupyingCP(player):
	vehicle = player.getVehicle()
	playerPos = vehicle.getPosition()
	
	# find closest CP
	closestCP = None
	if len(g_controlPoints) == 0: return None
	for obj in g_controlPoints:
		distanceTo = getVectorDistance(playerPos, obj.getPosition())
		if closestCP == None or distanceTo < closestCPdist:
			closestCP = obj
			closestCPdist = distanceTo
	
	# is the player in radius?
	pcos = bf2.triggerManager.getObjects(closestCP.triggerId)
	for o in pcos:
		if o == player.getDefaultVehicle():
			# Player is DEFAULT vehicle - this is needed when called from onEnterVehicle
			return closestCP
		else:
			for p in o.getOccupyingPlayers():
				if p == player:
					return closestCP
	
	return None



# get distance between two positions
def getVectorDistance(pos1, pos2):
	diffVec = [0.0, 0.0, 0.0]
	diffVec[0] = math.fabs(pos1[0] - pos2[0])
	diffVec[1] = math.fabs(pos1[1] - pos2[1])
	diffVec[2] = math.fabs(pos1[2] - pos2[2])
	 
	return math.sqrt(diffVec[0] * diffVec[0] + diffVec[1] * diffVec[1] + diffVec[2] * diffVec[2])
		
#from omnicide_final		
class timer(object):

    class once(object):

        def __init__(self, time, method, *args):
            self.time = host.timer_getWallTime() + time
            self.interval = 0
            self.alwaysTrigger = 1
            self.method = method
            self.args = args
            host.timer_created(self)

        def onTrigger(self):
            self.method(*self.args)
            self.abort()

        def abort(self):
            host.timer_destroy(self)
			
class loop(object):

        def __init__(self, interval, method, *args):
            self.time = host.timer_getWallTime()
            self.interval = interval
            self.alwaysTrigger = 1
            self.method = method
            self.args = args
            host.timer_created(self)

        def onTrigger(self):
            self.method(*self.args)

        def abort(self):
            host.timer_destroy(self)
#######################

'''def onEnterVehicleRush(player, vehicle, freeSoldier = False):
	if vehicle.templateName == TARGETNAME_A or vehicle.templateName == TARGETNAME_B:
		vehicle.playerEnterAt = host.timer_getWallTime()
		if vehicle.c4object == None and player.getTeam() == rushData.getAttackTeam():
			timer.once(C4_PLACE_DELAY, rushData.addC4OnTargetVehicle, vehicle)
			MSG_bombplacewait(player)
		elif vehicle.c4object != None and player.getTeam() == rushData.getDefenseTeam():
			timer.once(C4_DISARM_DELAY, rushData.disarmC4OnTargetVehicle, vehicle)
			MSG_bombdisarmwait(player)
	
	

def onExitVehicleRush(player, vehicle):
	if vehicle.templateName == TARGETNAME_A or vehicle.templateName == TARGETNAME_B:
		#messages will be implemented here to warn that exiting aborts place/disarm process
		if (vehicle.c4object == None and player.getTeam() == rushData.getAttackTeam()) or (vehicle.c4object != None and player.getTeam() == rushData.getDefenseTeam()):
			MSG_warnleaveseat(player)
	'''

def startC4Operation(player, vehicle):
	if player.killed: return
	vehicle.occupyingPlayer = player
	if vehicle.c4object == None and player.getTeam() == rushData.getAttackTeam():
		#vehicle.occupyingPlayer = player
		host.rcon_invoke("game.sayAll \"player " + player.getName() + " is going to place bomb on target\"")
		vehicle.playerEnterAt = host.timer_getWallTime()
		timer.once(C4_PLACE_DELAY * 0.25, rushData.c4PlaceProcess25, player, vehicle)
		timer.once(C4_PLACE_DELAY * 0.5, rushData.c4PlaceProcess50, player, vehicle)
		timer.once(C4_PLACE_DELAY * 0.75, rushData.c4PlaceProcess75, player, vehicle)
		timer.once(C4_PLACE_DELAY, rushData.addC4OnTargetVehicle, player, vehicle)
		MSG_bombplacewait(player)
	elif vehicle.c4object != None and player.getTeam() == rushData.getDefenseTeam():
		#vehicle.occupyingPlayer = player
		host.rcon_invoke("game.sayAll \"player " + player.getName() + " is going to disarm bomb on target\"")
		vehicle.playerEnterAt = host.timer_getWallTime()
		timer.once(C4_DISARM_DELAY * 0.25, rushData.c4DisarmProcess25, player, vehicle)
		timer.once(C4_DISARM_DELAY * 0.5, rushData.c4DisarmProcess50, player, vehicle)
		timer.once(C4_DISARM_DELAY * 0.75, rushData.c4DisarmProcess75, player, vehicle)
		timer.once(C4_DISARM_DELAY, rushData.disarmC4OnTargetVehicle, player, vehicle)
		MSG_bombdisarmwait(player)
	
def enterTargetRange(target, player):	
	if g_echooutput: host.rcon_invoke("echo debugenterTargetRange")
	if target.occupyingPlayer == None:
		startC4Operation(player, target)
	elif target.occupyingPlayer.getTeam() == player.getTeam() and target.occupyingPlayer != player: 
		if g_echooutput: host.rcon_invoke("echo debugfriendlyOperation")
		MSG_friendlyOperation(player)
	elif target.occupyingPlayer.getTeam() != player.getTeam():
		if g_echooutput: host.rcon_invoke("echo debugenemyOperation")
		MSG_enemyOperation(player)
	
def exitTargetRange(target, player):	
	if g_echooutput: host.rcon_invoke("echo debugexitTargetRange")
	if target.occupyingPlayer == player:
		target.occupyingPlayer = None
		if (target.c4object == None and player.getTeam() == rushData.getAttackTeam()) or (target.c4object != None and player.getTeam() == rushData.getDefenseTeam()):
			host.rcon_invoke("game.sayAll \"player " + player.getName() + " left target\"")
			if not player.killed: MSG_warnleaveseat(player)	
	elif target.occupyingPlayer and target.occupyingPlayer.getTeam() != player.getTeam():
		if g_echooutput: host.rcon_invoke("echo debugenemyOperation")
		MSG_enemyOperation(player)
	
# called when someone enters or exits target radius
def onTargetTrigger(triggerId, target, vehicle, enter, userData):
	if g_echooutput: host.rcon_invoke("echo debugonTargetTrigger")
	if not target.isValid() or target.destroyed: 
		if g_echooutput: host.rcon_invoke("echo debugValidTargetTrigger")
		return
	if vehicle and vehicle.getParent(): return

	playersInVehicle = None	
	if vehicle:
		playersInVehicle = vehicle.getOccupyingPlayers()
		
	if target.occupyingPlayer and (target.occupyingPlayer.killed or not target.occupyingPlayer.getDefaultVehicle() in bf2.triggerManager.getObjects(target.triggerId)):
		if len(target.getOccupyingPlayers()) == 0:
			if not target.occupyingPlayer in playersInVehicle:
				host.rcon_invoke("echo debugClearOccupyingPlayer")
				prevplayer = target.occupyingPlayer
				target.occupyingPlayer = None
				checkPlayerInTargetAllyFirst(target, prevplayer)
		elif target.occupyingPlayer.killed: target.occupyingPlayer = target.getOccupyingPlayers()[0]
	
	if enter:
		#if target.occupyingPlayer == None: 
			for player in playersInVehicle:
				#if vehicleplayer.getTeam(): 
					if player.getDefaultVehicle() in bf2.triggerManager.getObjects(target.triggerId) or player.getVehicle() == target:
						#target.occupyingPlayer = player
						enterTargetRange(target, player)#players must get off vehicles to operate a bomb

	else:
		for player in playersInVehicle:
			#if player.getVehicle() == player.getDefaultVehicle():# and target.occupyingPlayer == player: 
			if not (player.getVehicle().templateName == TARGETNAME_A or player.getVehicle().templateName == TARGETNAME_B):			
				exitTargetRange(target, player) 
	#if vehicle:	
	#	for p in playersInVehicle:

def onPlayerDeathRush(victim, vehicle):		

	'''# punish team with one ticket
	if victim != None:
		team = victim.getTeam()
		teamTickets = bf2.gameLogic.getTickets(team)
		teamTickets -= 1
		bf2.gameLogic.setTickets(team, teamTickets)

	# check if it was the last player
	foundLivingPlayer = False
	for p in bf2.playerManager.getPlayers():
		if p != victim and p.getTeam() == victim.getTeam() and p.isAlive():
			foundLivingPlayer = True
	
	if not foundLivingPlayer:
		updateTicketLoss()'''
	#if vehicle.templateName == TARGETNAME_A or vehicle.templateName == TARGETNAME_B:
	target = getOccupyingTargetV(vehicle)
	if target != None:
		checkPlayerInTargetAllyFirst(target, victim)
	


def onPlayerKilledRush(victim, attacker, weapon, assists, object):
	victim.killed = True
	if victim: 	
		target = getOccupyingTarget(victim)
		if target != None:
			onTargetTrigger(-1, target, victim.getVehicle(), False, None)
			checkPlayerInTargetAllyFirst(target, victim)
		'''# give defend score if killing enemy within cp radius
		if attacker != None and attacker.getTeam() != victim.getTeam():
		
			if target != None and attacker.getTeam() == rushData.getAttackTeam():
				attacker.score.cpDefends += 1
				addScore(attacker, SCORE_DEFEND, RPL)
				bf2.gameLogic.sendGameEvent(attacker, 12, 1) #12 = Conquest, 1 = Defend'''
			
			
			
def onPlayerRevivedRush(victim, attacker):

	victim.killed = False
	
	target = getOccupyingTarget(victim)
	if target != None:
		onTargetTrigger(-1, target, victim.getVehicle(), True, None)
	
	
	
def onPlayerSpawnRush(player, soldier):
	#player.killed = False
	pass
	
	
def onEnterVehicleRush(player, vehicle, freeSoldier = False):
	target = getOccupyingTarget(player)
	if target != None:
		if target == player.getVehicle() and vehicle != target: onTargetTrigger(-1, target, player.getVehicle(), True, None)
		else: onTargetTrigger(-1, target, player.getVehicle(), False, None)

def onExitVehicleRush(player, vehicle):
	target = getOccupyingTarget(player)
	if target != None:
		if vehicle != target: 
			onTargetTrigger(-1, target, player.getVehicle(), True, None)
			checkPlayerInTargetAllyFirst(target, player)

def checkPlayerInTargetAllyFirst(target, player):
	if len(target.getOccupyingPlayers()) != 0:
		onTargetTrigger(-1, target, target, True, None)
		return
	allyfound = False
	pcos = bf2.triggerManager.getObjects(target.triggerId)
	if not player:
		for o in pcos:
			onTargetTrigger(-1, target, o, True, None)
	else:
		for o in pcos:
			if len(o.getOccupyingPlayers()) != 0 and o.getOccupyingPlayers()[0].getTeam() == player.getTeam():
				allyfound = True
				onTargetTrigger(-1, target, o, True, None)
				break
		if not allyfound:
			for o in pcos:
				if len(o.getOccupyingPlayers()) != 0 and o.getOccupyingPlayers()[0].getTeam() != player.getTeam():
					onTargetTrigger(-1, target, o, True, None)
					break
				
def checkPlayerInTargetTrigger(target):
	pcos = bf2.triggerManager.getObjects(target.triggerId)
	for o in pcos:
		onTargetTrigger(-1, target, o, True, None)
		
# find target that player is occupying, if any		
def getOccupyingTarget(player):
	if not player: return None
	if g_echooutput: host.rcon_invoke("echo debuggetOccupyingTarget")
	if player.getVehicle().templateName == TARGETNAME_A or player.getVehicle().templateName == TARGETNAME_B: return player.getVehicle()
	if not rushData.Adestroyed:
		pcos = bf2.triggerManager.getObjects(rushData.getCurrentTargetObjectA().triggerId)
		for o in pcos:
			if o == player.getDefaultVehicle():
				return rushData.getCurrentTargetObjectA()
	
	if not rushData.Bdestroyed:
		pcos = bf2.triggerManager.getObjects(rushData.getCurrentTargetObjectB().triggerId)
		for o in pcos:
			if o == player.getDefaultVehicle():
				return rushData.getCurrentTargetObjectB()

	return None

def getOccupyingTargetV(vehicle):
	if not vehicle: return None
	if g_echooutput: host.rcon_invoke("echo debuggetOccupyingTargetV")
	if vehicle.templateName == TARGETNAME_A or vehicle.templateName == TARGETNAME_B: return vehicle
	if not rushData.Adestroyed:
		pcos = bf2.triggerManager.getObjects(rushData.getCurrentTargetObjectA().triggerId)
		for o in pcos:
			if o == vehicle:
				return rushData.getCurrentTargetObjectA()
	
	if not rushData.Bdestroyed:
		pcos = bf2.triggerManager.getObjects(rushData.getCurrentTargetObjectB().triggerId)
		for o in pcos:
			if o == vehicle:
				return rushData.getCurrentTargetObjectB()

	return None
	
def onVehicleDestroyedRush(vehicle, attacker):
	if vehicle.templateName == TARGETNAME_A :
		host.rcon_invoke("game.sayTeam %d \"We destroyed targetA!\"" % rushData.getAttackTeam())
		host.rcon_invoke("game.sayTeam %d \"We lost targetA!\"" % rushData.getDefenseTeam())
		vehicle.occupyingPlayer = None
		vehicle.destroyed = True
		host.rcon_invoke("echo debugVehicleDestroyed")
		#bf2.triggerManager.destroy(vehicle.triggerId)
		attacker = vehicle.c4placeplayer 
		rushData.Adestroyed =True
		if attacker:
			#attacker get score
			host.rcon_invoke("game.sayAll \"player " + attacker.getName() + " destroyed targetA!\"")
			if attacker.getTeam() == rushData.getAttackTeam():
				addScore(attacker, SCORE_DESTROYTARGET, RPL)
				bf2.gameLogic.sendGameEvent(attacker, 10, 5) #10 = Replenish, 5 = DestroyStrategic
			else: addScore(attacker, SCORE_DESTROYFRIENDLYTARGET, RPL)
			#messages should be implementes here
		'''for cp in rushData.getTargets():
			calcTakeOverChangePerSecondRush(cp)
		rushData.toNextTarget()'''
		#timer.once(FIND_TARGET_DELAY, rushData.linkTargetVehicle)
	elif vehicle.templateName == TARGETNAME_B:
		host.rcon_invoke("game.sayTeam %d \"We destroyed targetB!\"" % rushData.getAttackTeam())
		host.rcon_invoke("game.sayTeam %d \"We lost targetB!\"" % rushData.getDefenseTeam())
		vehicle.occupyingPlayer = None
		vehicle.destroyed = True
		host.rcon_invoke("echo debugVehicleDestroyed")
		#bf2.triggerManager.destroy(vehicle.triggerId)
		rushData.Bdestroyed =True
		attacker = vehicle.c4placeplayer 
		if attacker:
			#attacker get score
			host.rcon_invoke("game.sayAll \"player " + attacker.getName() + " destroyed targetB!\"")
			if attacker.getTeam() == rushData.getAttackTeam():
				addScore(attacker, SCORE_DESTROYTARGET, RPL)
				bf2.gameLogic.sendGameEvent(attacker, 10, 5) #10 = Replenish, 5 = DestroyStrategic
			else: addScore(attacker, SCORE_DESTROYFRIENDLYTARGET, RPL)
			
def targetCheck():
	if rushData.gameState != 1: return
	for cp in rushData.targetSequence:
		calcTakeOverChangePerSecondRush(cp)
	rushData.toNextTarget()
	
#debug
def rcon_debugoutput(self, ctx, cmd):
	global g_echooutput
	g_echooutput = 1
	if rushData.getCurrentTargetsDown(): host.rcon_invoke("echo debugcurrentTargetDown")
	if rushData.getCurrentTargetObjectA().destroyed: host.rcon_invoke("echo debugTargetADestroyed") 
	if rushData.Adestroyed: host.rcon_invoke("echo debugrushDataADestroyed") 
	if rushData.getCurrentTargetObjectA().isValid(): 
		host.rcon_invoke("echo debugTargetAValid") 
		if rushData.getCurrentTargetObjectA().isPlayerControlObject: host.rcon_invoke("echo isPlayerControlObjectA")
		if rushData.getCurrentTargetObjectA().hasArmor: host.rcon_invoke("echo hasArmorA")
		if hasattr(rushData.getCurrentTargetObjectA(), "getDamage"): host.rcon_invoke("echo \"Armor: %s \"" % rushData.getCurrentTargetObjectA().getDamage())
		else: host.rcon_invoke("echo noAttrgetDamageA")
		if not hasattr(rushData.getCurrentTargetObjectA(), "setDamage"):
			host.rcon_invoke("echo noAttrsetDamageA")
		if not hasattr(rushData.getCurrentTargetObjectA(), "getOccupyingPlayers"):
			host.rcon_invoke("echo noAttrgetOccupyingPlayersA")
		if rushData.getCurrentTargetObjectA().getIsWreck(): host.rcon_invoke("echo debugTargetAIsWreck") 
	if rushData.getCurrentTargetObjectB().destroyed: host.rcon_invoke("echo debugTargetBDestroyed")
	if rushData.Bdestroyed: host.rcon_invoke("echo debugrushDataBDestroyed") 
	if rushData.getCurrentTargetObjectB().isValid():
		host.rcon_invoke("echo debugTargetBValid") 
		if rushData.getCurrentTargetObjectB().isPlayerControlObject: host.rcon_invoke("echo isPlayerControlObjectB")
		if rushData.getCurrentTargetObjectB().hasArmor: host.rcon_invoke("echo hasArmorB")
		if hasattr(rushData.getCurrentTargetObjectB(), "getDamage"): host.rcon_invoke("echo \"Armor: %s \"" % rushData.getCurrentTargetObjectA().getDamage())
		else: host.rcon_invoke("echo noAttrgetDamageB")
		if not hasattr(rushData.getCurrentTargetObjectB(), "setDamage"):
			host.rcon_invoke("echo noAttrsetDamageB")
		if not hasattr(rushData.getCurrentTargetObjectB(), "getOccupyingPlayers"):
			host.rcon_invoke("echo noAttrgetOccupyingPlayersB")
		if rushData.getCurrentTargetObjectB().getIsWreck(): host.rcon_invoke("echo debugTargetBIsWreck") 
	for cp in rushData.getTargets():
		host.rcon_invoke("echo \"" + cp.templateName + ": team %s " % cp.cp_getParam('team')+ " flag %s \"" % cp.cp_getParam('flag'))
		if g_debug:
			print cp.targetVehicle.templateName + "**targetvehicle**"
			if cp.targetVehicle.isValid():
				print "valid"		
				if cp.targetVehicle.getIsWreck(): print "isWreck"
				else: print "not Wreck"
			else: print "not valid"
			if cp.targetVehicle.destroyed: print "destroyed=True"
			else: print "destroyed=False"
			if not cp.targetVehicle.occupyingPlayer: print "nooccupyingPlayers"
			else: print "hasOccupyingPlayer"
	
	
def rcon_debugdisableoutput(self, ctx, cmd):
	global g_echooutput
	g_echooutput = 0