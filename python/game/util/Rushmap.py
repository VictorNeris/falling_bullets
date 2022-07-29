#change a normal map to rush map

import sys
import conParser
import pdb

TARGETNAME_A = 'target_aircontroltower_mec_sp_A'
TARGETNAME_B = 'target_aircontroltower_mec_sp_B'

class ControlPointInfo:
	def __init__(self, templateName):
		self.templateName = templateName
		self.id = -1
		self.team = 0
		self.sequence = 0
		self.layer = 1
		self.AB = ''
		self.utct = 0
		self.position = '0/0/0'
		self.rotation = '0/0/0'

class TargetInfo:
	def __init__(self, templateName, team, controlPointId, position, rotation, layer):
		self.templateName = templateName
		self.team = team
		self.controlPointId = controlPointId
		self.position = position
		self.rotation = rotation
		self.layer = layer
		
		
def findCpInfo(cons):		
	cps = {}
	activeCpTemplate = ''#templateName
	activeCp = ''#templateName
	for con in cons:
		if len(activeCpTemplate) != 0 and con.get('ObjectTemplate.team'): 
			cps[activeCpTemplate].team = int(con['ObjectTemplate.team'][0])
			continue
		if len(activeCpTemplate) != 0 and con.get('ObjectTemplate.controlPointId'): 
			cps[activeCpTemplate].id = int(con['ObjectTemplate.controlPointId'][0])
			continue
		if len(activeCpTemplate) != 0 and con.get('ObjectTemplate.unableToChangeTeam'): 
			cps[activeCpTemplate].utct = int(con['ObjectTemplate.unableToChangeTeam'][0])
			continue
		if con.get('ObjectTemplate.create'):
			if con['ObjectTemplate.create'][0] == "ControlPoint":
				activeCpTemplate = con['ObjectTemplate.create'][1]
				cps[activeCpTemplate] = ControlPointInfo(activeCpTemplate)
			continue
		
		if con.get('Object.create') and cps.get(con['Object.create'][0]):
			activeCp = con['Object.create'][0]
			continue
		if len(activeCp) != 0 and con.get('Object.absolutePosition'):
			cps[activeCp].position = con['Object.absolutePosition'][0]
			continue
		if len(activeCp) != 0 and con.get('Object.layer'):
			cps[activeCp].layer = int(con['Object.layer'][0])
			continue
	return cps

def findFirstCpBySequence(cps, s):#returns a ControlPointInfo Object
	for cp in cps:
		if cps[cp].sequence == s: return cps[cp]
	return None
		
def findCpPeer(cps, peer):#returns a ControlPointInfo Object
	for cp in cps:
		if cps[cp].sequence == peer.sequence and cps[cp].id != peer.id: return cps[cp]
	return None
		
def findCpsBySequence(cps, s):#returns a ControlPointInfo Object
	result = []
	for cp in cps:
		if cps[cp].sequence == s: result.append(cps[cp])
	return result
	
def printCpInfo(cps):
	for cp in cps:
		#for property, value in vars(cps[cp]).iteritems():
		#	print property, ": ", value
		#if cps[cp].utct != 0: continue
		print cp + "	sequence = %s    " % cps[cp].sequence + cps[cp].AB

'''def setCpSequence(cps, S): #S is a dict:{'name':sequence,...}
	for cpname in S:
		if cps[cpname].utct != 0: continue
		cps[cpname].sequence = S[cpname]'''

def changeCon(cons, cps):
	activeCpTemplate = ''#templateName
	#activeCp = ''#templateName
	for con in cons:
		if con.get('ObjectTemplate.create'):
			if con['ObjectTemplate.create'][0] == "ControlPoint":
				activeCpTemplate = con['ObjectTemplate.create'][1]
			continue
		if len(activeCpTemplate) != 0 and con.get('ObjectTemplate.timeToGetControl'): 
			con['ObjectTemplate.timeToGetControl'][0] = "%s" % cps[activeCpTemplate].sequence
			continue
		if len(activeCpTemplate) != 0 and con.get('ObjectTemplate.timeToLoseControl'): 
			con['ObjectTemplate.timeToLoseControl'][0] = "%s" % cps[activeCpTemplate].sequence
			continue
	i = 0
	activeCpTemplate = ''
	while i < len(cons):
		if cons[i].get('ObjectTemplate.create'):
			if cons[i]['ObjectTemplate.create'][0] == "ControlPoint":
				if len(activeCpTemplate) != 0: 
					cons.insert(i, {"ObjectTemplate.timeToGetControl" : ["%s" % cps[activeCpTemplate].sequence]})
					cons.insert(i, {"ObjectTemplate.timeToLoseControl" : ["%s" % cps[activeCpTemplate].sequence]})
					i += 2
				activeCpTemplate = cons[i]['ObjectTemplate.create'][1]
		if cons[i].get('if'):
			if len(activeCpTemplate) != 0: 
				cons.insert(i, {"ObjectTemplate.timeToGetControl" : ["%s" % cps[activeCpTemplate].sequence]})
				cons.insert(i, {"ObjectTemplate.timeToLoseControl" : ["%s" % cps[activeCpTemplate].sequence]})
				i += 2
		i += 1
			
def changeAiCon(AIcons, cps):
	activeCpTemplate = ''#templateName
	i = 0
	while i < len(AIcons):
		if AIcons[i].get('aiStrategicArea.setActive'):
			activeCpTemplate = AIcons[i]['aiStrategicArea.setActive'][0]
			prev = findCpsBySequence(cps, cps[activeCpTemplate].sequence - 1)	
			for cp in prev:	
				i += 1
				AIcons.insert(i,{"AIStrategicArea.addNeighbour" : [cp.templateName]})				
			next = findCpsBySequence(cps, cps[activeCpTemplate].sequence + 1)	
			for cp in next:	
				i += 1
				AIcons.insert(i,{"AIStrategicArea.addNeighbour" : [cp.templateName]})
			peer = findCpPeer(cps, cps[activeCpTemplate])
			if peer: 
				i += 1
				AIcons.insert(i,{"AIStrategicArea.addNeighbour" : [peer.templateName]})
			i += 1
		while AIcons[i].get('AIStrategicArea.addNeighbour'):
			del AIcons[i]
		if AIcons[i].get('aiStrategicArea.setSide'):
			if cps[activeCpTemplate].utct != 0:
				AIcons[i]['aiStrategicArea.setSide'] = "%s" % cps[activeCpTemplate].team
		i += 1
		
		
def createTargetInfo(cps):
	targets = {}
	for cpname in cps:
		if cps[cpname].utct != 0 or cps[cpname].sequence == 0: continue
		targetName = cpname + "_target" + cps[cpname].AB
		if cps[cpname].team == 2: team = 1
		else: team = 2
		position = cps[cpname].position
		#rotation = cps[cpname].rotation
		layer = cps[cpname].layer
		print cps[cpname].templateName
		print cps[cpname].sequence
		controlPointId = findFirstCpBySequence(cps, cps[cpname].sequence - 1).id
		
		targets[targetName] = TargetInfo(targetName, team, controlPointId, position, '90/0/0', layer)
	return targets

def printTargetInfo(targets):
	for targetName in targets:
		for property, value in vars(targets[targetName]).iteritems():
			print property, ": ", value
	
def cmdTargetInfo(targets):
	cmds = ["rem ***target info***"]
	for targetName in targets:	
		cmds.append("ObjectTemplate.create ObjectSpawner "+targetName)
		cmds.append("ObjectTemplate.activeSafe ObjectSpawner "+targetName)
		cmds.append("ObjectTemplate.isNotSaveable 1")
		cmds.append("ObjectTemplate.hasMobilePhysics 0")
		if targetName[-1] == 'A':
			cmds.append(("ObjectTemplate.setObjectTemplate %s " % targets[targetName].team)+TARGETNAME_A)
		else: cmds.append(("ObjectTemplate.setObjectTemplate %s " % targets[targetName].team)+TARGETNAME_B)
		cmds.append("ObjectTemplate.minSpawnDelay 9999")
		cmds.append("ObjectTemplate.maxSpawnDelay 9999")
		cmds.append("\n")
		cmds.append("Object.create "+targetName)
		cmds.append("Object.absolutePosition "+targets[targetName].position)
		cmds.append("Object.rotation "+targets[targetName].rotation)
		cmds.append("Object.setControlPointId %s" % targets[targetName].controlPointId)
		cmds.append("Object.layer %s" % targets[targetName].layer)
		cmds.append("\n")
	return cmds
	
def writeTargetInfo(cmds, filename):
	try:
		f = file(filename, 'a+')
		for cmd in cmds:
			f.write(cmd)
			f.write("\n")
	except IOError:
		return False
	return True

#__main__
cons = conParser.readCon('gameplayobjects.con')
AIcons = conParser.readCon('ai/StrategicAreas.ai')
cps = findCpInfo(cons)
#if (len(cps)/2)*2 != len(cps): print "Warning: Number of CP is odd!"
print "Please set the sequence and AB for ControlPoints(1A,2B,3B,4A)"
for cp in cps:
	print cp + ": "
	if cps[cp].utct != 0:
		print "unableToChangeTeam!"
		continue
	info = raw_input().strip()
	#if info == "0": continue
	while(len(info) != 2):
		print "SyntaxError! Please input number and AB"
		info = raw_input().strip()
	else:
		cps[cp].sequence = int(info[0])
		cps[cp].AB = info[1].upper()
#adjust sequence
defTeam = 0
maxSequence = 0
for cp in cps:
	if cps[cp].utct == 0: 
		if defTeam == 0: defTeam = cps[cp].team
		if maxSequence < cps[cp].sequence: maxSequence = cps[cp].sequence
	
for cp in cps:
	if cps[cp].team == defTeam and cps[cp].utct != 0:
		cps[cp].sequence = maxSequence + 1
printCpInfo(cps)
print "Please confirm, input 'exit' to exit, else to continue:"
cmd = raw_input()
if cmd == 'exit': exit()
else:
	changeCon(cons, cps)
	changeAiCon(AIcons, cps)
	for con in AIcons:
		print con
	#pdb.set_trace()
	conParser.writeCon(cons, "GamePlayObjectsNEW.con")
	conParser.writeCon(AIcons, "ai/StrategicAreasNEW.ai")
	print "Write NEW success"
	targets = createTargetInfo(cps)
	printTargetInfo(targets)
	cmds = cmdTargetInfo(targets)
	#pdb.set_trace()
	#for c in cmds:
	#	print c
	print "Please confirm, input 'exit' to exit, else to continue:"
	cmd = raw_input().lower()
	if cmd == 'exit': exit()
	else: 
		if writeTargetInfo(cmds, "GamePlayObjectsNEW.con"):
			print "Write target success"
			cmd = raw_input()
		else:
			print "Error writing GamePlayObjectsNEW.con" 
			cmd = raw_input()