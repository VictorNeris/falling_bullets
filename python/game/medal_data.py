from constants import *
from bf2 import g_debug

globalKeysNeeded = {}

# criteria functions

def player_score (player_attr, value=None):
	if value == None:
		def _player_score (player):
			return getattr (player.score, player_attr)
	else:
		def _player_score (player):
			return getattr (player.score, player_attr) >= value
	return _player_score


def player_stat (player_attr, value):
	def _player_stat (player):
		return getattr (player.stats, player_attr) >= value
	return _player_stat

def object_stat (object_type, item_attr, item_type, value=None):
	if value == None:
		def _object_stat (player):
			return getattr (getattr (player.stats, object_type)[item_type], item_attr)
	else:
		def _object_stat (player):
			return getattr (getattr (player.stats, object_type)[item_type], item_attr) >= value
	return _object_stat

def has_medal (id, level=1):
	def _has_medal (player):
#		if not (id in player.medals.roundMedals and player.medals.roundMedals[id] >= level):
#			if g_debug: print "Didnt have medal: ", id, " in ", player.medals.roundMedals
		return id in player.medals.roundMedals and player.medals.roundMedals[id] >= level
	return _has_medal

def times_awarded(id, player):
	if id in player.medals.roundMedals:
#		if g_debug: print "Found medal %s with level %d" % (id, player.medals.roundMedals[id])
		return player.medals.roundMedals[id] # TIMES awarded, not level
	else:
		return 0

def global_stat_multiple_times (stat_key, value, id):
	globalKeysNeeded[stat_key] = 1
	def _global_stat_multiple_times (player):
		new_time_value = (value * (times_awarded(id, player)+1))
		return stat_key in player.medals.globalKeys and player.medals.globalKeys[stat_key] >= new_time_value
	return _global_stat_multiple_times

def global_stat (stat_key, value=None):
	globalKeysNeeded[stat_key] = 1
	if value == None:
		def _global_stat (player):
			if stat_key in player.medals.globalKeys: return player.medals.globalKeys[stat_key]
			else: return 0
	else:
		def _global_stat (player):
			return stat_key in player.medals.globalKeys and player.medals.globalKeys[stat_key] >= value
	return _global_stat


def has_rank (rank):
	def _has_rank (player):
		# Can be very noisy
		#if g_debug: print "Current rank: %d, going for rank: %d" % (player.score.rank, rank)
		return player.score.rank == rank
	return _has_rank
			
# logical functions

def f_and (*arg_list):
	def _f_and (player):
		res = True
		for f in arg_list:
			res = res and f(player)
			#if g_debug: print f(player)
		return res
	return _f_and

def f_or (*arg_list):
	def _f_or (player):
		res = True
		for f in arg_list:
			res = res or f(player)
		return res
	return _f_or

def f_not (f):
	def _f_not (player):
		return not f(player)
	return _f_not

def f_plus(a, b, value=None):
	if value == None:
		def _f_plus (player):
			return a(player) + b(player)
	else:
		def _f_plus (player):
			return a(player) + b(player) >= value
	return _f_plus

def f_div(a, b, value=None):
	if value == None:
		def _f_div (player):
			denominator = b(player)
			if denominator == 0: return a(player)+1
			else: return a(player) / denominator
	else:
		def _f_div (player):
			denominator = b(player)
			
			if denominator == 0: 
				return a(player)+1
			else: 
				return a(player) / denominator >= value

	return _f_div



# medal definitions

medal_data = (

	#Badges - Infantry
		#Knife Combat Badge
			#Basic
			('1031406_1',	'kcb',	1, object_stat ('weapons', 'kills', WEAPON_TYPE_KNIFE, 3)),

			#Veteran
			('1031406_2',	'kcb',	1, f_and( 	has_medal ('1031406_1'), object_stat ('weapons', 'kills', WEAPON_TYPE_KNIFE, 5))),

			#Expert	
			('1031406_3',	'kcb',	1, f_and( 	has_medal ('1031406_2'), object_stat ('weapons', 'kills', WEAPON_TYPE_KNIFE, 10))),

		#Pistol Combat Badge
			#Basic
			('1031619_1', 'pcb',	1, object_stat ('weapons', 'kills', WEAPON_TYPE_PISTOL, 5)),

			#Veteran
			('1031619_2', 'pcb',	1, f_and( 	has_medal ('1031619_1'), object_stat ('weapons', 'kills', WEAPON_TYPE_PISTOL, 10))),

			#Expert
			('1031619_3', 'pcb',	1, f_and( 	has_medal ('1031619_2'), object_stat ('weapons', 'kills', WEAPON_TYPE_PISTOL, 20))),

		#Assault Combat Badge
			#Basic
			('1031119_1', 'Acb',	1, object_stat ('kits', 'kills', KIT_TYPE_ASSAULT, 10)),

			#Veteran
			('1031119_2', 'Acb',	1, f_and( 	has_medal ('1031119_1'), object_stat ('kits', 'kills', KIT_TYPE_ASSAULT, 20))),

			#Expert
			('1031119_3', 'Acb',	1, f_and( 	has_medal ('1031119_2'), object_stat ('kits', 'kills', KIT_TYPE_ASSAULT, 40))),

		#Anti-Tank Combat Badge
			#Basic
			('1031120_1', 'Atcb',	1, object_stat ('kits', 'kills', KIT_TYPE_AT, 10)),

			#Veteran
			('1031120_2', 'Atcb',	1, f_and( 	has_medal ('1031120_1'), object_stat ('kits', 'kills', KIT_TYPE_AT, 20))),

			#Expert
			('1031120_3', 'Atcb',	1, f_and( 	has_medal ('1031120_2'), object_stat ('kits', 'kills', KIT_TYPE_AT, 40))),

		#Sniper Combat Badge
			#Basic
			('1031109_1', 'Sncb',	1, object_stat ('kits', 'kills', KIT_TYPE_SNIPER, 10)),

			#Veteran
			('1031109_2', 'Sncb',	1, f_and( 	has_medal ('1031109_1'), object_stat ('kits', 'kills', KIT_TYPE_SNIPER, 20))),

			#Expert
			('1031109_3', 'Sncb',	1, f_and( 	has_medal ('1031109_2'), object_stat ('kits', 'kills', KIT_TYPE_SNIPER, 40))),

		#Spec Ops Combat Badge
			#Basic
			('1031115_1', 'Socb',	1, object_stat ('kits', 'kills', KIT_TYPE_SPECOPS, 10)),

			#Veteran
			('1031115_2', 'Socb',	1, f_and( 	has_medal ('1031115_1'), object_stat ('kits', 'kills', KIT_TYPE_SPECOPS, 20))),

			#Expert
			('1031115_3', 'Socb',	1, f_and( 	has_medal ('1031115_2'), object_stat ('kits', 'kills', KIT_TYPE_SPECOPS, 40))),

		#Support Combat Badge
			#Basic
			('1031121_1', 'Sucb',	1, object_stat ('kits', 'kills', KIT_TYPE_SUPPORT, 10)),

			#Veteran
			('1031121_2', 'Sucb',	1, f_and( 	has_medal ('1031121_1'), object_stat ('kits', 'kills', KIT_TYPE_SUPPORT, 20))),

			#Expert
			('1031121_3', 'Sucb',	1, f_and( 	has_medal ('1031121_2'), object_stat ('kits', 'kills', KIT_TYPE_SUPPORT, 40))),

		#Engineer Combat Badge
			#Basic
			('1031105_1', 'Ecb',	1, object_stat ('kits', 'kills', KIT_TYPE_ENGINEER, 10)),

			#Veteran
			('1031105_2', 'Ecb',	1, f_and( 	has_medal ('1031105_1'), object_stat ('kits', 'kills', KIT_TYPE_ENGINEER, 20))),

			#Expert
			('1031105_3', 'Ecb',	1, f_and( 	has_medal ('1031105_2'), object_stat ('kits', 'kills', KIT_TYPE_ENGINEER, 40))),

		#Medic Combat Badge
			#Basic
			('1031113_1', 'Mcb',	1, object_stat ('kits', 'kills', KIT_TYPE_MEDIC, 10)),

			#Veteran
			('1031113_2', 'Mcb',	1, f_and( 	has_medal ('1031113_1'), object_stat ('kits', 'kills', KIT_TYPE_MEDIC, 20))),

			#Expert
			('1031113_3', 'Mcb',	1, f_and( 	has_medal ('1031113_2'), object_stat ('kits', 'kills', KIT_TYPE_MEDIC, 40))),

		#Explosive Ordinance Badge
			#Basic
			('1032415_1', 'Eob',	1,	f_plus(	object_stat ('weapons', 'kills', WEAPON_TYPE_C4), f_plus(		object_stat ('weapons', 'kills', WEAPON_TYPE_ATMINE),
															object_stat ('weapons', 'kills', WEAPON_TYPE_CLAYMORE)), 3)),
												

			#Veteran
			('1032415_2', 'Eob',	1, f_and( 	has_medal ('1032415_1'), f_plus(	object_stat ('weapons', 'kills', WEAPON_TYPE_C4),
														f_plus(	object_stat ('weapons', 'kills', WEAPON_TYPE_ATMINE),
																object_stat ('weapons', 'kills', WEAPON_TYPE_CLAYMORE)), 5))),

			#Expert
			('1032415_3', 'Eob',	1, f_and( 	has_medal ('1032415_2'), f_plus(	object_stat ('weapons', 'kills', WEAPON_TYPE_C4),
														f_plus(	object_stat ('weapons', 'kills', WEAPON_TYPE_ATMINE),
																object_stat ('weapons', 'kills', WEAPON_TYPE_CLAYMORE)), 10))),

		#First Aid Badge
			#Basic
			('1190601_1', 'Fab',	1, player_score ('heals', 3)),

			#Veteran
			('1190601_2', 'Fab',	1, f_and( 	has_medal ('1190601_1'), player_score ('heals', 5))),

			#Expert
			('1190601_3', 'Fab',	1, f_and( 	has_medal ('1190601_2'), player_score ('heals', 10))),

		#Engineer Badge
			#Basic
			('1190507_1', 'Eb',	1, player_score ('repairs', 3)),

			#Veteran
			('1190507_2', 'Eb',	1, f_and( 	has_medal ('1190507_1'), player_score ('repairs', 5))),

			#Expert
			('1190507_3', 'Eb',	1, f_and( 	has_medal ('1190507_2'), player_score ('repairs', 10))),

		#Resupply Badge
			#Basic
			('1191819_1', 'Rb',	1, player_score ('ammos', 3)),

			#Veteran
			('1191819_2', 'Rb',	1, f_and( 	has_medal ('1191819_1'), player_score ('ammos', 5))),

			#Expert
			('1191819_3', 'Rb',	1, f_and( 	has_medal ('1191819_2'), player_score ('ammos', 10))),

		#Command Badge
			#Basic
			('1190304_1', 'Cb',	1, player_stat ('timeAsCmd', 600)),

			#Veteran
			('1190304_2', 'Cb',	1, f_and( 	has_medal ('1190304_1'), player_stat ('timeAsCmd', 1200))),

			#Expert
			('1190304_3', 'Cb',	1, f_and( 	has_medal ('1190304_2'), player_stat ('timeAsCmd', 1800))),

	#Badges - Vehicles
		#Armour Badge
			#Basic
			('1220118_1', 'Ab',	1, object_stat ('vehicles', 'rtime', VEHICLE_TYPE_ARMOR, 300)),

			#Veteran
			('1220118_2', 'Ab',	1, f_and( 	has_medal ('1220118_1'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_ARMOR, 12), object_stat ('vehicles', 'rtime', VEHICLE_TYPE_ARMOR, 600))),

			#Expert
			('1220118_3', 'Ab',	1, f_and( 	has_medal ('1220118_2'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_ARMOR, 24), object_stat ('vehicles', 'rtime', VEHICLE_TYPE_ARMOR, 1200))),

		#Transport Badge
			#Basic
			('1222016_1', 'Tb',	1, object_stat ('vehicles', 'rtime', VEHICLE_TYPE_TRANSPORT, 600)),

			#Veteran
			('1222016_2', 'Tb',	1, f_and( 	has_medal ('1222016_1'), object_stat ('vehicles', 'roadKills', VEHICLE_TYPE_TRANSPORT, 1))),

			#Expert
			('1222016_3', 'Tb',	1, f_and( 	has_medal ('1222016_2'), object_stat ('vehicles', 'roadKills', VEHICLE_TYPE_TRANSPORT, 5))),

		#Helicopter Badge
			#Basic
			('1220803_1', 'Hb',	1, object_stat ('vehicles', 'rtime', VEHICLE_TYPE_HELICOPTER, 300)),

			#Veteran
			('1220803_2', 'Hb',	1, f_and( 	has_medal ('1220803_1'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_HELICOPTER, 12), object_stat ('vehicles', 'rtime', VEHICLE_TYPE_HELICOPTER, 600))),

			#Expert
			('1220803_3', 'Hb',	1, f_and( 	has_medal ('1220803_2'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_HELICOPTER, 24), object_stat ('vehicles', 'rtime', VEHICLE_TYPE_HELICOPTER, 1200))),

		#Aviator Badge
			#Basic
			('1220122_1', 'Avb',	1, object_stat ('vehicles', 'rtime', VEHICLE_TYPE_AVIATOR, 300)),

			#Veteran
			('1220122_2', 'Avb',	1, f_and( 	has_medal ('1220122_1'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_AVIATOR, 12), object_stat ('vehicles', 'rtime', VEHICLE_TYPE_AVIATOR, 600))),

			#Expert
			('1220122_3', 'Avb',	1, f_and( 	has_medal ('1220122_2'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_AVIATOR, 24), object_stat ('vehicles', 'rtime', VEHICLE_TYPE_AVIATOR, 1200))),

		#Air Defence Badge
			#Basic
			('1220104_1', 'adb',	1, object_stat ('vehicles', 'kills', VEHICLE_TYPE_AIRDEFENSE, 5)),

			#Veteran
			('1220104_2', 'adb',	1, f_and( 	has_medal ('1220104_1'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_AIRDEFENSE, 10))),

			#Expert
			('1220104_3', 'adb',	1, f_and( 	has_medal ('1220104_2'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_AIRDEFENSE, 20))),

		#Ground Defence Badge
			#Basic
			('1031923_1', 'Swb',	1, object_stat ('vehicles', 'kills', VEHICLE_TYPE_GRNDDEFENSE, 10)),

			#Veteran
			('1031923_2', 'Swb',	1, f_and( 	has_medal ('1031923_1'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_GRNDDEFENSE, 20))),

			#Expert
			('1031923_3', 'Swb',	1, f_and( 	has_medal ('1031923_2'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_GRNDDEFENSE, 40))),

		#Ribbons
# Added by Chump - for bf2statistics stats
			#Updated these service ribbons to be based on Global Map Time
			#Mid-East Service
			# Move to BACKEND!!
			# ('3191305', 'Msr', 1, f_and(	global_stat('mtm-0', 1),	# kubra_dam
											# global_stat('mtm-1', 1),	# mashtuur_city
											# global_stat('mtm-2', 1),	# operation_clean_sweep
											# global_stat('mtm-3', 1),	# zatar_wetlands
											# global_stat('mtm-4', 1),	# strike_at_karkand
											# global_stat('mtm-5', 1),	# sharqi_peninsula
											# global_stat('mtm-6', 1),	# gulf_of_oman
										# )),

			#Far-East Service
			# Moved to BACKEND!!
			# ('3190605', 'Fsr', 1, f_and(	global_stat('mtm-100', 1),	# daqing_oilfields
											# global_stat('mtm-101', 1),	# dalian_plant
											# global_stat('mtm-102', 1),	# dragon_valley
											# global_stat('mtm-103', 1),	# fushe_pass
											# #global_stat('mtm-104', 1),	# hingan_hills (Doesn't Exist!)
											# global_stat('mtm-105', 1),	# songhua_stalemate
											# global_stat('mtm-601', 1),	# wake_island_2007
										# )),

			#Combat Action Ribbon
			('3240301',	'Car',	1, f_and(	global_stat ('bksk', 10),
											player_score ('kills', 18))),

			#Meritorious Unit Ribbon
			('3211305',	'Mur',	1, f_and(	player_stat ('timeInSquad', 1560),
											player_score ('rplScore', 5))),

			#Infantry Officer Ribbon
			('3150914',	'Ior',	1, f_and(	global_stat ('twsc', 250),
											player_stat ('timeAsSql', 1500))),

			#Staff Officer Ribbon
			('3151920',	'Sor',	1, f_and(	player_stat ('timeAsCmd', 1680),
											player_score ('cmdScore', 50))),

			#Distinguished Service Ribbon
			('3190409',	'Dsr',	1, f_and(	global_stat ('tsqm', 3600),
											global_stat ('tsql', 360),
											global_stat ('tcdr', 360),
											player_score ('rplScore', 12))),

			#War College Ribbon
			('3242303',	'Wcr',	1, f_and(	global_stat ('tcdr', 3600),
											global_stat ('wins', 5),
											global_stat ('cdsc', 250))), 

			#Valorous Unit Ribbon
			('3212201',	'Vur',	1, f_and(	global_stat ('tsqm', 9000),
											global_stat ('tsql', 900),
											player_score ('rplScore', 8))),

			#Legion of Merit Ribbon
			('3241213',	'Lmr',	1, f_and(	global_stat ('time', 24000),
											global_stat ('bksk', 10),
											global_stat ('wdsk', 8),
											player_score ('rplScore', 50))),

			#Crew Service Ribbon
			('3190318',	'Csr',	1, f_and(	f_plus(
												player_score ('driverSpecials'), 
												player_score ('driverAssists'), 13),
											player_score ('kills', 5))),

			#Armoured Service Ribbon
			('3190118',	'Arr',	1, f_and(	object_stat ('vehicles', 'rtime', VEHICLE_TYPE_ARMOR, 1200),
											object_stat ('vehicles', 'kills', VEHICLE_TYPE_ARMOR, 10))),

			#Aerial Service Ribbon
			('3190105',	'Aer',	1, f_and(	object_stat ('vehicles', 'rtime', VEHICLE_TYPE_AVIATOR, 900),
											object_stat ('vehicles', 'kills', VEHICLE_TYPE_AVIATOR, 10))),

			#Helicopter Service Ribbon
			('3190803',	'Hsr',	1, f_and(	object_stat ('vehicles', 'rtime', VEHICLE_TYPE_HELICOPTER, 900),
											object_stat ('vehicles', 'kills', VEHICLE_TYPE_HELICOPTER, 10))),

			#Air-Defence Ribbon
			('3040109',	'Adr',	1, f_and(	object_stat ('vehicles', 'rtime', VEHICLE_TYPE_AIRDEFENSE, 180),
											object_stat ('vehicles', 'kills', VEHICLE_TYPE_AIRDEFENSE, 3))),

			#Ground Defence Ribbon
			('3040718',	'Gdr',	1, f_and(	object_stat ('vehicles', 'rtime', VEHICLE_TYPE_GRNDDEFENSE, 180),
											object_stat ('vehicles', 'kills', VEHICLE_TYPE_GRNDDEFENSE, 5))),

			#Airborne Ribbon
			('3240102',	'Ar',	1, f_and(	object_stat ('vehicles', 'rtime', VEHICLE_TYPE_PARACHUTE, 10))),

			#Good Conduct Ribbon 
			#Move to BACKEND??
			('3240703',	'gcr',	1, f_and(	global_stat ('time', 6000),
											player_score ('kills', 14),
											f_not (	f_plus(player_score ('TKs'),
													f_plus(player_score ('teamDamages'), player_score ('teamVehicleDamages')), 1))
										)),

		#Medals
			#Purple Heart
			('2191608',	'ph',	0, f_and(	player_score ('kills', 5),
											player_score ('deaths', 20),
											f_div (player_score ('deaths'), player_score ('kills'), 4)
										)),

# Added by Chump - these are calculated in medals.py
			#Gold Star
			#(2051907,
			#Silver Star
			#
			#Bronze Star
			#

			#Meritorious Service Medal
			('2191319',	'Msm',	2, f_and(	global_stat_multiple_times ('time', 9000, '2191319'),
											global_stat_multiple_times ('heal', 10, '2191319'),
											global_stat_multiple_times ('rpar', 10, '2191319'),
											global_stat_multiple_times ('rsup', 10, '2191319'))),

			#Combat Action Medal
			('2190303',	'Cam',	2, f_and(	global_stat_multiple_times ('time', 9000, '2190303'),
											global_stat_multiple_times ('kill', 50, '2190303'),
											global_stat ('bksk', 25),
											player_stat ('timePlayed', 1980))),

			#Air Combat Medal
			('2190309',	'Acm',	2, f_and(	global_stat_multiple_times ('vtm-1', 9000, '2190309'),object_stat ('vehicles', 'kills', VEHICLE_TYPE_AVIATOR, 25))),

			#Armour Combat Medal
			('2190318',	'Arm',	2, f_and(	global_stat_multiple_times ('vtm-0', 9000, '2190318'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_ARMOR, 25))),

			#Helicopter Combat Medal
			('2190308',	'Hcm',	2, f_and(	global_stat_multiple_times ('vtm-3', 9000, '2190308'), object_stat ('vehicles', 'kills', VEHICLE_TYPE_HELICOPTER, 30))),

			#Good Conduct MEDAL 
			#Move to BACKEND??
			('2190703',	'gcm',	2, f_and(	global_stat_multiple_times ('time', 9000, '2190703'),
											player_score ('kills', 27),
											f_not (	f_plus(	player_score ('TKs'),
												f_plus(player_score ('teamDamages'), player_score ('teamVehicleDamages')), 1))
										)),

			#Combat Infantry Medal
			('2020903',	'Cim',	1, f_and(	global_stat ('time', 12000),
											has_medal ('1031406_1'),
											has_medal ('1031619_1'),
											has_medal ('1031119_1'),
											has_medal ('1031120_1'),
											has_medal ('1031109_1'),
											has_medal ('1031115_1'),
											has_medal ('1031121_1'),
											has_medal ('1031105_1'),
											has_medal ('1031113_1'))),

			#Marksman Infantry Medal
			('2020913',	'Mim',	1, f_and(	global_stat ('time', 10800),
											has_medal ('2020903'),
											has_medal ('1031406_2'),
											has_medal ('1031619_2'),
											has_medal ('1031119_2'),
											has_medal ('1031120_2'),
											has_medal ('1031109_2'),
											has_medal ('1031115_2'),
											has_medal ('1031121_2'),
											has_medal ('1031105_2'),
											has_medal ('1031113_2'))),

			#Sharpshooter Infantry Medal
			('2020919',	'Sim',	1, f_and(	global_stat ('time', 14400),
											has_medal ('2020913'),
											has_medal ('1031406_3'),
											has_medal ('1031619_3'),
											has_medal ('1031119_3'),
											has_medal ('1031120_3'),
											has_medal ('1031109_3'),
											has_medal ('1031115_3'),
											has_medal ('1031121_3'),
											has_medal ('1031105_3'),
											has_medal ('1031113_3'))),

			#Medal of Valour
			('2021322',	'Mvm',	2, f_and(	global_stat_multiple_times ('time', 9000, '2021322'),
											global_stat_multiple_times ('dsab', 50, '2021322'),
											global_stat_multiple_times ('dfcp', 10,  '2021322'),
											global_stat_multiple_times ('twsc', 300, '2021322'))),

			#Distinguished Service Medal
			('2020419',	'Dsm',	2, f_and(	global_stat_multiple_times ('tcdr', 12000, '2020419'),
											global_stat_multiple_times ('tsql', 120, '2020419'),
											global_stat_multiple_times ('tsqm', 120, '2020419'),
											player_score ('rplScore', 45))),

# Added by Chump - added for bf2statistics
			#Navy Cross
			# Move to BACKEND ??
			# ('2021403',	'Ncm',	2, f_and(	global_stat_multiple_times ('atm-0', 12000, '2021403'),
											# global_stat_multiple_times ('abr-0', 10, '2021403'),
											# global_stat_multiple_times ('awn-0', 10, '2021403'))),

			#Golden Scimitar
			# Move to BACKEND ??
			# ('2020719',	'Gsm',	2, f_and(	global_stat_multiple_times ('atm-1', 12000, '2020719'),
											# global_stat_multiple_times ('abr-1', 10, '2020719'),
											# global_stat_multiple_times ('awn-1', 10, '2020719'))),

			#People's Medallion
			# Move to BACKEND ??
			# ('2021613',	'pmm',	2, f_and(	global_stat_multiple_times ('atm-2', 360000, '2021613'),
											# global_stat_multiple_times ('abr-2', 10, '2021613'),
											# global_stat_multiple_times ('awn-2', 10, '2021613'))),

#****************************************************************************************
#   B P 1 / B P 2      stuff       Ribbons = 3, Medals = 2, Badges = 1
#****************************************************************************************			
			# Added by Wolverine 2006-06-18
			#European Union Special Service Medal
			# WARNING!  Can Cause problems if EF Booster Pack not isnatlled correctly! :(
			# Move to BACKEND ??
			# ('2270521',	'Eum',	2, f_and(	global_stat_multiple_times ('atm-9', 18000, '2270521'),
											# global_stat_multiple_times ('abr-9', 10, '2270521'),
											# global_stat_multiple_times ('awn-9', 5, '2270521'))),

			#European Union Service ribbon
			# WARNING!  Can Cause problems if EF Booster Pack not installed correctly! :(
			# Move to BACKEND ??
			# ('3270519',	'Esr',	1,  f_and(	f_plus(global_stat('mtm-10'),
												# f_plus(global_stat('mtm-11'),
													# global_stat('mtm-110')), 18000),	# 50hrs in European Theater
											# global_stat('mtm-10', 1),	# EF: operationsmokescreen
											# global_stat('mtm-11', 1),	# EF: taraba_quarry
											# global_stat('mtm-110', 1),	# EF: greatwall
										# )),

			#North American Service Ribbon
			# WARNING!  Can Cause problems if AF Booster Pack not installed correctly! :(
			# Move to BACKEND ??
			# ('3271401',	'Nas',	1,  f_and(	f_plus(global_stat('mtm-200'),
												# f_plus(global_stat('mtm-201'),
													# global_stat('mtm-202')), 90000),	# 25hrs in Nth American Theater
											# global_stat('mtm-200', 1),	# AF: midnight_sun
											# global_stat('mtm-201', 1),	# AF: operationroadrage
											# global_stat('mtm-202', 1),	# AF: operationharvest
										# )),

			#end of medals_data
			)



rank_data = (

# Level 1:
	(1,	'rank',		f_plus (global_stat ('scor'), player_score ('score'), 1000)),
# Level 2:
	(2,	'rank',		f_and(
						has_rank(1),	
						f_plus (global_stat ('scor'), player_score ('score'), 2250))),
# Level 3:
	(3,	'rank',		f_and(
						has_rank(2),
						f_plus (global_stat ('scor'), player_score ('score'), 3750))),
# Level 4:
	(4,	'rank',		f_and(
						has_rank(3),
						f_plus (global_stat ('scor'), player_score ('score'), 5500))),
# Level 5:
	(5,	'rank',		f_and(
						has_rank(4),
						f_plus (global_stat ('scor'), player_score ('score'), 7500))),
# Level 6:
	(6,	'rank',		f_and(
						has_rank(5),
						f_plus (global_stat ('scor'), player_score ('score'), 9750))),
# Level 7:
	(7,	'rank',		f_and(
						has_rank(6),
						f_plus (global_stat ('scor'), player_score ('score'), 12250))),

	(8,	'rank',		f_and(
						has_rank(7),
						f_plus (global_stat ('scor'), player_score ('score'), 15000))),

# Level 8:
	(9,	'rank',		f_and(
						has_rank(8),
						f_plus (global_stat ('scor'), player_score ('score'), 18000))),
				
	(10,'rank',		f_and(
						has_rank(9),
						f_plus (global_stat ('scor'), player_score ('score'), 21250))),

# Added by Chump - for bf2statistics stats (smoc is awarded in bf2statistics.php)
# Level 10:
	(11, 	'rank', 	f_and(
					f_plus (global_stat ('scor'), player_score ('score'), 24750),
					has_medal('6666666'))), # highest rank this month, never awarded from here
# Added by Chump - for new rank structure/points
# 2nd Lieutenant
	(12,	'rank',		f_and(
						f_or(f_or(has_rank(9), has_rank(10)), has_rank(11)),
						f_plus (global_stat ('scor'), player_score ('score'), 28500))),

# 1st Lieutenant
	(13,	'rank',		f_and(
						has_rank(12),	
						f_plus (global_stat ('scor'), player_score ('score'), 32500))),
# Captain
	(14,	'rank',		f_and(
						has_rank(13),	
						f_plus (global_stat ('scor'), player_score ('score'), 36750))),
# Major
	(15,	'rank',		f_and(
						has_rank(14),	
						f_plus (global_stat ('scor'), player_score ('score'), 41250))),
# Lt Colonel
	(16,	'rank',		f_and(
						has_rank(15),	
						f_plus (global_stat ('scor'), player_score ('score'), 46000))),
# Colonel
	(17,	'rank',		f_and(
						has_rank(16),	
						f_plus (global_stat ('scor'), player_score ('score'), 51000))),
# Brigadier General
	(18,	'rank',		f_and(
						has_rank(17),	
						f_plus (global_stat ('scor'), player_score ('score'), 56250),
						has_medal('1220118_2'), # armour
						has_medal('1222016_2'), # transport
						has_medal('1220803_2'), # helicopter
						has_medal('1220122_2'), # aviator
						has_medal('1220104_2'), # Air defence
						has_medal('1031923_2'), # Ground Defence
						global_stat ('time', 12000)
				)),
						
# Major General
	(19,	'rank',		f_and(
						has_rank(18),	
						f_plus (global_stat ('scor'), player_score ('score'), 61750),
						has_medal('1031406_2'), #knife
						has_medal('1031619_2'), #pistol
						has_medal('1031119_2'), #assault
						has_medal('1031120_2'), #AT
						has_medal('1031109_2'), #Sniper
						has_medal('1031115_2'), #spec op
						has_medal('1031121_2'), #Support
						has_medal('1031105_2'), #Eng
						has_medal('1031113_2'), #medic
						global_stat ('time', 15000)
				)),
# Lieutenant General
	(20,	'rank',		f_and(
						has_rank(19),	
						f_plus (global_stat ('scor'), player_score ('score'), 67500),
						global_stat ('time', 18000)
				)),
# General (awarded from back end.  Must be Lt Gen and make leaderboard for 1 week.)
	(21,	'rank',		f_and(
						has_rank(20),	
						f_plus (global_stat ('scor'), player_score ('score'), 73500),
						has_medal('6666666') # highest rank this month, never awarded from here
				)),
	)