#set encoding to UTF-8 to insert non-English words like Chinese, if any
# coding=UTF-8

# rush v2.0.0 Beta

#This script is created by worldlife. You are free to use it in any mod.
#If you want to modify and release it, just add your name to the MODIFIER_MAP with the version.
#Credits:
#Credit to DICE for the vBF2 gpm_cp.py as my reference
#Credit to http://www.bf2tech.org/
#Thanks for the excellent bf2 python docs.I learned a lot!
#Credit to Omnicide_Final
#Thanks for the convenient timer.once class and loop class.It helps a lot!
#Credit to alpha project
#Thanks for the BF2Object.py that helps me to spawn vehicles!

'''
MODIFIER_MAP = {
	"V2.0.0 beta" : "worldlife",
	#add modifier names to this list
}
'''

TAKEOVERTYPE_CAPTURE = 1
TAKEOVERTYPE_NEUTRALIZE = 2

#constants
#from BF2Object.py alpha_project
#FIND_TARGET_DELAY = 0.2 #time delay between addTargetVehicle() and linkTargetVehicle()
#TARGET_SPAWN_HEIGHT = 10000.0 #spawn the targets high up in the air at first
#######
CPSTATUSCHANGE_DELAY = 0.1
FIND_TARGET_DELAY = 0.5
TIME_RETRY = 0.5
C4_PLACE_DELAY = 8
C4_DISARM_DELAY = 8 #currently, those two should be the same
C4_DETONATE_DELAY = 40
TARGETNAME_A = 'target_aircontroltower_mec_sp_A'
TARGETNAME_B = 'target_aircontroltower_mec_sp_B'
C4OBJECTNAME = 'c4_explosives_bigpack_pco2'
#TARGETNAME_A = 'ats_hj8'
#TARGETNAME_B = 'ats_tow'
DUMMYTARGETNAME_A = 'target_aircontroltower_mec_dummyA'#not used
DUMMYTARGETNAME_B = 'target_aircontroltower_mec_dummyB'#not used
TARGETA_OBJSPAWNER_SUFFIX = '_targetA'
TARGETB_OBJSPAWNER_SUFFIX = '_targetB'
ATKSPDUMMY_SUFFIX = '_spdummy_atk'
DEFSPDUMMY_SUFFIX = '_spdummy_def'
ATK_INFERIOR_DUMMY_SUFFIX = '_infdummy_atk'
DEF_INFERIOR_DUMMY_SUFFIX = '_infdummy_def'
ATK_INFERIOR2_DUMMY_SUFFIX = '_inf2dummy_atk'
DEF_INFERIOR2_DUMMY_SUFFIX = '_inf2dummy_def'
TRIGGER_RADIUS = 5

#ticket loss
TIME_BEGINTICKETLOSS = 300 #5 minute
TICKETLOSS_LINEAR = 0.002 #add 1 tkloss/sec per 500s
TICKETLOSS_CONST = 0.1

#attack team inferior state
TIME_BEGININFERIOR = 300
TICKETPERCENT_ATK_INFERIOR = 0.2
TICKETPERCENT_ATK_INFERIOR2 = 0.1
TICKETPERCENT_DEF_INFERIOR = 0.5
TICKETPERCENT_DEF_INFERIOR2 = 0.7

#rush scores
SCORE_DESTROYTARGET = 30
SCORE_DESTROYFRIENDLYTARGET = -50 #could not happen
SCORE_PLACEC4 = 5
SCORE_DISARMC4 = 20
#SCORE_CAPTURE = 2
#SCORE_NEUTRALIZE = 2
#SCORE_CAPTUREASSIST = 1
#SCORE_NEUTRALIZEASSIST = 1
SCORE_DEFEND = 5

Top = 0
Middle = 1
Bottom = 2

import host
import bf2
import math,sys,time
from game.scoringCommon import addScore, RPL
from bf2 import g_debug
from rush_maps import RUSHV2_MAPS
from exceptionoutput import *
import log
from game.rcons import *
from game.messages import *
from BF2Object import BF2Object
import aiArty
import random_objectspawner
import spawnpoint_protect
from spawnpoint_protect import getSpawnPointTemplateNames, getSpawnPointCPId, getEngineIdString

#settings = None
debugtimer = None

#debug
g_echooutput = 0

class TargetState:
	def __init__(self, triggerId=-1):
		self.object = None
		#self.atkspCp = None
		#self.defspCp = None
		#self.flagCp = None
		self.c4object = None 
		self.c4placeplayer = None
		self.playerEnterAt = 0.0 #sets when player start operate the c4
		self.occupyingPlayer = None
		self.playersInRange = []
		self.destroyed = False						
		self.triggerId = triggerId

class RushGameStat:
	def __init__(self):
		self.currentInferiorTeam = 0 #Team in inferior strength
		self.inferiorLevel = 0
		
		self.attackTeamInferiorCount = 0
		self.defenseTeamInferiorCount = 0
		
		self.attackTeamMaxTickets = 0
	
class Rush:
	def __init__(self, settings):
		self.settings = settings
		self.gameState = 0#0:pregame,1:ingame,2:notready
		self.targetSequence = [] #cps that indicates the target state
		self.attackTeamInferiorDummy = [] #cps that control objectSpawners/spawnPoints when team is in inferior state
		self.defenseTeamInferiorDummy = []
		self.attackTeamInferior2Dummy = [] #cps that control objectSpawners/spawnPoints when team is in inferior2 state (currently not used)
		self.defenseTeamInferior2Dummy = []
		self.attackTeamBase = []
		self.defenseTeamBase = []
		self.cpTable = {}
		self.targetSpawner = [] #target objectspawners
		self.currentTarget = 1
		self.defenseTeam = 1
		self.attackTeam = 2
		self.targetAState = TargetState()
		self.targetBState = TargetState()
		self.targetCheckTimer = None
		self.lastDestroyTargetTime = host.timer_getWallTime()
		self.registeredHandlers = {} #avoids a same handler registers multiple times
		self.statTracker = RushGameStat()
		self.spawnPoints = []
		self.baseSPDisabled = False
		#self.initGame()
	
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
			return True
		else:
			return False
	
	#judge methods
	def getCurrentTargetsDown(self):
		return self.targetAState.destroyed and self.targetBState.destroyed
		
	####################
	###ingame methods###
	####################
	
	#registers an ingame handler and avoids multiple registering
	def registerHandler(self, event, handler):
		'''if not handler in self.registeredHandlers:
			self.registeredHandlers[handler] = event''' #do not work...
		if not event in self.registeredHandlers:		
			self.registeredHandlers[event] = handler
			host.registerHandler(event, handler)
			if g_debug: log.output("Register handler %s for %s event" % (handler, event))
		else:
			if g_debug: log.output("Handler %s already registered for %s event" % (handler, event))
	
	def initGame(self):
		if g_debug: log.output("initGame")
		host.registerGameStatusHandler(self.onGameStatusChanged)
		host.registerHandler('TimeLimitReached', self.onTimeLimitReached, 1)	
	
	def deinitGame(self):
		if g_debug: log.output("deinitGame")
		bf2.triggerManager.destroyAllTriggers()
		host.unregisterGameStatusHandler(self.onGameStatusChanged)
	
	def onGameStatusChanged(self, status):	
		try:
			if status == bf2.GameStatus.Playing: 
				self.startGame()
			elif status == bf2.GameStatus.EndGame:
				self.endGame()
			else:
				#bf2.triggerManager.destroyAllTriggers()
				self.endGame()	
		except:
			ExceptionOutput()
	
	def onTimeLimitReached(self, value):
		#if time limit reached, the defense wins
		host.sgl_endGame(self.getDefenseTeam(), 3)		
	
	def startGame(self):
		#print self.registeredHandlers	
		if self.gameState == 1: return #this avoids multiple handler registering...(cq do not need this, why?)
		if g_debug: log.output("startGame")
		#self.__init__(self.settings)
		cps = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
		for cp in cps:
			self.cpTable[cp.templateName] = cp
			if cp.cp_getParam('team') > 0:
				cp.flagPosition = Top
			else:
				cp.flagPosition = Bottom
				
		self.registerHandler('TicketLimitReached', self.onTicketLimitReached)
		self.registerHandler('VehicleDestroyed', self.onVehicleDestroyedRush)#for switching targets
		self.registerHandler('PlayerDeath', self.onPlayerDeathRush)
		self.registerHandler('PlayerKilled', self.onPlayerKilledRush)
		self.registerHandler('PlayerRevived', self.onPlayerRevivedRush)
		self.registerHandler('PlayerSpawn', self.onPlayerSpawnRush)
		self.registerHandler('EnterVehicle', self.onEnterVehicleRush)
		self.registerHandler('ExitVehicle', self.onExitVehicleRush)
		self.registerHandler('ControlPointChangedOwner', self.onCPStatusChangeRush)#used to control cps to control flags, objectspawners and spawnpoints
		
		self.gameSetting()
		timer.once(FIND_TARGET_DELAY, self.linkTargetVehicle)
		
		# ticketsAtkTeam = self.calcStartTickets(bf2.gameLogic.getDefaultTickets(self.getAttackTeam())) #bf2.gameLogic.getDefaultTickets(self.getAttackTeam())#
		ticketsAtkTeam = self.calcStartTicketsAttackTeam()
		self.statTracker.attackTeamMaxTickets = ticketsAtkTeam
		
		bf2.gameLogic.setTickets(self.getAttackTeam(), ticketsAtkTeam)		
		bf2.gameLogic.setTickets(self.getDefenseTeam(), len(self.targetSequence)/2)#set defense ticket to target group numbers	
		#if g_debug: log.output("initial ticket: %s %s" % (ticketsAtkTeam,len(self.targetSequence)/2))
		bf2.gameLogic.setTicketState(1, 0)
		bf2.gameLogic.setTicketState(2, 0)
		bf2.gameLogic.setTicketLimit(self.getAttackTeam(), 1, 0)
		bf2.gameLogic.setTicketLimit(self.getAttackTeam(), 2, 10)
		bf2.gameLogic.setTicketLimit(self.getAttackTeam(), 3, int(ticketsAtkTeam*0.1))
		bf2.gameLogic.setTicketLimit(self.getAttackTeam(), 4, int(ticketsAtkTeam*0.2))
		
		templateNames = getSpawnPointTemplateNames()
		for name in templateNames:
			spawnPoints = bf2.objectManager.getObjectsOfTemplate(name)
			for obj in spawnPoints:
				self.spawnPoints.append(obj)
		
		self.updateTicketLoss()
		self.updateCpState()
		
		self.lastDestroyTargetTime = host.timer_getWallTime()
		
		self.writeStatsStartGame()
		
		self.gameState = 1
		#print self.registeredHandlers
		
	def calcStartTickets(self, mapDefaultTickets):
		return int(mapDefaultTickets * (bf2.serverSettings.getTicketRatio() / 100.0))
	
	def calcStartTicketsAttackTeam(self):
		numPlayers = len(bf2.playerManager.getPlayers())
		layoutPlayers = min(max(int(2**math.ceil(math.log(numPlayers)/math.log(2))), 16), 64)
		team = self.getAttackTeam()
		# log.output("calcStartTicketsAttackTeam")
		# log.output(host.rcon_invoke("gameLogic.getDefaultNumberOfTicketsEx %s %s" % (layoutPlayers, team)))
		try:
			mapDefaultTickets = int(host.rcon_invoke("gameLogic.getDefaultNumberOfTicketsEx %s %s" % (layoutPlayers, team)))
		except:
			
			mapDefaultTickets = bf2.gameLogic.getDefaultTickets(team)
		return int(mapDefaultTickets * (bf2.serverSettings.getTicketRatio() / 100.0))
	
	def onTicketLimitReached(self, team, limitId):
		#only control attackTeam ticket state
		if (team == self.getAttackTeam()):
			if (limitId == -1):
				bf2.gameLogic.setTicketState(1, 0)
				bf2.gameLogic.setTicketState(2, 0)		
				if self.gameState == 1: host.sgl_endGame(self.getDefenseTeam(), 3)		
			# update ticket state
			else:
				self.updateTicketWarning(team, limitId)

	# called when the ticket state should be updated (for triggering messages and sounds based on tickets left)
	def updateTicketWarning(self, team, limitId):
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
	
	def onCPStatusChangeRush(self, cp, top):
		if g_debug: log.output("debugonCPStatusChangeRush(cp=%s)"%cp.templateName)
		newTeam = -1
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
				cp.cp_setParam('flag', 0)#newly add	
		else:
			if top:
				# capture
				newTeam = cp.cp_getParam('flag')
			else:
				# hit bottom, but still neutral
				pass
		if newTeam != -1 and cp.cp_getParam('team') != newTeam:
			cp.cp_setParam('team', newTeam)
	
	def endGame(self):
		if g_debug: log.output("endGame")
		bf2.triggerManager.destroyAllTriggers()
		self.gameState = 0
		self.targetSequence = []
		self.attackTeamInferiorDummy = []
		self.defenseTeamInferiorDummy = []
		self.attackTeamInferior2Dummy = []
		self.defenseTeamInferior2Dummy = []
		self.attackTeamBase = []
		self.defenseTeamBase = []
		self.cpTable = {}
		self.targetSpawner = []
		self.currentTarget = 1
		self.defenseTeam = 1
		self.attackTeam = 2
		self.targetAState = TargetState()
		self.targetBState = TargetState()
		if self.targetCheckTimer:
			self.targetCheckTimer.abort()
			self.targetCheckTimer = None
		self.lastDestroyTargetTime = host.timer_getWallTime()
		self.statTracker = RushGameStat()
		self.spawnPoints = []
		self.baseSPDisabled = False
		
		self.writeStatsEndGame()
		
	def gameSetting(self):
		#host.rcon_invoke("run objects/weapons/projectile/c4_explosives_bigpack/" + C4OBJECTNAME +".con")#make sure the name matches
		tmpSequence = []
		cps = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
		
		for obj in cps:
			#print "obj.cp_getParam('team')= %s, name = %s, suffix = %s" % (obj.cp_getParam('team'),obj.templateName,obj.templateName[-len(ATKSPDUMMY_SUFFIX):])
			if obj.cp_getParam('unableToChangeTeam') or obj.templateName[-len(ATKSPDUMMY_SUFFIX):] == ATKSPDUMMY_SUFFIX or obj.templateName[-len(DEFSPDUMMY_SUFFIX):] == DEFSPDUMMY_SUFFIX: 
				continue
			#obj.targetVehicle = None #this links to the target VehicleObject
			elif obj.templateName[-len(ATK_INFERIOR_DUMMY_SUFFIX):] == ATK_INFERIOR_DUMMY_SUFFIX:
				self.attackTeamInferiorDummy.append(obj)
			elif obj.templateName[-len(DEF_INFERIOR_DUMMY_SUFFIX):] == DEF_INFERIOR_DUMMY_SUFFIX:
				self.defenseTeamInferiorDummy.append(obj)
			elif obj.templateName[-len(ATK_INFERIOR2_DUMMY_SUFFIX):] == ATK_INFERIOR2_DUMMY_SUFFIX:
				self.attackTeamInferior2Dummy.append(obj)
			elif obj.templateName[-len(DEF_INFERIOR2_DUMMY_SUFFIX):] == DEF_INFERIOR2_DUMMY_SUFFIX:
				self.defenseTeamInferior2Dummy.append(obj)
			else:
				tmpSequence.append(obj)
		#determine defenseTeam
		for obj in tmpSequence:
			#if obj.cp_getParam('unableToChangeTeam') != 1:
			index = int(obj.cp_getParam('timeToGetControl'))
			if index==1:
				self.defenseTeam = obj.cp_getParam('team')
				if self.defenseTeam == 1: self.attackTeam = 2
				else: self.attackTeam = 1
				break
		
		for obj in cps:
			if obj.cp_getParam('unableToChangeTeam'):
				if obj.cp_getParam('team') == self.attackTeam: self.attackTeamBase.append(obj)
				if obj.cp_getParam('team') == self.defenseTeam: self.defenseTeamBase.append(obj)
		
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
			if obj.templateName[-len(TARGETA_OBJSPAWNER_SUFFIX):] == TARGETA_OBJSPAWNER_SUFFIX or obj.templateName[-len(TARGETB_OBJSPAWNER_SUFFIX):] == TARGETB_OBJSPAWNER_SUFFIX:
				if not obj in self.targetSpawner: self.targetSpawner.append(obj)
		for obj in objspws:
			if obj.templateName[-len(TARGETA_OBJSPAWNER_SUFFIX):] == TARGETA_OBJSPAWNER_SUFFIX:
				self.addObjectOnTeam(DUMMYTARGETNAME_A, obj.getPosition(), obj.getRotation(), 0)#prevent vehicles disturbing target spawn
				cpname = obj.templateName[:-len(TARGETA_OBJSPAWNER_SUFFIX)]
				i = 0
				try:
					i = cpnames.index(cpname)
				except:
					if g_debug: 
						print "Name error!Check the map and fix this!Current object: %s ; CP name: %s" % (obj.templateName[:-len(TARGETA_OBJSPAWNER_SUFFIX)],cpname)
				if (i/2)*2 != i :
					self.targetSequence[i],	self.targetSequence[i-1] = self.targetSequence[i-1], self.targetSequence[i]#swap a and b
					cpnames[i], cpnames[i-1] = cpnames[i-1], cpnames[i]
					self.targetSpawner[i-1] = obj
				else: self.targetSpawner[i] = obj
			elif obj.templateName[-len(TARGETB_OBJSPAWNER_SUFFIX):] == TARGETB_OBJSPAWNER_SUFFIX: 
				self.addObjectOnTeam(DUMMYTARGETNAME_B, obj.getPosition(), obj.getRotation(), 0)#prevent vehicles disturbing target spawn
				cpname = obj.templateName[:-len(TARGETB_OBJSPAWNER_SUFFIX)]
				try:
					i = cpnames.index(cpname)
				except:
					if g_debug: print "Name error!Check the map and fix this!Current object: %s ; CP name: %s" % (obj.templateName[:-len(TARGETB_OBJSPAWNER_SUFFIX)],cpname)
				if (i/2)*2 == i :
					self.targetSequence[i],	self.targetSequence[i+1] = self.targetSequence[i+1], self.targetSequence[i]#swap a and b
					cpnames[i], cpnames[i+1] = cpnames[i+1], cpnames[i]
					self.targetSpawner[i+1] = obj
				else: self.targetSpawner[i] = obj
		#self.c4setting()
		#check timer, enable it to do recovering in case of error
		#Ex. No target spawn, c4 do not destroy the target, not moving to next target even if all targets are destroyed, etc.
		self.targetCheckTimer = loop(1, self.targetCheck)
		sys.stdout.flush()
		if g_debug: 	
			print "targetSequenceAfterAdjust:"	
			for obj in self.targetSequence:
				print obj.templateName
			print "targetSpawner:"
			for obj in self.targetSpawner:
				print obj.templateName
		sys.stdout.flush()
		self.gameState = 2
	
	#set C4 denonation time
	def c4setting(self):
		host.rcon_invoke('ObjectTemplate.active ' + C4OBJECTNAME)
		hp = float(host.rcon_invoke('ObjectTemplate.armor.hitPoints'))
		host.rcon_invoke('ObjectTemplate.armor.hpLostWhileCriticalDamage %s' % (hp/C4_DETONATE_DELAY))
	
	def getCurrentTargetObjectA(self):
		return self.targetAState.object
	
	def getCurrentTargetObjectB(self):
		return self.targetBState.object
	
	#Move to next target
	def toNextTarget(self):
		#if g_echooutput: log.output("debugtryToNextTarget")
		'''if g_debug: 
			if self.getCurrentTargetObjectA():
				print self.getCurrentTargetObjectA().templateName + " state %s" % self.getCurrentTargetObjectA().getIsWreck()
			if self.getCurrentTargetObjectB():
				print self.getCurrentTargetObjectB().templateName + " state %s" % self.getCurrentTargetObjectB().getIsWreck()'''
		if self.gameState != 1: 
			#timer.once(TIME_RETRY, self.toNextTarget)
			return
		#if (not self.getCurrentTargetObjectA().isValid() or self.getCurrentTargetObjectA().getIsWreck()) and (not self.getCurrentTargetObjectB().isValid() or self.getCurrentTargetObjectB().getIsWreck()):
		if self.targetAState.destroyed and self.targetBState.destroyed:
			log.output("debugtoNextTarget")
			self.updateTicketLoss()
			if self.currentTarget*2 >= len(self.targetSequence):
				host.rcon_invoke("game.sayAll \"All targets destroyed! Round is ending...\"")
				self.gameState = 2
				bf2.gameLogic.setTickets(self.defenseTeam, 0)#set defenseTeam's ticket to min
				self.gameState = 2 #end game
				timer.once(3, host.sgl_endGame, self.attackTeam, 3)
			else:
				host.rcon_invoke("game.sayAll \"Current targets down! Moving to next targets!\"")
				self.currentTarget += 1
				bf2.gameLogic.setTickets(self.getDefenseTeam(), (len(self.targetSequence)/2) - self.currentTarget + 1)
				#self.addTargetVehicle()
				#need to use linkTargetVehicle() after some time
				self.targetAState.destroyed = False
				self.targetBState.destroyed = False
				bf2.triggerManager.destroyAllTriggers()
				timer.once(FIND_TARGET_DELAY, self.linkTargetVehicle)
				#message
				for player in bf2.playerManager.getPlayers():
					if player.getTeam() == self.getAttackTeam():
						MSG_teammoveon(player)
		else:
			#timer.once(TIME_RETRY, self.toNextTarget)
			pass
	
	def updateInferiorState(self):
		atkInferior = self.inferiorLogicAttackTeam()
		defInferior = self.inferiorLogicDefenseTeam()
		atkInferior2 = self.inferior2LogicAttackTeam()
		defInferior2 = self.inferior2LogicDefenseTeam()
		if atkInferior: 
			self.statTracker.attackTeamInferiorCount += 1
			if atkInferior2:
				self.statTracker.inferiorLevel = 2
			else:
				self.statTracker.inferiorLevel = 1
			if not defInferior:
				self.statTracker.currentInferiorTeam = self.attackTeam
		if defInferior: 
			self.statTracker.defenseTeamInferiorCount += 1
			if defInferior2:
				self.statTracker.inferiorLevel = 2
			else:
				self.statTracker.inferiorLevel = 1
			if not atkInferior:
				self.statTracker.currentInferiorTeam = self.defenseTeam
		if atkInferior==defInferior:
			self.statTracker.currentInferiorTeam = 0
			self.statTracker.inferiorLevel = 0
		if g_debug: log.output("updateInferiorState: atkInferior:%d defInferior:%d current:%d" % (atkInferior, defInferior, self.statTracker.currentInferiorTeam))
	
	def inferiorLogicAttackTeam(self):
		if g_debug: log.output("attackTeam ticket state: %d" % bf2.gameLogic.getTicketState(self.attackTeam))
		return ((host.timer_getWallTime() - self.lastDestroyTargetTime) > TIME_BEGININFERIOR \
			or float(bf2.gameLogic.getTickets(self.attackTeam))/self.statTracker.attackTeamMaxTickets < TICKETPERCENT_ATK_INFERIOR) \
			#and self.statTracker.currentInferiorTeam != self.defenseTeam
	
	def inferior2LogicAttackTeam(self):
		return self.inferiorLogicAttackTeam() \
			and float(bf2.gameLogic.getTickets(self.attackTeam))/self.statTracker.attackTeamMaxTickets < TICKETPERCENT_ATK_INFERIOR2 \
			#and self.statTracker.currentInferiorTeam != self.defenseTeam

	def inferiorLogicDefenseTeam(self):
		return self.currentTarget*2 == len(self.targetSequence) and \
			(self.statTracker.attackTeamInferiorCount < 1 or \
			float(bf2.gameLogic.getTickets(self.attackTeam))/self.statTracker.attackTeamMaxTickets > TICKETPERCENT_DEF_INFERIOR)
	
	def inferior2LogicDefenseTeam(self):
		return self.inferiorLogicDefenseTeam() and\
			float(bf2.gameLogic.getTickets(self.attackTeam))/self.statTracker.attackTeamMaxTickets > TICKETPERCENT_DEF_INFERIOR2
	# renew all cp state
	# singleplayer/coop:
	#						flag(for ai)	atk_spdummy			def_spdummy
	#	atkTakenCp			atk				0					0
	#	prevTargetCp		atk				atk					0
	#	currentTargetCp		def				0					def
	#	currentTargetDown	atk				0					0
	#	defTakenCp			atk				0					0
	def updateCpState(self):
		if g_debug: log.output('debugupdateCpState')
		# target cp
		i=0
		while i<len(self.targetSequence)/2:
			self.targetSequence[i*2].cp_setParam('takeOverChangePerSecond', 1.0)
			self.targetSequence[i*2+1].cp_setParam('takeOverChangePerSecond', 1.0)
			if i == self.currentTarget - 1: #currentTargetCp
				if self.targetAState.destroyed:
					teamsA = (self.getAttackTeam(),0,0)
				else:
					teamsA = (self.getDefenseTeam(),0,self.getDefenseTeam())
				if self.targetBState.destroyed:
					teamsB = (self.getAttackTeam(),0,0)
				else:
					teamsB = (self.getDefenseTeam(),0,self.getDefenseTeam())
				self.setCpStateRush(self.targetSequence[i*2],teamsA)
				self.setCpStateRush(self.targetSequence[i*2+1],teamsB)
				#lower the flag a bit to call bots to defend
				#self.targetSequence[i*2].cp_setParam('takeOverChangePerSecond', 0)
				if not self.targetAState.destroyed and self.targetAState.c4object!=None: self.targetSequence[i*2].cp_setParam('takeOverChangePerSecond', -0.001)
				#else: self.targetSequence[i*2].cp_setParam('takeOverChangePerSecond', 0)
				if not self.targetBState.destroyed and self.targetBState.c4object!=None: self.targetSequence[i*2+1].cp_setParam('takeOverChangePerSecond', -0.001)
				#else: self.targetSequence[i*2+1].cp_setParam('takeOverChangePerSecond', 0)
			else:
				if i == self.currentTarget - 2: #prevTargetCp
					teams = (self.getAttackTeam(),self.getAttackTeam(),0)	
				elif i < self.currentTarget - 2: #atkTakenCp
					teams = (self.getAttackTeam(),0,0)
				elif i == self.currentTarget: # nextCp
					teams = (0,0,0)
				else: #defTakenCp
					teams = (self.getAttackTeam(),0,0)	
				self.setCpStateRush(self.targetSequence[i*2],teams)
				self.setCpStateRush(self.targetSequence[i*2+1],teams)	
			i+=1
		
		#inferior cp
		self.updateInferiorState()
		if self.statTracker.currentInferiorTeam == self.attackTeam:
			if self.statTracker.inferiorLevel >= 1:
				for cp in self.attackTeamInferiorDummy:
					self.setCpTeam(cp,self.attackTeam)
			if self.statTracker.inferiorLevel >= 2:
				for cp in self.attackTeamInferior2Dummy:
					self.setCpTeam(cp,self.attackTeam)
			for cp in self.defenseTeamInferiorDummy:
					self.setCpTeam(cp,0)
			for cp in self.defenseTeamInferior2Dummy:
				self.setCpTeam(cp,0)
		elif self.statTracker.currentInferiorTeam == self.defenseTeam:
			for cp in self.attackTeamInferiorDummy:
				self.setCpTeam(cp,0)
			for cp in self.attackTeamInferior2Dummy:
				self.setCpTeam(cp,0)
			if self.statTracker.inferiorLevel >= 1:
				for cp in self.defenseTeamInferiorDummy:
					self.setCpTeam(cp,self.defenseTeam)
			if self.statTracker.inferiorLevel >= 2:
				for cp in self.defenseTeamInferior2Dummy:
					self.setCpTeam(cp,self.defenseTeam)
		else:
			for cp in self.attackTeamInferiorDummy:
				self.setCpTeam(cp,0)
			for cp in self.defenseTeamInferiorDummy:
				self.setCpTeam(cp,0)
			for cp in self.attackTeamInferior2Dummy:
				self.setCpTeam(cp,0)
			for cp in self.defenseTeamInferior2Dummy:
				self.setCpTeam(cp,0)
		
		#base cp
		if self.settings.disableAtkBaseAfterFirstRush and not self.baseSPDisabled and self.currentTarget > 1:
			for cp in self.attackTeamBase:
				# This causes bot to attack base, find a better way
				# self.setCpTeam(cp,0)
				# self.settings.disableAtkBaseAfterFirstRush = False # tmp workaround to avoid multiple processing (do not work at the second round if this is set in the first round)
				self.baseSPDisabled = True # avoid multiple processing
				# Disable all spawnpoints in the base
				try:
					cpid = int(self.getControlPointIdString(cp))
				except:
					continue
				for obj in self.spawnPoints:
					if getSpawnPointCPId(obj) == cpid:
						log.output(obj.templateName + " Disabled!")
						host.rcon_invoke("Object.active " + getEngineIdString(obj.templateName))
						host.rcon_invoke("Object.delete")
		if g_debug: log.output('debugupdateCpStateEnd')
		
	def setCpStateRush(self, cp, teams=(0,0,0)):
		try:
			cpname = cp.templateName
			self.setCpTeam(self.cpTable[cpname], teams[0])
			self.setCpTeam(self.cpTable[cpname+ATKSPDUMMY_SUFFIX], teams[1])
			self.setCpTeam(self.cpTable[cpname+DEFSPDUMMY_SUFFIX], teams[2])
		except:
			ExceptionOutput()
	
	#can't be used at the start of the game(dunno why)
	def setCpTeam(self, cp, team):
		if not cp or not cp.isValid():
			log.output("Invalid call cp at setCpTeam(cp,team)")
			return
		#if g_debug: log.output("debug setCpTeam %s %s  currentTeam:%s flag:%s change/sec:%s" % (cp.templateName, team, cp.cp_getParam('team'), cp.cp_getParam('flag'), cp.cp_getParam('takeOverChangePerSecond')))
		if cp.cp_getParam('team') == team: return
		
		if cp.cp_getParam('team') == 0:
			cp.cp_setParam('flag', team)
			cp.cp_setParam('takeOverChangePerSecond', 999)
			#if g_debug: log.output("raising flag...")
		else:
			cp.cp_setParam('takeOverChangePerSecond', -999)
			#if g_debug: log.output("lowing flag...")
		#retry later to confirm
		timer.once(CPSTATUSCHANGE_DELAY, self.setCpTeam, cp, team)
	
	#find newly spawned target object, link it to targetState and activate its trigger
	def linkTargetVehicle(self):
		log.output("debuglinkTargetVehicle")
		pcos = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.PlayerControlObject')
		Afound = False
		Bfound = False
		for obj in pcos:
			if not obj.isValid() or obj.getIsWreck() or self.getVectorDistance((0.0,0.0,0.0),obj.getPosition())<0.1: continue
			if obj.templateName == TARGETNAME_A and self.targetAState.object != obj:
					'''obj.c4object = None 
					obj.c4placeplayer = None
					obj.playerEnterAt = 0.0 #sets when player start operate the c4
					obj.occupyingPlayer = None
					obj.destroyed = False #do not work when bugs occurs
					self.targetSequence[self.currentTarget*2-2].targetVehicle = obj'''
					self.targetAState.__init__()#self.targetAState = TargetState()
					self.targetAState.object = obj
					#obj.setPosition(self.targetSequence[self.currentTarget*2-2].getPosition())
					'''isHemi = int(self.targetSequence[self.currentTarget*2-2].cp_getParam('isHemisphere'))
					if isHemi != 0:
						id = bf2.triggerManager.createHemiSphericalTrigger(obj, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))
					else:
						id = bf2.triggerManager.createRadiusTrigger(obj, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))			'''								
					#id = bf2.triggerManager.createHemiSphericalTrigger(obj, self.onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, 'A')#ONLY USE HEMI TRIGGER
					id = bf2.triggerManager.createHemiSphericalTrigger(obj, self.onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))#ONLY USE HEMI TRIGGER
					obj.triggerId = id
					self.targetAState.triggerId = id
					Afound = True
					log.output("debuglinkTargetVehicleA")
			if obj.templateName == TARGETNAME_B and self.targetBState.object != obj:
					'''obj.c4object = None 
					obj.c4placeplayer = None
					obj.playerEnterAt = 0.0
					obj.occupyingPlayer = None
					obj.destroyed = False #do not work when bugs occurs
					self.targetSequence[self.currentTarget*2-1].targetVehicle = obj'''
					self.targetBState.__init__()#self.targetBState = TargetState()
					self.targetBState.object = obj
					'''isHemi = int(self.targetSequence[self.currentTarget*2-1].cp_getParam('isHemisphere'))
					if isHemi != 0:
						id = bf2.triggerManager.createHemiSphericalTrigger(obj, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))
					else:
						id = bf2.triggerManager.createRadiusTrigger(obj, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))		'''	
					#id = bf2.triggerManager.createHemiSphericalTrigger(obj, self.onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, 'B')#ONLY USE HEMI TRIGGER
					id = bf2.triggerManager.createHemiSphericalTrigger(obj, self.onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))
					obj.triggerId = id
					self.targetBState.triggerId = id
					#obj.setPosition(self.targetSequence[self.currentTarget*2-1].getPosition())
					Bfound = True
					log.output("debuglinkTargetVehicleB")
		'''id = bf2.triggerManager.createHemiSphericalTrigger(self.targetSequence[self.currentTarget*2-2].targetVehicle, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))#ONLY USE HEMI TRIGGER
		self.targetSequence[self.currentTarget*2-2].targetVehicle.triggerId = id
		id = bf2.triggerManager.createHemiSphericalTrigger(self.targetSequence[self.currentTarget*2-1].targetVehicle, onTargetTrigger, '<<PCO>>', TRIGGER_RADIUS, (1, 2, 3))#ONLY USE HEMI TRIGGER
		self.targetSequence[self.currentTarget*2-1].targetVehicle.triggerId = id'''

		#debug
		'''for obj in self.targetSequence:
			#log.output("linkTargetVehicledebugA" + obj.templateName )
			if obj.targetVehicle == None:
				log.output("\"DEBUG:No spawning target vehicle on " + obj.templateName + "\"")
			else: log.output("\"DEBUG:target vehicle on " + obj.templateName + " is " + obj.targetVehicle.templateName + "\"")
		if g_debug:
			print "A:" + host.rcon_invoke("Object.listObjectsofTemplate " +TARGETNAME_A)
			print "B:" + host.rcon_invoke("Object.listObjectsofTemplate " +TARGETNAME_B)'''			
		#self.gameState = 1
		if not (Afound and Bfound): timer.once(TIME_RETRY, self.linkTargetVehicle)
		else: self.updateCpState()
	
	#get targetState A or B; target is string 'A' or 'B'
	'''def getTargetState(self, target):
		targetState = None
		if target == 'A': targetState = self.targetAState
		elif target == 'B': targetState = self.targetBState
		else:#should not happen
			log.output("Error: getTargetState(target) receives in valid target %s" % target)	
		return targetState'''
		
	#get targetState A or B; target is object or string 'A' or 'B'
	def getTargetState(self, target):
		targetState = None
		if target == 'A': targetState = self.targetAState
		elif target == 'B': targetState = self.targetBState
		#elif target == self.targetAState.object: targetState = self.targetAState
		#elif target == self.targetBState.object: targetState = self.targetBState
		elif hasattr(target, 'templateName') and target.templateName == TARGETNAME_A: targetState = self.targetAState
		elif hasattr(target, 'templateName') and target.templateName == TARGETNAME_B: targetState = self.targetBState
		else:#should not happen
			log.output("Error: getTargetState(target) receives invalid target %s" % target)	
		return targetState
	
	#add C4 on target, target is indicated by targetState
	def addC4OnTargetVehicle(self, currentPlayer, targetState):
		try:
			if g_debug: log.output("debugaddC4OnTargetVehicle")
			targetVehicle = targetState.object
			if not targetVehicle.isValid():
				if g_debug: log.output("addC4OnTargetVehicle: targetVehicle %s Not valid!" % targetState.object.templateName)
				return
			if targetState == self.targetAState: target = 'A'
			elif targetState == self.targetBState: target = 'B'
			else: return
			if targetState.c4object == None and targetState.occupyingPlayer == currentPlayer and currentPlayer.getTeam() == self.attackTeam and abs(host.timer_getWallTime() - targetState.playerEnterAt - C4_PLACE_DELAY) <=0.1:
				#spawnpos = (TARGET_SPAWN_HEIGHT * 0.6, TARGET_SPAWN_HEIGHT * 1.2, TARGET_SPAWN_HEIGHT * 0.6)
				targetpos = targetVehicle.getPosition()
				c4pos = (targetpos[0] - 0.0, targetpos[1] + 1.64, targetpos[2] + 0.0)
				obj = self.addObjectOnTeam(C4OBJECTNAME, c4pos, (90.0, 0.0, 0.0), 0)
				#timer.once(FIND_TARGET_DELAY, self.linkC4ToTargetVehicle, targetVehicle)
				targetState.c4object = obj				
				targetState.c4placeplayer = currentPlayer
				self.clearOccupyingPlayer(targetState)
				#player score
				addScore(targetState.c4placeplayer, SCORE_PLACEC4, RPL)
				#message
				#host.rcon_invoke("game.sayAll \"Bomb placed on target " + target + " by player " + targetState.c4placeplayer.getName() + " !\"")
				host.rcon_invoke("game.sayAll \"" + targetState.c4placeplayer.getName() + " has PLANTED the bomb at " + target + "!\"")
				MSG_bombplace(targetState.c4placeplayer)
				#event
				aiArty.eventNotify(self.getDefenseTeam(), aiArty.EVENT_C4_PLACED, targetpos)
				
			if g_debug: log.output("debugaddC4OnTargetVehicleEnd")
		except:
			ExceptionOutput()

	'''def linkC4ToTargetVehicle(self, targetVehicle):
		log.output("debuglinkC4")
		c4found = False
		pcos = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.PlayerControlObject')
		if targetVehicle.c4object != None or not targetVehicle.occupyingPlayer: return
		for obj in pcos:
			if not obj.isValid() or obj.getIsWreck(): continue
			#log.output(""+ "%s" % self.getRoughDistance(obj.getPosition(), (0.0, TARGET_SPAWN_HEIGHT * 1.2, 0.0)))
			if obj.templateName == C4OBJECTNAME:# and self.getRoughDistance(obj.getPosition(), (0.0, TARGET_SPAWN_HEIGHT * 1.2, 0.0)) < 1:
				if not hasattr(obj, 'hasLink') or obj.hasLink == False: obj.hasLink = True
				else: continue
				log.output(" debuglinkC4Success")
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
		if not c4found: timer.once(TIME_RETRY, self.linkC4ToTargetVehicle, targetVehicle)'''
	
	#disarm C4 on target, target is indicated by targetState
	def disarmC4OnTargetVehicle(self, currentPlayer, targetState):
		log.output("debugdisarmC4")
		targetVehicle = targetState.object
		if targetState == self.targetAState: target = 'A'
		elif targetState == self.targetBState: target = 'B'
		else: return
		if not targetState.destroyed and targetState.occupyingPlayer == currentPlayer and currentPlayer.getTeam() == self.defenseTeam and targetState.c4object != None and abs(host.timer_getWallTime() - targetState.playerEnterAt - C4_DISARM_DELAY) <=0.1:
			log.output("debugdisarmC4Success")
			#targetState.c4object.setPosition((TARGET_SPAWN_HEIGHT * 0.6, TARGET_SPAWN_HEIGHT * 1.5, TARGET_SPAWN_HEIGHT * 0.6))
			#targetState.c4object.delete() #this make c4 explode...
			targetState.c4object.setPosition((10000.0,10000.0,10000.0))
			targetState.c4object.delete()
			targetState.c4object = None
			self.clearOccupyingPlayer(targetState)
			#player score
			addScore(currentPlayer, SCORE_DISARMC4, RPL)
			#message
			MSG_bombdisarm(currentPlayer)
			#host.rcon_invoke("game.sayAll \"Bomb on target " + target + " disarmed by player" + currentPlayer.getName() + " !\"")
			host.rcon_invoke("game.sayAll \"" + currentPlayer.getName() + " has DISARMED the bomb at " + target + "!\"")
			MSG_placerbombdisarmed(targetState.c4placeplayer)
			targetState.c4placeplayer = None
			
	#message methods
	def c4PlaceProcess25(self, currentPlayer, targetState):
		#targetState = self.getTargetState()
		if targetState.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetState.playerEnterAt - C4_PLACE_DELAY * 0.25) <= 0.1:
			MSG_c4Process25(currentPlayer)
			
	def c4PlaceProcess50(self, currentPlayer, targetState):
		#targetState = self.getTargetState()
		if targetState.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetState.playerEnterAt - C4_PLACE_DELAY * 0.5) <= 0.1:
			MSG_c4Process50(currentPlayer)
			
	def c4PlaceProcess75(self, currentPlayer, targetState):
		#targetState = self.getTargetState()
		if targetState.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetState.playerEnterAt - C4_PLACE_DELAY * 0.75) <= 0.1:
			MSG_c4Process75(currentPlayer)
			
	def c4DisarmProcess25(self, currentPlayer, targetState):
		#targetState = self.getTargetState(targetState)
		if targetState.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetState.playerEnterAt - C4_DISARM_DELAY * 0.25) <= 0.1:
			MSG_c4Process25(currentPlayer)
			
	def c4DisarmProcess50(self, currentPlayer, targetState):
		#targetState = self.getTargetState(targetState)
		if targetState.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetState.playerEnterAt - C4_DISARM_DELAY * 0.5) <= 0.1:
			MSG_c4Process50(currentPlayer)
			
	def c4DisarmProcess75(self, currentPlayer, targetState):
		#targetState = self.getTargetState(targetState)
		if targetState.occupyingPlayer == currentPlayer and abs(host.timer_getWallTime() - targetState.playerEnterAt - C4_DISARM_DELAY * 0.75) <= 0.1:
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
		
	def getControlPointIdString(self, cp):
		host.rcon_invoke("ObjectTemplate.activeSafe ControlPoint " + cp.templateName)
		cpId = host.rcon_invoke("ObjectTemplate.controlPointId").split("\n")[0]
		#if g_debug: print str(type(cpId))
		if g_debug: print cp.templateName + "\'s cpId is " + cpId
		return cpId #note:cpId is a string
	
	'''def addObjectOnCp(self, templateName, cp, position, rotation):
		log.output("debugaddObjectOnCp" + cp.templateName)
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
			#"Object.setControlPointId " + self.getControlPointIdString(cp),
			#"Object.layer %s" % self.currentTarget
			#"Object.delete"
		]
		cmds = spawnerCmds + createCmds
		if g_debug: print cmds
		for cmd in cmds:
			host.rcon_invoke(cmd)	'''
	
	#actually team do not work -- just spawn an object(Replaced with BF2Object)
	def addObjectOnTeam(self, templateName, position, rotation, team=0):
		'''spawnerName = "bf2obj_" + templateName
		
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
			host.rcon_invoke(cmd)'''
		#log.output('addObjectOnTeam')
		obj = BF2Object(templateName)
		obj.setPosition(position)
		obj.setRotation(rotation)
		return obj
		
	def getVectorDistance(self, pos1, pos2):
		diffVec = [0.0, 0.0, 0.0]
		diffVec[0] = math.fabs(pos1[0] - pos2[0])
		diffVec[1] = math.fabs(pos1[1] - pos2[1])
		diffVec[2] = math.fabs(pos1[2] - pos2[2])
	 
		return math.sqrt(diffVec[0] * diffVec[0] + diffVec[1] * diffVec[1] + diffVec[2] * diffVec[2])
	
	#faster calculation
	def getRoughDistance(self, pos1, pos2):
		return math.fabs(pos1[0] - pos2[0]) + math.fabs(pos1[1] - pos2[1]) + math.fabs(pos1[2] - pos2[2])	
		
	#trigger methods
	#this should be the only method that sets targetState.occupyingPlayer!!
	def startC4Operation(self, player, targetState):
		if player.killed or targetState.occupyingPlayer!=None: return
		#targetState.occupyingPlayer = player
		if targetState == self.targetAState: target = 'A'
		elif targetState == self.targetBState: target = 'B'
		else: return
		if targetState.c4object == None and player.getTeam() == self.getAttackTeam():
			targetState.occupyingPlayer = player
			host.rcon_invoke("game.sayAll \"%s is PLANTING the bomb on %s\"" % (player.getName(), target))
			targetState.playerEnterAt = host.timer_getWallTime()
			timer.once(C4_PLACE_DELAY * 0.25, self.c4PlaceProcess25, player, targetState)
			timer.once(C4_PLACE_DELAY * 0.5, self.c4PlaceProcess50, player, targetState)
			timer.once(C4_PLACE_DELAY * 0.75, self.c4PlaceProcess75, player, targetState)
			timer.once(C4_PLACE_DELAY, self.addC4OnTargetVehicle, player, targetState)
			MSG_bombplacewait(player)
			aiArty.eventNotify(self.getDefenseTeam(), aiArty.EVENT_C4_OPERATING, targetState.object.getPosition())
			#notify bot to defend by lowering the flag a bit
			if targetState == self.targetAState:
				self.targetSequence[self.currentTarget*2-2].cp_setParam('takeOverChangePerSecond',-0.0001)
			elif targetState == self.targetBState:
				self.targetSequence[self.currentTarget*2-1].cp_setParam('takeOverChangePerSecond',-0.0001)
		elif targetState.c4object != None and player.getTeam() == self.getDefenseTeam():
			targetState.occupyingPlayer = player
			host.rcon_invoke("game.sayAll \"%s is DISARMING the bomb on %s\"" % (player.getName(), target))
			targetState.playerEnterAt = host.timer_getWallTime()
			timer.once(C4_DISARM_DELAY * 0.25, self.c4DisarmProcess25, player, targetState)
			timer.once(C4_DISARM_DELAY * 0.5, self.c4DisarmProcess50, player, targetState)
			timer.once(C4_DISARM_DELAY * 0.75, self.c4DisarmProcess75, player, targetState)
			timer.once(C4_DISARM_DELAY, self.disarmC4OnTargetVehicle, player, targetState)
			MSG_bombdisarmwait(player)
			aiArty.eventNotify(self.getAttackTeam(), aiArty.EVENT_C4_OPERATING, targetState.object.getPosition())
	
	#target can only be occupied by attackTeam when c4's not placed and by defenseTeam when c4 is placed
	def canOccupyTarget(self, targetState, player):
		return (targetState.c4object == None and player.getTeam() == self.getAttackTeam()) or (targetState.c4object != None and player.getTeam() == self.getDefenseTeam())
	
	def clearOccupyingPlayer(self, targetState):
		if targetState.occupyingPlayer:
			targetState.occupyingPlayer = None
			#notify bot
			if targetState == self.targetAState:
				self.targetSequence[self.currentTarget*2-2].cp_setParam('takeOverChangePerSecond',0)
			elif targetState == self.targetBState:
				self.targetSequence[self.currentTarget*2-1].cp_setParam('takeOverChangePerSecond',0)
			self.findPlayerToOccupy(targetState)
			
	def findPlayerToOccupy(self, targetState):
		for p in targetState.playersInRange:
			#check if the player is still in range
			if not p.killed and self.getVectorDistance(p.getVehicle().getPosition(), targetState.object.getPosition()) < TRIGGER_RADIUS: 
				if self.canOccupyTarget(targetState, p):
					self.startC4Operation(p, targetState)
					break
				
	def enterTargetRange(self, targetState, player):	
		if g_echooutput: log.output("player %s enterTargetRange" % player.getName())
		if not player in targetState.playersInRange: targetState.playersInRange.append(player)
		else: return
		if targetState.occupyingPlayer == None:
			self.startC4Operation(player, targetState)
		#messages
		elif targetState.occupyingPlayer.getTeam() == player.getTeam() and targetState.occupyingPlayer != player: 
			#if g_echooutput: log.output("debugfriendlyOperation")
			MSG_friendlyOperation(player)
		elif targetState.occupyingPlayer.getTeam() != player.getTeam():
			#if g_echooutput: log.output("debugenemyOperation")
			MSG_enemyOperation(player)
		
	def exitTargetRange(self, targetState, player):	
		if g_echooutput: log.output("player %s exitTargetRange" % player.getName())
		if player in targetState.playersInRange: targetState.playersInRange.remove(player)
		else: return
		if targetState.occupyingPlayer == player:
			self.clearOccupyingPlayer(targetState)
			#try to find other players to occupy(done in clearOccupyingPlayer)
			#if len(targetState.playersInRange)>0:
				#targetState.occupyingPlayer = targetState.occupyingPlayer[0]	
			#self.findPlayerToOccupy(targetState)
			#message
			if self.canOccupyTarget(targetState, player):
				host.rcon_invoke("game.sayAll \"" + player.getName() + " left the bomb site, operation failed!\"")
				if not player.killed: MSG_warnleaveseat(player)	
				eventTeam = (player.getTeam()==1) and 2 or 1
				aiArty.eventDelete(eventTeam, aiArty.EVENT_C4_OPERATING, targetState.object.getPosition())
		#message
		'''elif targetState.occupyingPlayer and targetState.occupyingPlayer.getTeam() != player.getTeam():
			#if g_echooutput: log.output("debugenemyOperation")
			MSG_enemyOperation(player)'''
		
	# called when someone enters or exits target radius
	def onTargetTrigger(self, triggerId, targetObj, vehicle, enter, userData):
		try:
			if g_debug: log.output("debugonTargetTrigger: triggerId=%s" % triggerId)
			if not targetObj.isValid(): 
				if g_echooutput: log.output("debugInvalidTargetTrigger")
				return
			if vehicle and vehicle.getParent(): return
			
			playersInVehicle = None	
			if vehicle:
				playersInVehicle = vehicle.getOccupyingPlayers()
			
			#targetState = self.getTargetState(userData)#use userData to specify target type('A','B')
			'''if targetObj == self.targetAState.object: targetState = self.targetAState
			elif targetObj == self.targetBState.object: targetState = self.targetBState
			else: return'''
			targetState = self.getTargetState(targetObj)
			if not targetState or targetState.destroyed: return
			
			#check distance
			if enter and self.getVectorDistance(vehicle.getPosition(), targetObj.getPosition()) > TRIGGER_RADIUS+5: 
				if g_debug: log.output("Invalid Trigger: Too far away!")
				for player in playersInVehicle:
					self.exitTargetRange(targetState, player) 
				return
			
			#if g_debug: log.output("debugonTargetTriggerA")
			#if the occupyingPlayer does not meet condition any more, make him exit(may not be needed in perfect condition)
			if targetState.occupyingPlayer and (targetState.occupyingPlayer.killed or not targetState.occupyingPlayer.getDefaultVehicle() == targetState.occupyingPlayer.getVehicle()):
				'''if len(targetObj.playersInRange) == 0:
					if not targetState.occupyingPlayer in playersInVehicle:
						log.output("debugClearOccupyingPlayer")
						prevplayer = targetState.occupyingPlayer
						targetState.occupyingPlayer = None
						checkPlayerInTargetAllyFirst(targetState, prevplayer)
				elif targetState.occupyingPlayer.killed: targetState.occupyingPlayer = targetState.playersInRange[0]'''
				self.exitTargetRange(targetState, targetState.occupyingPlayer) 
			#if g_debug: log.output("debugonTargetTriggerB")
			if enter:
				for player in playersInVehicle:
					#must be on foot or inside target object(this feature may be removed)
					#if g_debug: log.output("debugonTargetTriggerC1")
					if not player.killed and player.getDefaultVehicle() == player.getVehicle() or player.getVehicle() == targetState.object: #using bf2.triggerManager.getObjects(targetState.triggerId) causes game crash
						#if g_debug: log.output("debugonTargetTriggerD1")
						self.enterTargetRange(targetState, player)
			else:
				for player in playersInVehicle:
					#may not need this
					#if g_debug: log.output("debugonTargetTriggerC2")
					if not (player.getVehicle().templateName == TARGETNAME_A or player.getVehicle().templateName == TARGETNAME_B):			
						#if g_debug: log.output("debugonTargetTriggerD2")
						self.exitTargetRange(targetState, player) 
			if g_debug: log.output("debugonTargetTriggerEnd")
		except:
			ExceptionOutput()
		
	def onPlayerDeathRush(self, victim, vehicle):		
		try:
			# punish attack team with one ticket (bug)
			if self.gameState != 1: return
			if victim != None:
				team = victim.getTeam()
				if team == self.getAttackTeam():
					teamTickets = bf2.gameLogic.getTickets(team)
					teamTickets -= 1
					bf2.gameLogic.setTickets(team, teamTickets)
			'''
			# check if it was the last player
			foundLivingPlayer = False
			for p in bf2.playerManager.getPlayers():
				if p != victim and p.getTeam() == victim.getTeam() and p.isAlive():
					foundLivingPlayer = True
			
			if not foundLivingPlayer:
				updateTicketLoss()'''
			#if vehicle.templateName == TARGETNAME_A or vehicle.templateName == TARGETNAME_B:
			'''target = getOccupyingTargetV(vehicle)
			if target != None:
				checkPlayerInTargetAllyFirst(target, victim)'''
		except:
			ExceptionOutput()
		


	def onPlayerKilledRush(self, victim, attacker, weapon, assists, object):
		try:
			if victim: 	
				victim.killed = True
				target = self.getOccupyingTarget(victim)
				if target != None:
					self.onTargetTrigger(-1, target, victim.getVehicle(), False, None)
					#checkPlayerInTargetAllyFirst(target, victim)
				# give defend score if killing enemy within cp radius
				if g_debug: log.output("debugonPlayerKilledRushA")
				if attacker != None and attacker.getTeam() != victim.getTeam():
					#if g_debug: log.output("debugonPlayerKilledRushB")
					if target != None and self.canOccupyTarget(self.getTargetState(target),victim):
						#if g_debug: log.output("debugonPlayerKilledRushC")
						attacker.score.cpDefends += 1
						#if g_debug: log.output("debugonPlayerKilledRushD")
						addScore(attacker, SCORE_DEFEND, RPL)
						bf2.gameLogic.sendGameEvent(attacker, 12, 1) #12 = Conquest, 1 = Defend
				if g_debug: log.output("debugonPlayerKilledRushEnd")
		except:
			ExceptionOutput()	
				
				
	def onPlayerRevivedRush(self, victim, attacker):
		try:
			if victim:
				victim.killed = False
				target = self.getOccupyingTarget(victim)
				if target != None:
					self.onTargetTrigger(-1, target, victim.getVehicle(), True, None)
		except:
			ExceptionOutput()
		
		
	def onPlayerSpawnRush(self, player, soldier):
		try:
			player.killed = False		
		except:
			ExceptionOutput()
		
	def onEnterVehicleRush(self, player, vehicle, freeSoldier = False):
		try:
			#if g_debug: log.output("debugonEnterVehicleRush")
			target = self.getOccupyingTarget(player)
			if target != None:
				if vehicle == target: #enter target vehicle
					#self.onTargetTrigger(-1, target, player.getVehicle(), True, None)
					pass
				else: #enter other vehicle(exit target)
					self.onTargetTrigger(-1, target, player.getVehicle(), False, None)
		except:
			ExceptionOutput()

	def onExitVehicleRush(self, player, vehicle):
		try:
			#if g_debug: log.output("debugonExitVehicleRush")
			target = self.getOccupyingTarget(player)
			if target != None:
				if vehicle != target and player.getVehicle() == player.getDefaultVehicle(): 
					self.onTargetTrigger(-1, target, player.getVehicle(), True, None)
					#checkPlayerInTargetAllyFirst(target, player)
		except:
			ExceptionOutput()

	def onVehicleDestroyedRush(self, vehicle, attacker):
		try:
			if g_debug: log.output("onVehicleDestroyedRush: vehicletemp: %s" % vehicle.templateName)
			if vehicle.templateName == TARGETNAME_A and not self.targetAState.destroyed and vehicle == self.targetAState.object:
				host.rcon_invoke("game.sayTeam %d \"We have destroyed A!\"" % self.getAttackTeam())
				host.rcon_invoke("game.sayTeam %d \"The enemy has destroyed A!\"" % self.getDefenseTeam())
				#vehicle.occupyingPlayer = None
				#vehicle.destroyed = True
				log.output("debugTargetADestroyed")
				#bf2.triggerManager.destroy(vehicle.triggerId)
				attacker = self.targetAState.c4placeplayer 
				self.targetAState.destroyed = True
				self.targetAState.c4object = None
				self.lastDestroyTargetTime = host.timer_getWallTime()
				#bf2.triggerManager.destroy(self.targetAState.triggerId) #triggerId not found?(cause crash)
				self.toNextTarget()
				self.updateCpState()
				if attacker:
					#attacker get score
					host.rcon_invoke("game.sayAll \"" + attacker.getName() + " destroyed A!\"")
					if attacker.getTeam() == self.getAttackTeam():
						addScore(attacker, SCORE_DESTROYTARGET, RPL)
						bf2.gameLogic.sendGameEvent(attacker, 10, 5) #10 = Replenish, 5 = DestroyStrategic
					else: addScore(attacker, SCORE_DESTROYFRIENDLYTARGET, RPL)
			elif vehicle.templateName == TARGETNAME_B and not self.targetBState.destroyed and vehicle == self.targetBState.object:
				host.rcon_invoke("game.sayTeam %d \"We have destroyed B!\"" % self.getAttackTeam())
				host.rcon_invoke("game.sayTeam %d \"The enemy has destroyed B!\"" % self.getDefenseTeam())
				#vehicle.occupyingPlayer = None
				#vehicle.destroyed = True
				log.output("debugTargetBDestroyed")
				#bf2.triggerManager.destroy(vehicle.triggerId)
				attacker = self.targetBState.c4placeplayer 
				self.targetBState.destroyed = True
				self.targetBState.c4object = None
				self.lastDestroyTargetTime = host.timer_getWallTime()
				#bf2.triggerManager.destroy(self.targetBState.triggerId) #triggerId not found?(cause crash)
				self.toNextTarget()
				self.updateCpState()
				if attacker:
					#attacker get score
					host.rcon_invoke("game.sayAll \"" + attacker.getName() + " destroyed B!\"")
					if attacker.getTeam() == self.getAttackTeam():
						addScore(attacker, SCORE_DESTROYTARGET, RPL)
						bf2.gameLogic.sendGameEvent(attacker, 10, 5) #10 = Replenish, 5 = DestroyStrategic
					else: addScore(attacker, SCORE_DESTROYFRIENDLYTARGET, RPL)
		except:
			ExceptionOutput()
				
	def targetCheck(self):
		try:
			if self.gameState != 1: return
			#for cp in self.targetSequence:
			#	calcTakeOverChangePerSecondRush(cp)
			#self.toNextTarget()
			self.updateTicketLoss()
			self.updateCpState()
		except:
			ExceptionOutput()
		
	# find target that player is occupying, if any
	# an alt way: use self.targetAState.playersInRange
	def getOccupyingTarget(self, player):
		'''if not player: return None
		if g_echooutput: log.output("debuggetOccupyingTarget")
		if player.getVehicle().templateName == TARGETNAME_A or player.getVehicle().templateName == TARGETNAME_B: return player.getVehicle()
		if not self.targetAState.destroyed:
			pcos = bf2.triggerManager.getObjects(self.targetAState.triggerId)
			if player.getDefaultVehicle() in pcos:
				return self.targetAState.object		
		if not self.targetBState.destroyed:
			pcos = bf2.triggerManager.getObjects(self.targetBState.triggerId)
			if player.getDefaultVehicle() in pcos:
				return self.targetBState.object
		return None'''
		if player in self.targetAState.playersInRange: return self.targetAState.object
		elif player in self.targetBState.playersInRange: return self.targetBState.object
		else: 
			#check distance
			if not self.targetAState.destroyed:
				if g_debug: log.output("getOccupyingTarget: looking for trigger at A..")
				try:
					pcos = bf2.triggerManager.getObjects(self.targetAState.triggerId) #may cause "no such trigger"
					if player.getDefaultVehicle() in pcos:
						if g_debug: log.output("getOccupyingTarget: Found at A")
						return self.targetAState.object		
				except:
					if g_debug: log.output("getOccupyingTarget: Invalid triggerId %s" % self.targetAState.triggerId)
					return None
			if not self.targetBState.destroyed:
				if g_debug: log.output("getOccupyingTarget: looking for trigger at B..")
				try:
					pcos = bf2.triggerManager.getObjects(self.targetBState.triggerId)
					if player.getDefaultVehicle() in pcos:
						if g_debug: log.output("getOccupyingTarget: Found at B")
						return self.targetBState.object
				except:
					if g_debug: log.output("getOccupyingTarget: Invalid triggerId %s" % self.targetBState.triggerId)
					return None
			return None

	def getOccupyingTargetV(self, vehicle):
		if not vehicle: return None
		if g_echooutput: log.output("debuggetOccupyingTargetV")
		if vehicle.templateName == TARGETNAME_A or vehicle.templateName == TARGETNAME_B: return vehicle
		if not self.targetAState.destroyed:
			pcos = bf2.triggerManager.getObjects(self.targetAState.triggerId)
			if vehicle in pcos:
				return self.targetAState.object		
		if not self.targetBState.destroyed:
			pcos = bf2.triggerManager.getObjects(self.targetBState.triggerId)
			if vehicle in pcos:
				return self.targetBState.object
		return None
	
	#add ticket loss feature
	def updateTicketLoss(self):
		timePassed = host.timer_getWallTime() - self.lastDestroyTargetTime
		#log.output("timePassed:%s"%timePassed)
		if timePassed > TIME_BEGINTICKETLOSS:
			ticketLossPerSec = -TICKETLOSS_LINEAR * (timePassed - TIME_BEGINTICKETLOSS) - TICKETLOSS_CONST
		else:
			ticketLossPerSec = 0
		bf2.gameLogic.setTicketChangePerSecond(self.getAttackTeam(), ticketLossPerSec)
	
	def writeStatsStartGame(self):
		statFile = open(host.sgl_getModDirectory() + '/stats.log','a')
		mapname = bf2.gameLogic.getMapName()
		gamemode = bf2.serverSettings.getGameMode()
		maxplayer = bf2.serverSettings.getMaxPlayers()
		statFile.write("************************************\n")
		statFile.write("Game Starts at %s\n" % time.strftime("%Y/%m/%d %H:%M:%S"))
		statFile.write("Map: %s - %s %s\n" % (mapname,gamemode,maxplayer))
		statFile.write("Team %s(%s) attack, Team %s(%s) defend\n" % (self.attackTeam,bf2.gameLogic.getTeamName(self.attackTeam),self.defenseTeam,bf2.gameLogic.getTeamName(self.defenseTeam)))
		statFile.close()
		
	def writeStatsEndGame(self):
		statFile = open(host.sgl_getModDirectory() + '/stats.log','a')
		winner = bf2.gameLogic.getWinner()
		if winner==0: return
		t1tick = bf2.gameLogic.getTickets(1)
		t2tick = bf2.gameLogic.getTickets(2)
		statFile.write("Game Ends at %s\n" % time.strftime("%Y/%m/%d %H:%M:%S"))
		statFile.write("Team %s(%s) win!\n" % (winner,bf2.gameLogic.getTeamName(winner)))
		statFile.write("Remaining ticket: %s - %s\n" % (t1tick,t2tick))
		statFile.close()

def getSettingsFromMap():
	mapname = bf2.gameLogic.getMapName()
	gamemode = bf2.serverSettings.getGameMode()
	maxplayer = bf2.serverSettings.getMaxPlayers()
	try:
		return RUSHV2_MAPS[mapname.lower()]
	except:
		log.output("Error reading mapsettings!")
	
rushData = None
	
def init():
	# events hook
	global rushData
	#host.registerGameStatusHandler(onGameStatusChanged)
	aiArty.init(False)
	random_objectspawner.init()
	spawnpoint_protect.init()
	# if host.sgl_getIsAIGame() == 1:
		# host.sh_setEnableCommander(1)
	# else:
		# host.sh_setEnableCommander(0)
	if not rushData:
		rushData = Rush(getSettingsFromMap())
	else:
		rushData.settings = getSettingsFromMap()
		#rushData.__init__(getSettingsFromMap())
	rushData.initGame()
	#host.registerHandler('TimeLimitReached', onTimeLimitReached, 1)	
	global g_debug
	g_debug = 1
	if g_debug: 
		log.init()
		registerRConCommand('output', rcon_debugoutput)
		registerRConCommand('disableoutput', rcon_debugdisableoutput)
		registerRConCommand('boom', rcon_destroytargets)
		#registerRConCommand('feedback', rcon_feedback)
		print "rush_v2.py initialized"
		
def deinit():
	bf2.triggerManager.destroyAllTriggers()
	global rushData
	rushData.deinitGame()
	#rushData = None
	aiArty.deinit()
	random_objectspawner.deinit()
	spawnpoint_protect.deinit()
	#host.unregisterGameStatusHandler(onGameStatusChanged)
	if g_debug: 
		log.deinit()
		print "rush_v2.py deinitialized"
'''
def onTimeLimitReached(value):
	#if time limit reached, the defense wins
	host.sgl_endGame(rushData.getDefenseTeam(), 3)
		
def onGameStatusChanged(status):	
	global rushData
	if status == bf2.GameStatus.Playing: 
		rushData = Rush(settings)
		rushData.startGame()
	else:
		rushData.endGame()
		rushData = None
'''
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
	
#debug
def rcon_debugoutput(self, ctx, cmd):
	global g_echooutput
	g_echooutput = 1
	try:
		if rushData.getCurrentTargetsDown(): log.output("debugcurrentTargetDown")
		#if rushData.getCurrentTargetObjectA().destroyed: log.output("debugTargetADestroyed") 
		if rushData.targetAState.destroyed: log.output("debugrushDataADestroyed") 
		if rushData.getCurrentTargetObjectA().isValid(): 
			log.output("debugTargetAValid") 
			if rushData.getCurrentTargetObjectA().isPlayerControlObject: log.output("isPlayerControlObjectA")
			if rushData.getCurrentTargetObjectA().hasArmor: log.output("hasArmorA")
			if hasattr(rushData.getCurrentTargetObjectA(), "getDamage"): log.output("\"Armor: %s \"" % rushData.getCurrentTargetObjectA().getDamage())
			else: log.output("noAttrgetDamageA")
			if not hasattr(rushData.getCurrentTargetObjectA(), "setDamage"):
				log.output("noAttrsetDamageA")
			if not hasattr(rushData.getCurrentTargetObjectA(), "getOccupyingPlayers"):
				log.output("noAttrgetOccupyingPlayersA")
			if rushData.getCurrentTargetObjectA().getIsWreck(): log.output("debugTargetAIsWreck") 
		#if rushData.getCurrentTargetObjectB().destroyed: log.output("debugTargetBDestroyed")
		if rushData.targetBState.destroyed: log.output("debugrushDataBDestroyed") 
		if rushData.getCurrentTargetObjectB().isValid():
			log.output("debugTargetBValid") 
			if rushData.getCurrentTargetObjectB().isPlayerControlObject: log.output("isPlayerControlObjectB")
			if rushData.getCurrentTargetObjectB().hasArmor: log.output("hasArmorB")
			if hasattr(rushData.getCurrentTargetObjectB(), "getDamage"): log.output("\"Armor: %s \"" % rushData.getCurrentTargetObjectA().getDamage())
			else: log.output("noAttrgetDamageB")
			if not hasattr(rushData.getCurrentTargetObjectB(), "setDamage"):
				log.output("noAttrsetDamageB")
			if not hasattr(rushData.getCurrentTargetObjectB(), "getOccupyingPlayers"):
				log.output("noAttrgetOccupyingPlayersB")
			if rushData.getCurrentTargetObjectB().getIsWreck(): log.output("debugTargetBIsWreck") 
		'''for cp in rushData.getTargets():
			log.output("\"" + cp.templateName + ": team %s " % cp.cp_getParam('team')+ " flag %s \"" % cp.cp_getParam('flag'))
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
				else: print "hasOccupyingPlayer"'''
	except:
		ExceptionOutput()
	
	
def rcon_debugdisableoutput(self, ctx, cmd):
	global g_echooutput
	g_echooutput = 0
	
def rcon_destroytargets(self, ctx, cmd):
	global rushData
	log.output("rcon_destroytargets")
	#rconPlayer = ctx.player
	for player in bf2.playerManager.getPlayers():
		if player.getTeam() == rushData.getDefenseTeam():
			# kill all defense players(crash the game..)
			#player.getDefaultVehicle().setDamage(0)
			pass
	# add c4(not functioning)
	# for targetState in (rushData.targetAState, rushData.targetBState):
		# if not targetState.destroyed:
			# targetpos = targetState.object.getPosition()
			# c4pos = (targetpos[0] - 0.0, targetpos[1] + 1.64, targetpos[2] + 0.0)
			# log.output(C4OBJECTNAME + "%s/%s/%s" % c4pos)
			# # obj = rushData.addObjectOnTeam(C4OBJECTNAME, c4pos, (90.0, 0.0, 0.0), 0)
			# # does not spawn???
			# obj = BF2Object(C4OBJECTNAME)
			# obj.setPosition(c4pos)
			# obj.setRotation((90.0, 0.0, 0.0))
			# targetState.c4object = obj
	# to next
	rushData.targetAState.destroyed, rushData.targetBState.destroyed = True, True
	rushData.toNextTarget()
