import aiArtyV2
from artySettings import *

def init(enableCPArtyEvent=True):
	aiArtyV2.init(enableCPArtyEvent)
	
def deinit():
	aiArtyV2.deinit()
	
def eventNotify(team, type, position):
	aiArtyV2.aiCommander.eventNotify(team, aiArtyV2.EventInfo(type, position))
	
def eventDelete(team, type, position):
	aiArtyV2.aiCommander.eventDelete(team, aiArtyV2.EventInfo(type, position))