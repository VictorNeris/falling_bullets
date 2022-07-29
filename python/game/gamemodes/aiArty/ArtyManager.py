import host
import bf2
import math, random
import log
from BF2Object import *
from artySettings import g_debug
from timer import timer
from exceptionoutput import *

class ArtyManager:

	def __init__(self, settings):
		if g_debug: log.output("ArtyManager:__init__")
		self.settings = settings
		self.team1_arty_num = 0
		self.team2_arty_num = 0
		self.team1_arty_objs = []
		self.team2_arty_objs = []
		self.team1_operating_anims = 0
		self.team2_operating_anims = 0
		self.team1_arty_ready = True
		self.team2_arty_ready = True
		self.team1_lastArtyTime = host.timer_getWallTime()
		self.team2_lastArtyTime = host.timer_getWallTime()
		#self.team1_hasCommander = False
		#self.team2_hasCommander = False
		self.renewArtyState()
	
	#disable artillery for ARTY_ROUND_INTERVAL time
	def disableArty(self, team):
		if team==1: 
			self.team1_arty_ready = False
			self.team1_lastArtyTime = host.timer_getWallTime()
		elif team==2: 
			self.team2_arty_ready = False
			self.team2_lastArtyTime = host.timer_getWallTime()
		timer.once(self.settings["ARTY_ROUND_INTERVAL"], self.enableArty, team)
		
	def enableArty(self, team):
		if team==1: 
			self.team1_arty_ready = True
		elif team==2: 
			self.team2_arty_ready = True

	def renewArtyState(self):
		#if g_debug:log.output("bf2.playerManager.getCommander(1) %s; bf2.playerManager.getCommander(2): %s" % (bf2.playerManager.getCommander(1),bf2.playerManager.getCommander(2)))
		#self.team1_hasCommander = (bf2.playerManager.getCommander(1) != None)
		#self.team2_hasCommander = (bf2.playerManager.getCommander(2) != None)
		self.team1_arty_num = 0
		self.team2_arty_num = 0
		self.team1_arty_objs = []
		self.team2_arty_objs = []
		try:
			for pco in bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.PlayerControlObject'):	
				# if pco.getIsRemoteControlled():
					# if hasattr(pco,'getDamage'):
						# armorString = "Armor = %s" % pco.getDamage()
					# else:
						# armorString = "Armor = None"
					# if g_debug: log.output(pco.templateName + " at %s/%s/%s" % pco.getPosition() + " hasArmor = %s " % pco.hasArmor + " token = %s " % pco.token + " isWreck = %s " % pco.getIsWreck() + armorString)
				if not pco.isValid() or pco.getIsWreck() or not pco.getIsRemoteControlled(): #or pco.getDamage()<0.01
					pass
					#if pco.getIsRemoteControlled() and g_debug: log.output(pco.templateName + " at %s/%s/%s" % pco.getPosition() + " isWreck = %s armor = %s" % (pco.getIsWreck(),pco.getDamage()))
				else:
					if hasattr(pco,'getDamage') and pco.getDamage()<0.01 or self.getVectorDistance((0.0,0.0,0.0),pco.getPosition())<0.1: #exclude error objects
						continue
					if pco.templateName.lower() in self.settings["TEAM1_ARTY_NAME"]:
						self.team1_arty_objs.append(pco)
						self.team1_arty_num+=1
					elif pco.templateName.lower() in self.settings["TEAM2_ARTY_NAME"]:
						self.team2_arty_objs.append(pco)
						self.team2_arty_num+=1
		except:
			ExceptionOutput()
		if g_debug: 
			log.output("Team 1 arty num: %s; Team 2 arty num: %s" % (self.team1_arty_num,self.team2_arty_num))
			log.output("Team 1 arty ready: %s; Team 2 arty ready: %s" % (self.team1_arty_ready,self.team2_arty_ready))
			#log.output("Team 1 hasCommander: %s; Team 2 hasCommander: %s" % (self.team1_hasCommander,self.team2_hasCommander))
	
	#Is artillery ready?
	def isAvailable(self, team):
		self.renewArtyState()
		if team==1:
			return (self.team1_arty_num!=0) and self.team1_arty_ready
		elif team==2:
			return (self.team2_arty_num!=0) and self.team2_arty_ready
		else:
			return False
	
	#return True if successfully start Artillery
	def startArtyAt(self, team, position):
		#if random.random()>self.settings.RANDOM_ARTY: return #add random
		if g_debug: log.output("Team %s:" % team + "Requesting artillery strike at %s/%s/%s!" % position)
		if self.isAvailable(team):
			#collect garbage objects
			'''try:
				config = self.settings["ARTY_CONFIG"][artyObj.templateName.lower()]
			except:
				log.output("Error! No valid config found for %s! Will use global config.." % artyObj.templateName.lower())
				config = self.settings'''
			#TODO: adjust this
			'''for id in self.getEngineIdStrings(self.settings["ARTY_MUZZ_SPAWNER_NAME"]):
				host.rcon_invoke("Object.active " + id)
				host.rcon_invoke("Object.delete")'''
			#start
			self.setArtyTransformAndStart(team, position)
			#self.spawnArtyAt(team, position, self.settings["ARTY_BURSTSIZE"])
			self.disableArty(team)
			return True
		else:
			return False
		
	#use team artillery at position	(as well as artyobj animation and effect)
	def spawnArtyAt(self, team, position, roundsLeft, isSignal):
		if roundsLeft<=0: 
			#disableArty(team)
			if isSignal: self.spawnArtyAt(team, position, self.settings["ARTY_BURSTSIZE"], False)
			else: return
		self.renewArtyState()
		arty_num = 0
		arty_objs = []
		if team==1:
			arty_num = self.team1_arty_num
			arty_objs = self.team1_arty_objs
		else:
			arty_num = self.team2_arty_num	
			arty_objs = self.team2_arty_objs
		if arty_num == 0: 
			if g_debug: log.output("No artillery available!")
			return
		for i in range(arty_num):
			timer.once(self.settings["ARTY_SYNCFIRE_DELAY"]*i, self.startArtyFromObject, arty_objs[i], position, roundsLeft, isSignal)
		return
		
		'''if isSignal:
			arty_spwname = (team==1) and self.settings["TEAM1_ARTY_SIGNAL_SPAWNER_NAME"] or self.settings["TEAM2_ARTY_SIGNAL_SPAWNER_NAME"]
		else:
			arty_spwname = (team==1) and self.settings["TEAM1_ARTY_SPAWNER_NAME"] or self.settings["TEAM2_ARTY_SPAWNER_NAME"]
		arty_effect_spwname = (team==1) and self.settings["TEAM1_ARTY_MUZZ_SPAWNER_NAME"] or self.settings["TEAM2_ARTY_MUZZ_SPAWNER_NAME"]
		#spawn arty
		for i in range(arty_num):
			#start animation and effect
			childrens = self.getAllChildren(arty_objs[i])
			for childrenObj in childrens:
				for controlObj in childrenObj.getChildren():
					# ''if controlObj.templateName == "VerticalTurnObject":
						obj.getPosition() returns absolute position..
						# pos = childrenObj.getPosition()
						# self.startAnimation(childrenObj, (pos[0],pos[1]-0.5,pos[2]), (0,5,0), None, None, 
						# self.startAnimation, childrenObj, pos, (0,0.5,0), None, None)
						# break
					#if controlObj.templateName == "e_muzz_artillery": #temp workaround for vBF2 artillery objects ,not found in dedicated servers
					if controlObj.templateName == self.settings["ARTY_MUZZ_PLACEHOLDER_NAME"] or controlObj.templateName == "e_muzz_artillery":
						barrel_pos = childrenObj.getPosition()
						recoil_dist = self.settings["ANIM_BARREL_RECOIL_DISTANCE"]
						recoil_speed = self.settings["ANIM_BARREL_RECOIL_SPEED"]
						pushback_speed = self.settings["ANIM_BARREL_PUSHBACK_SPEED"]
						self.startAnimation(childrenObj, (barrel_pos[0],barrel_pos[1]-recoil_dist,barrel_pos[2]), (0,recoil_speed,0), None, None, 
						self.startAnimation, childrenObj, barrel_pos, (0,pushback_speed,0), None, None)
						#artyEffectSpw = BF2Object(arty_effect_spwname)
						#artyEffectSpw.setPosition(controlObj.getPosition())
						#artyEffectSpw.setRotation((0,5,0)) # this causes delete not functioning
						#artyEffectSpw.delete() # the delete won't trigger armoreffect on client
						#timer.once(0.5, lambda x: x.delete(), artyEffectSpw) # this makes the object to explode
						spawnObject(arty_effect_spwname, controlObj.getPosition())
						break
			#spawn arty expobjs
			artySpw = BF2Object(arty_spwname)
			if isSignal:
				pos = self.rndDevPosition(position, self.settings["ARTY_DEVIATION_RADIUS"], self.settings["ARTY_SIGNAL_SPAWN_HEIGHT"], self.settings["ARTY_SIGNAL_SPAWN_HEIGHT_RANDOM"])
			else:
				pos = self.rndDevPosition(position, self.settings["ARTY_DEVIATION_RADIUS"], self.settings["ARTY_SPAWN_HEIGHT"], self.settings["ARTY_SPAWN_HEIGHT_RANDOM"])
			artySpw.setPosition(pos)
			if g_debug: log.output("Artillery object " + arty_spwname + " spawn at %s/%s/%s!" % pos)
		#next shot
		if isSignal:
			if roundsLeft>1: timer.once(self.settings["ARTY_SIGNAL_FIRE_INTERVAL"], self.spawnArtyAt, team, position, roundsLeft-1, True)
			else: timer.once(self.settings["ARTY_SIGNAL_FIRE_INTERVAL"], self.spawnArtyAt, team, position, self.settings["ARTY_BURSTSIZE"], False)
		else:
			if roundsLeft>1: timer.once(self.settings["ARTY_FIRE_INTERVAL"], self.spawnArtyAt, team, position, roundsLeft-1, False)'''
			
	def startArtyFromObject(self, artyObj, position, roundsLeft, isSignal):
		if not artyObj.isValid() or artyObj.getIsWreck() or not artyObj.getIsRemoteControlled(): return
		try:
			config = self.settings["ARTY_CONFIG"][artyObj.templateName.lower()]
		except:
			log.output("Error! No valid config found for %s! Will use global config.." % artyObj.templateName.lower())
			config = self.settings
		if isSignal:
			arty_spwname = config["ARTY_SIGNAL_SPAWNER_NAME"]
		else:
			arty_spwname = config["ARTY_SPAWNER_NAME"]
		arty_effect_spwname = config["ARTY_MUZZ_SPAWNER_NAME"]
		arty_muzz_placeholder_names = config["ARTY_MUZZ_PLACEHOLDER_NAMES"]
		recoil_dist = config["ANIM_BARREL_RECOIL_DISTANCE"]
		recoil_speed = config["ANIM_BARREL_RECOIL_SPEED"]
		pushback_speed = config["ANIM_BARREL_PUSHBACK_SPEED"]
		#start animation and effect
		childrens = self.getAllChildren(artyObj)
		for childrenObj in childrens:
			for controlObj in childrenObj.getChildren():
				if controlObj.templateName.lower() in arty_muzz_placeholder_names:
					barrel_pos = childrenObj.getPosition()
					self.startAnimation(childrenObj, (barrel_pos[0],barrel_pos[1]-recoil_dist,barrel_pos[2]), (0,recoil_speed,0), None, None, 
					self.startAnimation, childrenObj, barrel_pos, (0,pushback_speed,0), None, None)
					spawnObject(arty_effect_spwname, controlObj.getPosition())
					break
		#spawn arty expobjs
		artySpw = BF2Object(arty_spwname)
		if isSignal:
			pos = self.rndDevPosition(position, config["ARTY_DEVIATION_RADIUS"], config["ARTY_SIGNAL_SPAWN_HEIGHT"], config["ARTY_SIGNAL_SPAWN_HEIGHT_RANDOM"])
		else:
			pos = self.rndDevPosition(position, config["ARTY_DEVIATION_RADIUS"], config["ARTY_SPAWN_HEIGHT"], config["ARTY_SPAWN_HEIGHT_RANDOM"])
		artySpw.setPosition(pos)
		if g_debug: log.output("Artillery object " + arty_spwname + " spawn at %s/%s/%s!" % pos)
		#next shot
		if isSignal:
			if roundsLeft>1: timer.once(config["ARTY_SIGNAL_FIRE_INTERVAL"], self.startArtyFromObject, artyObj, position, roundsLeft-1, True)
			else: timer.once(config["ARTY_SIGNAL_FIRE_INTERVAL"], self.startArtyFromObject, artyObj, position, config["ARTY_BURSTSIZE"], False)
		else:
			if roundsLeft>1: timer.once(config["ARTY_FIRE_INTERVAL"], self.startArtyFromObject, artyObj, position, roundsLeft-1, False)


	def setArtyTransformAndStart(self, team, targetPos):
		try:
			if team==1:
				arty_objs = self.team1_arty_objs
			else:
				arty_objs = self.team2_arty_objs
			#rcObjs = bf2.objectManager.getObjectsOfTemplate("HorizontalTurnObject") #does not work!
			for artyObj in arty_objs:
				if not artyObj.isValid() or artyObj.getIsWreck() or not artyObj.getIsRemoteControlled(): continue #do not count invalid objs
				childrens = self.getAllChildren(artyObj)
				for childrenObj in childrens:
					for controlObj in childrenObj.getChildren():
						if controlObj.templateName == "HorizontalTurnObject":
							xAngle = self.calcXAngle(targetPos, artyObj.getPosition()) - artyObj.getRotation()[0]
							#tmp workaround
							while xAngle < -180.0 : xAngle += 360.0
							while xAngle > 180.0 : xAngle -= 360.0
							
							if g_debug: log.output("Setting artillery control object %s horizontal rotation %s" % (childrenObj.templateName, xAngle))
							#childrenObj.setRotation((xAngle,0.,0.))
							#host.rcon_invoke("ObjectTemplate.active "+childrenObj.templateName)
							#speedString = host.rcon_invoke("objectTemplate.maxSpeed")
							#angleSpeed = [float(s) for s in speedString.split('/')]
							if team==1: self.team1_operating_anims += 1
							else: self.team2_operating_anims += 1
							self.startAnimation(childrenObj, None, None, (xAngle,0.,0.), (30., 0., 0.), self.joinArtyObjAnimation, team, targetPos)
						elif controlObj.templateName == "VerticalTurnObject":
							if g_debug: log.output("Setting artillery control object %s vertical rotation %s" % (childrenObj.templateName, -90))
							#childrenObj.setRotation((0.,-90.,0.))
							#host.rcon_invoke("ObjectTemplate.active "+childrenObj.templateName)
							#speedString = host.rcon_invoke("objectTemplate.maxSpeed")
							#angleSpeed = [float(s) for s in speedString.split('/')]
							if team==1: self.team1_operating_anims += 1
							else: self.team2_operating_anims += 1
							self.startAnimation(childrenObj, None, None, (0.,-90.,0.), (0., 60., 0.), self.joinArtyObjAnimation, team, targetPos)
		except:
			ExceptionOutput()
	
	# start animation to set obj at targetPos and/or targetRot, and execute afterFunc after animation is done
	def startAnimation(self, obj, targetPos=None, posSpeed=None, targetRot=None, rotSpeed=None, afterFunc=None, *args):
		#if g_debug: log.output("startAnimation: %s, %s, %s, %s, %s" % (obj.templateName, targetPos, posSpeed, targetRot, rotSpeed))
		interval = self.settings["ANIM_UPDATE_INTERVAL"]
		onTarget = True
		if (targetPos and posSpeed):
			nowPos = obj.getPosition()
			if g_debug: log.output("nowPos: %s/%s/%s" % tuple(nowPos))
			newPos = list(targetPos)
			for i in range(3):
				if posSpeed[i]==0 or math.fabs(targetPos[i] - nowPos[i])<0.001: continue # on position
				dir = (targetPos[i] - nowPos[i]) > 0 and 1 or -1
				newPos[i] = nowPos[i] + dir*posSpeed[i]*interval
				newdir = (targetPos[i] - newPos[i]) > 0 and 1 or -1
				if dir*newdir < 0: newPos[i] = targetPos[i]
				onTarget = False
			if g_debug: log.output("newPos: %s/%s/%s" % tuple(newPos))
			obj.setPosition(tuple(newPos))
		if (targetRot and rotSpeed):
			nowRot = obj.getRotation()
			newRot = list(targetRot)
			for i in range(3):
				if rotSpeed[i]==0 or math.fabs(targetRot[i] - nowRot[i])<0.001: continue # on rotation
				dir = (targetRot[i] - nowRot[i]) > 0 and 1 or -1
				newRot[i] = nowRot[i] + dir*rotSpeed[i]*interval
				newdir = (targetRot[i] - newRot[i]) > 0 and 1 or -1
				if dir*newdir < 0: newRot[i] = targetRot[i]
				onTarget = False
			if g_debug: log.output("newRot: %s/%s/%s" % tuple(newRot))
			obj.setRotation(tuple(newRot))
		if not onTarget: 
			timer.once(interval, self.startAnimation, obj, targetPos, posSpeed, targetRot, rotSpeed, afterFunc, *args)
		else:
			#if g_debug: log.output("startAnimation: onTarget")
			if afterFunc: afterFunc(*args)
	
	def joinArtyObjAnimation(self, team, position):
		if team==1:
			if self.team1_operating_anims > 0: self.team1_operating_anims-=1
			else: 
				if g_debug: log.output("endAnimation: ending invalid animation!")
			if self.team1_operating_anims == 0:
				self.spawnArtyAt(team, position, self.settings["ARTY_SIGNAL_BURSTSIZE"], True) # throw signals first
		else:
			if self.team2_operating_anims > 0: self.team2_operating_anims-=1
			else: 
				if g_debug: log.output("endAnimation: ending invalid animation!")
			if self.team2_operating_anims == 0:
				self.spawnArtyAt(team, position, self.settings["ARTY_SIGNAL_BURSTSIZE"], True) # throw signals first
	
	def getAllChildren(self, obj):
		allChildren = []
		children = obj.getChildren()
		while len(children)>0:
			allChildren += list(children)
			nextchildren = ()
			for cobj in children:
				nextchildren += cobj.getChildren()
			children = nextchildren
		return allChildren
	
	def getEngineIdStrings(self, template):
		rets = host.rcon_invoke('Object.listObjectsOfTemplate ' + template).split('\n') # ret: "Untitled" with ID 3321 of template "CPNAME_SP_32_hotel_ATS" of primitive ObjectSpawner
		ids = []
		for line in rets:
			#only get the first line
			pos = line.find("with ID ")
			if pos<0: continue
			ids.append("id"+line[(pos+8):].split(' ')[0])
		return ids
	
	#return a random deviation position
	def rndDevPosition(self, position, radius, height, height_rnd):
		r = random.random()*radius
		th = random.random()*2*math.pi
		return (position[0] + r*math.cos(th), \
				position[1] + height + random.random()*height_rnd, \
				position[2] + r*math.sin(th))

	# get distance between two positions
	def getVectorDistance(self, pos1, pos2):
		diffVec = [0.0, 0.0, 0.0]
		diffVec[0] = math.fabs(pos1[0] - pos2[0])
		diffVec[1] = math.fabs(pos1[1] - pos2[1])
		diffVec[2] = math.fabs(pos1[2] - pos2[2])
		 
		return math.sqrt(diffVec[0] * diffVec[0] + diffVec[1] * diffVec[1] + diffVec[2] * diffVec[2])
		
	#pos1 is target position and pos2 is player position		
	def calcXAngle(self, pos1, pos2):	
		deltaX = pos1[0]-pos2[0]
		deltaZ = pos1[2]-pos2[2]
		atan = math.atan(deltaX/deltaZ)/math.pi * 180.0
		if deltaZ<0: 
			if deltaX<0: return atan - 180.0
			else: return atan + 180.0
		return atan

