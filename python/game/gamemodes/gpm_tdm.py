# tdm mode scoring indication
# modified by AGM114D (2017.6)

TAKEOVERTYPE_CAPTURE = 1
TAKEOVERTYPE_NEUTRALIZE = 2

SCORE_CAPTURE = 250
SCORE_NEUTRALIZE = 200
SCORE_CAPTUREASSIST = 100
SCORE_NEUTRALIZEASSIST = 100
SCORE_DEFEND = 25
SCORE_ATTACK = 25

Top = 0
Middle = 1
Bottom = 2

import host
import bf2
import math
import random

from game.scoringCommon import addScore, RPL, timer
from bf2 import g_debug

g_controlPoints = [] # cache, as this map won't change

def init():
        host.registerGameStatusHandler(onGameStatusChanged)
        if host.sgl_getIsAIGame() == 1:
                host.sh_setEnableCommander(1)
        else:
                host.sh_setEnableCommander(1)
                
        host.registerHandler('TimeLimitReached', onTimeLimitReached, 1) 

        if g_debug: print "gpm_tdm.py initialized"
                
def deinit():
        bf2.triggerManager.destroyAllTriggers()
        global g_controlPoints
        g_controlPoints = []
        host.unregisterGameStatusHandler(onGameStatusChanged)
        if g_debug: print "gpm_tdm.py uninitialized"

def onGameStatusChanged(status):
        if g_debug: print "onGameStatusChanged:", status
        
        global g_controlPoints
        if status == bf2.GameStatus.Playing: 
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

                host.registerHandler('ControlPointChangedOwner', onCPStatusChange)

                ticketsTeam1 = bf2.serverSettings.getTicketRatio()
                ticketsTeam2 = bf2.serverSettings.getTicketRatio()
                
                if g_debug: print "%d %d" % (ticketsTeam1, ticketsTeam2)
                
                bf2.gameLogic.setTickets(1, ticketsTeam1)
                bf2.gameLogic.setTickets(2, ticketsTeam2)

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
                
        
                
                #Rem all those above this out to remove the heartbeat sound --------------------------------------------
                #bf2.gameLogic.setTicketLimit(1, 3, int(ticketsTeam1*0.9))
                #bf2.gameLogic.setTicketLimit(2, 3, int(ticketsTeam2*0.9))
                #bf2.gameLogic.setTicketLimit(1, 4, int(ticketsTeam1*0.8))
                #bf2.gameLogic.setTicketLimit(2, 4, int(ticketsTeam1*0.8))
                
                host.registerHandler('TicketLimitReached', onTicketLimitReached)
                updateTicketLoss()

                host.registerHandler('PlayerDeath', onPlayerDeathCQ)
                host.registerHandler('PlayerKilled', onPlayerKilledCQ)
                host.registerHandler('PlayerRevived', onPlayerRevived)
                host.registerHandler('PlayerSpawn', onPlayerSpawn)
                host.registerHandler('EnterVehicle', onEnterVehicle)
                host.registerHandler('ExitVehicle', onExitVehicle)

                if g_debug: print "Team Death Match gamemode initialized."
        else:
                bf2.triggerManager.destroyAllTriggers()
                g_controlPoints = []


#def calcStartTickets(mapDefaultTickets):
#        return int(bf2.serverSettings.getTicketRatio())
        
        

        
def onTimeLimitReached(value):
        if g_debug: print "Time limit reached"
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

def updateTicketLoss():
        areaValueTeam1 = 0
        areaValueTeam2 = 0
        totalAreaValue = 0
        numCpsTeam0 = 0
        numCpsTeam1 = 0
        numCpsTeam2 = 0
        
        for obj in g_controlPoints:
                team = obj.cp_getParam('team')
                if team == 1:
                        areaValueTeam1 += obj.cp_getParam('areaValue', team)
                        totalAreaValue += areaValueTeam1
                        numCpsTeam1 += 1
                elif team == 2:
                        areaValueTeam2 += obj.cp_getParam('areaValue', team)
                        totalAreaValue += areaValueTeam2
                        numCpsTeam2 += 1
                else:
                        numCpsTeam0 += 1
                        totalAreaValue += 0
                
        if g_debug: print "Team 1 has %d CPs, area value %d" % (numCpsTeam1, areaValueTeam1)
        if g_debug: print "Team 2 has %d CPs, area value %d" % (numCpsTeam2, areaValueTeam2)
        if g_debug: print "Neutral has %d CPs" % (numCpsTeam0)

        team1AreaOverweight = areaValueTeam1 - areaValueTeam2
        percentualOverweight = 1.0
        if totalAreaValue != 0:
                percentualOverweight = abs(team1AreaOverweight / totalAreaValue)

        ticketLossPerSecTeam1 = 0
        ticketLossPerSecTeam2 = 0
        bf2.gameLogic.setTicketChangePerSecond(1, -ticketLossPerSecTeam1)
        bf2.gameLogic.setTicketChangePerSecond(2, -ticketLossPerSecTeam2)

        if g_debug: print "New ticketloss team1=%f (team1areaOW=%d)" % (ticketLossPerSecTeam1, team1AreaOverweight)
        if g_debug: print "New ticketloss team2=%f (team1areaOW=%d)" % (ticketLossPerSecTeam2, team1AreaOverweight)

def calcTicketLossForTeam(team, otherTeamAreaValue, otherTeamAreaOverweight):
        if otherTeamAreaValue >= 100 and otherTeamAreaOverweight > 0:
                ticketLossPerSecond = 0
                return ticketLossPerSecond
        else:
                return 0



        
DOWNWARDS = -1
UPWARDS = 1     
def onTicketLimitReached(team, limitId):
        if (limitId == -1):                     
                if (team == 1):
                        winner = 2
                
                elif (team == 2):
                        winner = 1
                
                bf2.gameLogic.setTicketState(1, 0)
                bf2.gameLogic.setTicketState(2, 0)
        
                host.sgl_endGame(winner, 3)             
        else:
                updateTicketWarning(team, limitId)

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
                
def onCPTrigger(triggerId, cp, vehicle, enter, userData):
        if not cp.isValid(): return
        
        if cp.cp_getParam('unableToChangeTeam') != 0:
                return                                  
                
        if enter:
                for p in vehicle.getOccupyingPlayers():
                        cp = getOccupyingCP(p)
                        if cp != None:
                                if not p.getIsInsideCP():
                                        if g_debug: print "Resetting enterPctAt for player ", p.getName()
                                        p.enterCpAt = host.timer_getWallTime()
        
        if vehicle:     
                for p in vehicle.getOccupyingPlayers():
                        p.setIsInsideCP(enter)                  
        team1Occupants = 0
        team2Occupants = 0

        pcos = bf2.triggerManager.getObjects(cp.triggerId)
        for o in pcos:
                if not o: continue 
                if o.getParent(): continue 

                for p in o.getOccupyingPlayers():
                        if p.isAlive() and not p.isManDown():
                                
                                if not p.killed:
                                        if p.getTeam() == 1:
                                                team1Occupants += 1
                                        elif p.getTeam() == 2:
                                                team2Occupants += 1

        team1OverWeight = team1Occupants - team2Occupants
        attackOverWeight = 0

        if team1OverWeight > 0:
                attackingTeam = 1
        elif team1OverWeight < 0:
                attackingTeam = 2
        else:
                attackingTeam = 0

        
        if team1Occupants == 0 and team2Occupants == 0:
                if cp.cp_getParam('team') == 0:
                        attackOverWeight = -0.5
                else:
                        attackOverWeight = 0.5
                        
                timeToChangeControl = cp.cp_getParam('timeToLoseControl')

        else:
                if cp.cp_getParam('flag') == attackingTeam or (cp.flagPosition == Bottom and cp.cp_getParam('team') == 0):

                        attackOverWeight = abs(team1OverWeight)
                        timeToChangeControl = cp.cp_getParam('timeToGetControl')
                else:

                        attackOverWeight = - abs(team1OverWeight)
                        timeToChangeControl = cp.cp_getParam('timeToLoseControl')


        if cp.cp_getParam('onlyTakeableByTeam') != 0 and cp.cp_getParam('onlyTakeableByTeam') != attackingTeam:
                return

        if cp.flagPosition == Bottom:
                cp.cp_setParam('flag', attackingTeam)

        if timeToChangeControl > 0:
                takeOverChangePerSecond = 1.0 * attackOverWeight / timeToChangeControl
        else:
                takeOverChangePerSecond = 0.0

        if (cp.flagPosition == Top and takeOverChangePerSecond > 0) or (cp.flagPosition == Bottom and takeOverChangePerSecond < 0):
                takeOverChangePerSecond = 0.0

        if abs(takeOverChangePerSecond) > 0:
                cp.flagPosition = Middle
                                
        cp.cp_setParam('takeOverChangePerSecond', takeOverChangePerSecond)

                
def onCPStatusChange(cp, top):

        playerId = -1
        takeoverType = -1
        newTeam = -1
        scoringTeam = -1
        
        if top: cp.flagPosition = Top
        else:   cp.flagPosition = Bottom
        
        if cp.cp_getParam('team') != 0:

                if top:
                        if g_debug: print "Controlpoint fully returned to owning team"
                        
                else:
                        newTeam = 0
                        if cp.cp_getParam('team') == 1:
                                scoringTeam = 2
                        else:
                                scoringTeam = 1
                                
                        takeoverType = TAKEOVERTYPE_NEUTRALIZE
                        if g_debug: print "Controlpoint neutralized by team %d" % scoringTeam

        else:

                if top:
                        newTeam = cp.cp_getParam('flag')
                        scoringTeam = newTeam
                        takeoverType = TAKEOVERTYPE_CAPTURE
                        if g_debug: print "Controlpoint captured by team %d" % newTeam

                else:
                        if g_debug: print "Neutral flag hit bottom"

        if takeoverType > 0:
                pcos = bf2.triggerManager.getObjects(cp.triggerId)
        
                scoringPlayers = []
                firstPlayers = []
                for o in pcos:
                        if not o.getOccupyingPlayers:
                                if g_debug: print "sanity check: got a non-pco object as a result of a pco trigger. type=", o.templateName
        
                        for p in o.getOccupyingPlayers():
                                if p.isAlive() and not p.isManDown() and p.getTeam() == scoringTeam:
                                        if len(firstPlayers) == 0 or p.enterCpAt < firstPlayers[0].enterCpAt:
                                                firstPlayers = [p]
                                        elif p.enterCpAt == firstPlayers[0].enterCpAt:
                                                firstPlayers += [p]
                                        
                                        if not p in scoringPlayers:
                                                scoringPlayers += [p]
        
        cp.cp_setParam('playerId', playerId) 
        if newTeam != -1 and cp.cp_getParam('team') != newTeam:
                cp.cp_setParam('team', newTeam)
        onCPTrigger(cp.triggerId, cp, 0, 0, 0)
        updateTicketLoss() 
                        
def onPlayerDeathCQ(victim, vehicle):           

        numCpsTeam00 = 0
        numCpsTeam01 = 0
        numCpsTeam02 = 0
        for obj in g_controlPoints:
                teams = obj.cp_getParam('team')
                if teams == 1:
                        numCpsTeam01 -= 1
                elif teams == 2:
                        numCpsTeam02 -= 1
                else:
                        numCpsTeam00 -= 1

        foundLivingPlayer = False
        for p in bf2.playerManager.getPlayers():
                if p != victim and p.getTeam() == victim.getTeam() and p.isAlive():
                        foundLivingPlayer = True
        
        if not foundLivingPlayer:
                if g_debug: print "Last player gone"
                updateTicketLoss()
        




def onPlayerKilledCQ(victim, attacker, weapon, assists, object):
        if not victim: 
                if g_debug: print "Killed event with no victim!"
                return
        
        victim.killed = True

        murderdeathkill = 0
        if victim != None:
                if attacker != None: 
                        Killed = victim.getTeam()
                        Attack = attacker.getTeam() 
                        if Attack != Killed:
                                if Killed == 2:
                                        teamTickets = bf2.gameLogic.getTickets(2)
                                        teamTickets -= 1
                                        bf2.gameLogic.setTickets(2, teamTickets)
                                if Killed == 1:
                                        teamTickets = bf2.gameLogic.getTickets(1)
                                        teamTickets -= 1
                                        bf2.gameLogic.setTickets(1, teamTickets)
                        
        if (bf2.gameLogic.getTickets(1) == murderdeathkill):
                winner = 2
                bf2.gameLogic.setTicketState(1, 0)
                bf2.gameLogic.setTicketState(2, 0)
                host.sgl_endGame(winner, 3)
        elif (bf2.gameLogic.getTickets(2) == murderdeathkill):
                winner = 1
                bf2.gameLogic.setTicketState(1, 0)
                bf2.gameLogic.setTicketState(2, 0)
                host.sgl_endGame(winner, 3)


	# update flag takeover status if victim was in a CP radius
	cp = getOccupyingCP(victim)
	cp2 = getOccupyingCP(attacker)

	if cp != None:
		onCPTrigger(-1, cp, victim.getVehicle(), False, None)

		# give defend score if killing enemy within cp radius
		if attacker != None and attacker.getTeam() != victim.getTeam()\
		   and cp.cp_getParam('unableToChangeTeam') == 0 and cp.cp_getParam('onlyTakeableByTeam') == 0:
		
			if cp != None and cp.cp_getParam('team') == attacker.getTeam():
				attacker.score.cpDefends += 1
				# bf2.gameLogic.sendGameEvent(attacker, 12, 1) #12 = Conquest, 1 = Defend
				if attacker.isCommander():
					return


				addScore(attacker, SCORE_DEFEND, RPL,"def" ,str(SCORE_DEFEND), 0)
	if cp2 != None:
		if attacker != None and attacker.getTeam() != victim.getTeam() and cp2.cp_getParam('team') == victim.getTeam():
			attacker.score.cpDefends += 1
			if attacker.isCommander():
				return
			addScore(attacker, SCORE_ATTACK, RPL,"att" ,str(SCORE_ATTACK), 0) 
                        
def onPlayerRevived(victim, attacker):


        victim.killed = False

        
        cp = getOccupyingCP(victim)
        if cp != None:
                onCPTrigger(-1, cp, victim.getVehicle(), True, None)
        
def onPlayerSpawn(player, soldier):
        player.killed = False



        
def onEnterVehicle(player, vehicle, freeSoldier = False):
        cp = getOccupyingCP(player)
        if cp != None:
                player.setIsInsideCP(True)
        else:           
                player.setIsInsideCP(False)

def onExitVehicle(player, vehicle):
        cp = getOccupyingCP(player)
        if cp != None:
                player.setIsInsideCP(True)
        else:           
                player.setIsInsideCP(False)
                             
def getOccupyingCP(player):
        vehicle = player.getVehicle()
        playerPos = vehicle.getPosition()
        
        closestCP = None
        if len(g_controlPoints) == 0: return None
        for obj in g_controlPoints:
                distanceTo = getVectorDistance(playerPos, obj.getPosition())
                if closestCP == None or distanceTo < closestCPdist:
                        closestCP = obj
                        closestCPdist = distanceTo
        
        pcos = bf2.triggerManager.getObjects(closestCP.triggerId)
        for o in pcos:
                if o == player.getDefaultVehicle():
                        return closestCP
                else:
                        for p in o.getOccupyingPlayers():
                                if p == player:
                                        return closestCP
        
        return None
