 #from http://www.bf2tech.org/index.php/Cookbook:How_To_Implement_Better_Error_Catching
 #submitted by King of Camelot

import sys
import inspect
import re
 
def ExceptionOutput():
    sys.stderr.write("\n" + "Exception Occured: " + str(sys.exc_info()[0]) + "\n")
    sys.stderr.write("Value: " + str(sys.exc_info()[1]) + "\n")	
    sys.stderr.write("Line:" + str(readline(inspect.getfile(sys.exc_info()[2]),
                     sys.exc_info()[2].tb_lineno)) + "\n")	
    sys.stderr.write("Line #: " + str(sys.exc_info()[2].tb_lineno) + "\n")
    sys.stderr.write("File: " + str(inspect.getfile(sys.exc_info()[2])) + "\n" + "\n")
 
 
def ExceptionOutputEcho():
    host.rcon_invoke("echo \""+"\n" + "Exception Occured: " + str(sys.exc_info()[0]) + "\"")
    host.rcon_invoke("echo \""+"Value: " + str(sys.exc_info()[1]) + "\"")	
    host.rcon_invoke("echo \""+"Line:" + str(readline(inspect.getfile(sys.exc_info()[2]),
                     sys.exc_info()[2].tb_lineno)) + "\"")	
    host.rcon_invoke("echo \""+"Line #: " + str(sys.exc_info()[2].tb_lineno) + "\"")
    host.rcon_invoke("echo \""+"File: " + str(inspect.getfile(sys.exc_info()[2])) + "\"") 
 
def readline(filename, lineno):
    filen = re.sub('\\\\', '/', filename)
    file = open(filen, 'rU')
    lines = file.readlines()
    file.close()
    linen = lineno - 1
    line = re.sub('\s+', ' ', lines[linen])
    return line