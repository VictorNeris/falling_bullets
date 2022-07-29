import host
import bf2
import log
import math, random, types

g_debug = 1

#globals
g_objectSpawnerIdTable = {}
g_loopTimer = None

#settings
RANDOM_SPAWNER_SUFFIX = "_rndspw"RANDOM_SPAWNER_TAG = "_rndspw"
LOOP_INTERVAL = 60.0 #
DEFAULT_SPAWN_RATE = 0.5


def init():
	host.registerGameStatusHandler(onGameStatusChanged)
	#global g_debug
	#g_debug = 1
	if g_debug: 
		log.init()
		print "random_objectspawner.py initialized"

def deinit():
	host.unregisterGameStatusHandler(onGameStatusChanged)
	if g_debug: 
		log.deinit()
		print "random_objectspawner.py deinitialized"

def onGameStatusChanged(status):

	global g_objectSpawnerIdTable, g_loopTimer
	if status == bf2.GameStatus.Playing: 
		objectSpawners = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ObjectSpawner')
		for obj in objectSpawners:
			if g_debug: 
				'''for line in host.rcon_invoke('ObjectTemplate.list').split('\n'):
					log.output(host.rcon_invoke('ObjectTemplate.info ' + line))'''
				log.output("ObjectSpawner %s has cpid %d" %(obj.templateName, getSpawnerCPId(obj)))
			#if obj.templateName.endswith(RANDOM_SPAWNER_SUFFIX):
			if RANDOM_SPAWNER_TAG in obj.templateName:
				g_objectSpawnerIdTable[obj] = getSpawnerCPId(obj)
		#host.registerHandler('ControlPointChangedOwner', onCPStatusChange)
		g_loopTimer = timer.loop(LOOP_INTERVAL, updateSpawnerStates)
		updateSpawnerStates()
		if g_debug: print "Random ObjectSpawner System initialized."
	else:
		g_objectSpawnerIdTable = {}
		g_loopTimer.abort()
		g_loopTimer = None

def updateSpawnerStates():
	for obj in g_objectSpawnerIdTable:
		if random.random() < DEFAULT_SPAWN_RATE:
			if g_debug: log.output("Spawner %s with id %s enabled!" % (obj.templateName, g_objectSpawnerIdTable[obj]))
			enableSpawner(obj)
		else:
			if g_debug: log.output("Spawner %s with id %s disabled!" % (obj.templateName, g_objectSpawnerIdTable[obj]))
			disableSpawner(obj)
		

# called when a control point flag reached top or bottom
def onCPStatusChange(cp, top):
	if cp.cp_getParam('team') == 0:
		if top:
			updateSpawnerStates()

	
def disableSpawner(obj):
	host.rcon_invoke('Object.active ' + getEngineIdString(obj))
	host.rcon_invoke('Object.setControlPointId 0')
	
def enableSpawner(obj):
	host.rcon_invoke('Object.active ' + getEngineIdString(obj))
	host.rcon_invoke('Object.setControlPointId %d' % g_objectSpawnerIdTable[obj])

def getEngineIdString(obj):
	rets = host.rcon_invoke('Object.listObjectsOfTemplate ' + obj.templateName).split('\n') # ret: "Untitled" with ID 3321 of template "CPNAME_SP_32_hotel_ATS" of primitive ObjectSpawner
	for line in rets:
		#only get the first line
		pos = line.find("with ID ")
		if pos<0: continue
		return "id"+line[(pos+8):].split(' ')[0]
	return None

def getSpawnerCPId(obj):
	host.rcon_invoke('Object.active ' + getEngineIdString(obj))
	try:
		return int(host.rcon_invoke('Object.getControlPointId'))
	except:
		return 0
	
	
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