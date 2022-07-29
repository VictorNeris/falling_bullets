import host
import bf2
import log
import math, random, types
from exceptionoutput import *
# from collections import namedtuple

g_debug = 1

#globals
g_spawnPointInfoTable = {}
#g_loopTimer = None

# SpawnPointInfo = namedtuple('SpawnPointInfo', ['cpid','position','team'])
# PlayerSpawnInfo = namedtuple('PlayerSpawnInfo', ['spawnTime','spawnPosition'])

class SpawnPointInfo:
	def __init__(self, name, cpid, position, rotation):
		self.name = name
		self.cpid = cpid
		self.position = position
		self.rotation = rotation

#settings
#RANDOM_SPAWNER_SUFFIX = "_rndspw"
LOOP_INTERVAL = 5.0 #
DEFAULT_SPAWN_RATE = 0.5
SPAWNKILL_THRESHOLD_TIME = 10.0
SPAWNKILL_THRESHOLD_DISTANCE = 5.0
SPAWNKILL_DISABLE_TIME = 30.0


def init():
	host.registerGameStatusHandler(onGameStatusChanged)
	#global g_debug
	#g_debug = 1
	if g_debug: 
		log.init()
		print "spawnpoint_protect.py initialized"

def deinit():
	host.unregisterGameStatusHandler(onGameStatusChanged)
	if g_debug: 
		log.deinit()
		print "spawnpoint_protect.py deinitialized"

def onGameStatusChanged(status):

	global g_spawnPointInfoTable#, g_loopTimer
	if status == bf2.GameStatus.Playing: 
		templateNames = getSpawnPointTemplateNames()
		for name in templateNames:
			spawnPoints = bf2.objectManager.getObjectsOfTemplate(name)
			for obj in spawnPoints:
				if g_debug: log.output("SpawnPoint %s at " % obj.templateName + "%s/%s/%s" % obj.getPosition())
				#if obj.templateName.endswith(RANDOM_SPAWNER_SUFFIX):
				g_spawnPointInfoTable[obj] = SpawnPointInfo(obj.templateName, getSpawnPointCPId(obj), obj.getPosition(), obj.getRotation())
		#host.registerHandler('ControlPointChangedOwner', onCPStatusChange)
		host.registerHandler('PlayerSpawn', onPlayerSpawn)
		host.registerHandler('PlayerKilled', onPlayerKilled)
		#g_loopTimer = timer.loop(LOOP_INTERVAL, updateSpawnPointStates)
		#updateSpawnerStates()
		if g_debug: log.output("SpawnPoint Protection System initialized.")
	else:
		g_spawnPointInfoTable = {}
		#g_loopTimer = None
		if g_debug: log.output("SpawnPoint Protection System deinitialized.")

def updateSpawnPointStates():
	for obj in g_spawnPointInfoTable:
		if random.random() < DEFAULT_SPAWN_RATE:
			if g_debug: log.output("Spawner %s with id %s enabled!" % (obj.templateName, g_spawnPointInfoTable[obj].cpid))
			enableSpawnPoint(obj)
		else:
			if g_debug: log.output("Spawner %s with id %s disabled!" % (obj.templateName, g_spawnPointInfoTable[obj].cpid))
			disableSpawnPoint(obj)
		

# called when a control point flag reached top or bottom
def onCPStatusChange(cp, top):
	if cp.cp_getParam('team') == 0:
		if top:
			updateSpawnPointStates()

def onPlayerSpawn(player, soldier):
	if g_debug: 
		log.output("Player Spawn at %s/%s/%s" % soldier.getPosition())
	player.spawnTime = host.timer_getWallTime()
	player.spawnPos = soldier.getPosition()

def onPlayerKilled(victim, attacker, weapon, assists, object):
	try:
		if attacker!=None and victim!=None:# and attacker.getTeam()!=victim.getTeam():
			if g_debug: 
				log.output("Player killed at %s/%s/%s, " % victim.getDefaultVehicle().getPosition())
			if hasattr(victim, "spawnTime") and host.timer_getWallTime()-victim.spawnTime < SPAWNKILL_THRESHOLD_TIME:
				#log.output("victim.spawnTime %s" % victim.spawnTime)
				if hasattr(victim, "spawnPos") and getVectorDistance(victim.spawnPos, victim.getDefaultVehicle().getPosition()) < SPAWNKILL_THRESHOLD_DISTANCE:
					#log.output("victim.spawnPos %s/%s/%s" % victim.spawnPos)
					obj = findNearestSpawnPoint(victim.getDefaultVehicle().getPosition())
					if obj:
						disableSpawnPoint(obj)
						timer.once(SPAWNKILL_DISABLE_TIME, enableSpawnPoint, obj)
	except:
		ExceptionOutput()


def disableSpawnPoint(obj):
	if g_debug: 
		log.output("SpawnPoint %s disabled!" % g_spawnPointInfoTable[obj].name)
	# origPos = g_spawnPointInfoTable[obj].position
	# obj.setPosition((origPos[0], origPos[1]-10000., origPos[2]))
	# host.rcon_invoke("ObjectTemplate.active " + obj.templateName)
	# host.rcon_invoke("ObjectTemplate.ControlPointId 0")
	host.rcon_invoke("Object.active " + getEngineIdString(g_spawnPointInfoTable[obj].name))
	host.rcon_invoke("Object.delete")
	
def enableSpawnPoint(obj):
	if g_debug: log.output("SpawnPoint %s enabled!" % g_spawnPointInfoTable[obj].name)
	# origPos = g_spawnPointInfoTable[obj].position
	# obj.setPosition(origPos)
	# host.rcon_invoke("ObjectTemplate.active " + obj.templateName)
	# host.rcon_invoke("ObjectTemplate.ControlPointId %d" % g_spawnPointInfoTable[obj].cpid)
	idstring = host.rcon_invoke("Object.create " + g_spawnPointInfoTable[obj].name)
	host.rcon_invoke("Object.absolutePosition %s/%s/%s" % g_spawnPointInfoTable[obj].position)
	host.rcon_invoke("Object.rotation %s/%s/%s" % g_spawnPointInfoTable[obj].rotation)
	#update object key
	try:
		spawnPoints = bf2.objectManager.getObjectsOfTemplate(g_spawnPointInfoTable[obj].name)
		g_spawnPointInfoTable.pop(obj)
		for newobj in spawnPoints:
			g_spawnPointInfoTable[newobj] = SpawnPointInfo(newobj.templateName, getSpawnPointCPId(newobj), newobj.getPosition(), newobj.getRotation())
	except:
		ExceptionOutput()

def findNearestSpawnPoint(pos):
	mindist = SPAWNKILL_THRESHOLD_DISTANCE
	nearest = None
	for obj in g_spawnPointInfoTable:
		if not obj.isValid(): continue
		newdist = getVectorDistance(pos, obj.getPosition())
		if newdist < mindist:
			mindist = newdist
			nearest = obj
	return nearest
	

def getSpawnPointTemplateNames():
	templateNames = []
	for template in host.rcon_invoke('ObjectTemplate.list').split('\n'):
		ret = host.rcon_invoke('ObjectTemplate.info ' + template) # "house_high_02_xp1" of primitive Bundle
		if ret.find("primitive SpawnPoint")>0:
			templateNames.append(template)
	return templateNames
	

def getEngineIdString(template):
	rets = host.rcon_invoke('Object.listObjectsOfTemplate ' + template).split('\n') # ret: "Untitled" with ID 3321 of template "CPNAME_SP_32_hotel_ATS" of primitive ObjectSpawner
	for line in rets:
		#only get the first line
		pos = line.find("with ID ")
		if pos<0: continue
		return "id"+line[(pos+8):].split(' ')[0]
	return ""

def getSpawnPointCPId(obj):
	host.rcon_invoke("ObjectTemplate.active " + obj.templateName)
	try:
		return int(host.rcon_invoke("ObjectTemplate.controlPointId"))
	except:
		return 0

def getVectorDistance(pos1, pos2):
	diffVec = [0.0, 0.0, 0.0]
	diffVec[0] = math.fabs(pos1[0] - pos2[0])
	diffVec[1] = math.fabs(pos1[1] - pos2[1])
	diffVec[2] = math.fabs(pos1[2] - pos2[2])
	
	return math.sqrt(diffVec[0] * diffVec[0] + diffVec[1] * diffVec[1] + diffVec[2] * diffVec[2])
	
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