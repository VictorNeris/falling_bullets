# -*- coding: iso-8859-15 -*-
# wookie sniper mod common script by Scouty (14-03-2008)
# provides common exception/rcon/output/vector/template functions
# modified and included for the AIX mod custom scoring

import sys
import traceback
import math

import host
import bf2

def print_exception():
    exceptiontype, exceptionmessage, tracebackobject = sys.exc_info()

    while tracebackobject:
        code = tracebackobject.tb_frame.f_code

        filenamestring = code.co_filename
        filenameparts = filenamestring.split("\\")
        filenametext = filenameparts[len(filenameparts)-1]
        
        print "Exception in: " + filenametext + " (line " + str(traceback.tb_lineno(tracebackobject)) + ")"
        sayall("Exception in: " + filenametext + " (line " + str(traceback.tb_lineno(tracebackobject)) + ")")

        tracebackobject = tracebackobject.tb_next

    print "Exception type: " + str(exceptiontype)
    print "Exception message: " + str(exceptionmessage)

    sayall("Exception type: " + str(exceptiontype))
    sayall("Exception message: " + str(exceptionmessage))

def rcon_invoke(command):
    #print "rcon_invoke: " + str(command)
    result = host.rcon_invoke(command).strip()
    #print "rcon_result: " + str(result)
    return result

def sayall(text):
    text = text.replace("\"","'")
    rcon_invoke("game.sayall \"" + str(text) + "\"")

def sayteam(text, team):
    text = text.replace("\"","'")
    rcon_invoke("game.sayteam " + str(team) + " \"" + str(text) + "\"")

def echo(text):
    text = text.replace("\"","'")
    rcon_invoke("echo '" + str(text) + "'")

def vectordistance(vector1, vector2):
    if vector1 == None or vector2 == None: return 0.0
    if len(vector1) != 3 or len(vector2) != 3: return 0.0
    
    difference = [0.0, 0.0, 0.0]
    difference[0] = abs(float(vector1[0]) - float(vector2[0]))
    difference[1] = abs(float(vector1[1]) - float(vector2[1]))
    difference[2] = abs(float(vector1[2]) - float(vector2[2]))

    # calculate square root
    return (difference[0]**2 + difference[1]**2 + difference[2]**2)**.5

def vectorcompare(vector1, vector2, error = 0):
    if vector1 == None or vector2 == None: return False
    if len(vector1) != 3 or len(vector2) != 3: return False

    if abs(float(vector1[0]) - float(vector2[0])) <= error:
        if abs(float(vector1[1]) - float(vector2[1])) <= error:
            if abs(float(vector1[2]) == float(vector2[2])) <= error:
                return True
    else:
        return False

def vectoriszero(vector):
    if float(vector[0]) == 0.0 and float(vector[1]) == 0.0 and float(vector[2]) == 0.0:
        return True
    else:
        return False

def vectorround(vector, digits):
    rounded = [0.0, 0.0, 0.0]
    rounded[0] = round(vector[0], digits)
    rounded[1] = round(vector[1], digits)
    rounded[2] = round(vector[2], digits)

    return rounded

def templatelist(template):
    result = rcon_invoke("object.listObjectsOfTemplate " + str(template))
    if result == None or result == "": return None

    idlist = []
    i = 0
    for line in result:
        parts = line.split(" ")
        id = parts[3]
        idlist[i] = id
        i += 1

    return idlist

def validate(object):
    return object.isValid()






