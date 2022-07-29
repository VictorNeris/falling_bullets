#******************************************************#
#							BF2Object.py                                
#								v0.1
#                                                                     
# Class for instantiating bf2 objects a bit better maybe 
#                                                                              
# This class does not have any additional functionality compared 
# to the physicalobject, thus it is only a class that should be    
# used when instantiating new objects. Finding and altering
# normally spawned objects should continue to be done 
# with the ObjectManager.
#
# WARNING!
# Spawning vehicles with this script will cause their armor component
# interface in python to become bugged. They will not have a getDamage or 
# setDamage function. I'm not completely sure as to why this happens, if you
# know a solution please send me a message. 
#
# The script does not have any dependencies other than the 
# host and bf2 modules, and should work correctly with most mods.
#
# - Hjid
# 
#*******************************************************#

#Note: the spawned vehicles cannot be used by bots

'''
There is a small delay after the script has sent the spawnCommand to the engine and the object has actually been instantiated.
To solve this problem the script starts looking for the object after a short time.
This constant is in seconds and should be as low as possible.
'''
FIND_OBJECT_DELAY = 0.1 


"""
The script will spawn the objects high up in the air at first while it tries to find the correct bf2 object that spawned.
This constant is in meters above the ground and should be left unchanged, unless you have good reasons not to.
"""
OBJECT_SPAWN_HEIGHT = 10000.0

 
'''
The script will spawn the objects at unique positions in the xz plane to be able to distinguish them better
When spawned, each object will be assigned a spawnID, which is a number between 10 and 99,  where the first digit gives the x position and the second digit gives the z position.
When reaching spawnID 99 the counter is set back to 10.
This constant is in meters and should be large enough so that vehicles and objects wont collide with eachother on spawn. 
'''
OBJECT_SPAWN_SPACING = 10.0


'''
Since the script uses a timer between spawning and finding the object, the object might have moved a bit (mostly due to gravity on mobile objects). 
This treshold decides how large the error can be in displacement to the expected position.
This constant is in meters and it is recommended that it is approximately half of the OBJECT_SPAWN_SPACING
'''
OBJECT_SPAWN_POSITION_TRESHOLD = 5.0





import math
import host
import bf2
import bf2.Timer
from log import output

class BF2Object(object):
	
	_currentId = 10
	
	def __init__(self, template, hasArmor=False):
		
		# Public variables that we will not use internally

		self.tempateName = template
		self.isControlPoint = False
		self.isPlayerControlObject = False
		self.hasArmor = hasArmor
		self.token = None
		
		
		# Internal variables
		self._actualObject = None
		self._id = None
		self._template = template
		self._cmdStack = []
		self._valid = False
		self._handlers = []
		

		# Assign a spawnId and update the currentId
		self._spawnId = BF2Object._currentId
		if BF2Object._currentId == 99:
			BF2Object._currentId = 10
		else:
			BF2Object._currentId += 1
		
		# Set the expected spawn position
		self._expectedSpawnPos = (
			OBJECT_SPAWN_SPACING * (self._spawnId / 10),
			OBJECT_SPAWN_HEIGHT,
			OBJECT_SPAWN_SPACING * (self._spawnId % 10)
		)
		
		

		# Need to know if we need to take extra precautions for armor
		# This is not implemented in this script
		self._hasArmor = hasArmor
		
		self._spawnObject()
		#output("BF2Object:spawnObject:tempateName = %s" % self._template)
		bf2.Timer(self.findObject, FIND_OBJECT_DELAY, 1, 1)

	#**************#
	# Helper methods
	#**************#
	
	# Finds the object we have spawned
	def findObject(self, dummy):
		output("BF2Object:findObject")
		
		# Return if this BF2bject already has an actualObject
		if self._actualObject:
			return
			
		# Get the current id list from the engine
		objIds = self._getIds(self._template)

		# Loop through objects
		for obj in bf2.objectManager.getObjectsOfTemplate(self._template):
						
			# Continue if the object already has an id attribute
			if hasattr(obj,"id"):
				continue
			
			# Skip invalid objects
			if not obj.isValid():
				continue
				
			# Check if this is the object we are expecting
			if ( self.getVectorDistance( obj.getPosition(), self._expectedSpawnPos) < OBJECT_SPAWN_POSITION_TRESHOLD):
				
				objId = None
				
				# Lets find the engine id
				for id in objIds:
					host.rcon_invoke("Object.active id"+id)
					rawpos = host.rcon_invoke("Object.absolutePosition").split("/")
					pos = (float(rawpos[0]), float(rawpos[1]), float(rawpos[2]))
					
					if ( self.getVectorDistance( pos, self._expectedSpawnPos) < OBJECT_SPAWN_POSITION_TRESHOLD): 
						objId = id
						break
				
				output("BF2Object:obj %s found!" % self._template)
				# We have found our object, time to set the correct variables
				self._valid = True
				self._actualObject = obj
				self._id = objId
				self.isPlayerControlObject = obj.isPlayerControlObject
				self.token = obj.token

				# Mark object so the script does not have to look for it again 
				obj.id = objId
				
				# Execute cmdStack
				for cmd in self._cmdStack:
					output("BF2Object: exec: %s" % cmd)
					exec(cmd)
				
				
				# Callback for create handlers	
				for handler in self._handlers:
					handler(self)
				
				# Break and return the function
				return
	
	# Deletes the object with the given id
	def _deleteId(self, id):
		host.rcon_invoke("Object.active id" + id)
		host.rcon_invoke("Object.delete")
		
		
		
	# Returns a list with ids for the given template
	def _getIds(self, template):
	
		
		rawIds = host.rcon_invoke("Object.listObjectsofTemplate " +template)	
		rawIds = rawIds.split("\n")
		
		objectIds = []
		
		for rawId in rawIds:
			if len(rawId) == 0:
				continue
			id = rawId.split(" ")
			id = id[3]
			objectIds.append(id)
			
		return objectIds

		
	# Creates an object spawner to spawn the object
	def _spawnObject(self):

		spawnerName = "bf2obj_" + self._template
		

		spawnerCmds = [
				
				"ObjectTemplate.create ObjectSpawner " + spawnerName,
				"ObjectTemplate.activeSafe ObjectSpawner " + spawnerName,
				"ObjectTemplate.isNotSaveable 1",
				"ObjectTemplate.hasMobilePhysics 0",
				"ObjectTemplate.setObjectTemplate 1 " + self._template,
		]
		
		createCmds = [

			"Object.create " + spawnerName,
			"Object.absolutePosition %s/%s/%s" % self._expectedSpawnPos,
			"Object.rotation 0.0/0.0/0.0",
			"Object.team 1",
			"Object.delete"
		]
		
		cmds = spawnerCmds + createCmds
		
		for cmd in cmds:
			host.rcon_invoke(cmd)
		
		
	# Returns the distance between two positions
	def getVectorDistance(self, a, b):
		return (math.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2) )
	


	#***********************#
	# BF2Object unique methods
	#***********************#
	
	# Returns engine id
	def getId(self):
		return self._id
	
	
	# Deletes the object
	def delete(self):
		if self._valid:
			self._valid = False
			self._deleteId(self._id)

	# Event handler
	def registerCreateHandler(self, handler):
		if not handler in self._handlers:
			self._handlers.append(handler)


	
	#*****************#
	# Wrapper functions
	#*****************#
	def isValid(self):
		if self._actualObject:
			return self._actualObject.isValid()
		else:
			return self._valid	

	def setPosition(self,pos):
		if self._valid:
			self._actualObject.setPosition(pos)
		else:
			self._cmdStack.append("self.setPosition((%s,%s,%s))" % pos )
			
	def getPosition(self):
		if self._valid:
			return self._actualObject.getPosition()
		else:
			return (0.0,0.0,0.0)
		
	def setRotation(self, rot):
		if self._valid:
			self._actualObject.setRotation(rot)
		else:
			self._cmdStack.append("self.setRotation((%s,%s,%s))" % rot)
			
	def getRotation(self):
		if self._valid:
			self._actualObject.getRotation()
		else:
			return (0.0,0.0,0.0)
			
	def getParent(self):
		if self._valid:
			return self._actualObject.getParent()
		else:
			return None
			
	def getChildren(self):
		if self._valid:
			return self._actualObject.getChildren()
		else:
			return ()
		
	def getTemplateProperty(self, property):
		if self._valid:
			return self._actualObject.getTemplateProperty(property)
		else:
			return None
		
	# VehicleObject related functions
	def hasArmor(self):
		return self._hasArmor
		
	# Should not be relied on
	def getDamage(self):
		if self._valid:
			return self._actualObject.getDamage()
		else:
			return 0.0
			
	# Should not be relied on
	def setDamage(self, damage):
		if self._valid:
			self._actualObject.setDamage(damage)
		else:
			self._cmdStack.append("self.setDamage(%s)" % damage)
		
	def getIsWreck(self):
		if self._valid:
			return self._actualObject.getIsWreck()
		else:
			return False
			
	def getOccupyingPlayers(self):
		if self._valid:
			return self._actualObject.getOccupyingPlayers()
		else:
			return ()
			
	def getIsRemoteControlled(self):
		if self._valid:
			return self._actualObject.getIsRemoteControlled()
		else:
			return False
