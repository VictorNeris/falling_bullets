import host
import bf2
import math, random
import log
from artySettings import g_debug
from timer import timer

LOOP_INTERVAL = 1.0

class ExtPlayerState:
	def __init__(self, player, team, alive, position, velocity):
		self.player = player
		self.team = team
		self.alive = alive
		self.position = position
		self.velocity = velocity
		self.velRate = math.sqrt(velocity[0]*velocity[0] + velocity[1]*velocity[1] + velocity[2]*velocity[2])

class PlayerTracker:
	def __init__(self):
		self.playerStates = {}
		self.loopTimer = timer.loop(LOOP_INTERVAL, self.getAllPlayerState)
		self.getAllPlayerState()
	
	def deinit(self):
		if self.loopTimer:
			self.loopTimer.abort()
			self.loopTimer = None
	
	def getAllPlayerState(self):
		for p in bf2.playerManager.getPlayers():
			if p.index in self.playerStates: 
				lastPosition = self.playerStates[p.index].position
				if not p.isAlive():
					self.playerStates[p.index] = ExtPlayerState(p, p.getTeam(), False, lastPosition, (0.0,0.0,0.0))
				else:
					position = p.getVehicle().getPosition()
					vel = ((position[0]-lastPosition[0])/LOOP_INTERVAL, (position[1]-lastPosition[1])/LOOP_INTERVAL, (position[2]-lastPosition[2])/LOOP_INTERVAL)
					self.playerStates[p.index] = ExtPlayerState(p, p.getTeam(), True, position, vel)
			else:
				if p.getVehicle(): position = p.getVehicle().getPosition()
				else: position = (0.0,0.0,0.0)
				self.playerStates[p.index] = ExtPlayerState(p, p.getTeam(), p.isAlive(), position, (0.0,0.0,0.0))
		#if g_debug: log.output("%s" % self.playerStates)
			
	