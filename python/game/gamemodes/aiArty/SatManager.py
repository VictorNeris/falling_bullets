import host
import bf2
import math, random
import log
from artySettings import g_debug
from timer import timer

class SatManager:

	def __init__(self, settings, playerTracker):
		self.settings = settings
		self.playerTracker = playerTracker
		self.team1_sat_ready = True
		self.team2_sat_ready = True
		self.team1_hasSatellite = True
		self.team2_hasSatellite = True
		self.team1_lastScanTime = host.timer_getWallTime()
		self.team2_lastScanTime = host.timer_getWallTime()
		self.team1_scan_result = {} # {playerindex: (position(vec3), velocity rate(float), object(ref))}
		self.team2_scan_result = {}
	
	#disable satellite for SAT_SCAN_INTERVAL time
	def disableSat(self, team):
		if team==1: 
			self.team1_sat_ready = False
			self.team1_lastScanTime = host.timer_getWallTime()
		elif team==2: 
			self.team2_sat_ready = False
			self.team2_lastScanTime = host.timer_getWallTime()
		timer.once(self.settings["SAT_SCAN_INTERVAL"], self.enableSat, team)
		
	def enableSat(self, team):
		if team==1: 
			self.team1_sat_ready = True
		elif team==2: 
			self.team2_sat_ready = True
	
	def renewSatState(self):
		self.team1_hasSatellite = False
		self.team2_hasSatellite = False
		for pco in bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.PlayerControlObject'):	
			if pco.getIsWreck() or not pco.getIsRemoteControlled(): #or pco.getDamage()<0.01
				pass
				#if pco.getIsRemoteControlled() and g_debug: log.output(pco.templateName + " at %s/%s/%s" % pco.getPosition() + " isWreck = %s armor = %s" % (pco.getIsWreck(),pco.getDamage()))
			else:
				#if g_debug: log.output(pco.templateName + " at %s/%s/%s" % pco.getPosition() + " isWreck = %s armor = %s" % (pco.getIsWreck(),pco.getDamage()))
				if hasattr(pco,'getDamage') and pco.getDamage()<0.01 or self.getVectorDistance((0.0,0.0,0.0),pco.getPosition())<0.1: #exclude error objects
					continue
				if pco.templateName.lower() in self.settings["TEAM1_SATELLITE_NAME"]:
					self.team1_hasSatellite = True
				elif pco.templateName.lower() in self.settings["TEAM2_SATELLITE_NAME"]:
					self.team2_hasSatellite = True
		if g_debug: 
			log.output("Team 1 sat ready: %s; Team 2 sat ready: %s" % (self.team1_sat_ready,self.team2_sat_ready))
			log.output("Team 1 hasSatellite: %s; Team 2 hasSatellite: %s" % (self.team1_hasSatellite,self.team2_hasSatellite))
	
	def isAvailable(self, team):
		self.renewSatState()
		if team==1:
			return self.team1_hasSatellite and self.team1_sat_ready
		elif team==2:
			return self.team2_hasSatellite and self.team2_sat_ready
		else:
			return False
	
	def getLastScanResult(self, team):
		if team==1:
			return self.team1_scan_result
		elif team==2:
			return self.team2_scan_result
		else:
			return
	
	def startSatScan(self, team):
		if not self.isAvailable(team): return False
		if team==1:
			playerInfo = self.team1_scan_result
			enemyTeam = 2
		elif team==2:
			playerInfo = self.team2_scan_result
			enemyTeam = 1
		else:
			return False
		if g_debug: log.output("SatManager: Team %s start satellite scan!" % team)
		playerInfo.clear()
		playerStates = self.playerTracker.playerStates
		if not playerStates: 
			if g_debug: log.output("SatManager: playerTracker not available!")
			return False
		for index in playerStates:
			playerState = playerStates[index]
			if playerState.team == enemyTeam and playerState.alive and playerState.player.getVehicle() and not (playerState.player.getKit() and playerState.player.getKit().templateName in self.settings["SAT_SCAN_EXCLUDE_KITS"]): 
				playerInfo[index] = (playerState.position, playerState.velRate, playerState.player.getVehicle())
		#if g_debug: log.output("SatManager: playerInfo: %s" % playerInfo)
		self.disableSat(team)
		return True
	
	# get distance between two positions
	def getVectorDistance(self, pos1, pos2):
		diffVec = [0.0, 0.0, 0.0]
		diffVec[0] = math.fabs(pos1[0] - pos2[0])
		diffVec[1] = math.fabs(pos1[1] - pos2[1])
		diffVec[2] = math.fabs(pos1[2] - pos2[2])
		 
		return math.sqrt(diffVec[0] * diffVec[0] + diffVec[1] * diffVec[1] + diffVec[2] * diffVec[2])
