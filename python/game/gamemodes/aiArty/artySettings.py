g_debug = 1

G_ARTY_SETTINGS = { #artillery settings

	#artillery object config
	"TEAM1_ARTY_NAME" : ["ars_d30"],								#artillery template names for team 1(mec,ch)
	"TEAM2_ARTY_NAME" : ["usart_lw155"],							#artillery template names for team 2(us,eu)
	
	#legacy config
	"TEAM1_ARTY_SPAWNER_NAME" : "pyart_expobj",						#artillery spawner template name for team 1. Not recommended to modify!
	"TEAM2_ARTY_SPAWNER_NAME" : "pyart_expobj2",					#artillery spawner template name for team 1. Not recommended to modify!
	"TEAM1_ARTY_SIGNAL_SPAWNER_NAME" : "pyart_signal_expobj",		#artillery signal spawner template name for team 1. Not recommended to modify!
	"TEAM2_ARTY_SIGNAL_SPAWNER_NAME" : "pyart_signal_expobj2",		#artillery signal spawner template name for team 1. Not recommended to modify!
	"TEAM1_ARTY_MUZZ_SPAWNER_NAME" : "pyart_muzz_bundle",			#artillery muzz effect spawner template name for team 1. Not recommended to modify!
	"TEAM2_ARTY_MUZZ_SPAWNER_NAME" : "pyart_muzz_bundle",			#artillery muzz effect spawner template name for team 2. Not recommended to modify!
	"ARTY_MUZZ_PLACEHOLDER_NAME" : "pyart_muzz_placeholder",		#We need to know where to spawn the muzz effect. This should be a Bundle object with networkable added in tweak file of the artillery template.
	
	#system config
	"ANIM_UPDATE_INTERVAL" : 0.05,		#interval of artillery object animation updating
	"ARTY_SYNCFIRE_DELAY" :0.4,			#interval of fire between artillery objects
	
	#global config for artillery object (objecttemplates not found in "ARTY_CONFIG" use this global config)
	"ARTY_SPAWN_HEIGHT" : 1000.0,		#artillery spawn height. Not recommended to modify!
	"ARTY_SPAWN_HEIGHT_RANDOM" : 0.0,	#artillery spawn height random distribution. Not recommended to modify!
	"ARTY_SIGNAL_SPAWN_HEIGHT" : 1000.0,		#artillery spawn height. Not recommended to modify!
	"ARTY_SIGNAL_SPAWN_HEIGHT_RANDOM" : 0.0,	#artillery spawn height random distribution. Not recommended to modify!
	"ARTY_DEVIATION_RADIUS" : 30.0,		#artillery cover range
	"ARTY_BURSTSIZE" : 5,				#artillery shots per round
	"ARTY_SIGNAL_BURSTSIZE" : 1,		#signal shots before atillery. Change to 0 to disable signal shots.
	"ARTY_FIRE_INTERVAL" : 2.0,			#interval between artillery shot
	"ARTY_SIGNAL_FIRE_INTERVAL" : 5.0,	#interval between signal shot
	"ARTY_ROUND_INTERVAL" : 60.0,		#interval between artillery rounds
	
	"ANIM_BARREL_RECOIL_DISTANCE" : 0.5,#recoil animation distance
	"ANIM_BARREL_RECOIL_SPEED" : 8.0,	#recoil speed
	"ANIM_BARREL_PUSHBACK_SPEED" : 0.5,	#pushback speed
	
	"ARTY_SPAWNER_NAME" : "pyart_expobj",											#The artillery shell object
	"ARTY_SIGNAL_SPAWNER_NAME" : "pyart_signal_expobj",								#The signal artillery shell object
	"ARTY_MUZZ_SPAWNER_NAME" : "pyart_muzz_bundle",									#The artillery muzzle object
	"ARTY_MUZZ_PLACEHOLDER_NAMES" : ["pyart_muzz_placeholder", "e_muzz_artillery"],	#The placeholder templates to spawn the muzzle object
	
	#config for specified artillery object
	"ARTY_CONFIG" : {
		"ars_d30" : {
			"ARTY_SPAWNER_NAME" : "pyart_expobj",											#The artillery shell object
			"ARTY_SIGNAL_SPAWNER_NAME" : "pyart_signal_expobj",								#The signal artillery shell object
			"ARTY_MUZZ_SPAWNER_NAME" : "pyart_muzz_bundle",									#The artillery muzzle object
			"ARTY_MUZZ_PLACEHOLDER_NAMES" : ["pyart_muzz_placeholder", "e_muzz_artillery"],	#The placeholder templates to spawn the muzzle object
			"ARTY_SPAWN_HEIGHT" : 1000.0,		#artillery spawn height. Not recommended to modify!
			"ARTY_SPAWN_HEIGHT_RANDOM" : 0.0,	#artillery spawn height random distribution. Not recommended to modify!
			"ARTY_SIGNAL_SPAWN_HEIGHT" : 1000.0,		#artillery spawn height. Not recommended to modify!
			"ARTY_SIGNAL_SPAWN_HEIGHT_RANDOM" : 0.0,	#artillery spawn height random distribution. Not recommended to modify!
			"ARTY_DEVIATION_RADIUS" : 30.0,		#artillery cover range
			"ARTY_BURSTSIZE" : 5,				#artillery shots per round
			"ARTY_SIGNAL_BURSTSIZE" : 1,		#signal shots before atillery. Change to 0 to disable signal shots.
			"ARTY_FIRE_INTERVAL" : 2.0,			#interval between artillery shot
			"ARTY_SIGNAL_FIRE_INTERVAL" : 5.0,	#interval between signal shot
			"ARTY_ROUND_INTERVAL" : 60.0,		#interval between artillery rounds
			"ANIM_BARREL_RECOIL_DISTANCE" : 0.5,#recoil animation distance
			"ANIM_BARREL_RECOIL_SPEED" : 8.0,	#recoil speed
			"ANIM_BARREL_PUSHBACK_SPEED" : 0.5,	#pushback speed
		},
		
		"usart_lw155" : {
			"ARTY_SPAWNER_NAME" : "pyart_expobj2",											#The artillery shell object
			"ARTY_SIGNAL_SPAWNER_NAME" : "pyart_signal_expobj2",								#The signal artillery shell object
			"ARTY_MUZZ_SPAWNER_NAME" : "pyart_muzz_bundle",									#The artillery muzzle object
			"ARTY_MUZZ_PLACEHOLDER_NAMES" : ["pyart_muzz_placeholder", "e_muzz_artillery"],	#The placeholder templates to spawn the muzzle object
			"ARTY_SPAWN_HEIGHT" : 1000.0,		#artillery spawn height. Not recommended to modify!
			"ARTY_SPAWN_HEIGHT_RANDOM" : 0.0,	#artillery spawn height random distribution. Not recommended to modify!
			"ARTY_SIGNAL_SPAWN_HEIGHT" : 1000.0,		#artillery spawn height. Not recommended to modify!
			"ARTY_SIGNAL_SPAWN_HEIGHT_RANDOM" : 0.0,	#artillery spawn height random distribution. Not recommended to modify!
			"ARTY_DEVIATION_RADIUS" : 30.0,		#artillery cover range
			"ARTY_BURSTSIZE" : 5,				#artillery shots per round
			"ARTY_SIGNAL_BURSTSIZE" : 1,		#signal shots before atillery
			"ARTY_FIRE_INTERVAL" : 2.0,			#interval between artillery shot
			"ARTY_SIGNAL_FIRE_INTERVAL" : 5.0,	#interval between signal shot. Change to 0 to disable signal shots.
			"ARTY_ROUND_INTERVAL" : 60.0,		#interval between artillery rounds
			"ANIM_BARREL_RECOIL_DISTANCE" : 0.8,#recoil animation distance
			"ANIM_BARREL_RECOIL_SPEED" : 8.0,	#recoil speed
			"ANIM_BARREL_PUSHBACK_SPEED" : 0.8,	#pushback speed
		},
	},
}

G_SAT_SETTINGS = { #satellite settings
	"TEAM1_SATELLITE_NAME" : ["mobileradar_ch_dest","mobileradar_mech_dest"],			#satellite template names for team 1(mec,ch)
	"TEAM2_SATELLITE_NAME" : ["mobileradar_us_dest","mobileradar_eu_dest"],				#satellite template names for team 2(us,eu)
	"SAT_SCAN_INTERVAL" : 30.0,															#interval between satellite scans
	"SAT_SCAN_EXCLUDE_KITS" : ["CH_Specops", "US_Specops", "MEC_Specops", "EU_Specops"],#kits that can't be scaned by satellite
}

G_AIRDROP_SETTINGS = { #airdrop settings
	"TEAM1_SUPPLYDROP_NAME" : "supply_crate",			#supply drop object name for team 1(mec,ch)
	"TEAM2_SUPPLYDROP_NAME" : "supply_crate",			#supply drop object name for team 2(us,eu)
	"SUPPLYDROP_INTERVAL" : 30.0,						#interval between supply drops
	"SUPPLYDROP_DEVIATION_RADIUS" : 10.0,				#max deviation of supply drops(in meters)
	"SUPPLYDROP_DEVIATION_RADIUS_MIN" : 2.0,			#min deviation of supply drops(in meters)(to avoid dropping directly at the soldier and crush him)
	"SUPPLYDROP_SPAWN_HEIGHT" : 50.0,					#how high the supply crate will be spawn(in meters)
	"VEHICLEDROP_NAME_SUFFIX" : "",#"_drop",			#unused
	"VEHICLEDROP_INTERVAL" : 60.0,						#interval between vehicle drops
	"VEHICLEDROP_DEVIATION_RADIUS" : 15.0,				#max deviation of vehicle drops(in meters)
	"VEHICLEDROP_DEVIATION_RADIUS_MIN" : 4.0,			#min deviation of vehicle drops(in meters)(to avoid dropping directly at the soldier and crush him)
	"VEHICLEDROP_SPAWN_HEIGHT" : 15.0,					#how high the vehicle will be spawn(in meters)(too high will damage the vehicle)
}

#Artillery target types
OBJECT_ENEMY_IDLE = 0
OBJECT_ENEMY_SOLDIER = 1
OBJECT_ENEMY_LIGHTARMOUR = 2
OBJECT_ENEMY_HEAVYARMOUR = 3
OBJECT_ENEMY_UNKNOWN = 4
OBJECT_FRIENDLY_SOLDIER = 5
OBJECT_FRIENDLY_LIGHTARMOUR = 6
OBJECT_FRIENDLY_HEAVYARMOUR = 7
OBJECT_FRIENDLY_UNKNOWN = 8
#Artillery event types
EVENT_CPSTATUSCHANGE_NEUTRALIZE = 9
EVENT_CPSTATUSCHANGE_TOP = 10
##events for rush mod
EVENT_C4_OPERATING = 11
EVENT_C4_PLACED = 12
EVENT_C4_PLACED_PROTECT = 13

#Artillery target dummy types. Do not change!
OBJECT_UNKNOWN = 0		#unknown types
OBJECT_HEAVYARMOUR = 1	#heavy armor that is almost invulnerable to artillery
OBJECT_LIGHTARMOUR = 2	#light armor that is sensitive to artillery
OBJECT_SOLDIER = 3		#soldiers that is sensitive to artillery
OBJECT_SKIP = 4			#this means heli/jets/invulnerable targets that can never or have little chance to be damaged by artillery.

#dummy type to target types converter. Do not change!
FRIENDLYTYPE_CONVERT = {
	OBJECT_UNKNOWN : OBJECT_FRIENDLY_UNKNOWN,
	OBJECT_HEAVYARMOUR : OBJECT_FRIENDLY_HEAVYARMOUR,
	OBJECT_LIGHTARMOUR : OBJECT_FRIENDLY_LIGHTARMOUR,
	OBJECT_SOLDIER : OBJECT_FRIENDLY_SOLDIER,
}
ENEMYTYPE_CONVERT = {
	OBJECT_UNKNOWN : OBJECT_ENEMY_UNKNOWN,
	OBJECT_HEAVYARMOUR : OBJECT_ENEMY_HEAVYARMOUR,
	OBJECT_LIGHTARMOUR : OBJECT_ENEMY_LIGHTARMOUR,
	OBJECT_SOLDIER : OBJECT_ENEMY_SOLDIER,
}

#object convert table
#This defines all vbf2 vehicle's armor. It's recommended to add your own vehicles to the table.
VEHICLETYPE_CONVERT = {
	"usapc_lav25"		: OBJECT_HEAVYARMOUR,
	"apc_btr90"		: OBJECT_HEAVYARMOUR,
	"apc_wz551"		: OBJECT_HEAVYARMOUR,
	"ustnk_m1a2"		: OBJECT_HEAVYARMOUR,
	"rutnk_t90"		: OBJECT_HEAVYARMOUR,
	"tnk_type98"		: OBJECT_HEAVYARMOUR,
	"usair_f18"		: OBJECT_SKIP,
	"ruair_mig29"		: OBJECT_SKIP,
	"air_j10"		: OBJECT_SKIP,
	"usair_f15"		: OBJECT_SKIP,
	"ruair_su34"		: OBJECT_SKIP,
	"air_su30mkk"		: OBJECT_SKIP,
	"air_f35b"		: OBJECT_SKIP,
	"usaav_m6"		: OBJECT_HEAVYARMOUR,
	"aav_tunguska"		: OBJECT_HEAVYARMOUR,
	"aav_type95"		: OBJECT_HEAVYARMOUR,
	"usaas_stinger"		: OBJECT_LIGHTARMOUR,
	"igla_djigit"		: OBJECT_LIGHTARMOUR,
	"wasp_defence_front"	: OBJECT_LIGHTARMOUR,
	"wasp_defence_back"	: OBJECT_LIGHTARMOUR,
	"usthe_uh60"		: OBJECT_SKIP,
	"the_mi17"		: OBJECT_SKIP,
	"chthe_z8"		: OBJECT_SKIP,
	"ahe_ah1z"		: OBJECT_SKIP,
	"ahe_havoc"		: OBJECT_SKIP,
	"ahe_z10"		: OBJECT_SKIP,
	"jeep_faav"		: OBJECT_LIGHTARMOUR,
	"usjep_hmmwv"		: OBJECT_LIGHTARMOUR,
	"jep_paratrooper"	: OBJECT_LIGHTARMOUR,
	"jep_mec_paratrooper"	: OBJECT_LIGHTARMOUR,
	"jep_vodnik"		: OBJECT_LIGHTARMOUR,
	"jep_nanjing"		: OBJECT_LIGHTARMOUR,
	"uslcr_lcac"		: OBJECT_LIGHTARMOUR,
	"boat_rib"		: OBJECT_LIGHTARMOUR,
	"usart_lw155"		: OBJECT_SKIP,
	"ars_d30"		: OBJECT_SKIP,
	"ats_tow"		: OBJECT_LIGHTARMOUR,
	"ats_hj8"		: OBJECT_LIGHTARMOUR,
	"hmg_m2hb"		: OBJECT_LIGHTARMOUR,
	"chhmg_kord"		: OBJECT_LIGHTARMOUR,
	"mec_bipod"		: OBJECT_SOLDIER,
	"us_bipod"		: OBJECT_SOLDIER,
	"ch_bipod"		: OBJECT_SOLDIER,
	"us_soldier"		: OBJECT_SOLDIER,
	"us_heavy_soldier"	: OBJECT_SOLDIER,
	"us_light_soldier"	: OBJECT_SOLDIER,
	"mec_soldier"		: OBJECT_SOLDIER,
	"mec_light_soldier"	: OBJECT_SOLDIER,
	"mec_heavy_soldier"	: OBJECT_SOLDIER,
	"ch_soldier"		: OBJECT_SOLDIER,
	"ch_light_soldier"	: OBJECT_SOLDIER,
	"ch_heavy_soldier"	: OBJECT_SOLDIER,
	"parachute"		: OBJECT_SKIP,
#xpack1 stuff	
	"seal_soldier"		: OBJECT_SOLDIER,
	"seal_heavy_soldier"	: OBJECT_SOLDIER,
	"sas_soldier"		: OBJECT_SOLDIER,
	"sas_heavy_soldier"	: OBJECT_SOLDIER,
	"spetz_soldier"		: OBJECT_SOLDIER,
	"spetz_heavy_soldier"	: OBJECT_SOLDIER,
	"mecsf_soldier"		: OBJECT_SOLDIER,
	"mecsf_heavy_soldier"	: OBJECT_SOLDIER,
	"chinsurgent_soldier"		: OBJECT_SOLDIER,
	"chinsurgent_heavy_soldier"	: OBJECT_SOLDIER,
	"meinsurgent_soldier"		: OBJECT_SOLDIER,
	"meinsurgent_heavy_soldier"	: OBJECT_SOLDIER,

	"xpak_bmp3"		: OBJECT_HEAVYARMOUR,
	"xpak_forklift"		: OBJECT_LIGHTARMOUR,
	"xpak_atv"		: OBJECT_LIGHTARMOUR,
	"xpak_civ1"		: OBJECT_LIGHTARMOUR,
	"xpak_civ2"		: OBJECT_LIGHTARMOUR,
	"xpak_jetski"		: OBJECT_LIGHTARMOUR,
	"xpak_ailraider"	: OBJECT_LIGHTARMOUR,
	"xpak_apache"		: OBJECT_SKIP,
	"xpak_hind"		: OBJECT_SKIP,
	"xpak_hummertow"	: OBJECT_LIGHTARMOUR,

# booster pack 1
	"xpak2_vbl"		: OBJECT_LIGHTARMOUR,
	"xpak2_tnkl2a6"		: OBJECT_HEAVYARMOUR,
	"xpak2_tnkc2"		: OBJECT_HEAVYARMOUR,
	"xpak2_tiger"		: OBJECT_SKIP,
	"xpak2_lynx"		: OBJECT_SKIP,
	"xpak2_eurofighter"	: OBJECT_SKIP,
	"xpak2_harrier"		: OBJECT_SKIP,
	"eu_soldier"		: OBJECT_SOLDIER,
	"eu_heavy_soldier"	: OBJECT_SOLDIER,
	
# booster pack 2
	"air_a10"		: OBJECT_SKIP,
	"air_su39"		: OBJECT_SKIP,
	"xpak2_fantan"		: OBJECT_SKIP,
	"che_wz11"		: OBJECT_SKIP,
	"she_ec635"		: OBJECT_SKIP,
	"she_littlebird"	: OBJECT_SKIP,
	"xpak2_musclecar"	: OBJECT_LIGHTARMOUR,
	"xpak2_semi"		: OBJECT_LIGHTARMOUR,
}

G_AI_SETTINGS = { #ai commander settings
	"RANDOM_ARTY" : 1, #percentage of artillery after cp status change(v1.0 legacy, not used anymore)
	"ONLY_IN_AIGAME" : True, #only enable this plugin in ai game(sp/coop).If False, this plugin will also function in pvp games.
	#Below are ai weights for different types of objects/events. Not recommended to change! Change only if you know what you are doing.
	#random weight
	"WEIGHT_RANDOM" : 0.25,
	#Position weight
	OBJECT_ENEMY_IDLE : 0.25,
	OBJECT_ENEMY_SOLDIER : 0.1,
	OBJECT_ENEMY_LIGHTARMOUR : 0.15,
	OBJECT_ENEMY_HEAVYARMOUR : 0.05,
	OBJECT_ENEMY_UNKNOWN : 0.1,
	OBJECT_FRIENDLY_SOLDIER : -0.4,
	OBJECT_FRIENDLY_LIGHTARMOUR : -0.6,
	OBJECT_FRIENDLY_HEAVYARMOUR : -0.1,
	OBJECT_FRIENDLY_UNKNOWN : -0.2,
	#event weight
	EVENT_CPSTATUSCHANGE_NEUTRALIZE : (0.6,20.0),#(addweight,decaytime)
	EVENT_CPSTATUSCHANGE_TOP : (0.4,10.0),
	##events for rush mod
	EVENT_C4_OPERATING : (0.8,5.0),
	EVENT_C4_PLACED : (0.4,4.0),
	EVENT_C4_PLACED_PROTECT : (0.8,20.0),
	
	#weight modifier according to range to cp. Not recommended to change!
	#INCP MODIFIER = 1 + (OBJECT_INCP_WEIGHT_MODIFIER_MAX-1) * distance / (cp.radius * OBJECT_INCP_DIST_THRESHOLD_RADIUS_MODIFIER)
	"OBJECT_INCP_WEIGHT_MODIFIER_MAX" : 2.0,
	"OBJECT_INCP_DIST_THRESHOLD_RADIUS_MODIFIER" : 3.0,
	
	"OBJECT_IDLE_DIST_THRESHOLD" : 10.0,	#objects that have moved shorter than this during two satellite scans are counted as idle objects, and therefore has more chance to be blown up by artillery
	"VEHICLE_SPEED_THRESHOLD" : 6.0,		#vehicles faster than this is not counted as weight. Not recommended to change!
	"ARTY_WEIGHT_THRESHOLD" : 0.3,			#only artillery points with weights bigger than this is artillery used. Not recommended to change!
	"ARTY_ROUGHDIST_THRESHOLD" : 25.0, 		#objects further than this to the artillery center is not counted as weight(should not be too far from "ARTY_DEVIATION_RADIUS")
	
	"LOOP_INTERVAL" : 3.0,					#main loop timer interval. Not recommended to change!
}