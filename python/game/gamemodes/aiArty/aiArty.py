#aiArty.py v1.0 (for conquest) beta
#By worldlife

#LEGACY CODE

import host
import bf2
import math, random
import log
from BF2Object import BF2Object
from bf2 import g_debug

TEAM1_ARTY_NAME = "ars_d30"
TEAM2_ARTY_NAME = "usart_lw155"
TEAM1_ARTY_SPAWNER_NAME = "pyart_expobj"
TEAM2_ARTY_SPAWNER_NAME = "pyart_expobj"
ARTY_SPAWN_HEIGHT = 1000.0
ARTY_SPAWN_HEIGHT_RANDOM = 500.0
ARTY_DEVIATION_RADIUS = 20.0
ARTY_BURSTSIZE = 5 #artillery shots per round
ARTY_FIRE_INTERVAL = 2.0 #interval between artillery shot
ARTY_ROUND_INTERVAL = 10.0 #interval between artillery rounds
RANDOM_ARTY = 1 #percentage of artillery after cp status change

LOOP_INTERVAL = 1.0
loopTimer = None

#global
g_artys = []
team1_arty_num = 0
team2_arty_num = 0
team1_arty_ready = True
team2_arty_ready = True
team1_hascommander = False
team2_hascommander = False

def init():
	host.registerGameStatusHandler(gameStatusChanged)
	global g_debug
	g_debug = 1
	if g_debug: 
		log.init()
		print "aiArty.py initialized"

def deinit():
	host.unregisterGameStatusHandler(gameStatusChanged)
	global g_artys
	global team1_arty_num
	global team2_arty_num
	global team1_arty_ready
	global team2_arty_ready
	global team1_hascommander
	global team2_hascommander
	g_artys = []
	team1_arty_num = 0
	team2_arty_num = 0
	team1_arty_ready = True
	team2_arty_ready = True
	team1_hascommander = False
	team2_hascommander = False
	if g_debug: 
		log.deinit()
		print "aiArty.py deinitialized"
	
def gameStatusChanged(status):
	
	global loopTimer 
	global team1_arty_num
	global team2_arty_num
	global g_artys
	if status == bf2.GameStatus.Playing:
		if team1_arty_num==0 and team2_arty_num==0:
			for pco in bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.PlayerControlObject'):	
				if not pco in g_artys:
					if pco.templateName == TEAM1_ARTY_NAME:
						if g_debug: log.output("Arty for team 1 found!")
						g_artys.append(pco)
						team1_arty_num+=1
					elif pco.templateName == TEAM2_ARTY_NAME:
						if g_debug: log.output("Arty for team 2 found!")
						g_artys.append(pco)
						team2_arty_num+=1
		#host.registerHandler('VehicleDestroyed', onVehicleDestroyed)
		#host.registerHandler('ControlPointChangedOwner', onCPStatusChange)
		host.registerHandler('ChangedCommander', onCommanderChanged)
		#host.registerHandler('PlayerRepairPoint', onVehicleRepaired)
		if not loopTimer: loopTimer = loop(LOOP_INTERVAL, loopScan) #not used now
				
	elif status == bf2.GameStatus.EndGame:
		
		if loopTimer :
			loopTimer.abort()
			loopTimer = None

def loopScan():
	if team1_arty_num!=0 and team1_arty_ready:
		pos = findPosForArty(1)
		if pos:
			startArtyAt(1, pos)
			#disableArty(1)
	if team2_arty_num!=0 and team2_arty_ready:
		pos = findPosForArty(2)
		if pos:
			startArtyAt(2, pos)
			#disableArty(2)

#disable artillery for ARTY_ROUND_INTERVAL time
def disableArty(team):
	if team==1: 
		global team1_arty_ready
		team1_arty_ready = False
	elif team==2: 
		global team2_arty_ready
		team2_arty_ready = False
	timer.once(ARTY_ROUND_INTERVAL, enableArty, team)
	
def enableArty(team):
	if team==1: 
		global team1_arty_ready
		team1_arty_ready = True
	elif team==2: 
		global team2_arty_ready
		team2_arty_ready = True

#scan all player positions/cp state and find the best place to throw artillery			
def findPosForArty(team):
	pass

def renewArtyState():
	global team1_arty_num
	global team2_arty_num
	team1_arty_num=0
	team2_arty_num=0
	#for pco in g_artys: #unknown bug
	for pco in bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.PlayerControlObject'):	
		if pco.getIsWreck() or not pco.getIsRemoteControlled(): #or pco.getDamage()<0.01
			pass
			#if pco.getIsRemoteControlled() and g_debug: log.output(pco.templateName + " at %s/%s/%s" % pco.getPosition() + " isWreck = %s armor = %s" % (pco.getIsWreck(),pco.getDamage()))
		else:
			#if g_debug: log.output(pco.templateName + " at %s/%s/%s" % pco.getPosition() + " isWreck = %s armor = %s" % (pco.getIsWreck(),pco.getDamage()))
			if hasattr(pco,'getDamage') and pco.getDamage()<0.01 or getVectorDistance((0.0,0.0,0.0),pco.getPosition())<0.1: #exclude error objects
				continue
			if pco.templateName == TEAM1_ARTY_NAME:
				team1_arty_num+=1
			elif pco.templateName == TEAM2_ARTY_NAME:
				team2_arty_num+=1
	if g_debug: log.output("Team 1 arty num: %s; Team 2 arty num: %s" % (team1_arty_num,team2_arty_num))
	if g_debug: log.output("Team 1 arty ready: %s; Team 2 arty ready: %s" % (team1_arty_ready,team2_arty_ready))
	if g_debug: log.output("Team 1 hascommander: %s; Team 2 hascommander: %s" % (team1_hascommander,team2_hascommander))
	
def startArtyAt(team, position):
	if g_debug: log.output("Team %s:" % team + "Requesting artillery strike at %s/%s/%s!" % position)
	renewArtyState()
	has_commander = False
	arty_ready = False
	if team==1:
		has_commander = team1_hascommander
		arty_ready = team1_arty_ready
	else:
		has_commander = team2_hascommander
		arty_ready = team2_arty_ready
	if has_commander or not arty_ready: 
		#if g_debug: log.output("Commander for Team %s on duty!" % team)
		return
	spawnArtyAt(team, position, ARTY_BURSTSIZE)
	disableArty(team)
	
#use team artillery at position	
def spawnArtyAt(team, position, roundsLeft):
	if roundsLeft<=0: 
		#disableArty(team)
		return	
	arty_num = 0
	if team==1:
		arty_num = team1_arty_num
	else:
		arty_num = team2_arty_num
	#arty_ready = (team==1) and team1_arty_ready or team2_arty_ready	
	if arty_num == 0: 
		if g_debug: log.output("No artillery available!")
		return
	arty_spwname = (team==1) and TEAM1_ARTY_SPAWNER_NAME or TEAM2_ARTY_SPAWNER_NAME
	#spawn arty
	for i in range(arty_num):
		artySpw = BF2Object(arty_spwname)
		pos = rndDevPosition(position)
		artySpw.setPosition(pos)
		if g_debug: log.output("Artillery object spawn at %s/%s/%s!" % pos)
	timer.once(ARTY_FIRE_INTERVAL, spawnArtyAt, team, position, roundsLeft-1)

#return a random deviation position
def rndDevPosition(position):
	r = random.random()*ARTY_DEVIATION_RADIUS
	th = random.random()*2*math.pi
	return (position[0] + r*math.cos(th), \
			position[1] + ARTY_SPAWN_HEIGHT + random.random()*ARTY_SPAWN_HEIGHT_RANDOM,\
			position[2] + r*math.sin(th))

#if human commander is on, disable ai artillery			
#Note that this event gives the oppsite team..
def onCommanderChanged(team, oldCommanderPlayerObject, newCommanderPlayerObject):
	global team1_hascommander
	global team2_hascommander
	#if g_debug: log.output("Commander changed!")
	if newCommanderPlayerObject!=None: #new commander on duty
		if g_debug: log.output("Team %s: New commander on duty!" % team)
		if team==2: team1_hascommander = True
		else: team2_hascommander = True
	if oldCommanderPlayerObject!=None: #commander off duty
		if g_debug: log.output("Team %s: Commander off duty!" % team)
		if team==2: team1_hascommander = False
		else: team2_hascommander = False

def isLocal():
	internet = int(host.rcon_invoke("sv.internet"))
	if internet:
		return False
	else:
		return True

# get distance between two positions
def getVectorDistance(pos1, pos2):
	diffVec = [0.0, 0.0, 0.0]
	diffVec[0] = math.fabs(pos1[0] - pos2[0])
	diffVec[1] = math.fabs(pos1[1] - pos2[1])
	diffVec[2] = math.fabs(pos1[2] - pos2[2])
	 
	return math.sqrt(diffVec[0] * diffVec[0] + diffVec[1] * diffVec[1] + diffVec[2] * diffVec[2])
		
def addProjectile(templateName, position, rotation):
		spawnerName = "emitter_" + templateName
		
		spawnerCmds = [
				
			"ObjectTemplate.create Emitter " + spawnerName,
			"ObjectTemplate.createdInEditor 1",
			"ObjectTemplate.floaterMod 0",
			"ObjectTemplate.hasMobilePhysics 0",
			"ObjectTemplate.template " + templateName,
			"ObjectTemplate.intensity CRD_NONE/10/0/0"
		]
		#newpos = (position[0], position[1]+0.5, position[2])
		createCmds = [

			"Object.create " + spawnerName,
			"Object.absolutePosition %s/%s/%s" % position,
			"Object.rotation %s/%s/%s" % rotation,

		]
		
		cmds = spawnerCmds + createCmds
	
		for cmd in cmds:
			host.rcon_invoke(cmd)
		
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

		def __init__(self, time, method, *args):
			self.__dict__['time'] = host.timer_getWallTime() + time
			self.interval = time
			self.alwaysTrigger = 1
			self.method = method
			self.args = args
			host.timer_created(self)

		def __setattr__(self, name, value):
			if name != "time":
				self.__dict__[name] = value

		def onTrigger(self):
			self.method(*self.args)
			self.__dict__['time'] += self.interval

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