
import sys
import host
#from bf2 import g_debug
import time

LOGFILE_ENABLE = 1
CMD_ECHO_ENABLE = 1
	
logFile = None
	
def init():
	#logFile = open('mods/Rush/logfile.log', 'w')
	global logFile
	if logFile==None: 
		logFile = open(host.sgl_getModDirectory() + '/logfile.log','w')
		sys.stdout = logFile
		sys.stderr = logFile
		#g_debug = 1
		print time.strftime("%Y/%m/%d %H:%M:%S	")
		print "local logfile init"
	#import os
	#print dir(os)
	sys.stdout.flush()
	
def deinit():
	global logFile
	sys.stdout.flush()
	#logFile.close() #cause "Fail to update remove player: " error

def output(outputinfo, writeTime=True, writelogfile=True, writecmdecho=True):
	if LOGFILE_ENABLE or CMD_ECHO_ENABLE:
		if (LOGFILE_ENABLE and writelogfile): 
			if writeTime:print time.strftime("%Y/%m/%d %H:%M:%S	")
			print outputinfo
			sys.stdout.flush()
		if (CMD_ECHO_ENABLE and writecmdecho): 
			if len(outputinfo)<100:#avoid cmd return/too long
				host.rcon_invoke("echo \"" + outputinfo + "\"")
			else:
				host.rcon_invoke("echo \"" + outputinfo[:100] + "...\"")
	
def batchOutput(outputinfos, writelogfile=True, writecmdecho=True):
	if LOGFILE_ENABLE or CMD_ECHO_ENABLE:
		output = " ".join(outputinfos)
		if (LOGFILE_ENABLE and writelogfile): 
			print time.strftime("%Y/%m/%d %H:%M:%S	")
			print output
		if (CMD_ECHO_ENABLE and writecmdecho): 
			if len(output)<100:
				host.rcon_invoke("echo \"" + output + "\"")
			else:
				host.rcon_invoke("echo \"" + output[:100] + "...\"")