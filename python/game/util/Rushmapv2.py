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
		self.atkSpDummyId = -1
		self.defSpDummyId = -1
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

def vec3Add(v1,v2):
	return (v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2])
	
def str2Vec3(str):
	nums = str.split('/')
	return (float(nums[0]),float(nums[1]),float(nums[2]))
	
def vec32Str(vec3):
	return "%s/%s/%s" % vec3
		
		
def getUsedIds(cps):
	usedIds=[]
	for cpname in cps:
		usedIds.append(cps[cpname].id)
		usedIds.append(cps[cpname].atkSpDummyId)
		usedIds.append(cps[cpname].defSpDummyId)
	return usedIds
		
def createSpawnDummyCpString(cpInfo):
	templateStr = [
		{"ObjectTemplate.create ControlPoint":["%s" % (cpInfo.templateName+"_spdummy_atk")]},
		{"ObjectTemplate.activeSafe ControlPoint":["%s" % (cpInfo.templateName+"_spdummy_atk")]},
		{"ObjectTemplate.modifiedByUser":["\"worldlife\""]},
		{"ObjectTemplate.setNetworkableInfo":["ControlPointInfo"]},
		{"ObjectTemplate.isNotSaveable":["1"]},
		{"ObjectTemplate.hasMobilePhysics":["0"]},
		{"ObjectTemplate.hasCollisionPhysics":["1"]},
		{"ObjectTemplate.physicsType":["Mesh"]},
		{"ObjectTemplate.setControlPointName":["%s" % cpInfo.templateName+"_spdummy_atk"]},
		{"ObjectTemplate.radius":["0"]},
		{"ObjectTemplate.team":["0"]},
		{"ObjectTemplate.timeToGetControl":["1"]},
		{"ObjectTemplate.timeToLoseControl":["1"]},
		{"ObjectTemplate.controlPointId":["%s" % cpInfo.atkSpDummyId]},
		{"ObjectTemplate.showOnMinimap":["0"]},
		{"ObjectTemplate.isUnstrategicControlPoint":["1"]},
		{"ObjectTemplate.hoistFlag":["0"]},
		{"ObjectTemplate.flagTemplateTeam0":["None"]},
		{"ObjectTemplate.flagTemplateTeam1":["None"]},
		{"ObjectTemplate.flagTemplateTeam2":["None"]},
		{"\n":[]},
		{"ObjectTemplate.create":["ControlPoint %s" % (cpInfo.templateName+"_spdummy_def")]},
		{"ObjectTemplate.activeSafe":["ControlPoint %s" % (cpInfo.templateName+"_spdummy_def")]},
		{"ObjectTemplate.modifiedByUser":["\"worldlife\""]},
		{"ObjectTemplate.setNetworkableInfo":["ControlPointInfo"]},
		{"ObjectTemplate.isNotSaveable":["1"]},
		{"ObjectTemplate.hasMobilePhysics":["0"]},
		{"ObjectTemplate.hasCollisionPhysics":["1"]},
		{"ObjectTemplate.physicsType":["Mesh"]},
		{"ObjectTemplate.setControlPointName":["%s" % cpInfo.templateName+"_spdummy_def"]},
		{"ObjectTemplate.radius":["0"]},
		{"ObjectTemplate.team":["%s" % (cpInfo.sequence==1 and cpInfo.team or 0)]},
		{"ObjectTemplate.timeToGetControl":["1"]},
		{"ObjectTemplate.timeToLoseControl":["1"]},
		{"ObjectTemplate.controlPointId":["%s" % cpInfo.defSpDummyId]},
		{"ObjectTemplate.showOnMinimap":["0"]},
		{"ObjectTemplate.isUnstrategicControlPoint":["1"]},
		{"ObjectTemplate.hoistFlag":["0"]},
		{"ObjectTemplate.flagTemplateTeam0":["None"]},
		{"ObjectTemplate.flagTemplateTeam1":["None"]},
		{"ObjectTemplate.flagTemplateTeam2":["None"]},
	]
	
	createStr = [
		{"Object.create":["%s" % (cpInfo.templateName+"_spdummy_atk")]},
		{"Object.absolutePosition":[vec32Str(vec3Add(str2Vec3(cpInfo.position),(0,5,0)))]},#for convenience in editor
		{"Object.layer":["%s" % cpInfo.layer]},
		{"\n":[]},
		{"Object.create":["%s" % (cpInfo.templateName+"_spdummy_def")]},
		{"Object.absolutePosition":[vec32Str(vec3Add(str2Vec3(cpInfo.position),(0,10,0)))]},#for convenience in editor
		{"Object.layer":["%s" % cpInfo.layer]},
	]
	
	return templateStr, createStr
	
def getValidCpId(usedIds, startFrom=1):
	id = startFrom
	while id in usedIds: id+=1
	usedIds.append(id)
	return id
		
def getCpInfoFromCons(cons):		
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
	#generate spawn dummy ids
	usedIds = getUsedIds(cps)
	for cpname in cps:
		if cps[cpname].utct == 0:
			cps[cpname].atkSpDummyId = getValidCpId(usedIds,cps[cpname].id)
			cps[cpname].defSpDummyId = getValidCpId(usedIds,cps[cpname].id)
	return cps

def findFirstCpBySequence(cps, s):#returns a ControlPointInfo Object
	for cpname in cps:
		if cps[cpname].sequence == s: return cps[cpname]
	return None

def findCpById(cps, id):
	for cpname in cps:
		if id == cps[cpname].id:	return cps[cpname]
	return None
	
def findCpPeer(cps, peer):#returns a ControlPointInfo Object
	for cpname in cps:
		if cps[cpname].sequence == peer.sequence and cps[cpname].id != peer.id: return cps[cpname]
	return None
		
def findCpsBySequence(cps, s):#returns a ControlPointInfo Object
	result = []
	for cpname in cps:
		if cps[cpname].sequence == s: result.append(cps[cpname])
	return result

def checkCpInfo(cps):
	defTeam = 0
	confirmed = False
	for cpname in cps:
		if cps[cpname].utct == 0: 
			if not confirmed:
				defTeam = cps[cpname].team
				confirmed = True
			elif defTeam != cps[cpname].team:
				print "Error! Unable to determine whether team is the defense! Please make sure that all capturable flags are the same team!"
				return False
	return True
	
def printCpInfo(cps):
	for cpname in cps:
		#for property, value in vars(cps[cp]).iteritems():
		#	print property, ": ", value
		#if cps[cp].utct != 0: continue
		print cpname + "	sequence = %s    " % cps[cpname].sequence + cps[cpname].AB

'''def setCpSequence(cps, S): #S is a dict:{'name':sequence,...}
	for cpname in S:
		if cps[cpname].utct != 0: continue
		cps[cpname].sequence = S[cpname]'''

def changeCon(cons, cps):
	#change 
	activeCpTemplate = ''#templateName
	#activeCp = ''#templateName
	for con in cons:
		#adjust cp timeToGetControl and timeToLoseControl
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
		if len(activeCpTemplate) != 0 and cps[activeCpTemplate].sequence>1 and cps[activeCpTemplate].utct==0 and con.get('ObjectTemplate.team'):
			if cps[activeCpTemplate].team==1: con['ObjectTemplate.team'][0] = '2'
			else: con['ObjectTemplate.team'][0] = '1'
		#change spawnpoint cpid to attack team spawn dummy's
		if con.get('ObjectTemplate.setControlPointId'):
			cpid = int(con['ObjectTemplate.setControlPointId'][0])
			cp = findCpById(cps,cpid)
			if cp and cp.utct == 0: con['ObjectTemplate.setControlPointId'][0] = "%s" % cp.atkSpDummyId
		#change objectspawner cpid to defense team spawn dummy's
		if con.get('Object.setControlPointId'):
			cpid = int(con['Object.setControlPointId'][0])
			cp = findCpById(cps,cpid)
			if cp and cp.utct == 0: con['Object.setControlPointId'][0] = "%s" % cp.defSpDummyId
			
	#insert timeToGetControl and timeToLoseControl if not exist, and insert spawn dummys if not unableToChangeTeam
	i = 0
	activeCpTemplate = ''
	while i < len(cons):
		if cons[i].get('ObjectTemplate.create'):
			if cons[i]['ObjectTemplate.create'][0] == "ControlPoint":
				if len(activeCpTemplate) != 0: 	
					cons.insert(i, {"ObjectTemplate.timeToGetControl" : ["%s" % cps[activeCpTemplate].sequence]})
					cons.insert(i, {"ObjectTemplate.timeToLoseControl" : ["%s" % cps[activeCpTemplate].sequence]})
					if cps[activeCpTemplate].utct == 0:
						templateStr, createStr = createSpawnDummyCpString(cps[activeCpTemplate])
						templateStr.reverse()
						for str in templateStr:
							cons.insert(i, str)
						cons.insert(i, {"ObjectTemplate.showOnMinimap" : ["0"]})
						cons.insert(i, {"ObjectTemplate.flagTemplateTeam0" : ["None"]})
						cons.insert(i, {"ObjectTemplate.flagTemplateTeam1" : ["None"]})
						cons.insert(i, {"ObjectTemplate.flagTemplateTeam2" : ["None"]})
						i += len(templateStr)+4		
					i += 2
				activeCpTemplate = cons[i]['ObjectTemplate.create'][1]
		#the last one
		if cons[i].get('if'):
			if len(activeCpTemplate) != 0: 
				cons.insert(i, {"ObjectTemplate.timeToGetControl" : ["%s" % cps[activeCpTemplate].sequence]})
				cons.insert(i, {"ObjectTemplate.timeToLoseControl" : ["%s" % cps[activeCpTemplate].sequence]})
				if cps[activeCpTemplate].utct == 0:
						templateStr, createStr = createSpawnDummyCpString(cps[activeCpTemplate])
						templateStr.reverse()
						for str in templateStr:
							cons.insert(i, str)
						cons.insert(i, {"ObjectTemplate.showOnMinimap" : ["0"]})
						cons.insert(i, {"ObjectTemplate.flagTemplateTeam0" : ["None"]})
						cons.insert(i, {"ObjectTemplate.flagTemplateTeam1" : ["None"]})
						cons.insert(i, {"ObjectTemplate.flagTemplateTeam2" : ["None"]})
						i += len(templateStr)+4
				i += 2
		i += 1
	#insert spawn dummys' create string
	i = 0
	activeCpTemplate = ''
	while i < len(cons):
		#print(cons[i])
		if cons[i].get('Object.create'):
			if cps.get(cons[i]['Object.create'][0]):
				if len(activeCpTemplate) != 0: 
					if cps[activeCpTemplate].utct == 0:
						templateStr, createStr = createSpawnDummyCpString(cps[activeCpTemplate])
						createStr.reverse()
						for str in createStr:
							cons.insert(i, str)			
						i += len(createStr)
				activeCpTemplate = cons[i]['Object.create'][0]
		#the last one
		#if cons[i].get('endIf'):#why 'endIf' cannot be found?
		if cons[i].get('CombatAreaManager.use'):
			if len(activeCpTemplate) != 0: 
				if cps[activeCpTemplate].utct == 0:
					templateStr, createStr = createSpawnDummyCpString(cps[activeCpTemplate])
					createStr.reverse()
					for str in createStr:
						cons.insert(i, str)			
					i += len(createStr)
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
		if AIcons[i].get('aiStrategicArea.addObjectTypeFlag'):
			if cps[activeCpTemplate].utct != 0:
				AIcons[i]['aiStrategicArea.addObjectTypeFlag'][0] = "Base"
		if AIcons[i].get('aiStrategicArea.setSide'):
			if cps[activeCpTemplate].utct != 0:
				AIcons[i]['aiStrategicArea.setSide'][0] = "%s" % cps[activeCpTemplate].team
		i += 1
		
		
def createTargetInfo(cps):
	targets = {}
	for cpname in cps:
		if cps[cpname].utct != 0 or cps[cpname].sequence == 0: continue
		targetName = cpname + "_target" + cps[cpname].AB
		#if cps[cpname].team == 2: team = 1
		#else: team = 2
		team = cps[cpname].team
		position = cps[cpname].position
		#rotation = cps[cpname].rotation
		layer = cps[cpname].layer
		print cps[cpname].templateName
		print cps[cpname].sequence
		controlPointId = cps[cpname].defSpDummyId#findFirstCpBySequence(cps, cps[cpname].sequence - 1).id
		
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

if __name__ == "__main__":
	cons = conParser.readCon('gameplayobjects.con')
	AIcons = conParser.readCon('ai/StrategicAreas.ai')
	cps = getCpInfoFromCons(cons)
	#if (len(cps)/2)*2 != len(cps): print "Warning: Number of CP is odd!"
	print "Please set the sequence and AB for ControlPoints(1A,2B,3B,4A,etc.)"
	for cpname in cps:
		print cpname + ": "
		if cps[cpname].utct != 0:
			print "unableToChangeTeam! Use as base!"
			continue
		info = raw_input().strip()
		#if info == "0": continue
		while(len(info) != 2):
			print "SyntaxError! Please input number and AB"
			info = raw_input().strip()
		else:
			cps[cpname].sequence = int(info[0])
			cps[cpname].AB = info[1].upper()
	#adjust sequence
	defTeam = 0
	maxSequence = 0
	for cpname in cps:
		if cps[cpname].utct == 0: 
			if defTeam == 0: defTeam = cps[cpname].team
			if maxSequence < cps[cpname].sequence: maxSequence = cps[cpname].sequence
		
	for cpname in cps:
		if cps[cpname].team == defTeam and cps[cpname].utct != 0:
			cps[cpname].sequence = maxSequence + 1

	if checkCpInfo(cps):
		printCpInfo(cps)
		print "Please confirm, input 'exit' to exit, else to continue:"
	else:
		cmd = raw_input()
		exit(0)
	cmd = raw_input()
	if cmd == 'exit': exit(0)
	else:
		changeCon(cons, cps)
		changeAiCon(AIcons, cps)
		#for con in AIcons:
		#	print con
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
		if cmd == 'exit': exit(0)
		else: 
			if writeTargetInfo(cmds, "GamePlayObjectsNEW.con"):
				print "Write target success"
				cmd = raw_input()
			else:
				print "Error writing GamePlayObjectsNEW.con" 
				cmd = raw_input()