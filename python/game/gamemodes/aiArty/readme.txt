This is a plugin that enables AI commander, which automatically use artillery and respond to "request supply drop" and "request vehicle drop" given by a squad leader. The plugin was tested under vallina bf2 and some bf2 mods(like CUR). You are free to use it in any mod. -- worldlife(worldlife123)


FEATURES£º
1. If there's no human player being the commander, AI commander would automatically use artillery strikes. Destroying enemy artillery objects can weaken or cut off enemy artillery strikes, like in online games.
2. If there's human player on command, there will be no auto-artillery for the team.
3. AI commander utilizes the satellite scan to get information about enemy locations, which is to say, destroying the radar can also protect firendly units from enemy artillery.
4. AI commander would respond to "request supply drop" and "request vehicle drop" given by a squad leader. Unlike human commander, the ai commander directly drops the object above the requester, not at the crosshair of the requester. Note that no radio message will be given.
The vehicle drop spawns a vehicle without parachute, so the vehicle may be damaged or explode on landing. The spawned vehicle template is same as what human commander drops, which is set in init.con in the map folder.


CHANGELOG£º
V2.0
1. Added artillery trails and sounds. Red trails for team 1 and Blue trails for team 2. Sounds from vanilla bf2.
2. Improved ai system. The artillery positions are not bounded by controlpoints any more! AI commander will automatically find the best place to use artillery.
3.Added satellite scan system. AI commander use this to get information about enemy locations.

V2.0.1
1. Various small fixes.
2. Added ONLY_IN_AIGAME option. Enabling this will disable this plugin in pvp games.

V3.0
1. Added barrel rotation and recoil animation and muzzle effect on artillery objects. A little tweak is made on bf2 artillery objects in order to make it work in multiplayer game. Note that muzzle effect is set to work only in singleplayer in order to avoid maximum networkable object issue. Muzzle effects from vanilla bf2.
2. Changed artillery shoot style: the artillery first shoot a round of signal smoke, then 5 rounds of explosive rounds. This can be tweaked in artySettings.py.
3. Added apply supply drop and vehicle drop system. A little tweak is made on the squadleader radio interface in order to make it work.
4. Update config system so that custom artillery objects can use this system easily.


INSTALL£º£¨Attention! If you've installed previous versions of this plugin, remove all previous files before installation!£©
(1)Backup your python folder in your mod folder.
(2)Copy and replace all files in this package into your mod folder.After this, open ServerArchieves.con,and add this line at the head of the file:
fileManager.mountArchive objects_server_aiArty.zip Objects
(3)Run mapinstall.bat. If any new map is added to the mod, this script need to be rerun in order to make the new map work.


CUSTOM INSTALL£º
If your mod has modified files in python/game/gamemodes£¬please do not copy and replace the python folder, and refer to python/game/gamemodes/aiArty/install.txt to complete your installation.


KNOWN BUGS:
The recoil animation sometimes play over and over, and no artillery will be shot. We are looking into this.


UNINSTALL£º
Recover the python folder and delete objects_server_aiArty.zip to uninstall the plugin¡£


CUSTOMIZATION£º
Many arguments like artillery interval and artillery cover radius can be modified¡£All arguments are set in python/game/gamemodes/aiArty/artySettings.py, with detailed explanation. Be careful! If you've got no knowledge or experience with python files, please backup the file every time you modify it or refer to the python docs.