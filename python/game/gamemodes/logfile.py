
import sys
import host
#from bf2 import g_debug
#from rush import loop
	
def init():
	#logFile = open('mods/Rush/logfile.log', 'w')
	logFile = open(host.sgl_getModDirectory() + '/logfile.log','w')
	sys.stdout = logFile
	sys.stderr = logFile
	#g_debug = 1
	#print host.sgl_getModDirectory()
	print "local logfile init"
	sys.stdout.flush()
	#loop(1, sys.stdout.flush)
	
def deinit():
	sys.stdout.flush()