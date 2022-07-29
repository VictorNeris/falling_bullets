import bf2
from rush_maps import *
#import rush
#import rush_mp
import cq
import rush_v2
import rush_sp5


#from game.settings import *

global current_mode

def init():
	current_map = bf2.gameLogic.getMapName().lower()
	global current_mode
	if current_map in RUSH_MAPS: #and bf2.gameLogic.isAIGame():
		current_mode = 'rush'
		#import rush_sp5
		rush_sp5.init()
		#cq.init()
	elif current_map in RUSHV2_MAPS:
		current_mode = 'rushv2'
		#import rush_v2
		rush_v2.init()
	else:
		current_mode = 'cq'
		#import cq
		cq.init()

def deinit():
	global current_mode
	if current_mode == 'rush':
		rush_sp5.deinit()
		#cq.deinit()
	elif current_mode == 'rushv2':
		rush_v2.deinit()
	else:	
		cq.deinit()