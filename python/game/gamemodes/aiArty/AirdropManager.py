import host
import bf2
import math, random, types
import log
from artySettings import g_debug
from BF2Object import BF2Object
from timer import timer

class AirdropManager:

	def __init__(self, settings):
		self.settings = settings
		self.team1_supplydrop_ready = True
		self.team2_supplydrop_ready = True
		self.team1_vehicledrop_ready = True
		self.team2_vehicledrop_ready = True
		self.team1_vehicledrop_name = host.rcon_invoke("gameLogic.getTeamDropVehicle 1").strip()
		self.team2_vehicledrop_name = host.rcon_invoke("gameLogic.getTeamDropVehicle 2").strip()
		self.team1_lastSupplydropTime = host.timer_getWallTime()
		self.team2_lastSupplydropTime = host.timer_getWallTime()
		self.team1_lastVehicledropTime = host.timer_getWallTime()
		self.team2_lastVehicledropTime = host.timer_getWallTime()
	
	#disable satellite for SUPPLYDROP_INTERVAL time
	def disableSupplydrop(self, team):
		if team==1: 
			self.team1_supplydrop_ready = False
			self.team1_lastSupplydropTime = host.timer_getWallTime()
		elif team==2: 
			self.team2_supplydrop_ready = False
			self.team2_lastSupplydropTime = host.timer_getWallTime()
		timer.once(self.settings["SUPPLYDROP_INTERVAL"], self.enableSupplydrop, team)
		
	def enableSupplydrop(self, team):
		if team==1: 
			self.team1_supplydrop_ready = True
		elif team==2: 
			self.team2_supplydrop_ready = True
	
	#disable satellite for SUPPLYDROP_INTERVAL time
	def disableVehicledrop(self, team):
		if team==1: 
			self.team1_vehicledrop_ready = False
			self.team1_lastVehicledropTime = host.timer_getWallTime()
		elif team==2: 
			self.team2_vehicledrop_ready = False
			self.team2_lastVehicledropTime = host.timer_getWallTime()
		timer.once(self.settings["VEHICLEDROP_INTERVAL"], self.enableVehicledrop, team)
		
	def enableVehicledrop(self, team):
		if team==1: 
			self.team1_vehicledrop_ready = True
		elif team==2: 
			self.team2_vehicledrop_ready = True
	
	def isSupplydropAvailable(self, team):
		if team==1:
			return self.team1_supplydrop_ready
		elif team==2:
			return self.team2_supplydrop_ready
		else:
			return False
	
	def isVehicledropAvailable(self, team):
		if team==1:
			return self.team1_vehicledrop_ready
		elif team==2:
			return self.team2_vehicledrop_ready
		else:
			return False
	
	def startSupplydrop(self, team, position):
		if not self.isSupplydropAvailable(team): 
			if g_debug: log.output("Supplydrop not available!")
			return False
		objName = (team==1) and self.settings["TEAM1_SUPPLYDROP_NAME"] or self.settings["TEAM2_SUPPLYDROP_NAME"]
		if g_debug: log.output("Dropping %s " % objName + "at %s/%s/%s" % position)
		self.disableSupplydrop(team)
		supplyObj = BF2Object(objName)
		newPos = self.rndDevPosition(position, self.settings["SUPPLYDROP_DEVIATION_RADIUS_MIN"], self.settings["SUPPLYDROP_DEVIATION_RADIUS"], self.settings["SUPPLYDROP_SPAWN_HEIGHT"])
		supplyObj.setPosition(newPos)
		return True
	
	def startVehicledrop(self, team, position):
		if not self.isVehicledropAvailable(team):
			if g_debug: log.output("Vehicledrop not available!")
			return False
		objName = (team==1) and self.team1_vehicledrop_name or self.team2_vehicledrop_name
		objName += self.settings["VEHICLEDROP_NAME_SUFFIX"]
		if g_debug: log.output("Dropping %s " % objName + "at %s/%s/%s" % position)
		self.disableVehicledrop(team)
		vehicleObj = BF2Object(objName)
		newPos = self.rndDevPosition(position, self.settings["VEHICLEDROP_DEVIATION_RADIUS_MIN"], self.settings["VEHICLEDROP_DEVIATION_RADIUS"], self.settings["VEHICLEDROP_SPAWN_HEIGHT"])
		vehicleObj.setPosition(newPos)
		return True
	
	#return a random deviation position
	def rndDevPosition(self, position, rndMin, rndMax, height):
		r = random.random()*(rndMax-rndMin) + rndMin
		th = random.random()*2*math.pi
		return (position[0] + r*math.cos(th), \
				position[1] + height,\
				position[2] + r*math.sin(th))
