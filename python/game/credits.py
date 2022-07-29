# -*- coding: iso-8859-15 -*-
# wookie sniper mod credits by Scouty (25-03-2008)
# displays in-game message for developers/contributors/testers
# modified and included for the AIX mod developers

import math

import host
import bf2

import game.common
import game.players

def init():
    host.registerGameStatusHandler(gamestatus)

def gamestatus(status):
    if status == bf2.GameStatus.Playing:
        host.registerHandler("PlayerSpawn", playerspawn)

def playerspawn(player, soldier):
    try:
        if not hasattr(player, 'isdev'):
            playername = game.players.getname(player)
            developer = getdeveloper(playername)

            if developer != None and developer != "":
                player.isdev = 1
                game.common.sayall(developer)
            else:
                player.isdev = 0
    except:
        game.common.print_exception()

# current developers (update as needed)

developers = {
    "kysterama"                     : "Kysterama - AIX Developer",
    "aix_clivewil"                  : "Clivewil - AIX Developer",
    "dasroach"                      : "DasRoach - AIX Developer",
    "chad509"                       : "Chad509 - AIX Developer",
    "ffolkes"                       : "FFOLKES - AIX Developer",
    "head_hunter"                   : "imtheheadhunter - AIX Contributor",
    "Wujj12345"                     : "wujj123456 - AIX Contributor",
    "r4z0r49"                       : "R4Z0R49 - AIX Stats Developer",
    "scoutstrike"                   : "ScoutStrike AKA Scouty - Mod Contributor",
    "caliber_k"                     : "Caliber_k - AIX Developer",
    "velocity"                      : "Velocity - AIX Developer",
    "arn354"                        : "Ti_GER arn354 - AIX Stats Developer",
    "gerhart"                       : "Gerhart - AIX Tester",
    "realgrain"                     : "RealGrainWood - AIX Tester",
    "maniacvvv"                     : "ManiacVVV - AIX Tester",
    "red_devil_leader"              : "Red_Devil - AIX Tester",
    "im_freebase"                   : "freebase6 - AIX Tester"



}

def getdeveloper(playername):
    playername = playername.lower()
    if developers.has_key(playername):
        return developers[playername]
    else:
        return ""



