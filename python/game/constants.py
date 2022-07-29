# stats keys

import host
import string
from bf2 import g_debug

VEHICLE_TYPE_ARMOR 					= 0
VEHICLE_TYPE_AVIATOR					= 1
VEHICLE_TYPE_AIRDEFENSE					= 2
VEHICLE_TYPE_HELICOPTER					= 3
VEHICLE_TYPE_TRANSPORT					= 4
VEHICLE_TYPE_ARTILLERY					= 5
VEHICLE_TYPE_GRNDDEFENSE				= 6
VEHICLE_TYPE_PARACHUTE					= 7
VEHICLE_TYPE_SOLDIER					= 8
VEHICLE_TYPE_NIGHTVISION				= 9
VEHICLE_TYPE_GASMASK					= 10
VEHICLE_TYPE_COMMANDER 					= 11
NUM_VEHICLE_TYPES 					= 12
VEHICLE_TYPE_UNKNOWN 					= NUM_VEHICLE_TYPES

WEAPON_TYPE_ASSAULT 					= 0
WEAPON_TYPE_ASSAULTGRN					= 1
WEAPON_TYPE_CARBINE					= 2
WEAPON_TYPE_LMG						= 3
WEAPON_TYPE_SNIPER					= 4
WEAPON_TYPE_PISTOL					= 5
WEAPON_TYPE_ATAA					= 6
WEAPON_TYPE_SMG						= 7
WEAPON_TYPE_SHOTGUN					= 8
WEAPON_TYPE_COMMANDER					= 9
WEAPON_TYPE_KNIFE					= 10
WEAPON_TYPE_C4						= 11
WEAPON_TYPE_CLAYMORE					= 12
WEAPON_TYPE_HANDGRENADE 				= 13
WEAPON_TYPE_SHOCKPAD					= 14
WEAPON_TYPE_ATMINE					= 15
WEAPON_TYPE_TARGETING					= 16
WEAPON_TYPE_GRAPPLINGHOOK				= 17
WEAPON_TYPE_ZIPLINE					= 18
WEAPON_TYPE_TACTICAL					= 19
NUM_WEAPON_TYPES 					= 20
WEAPON_TYPE_UNKNOWN					= NUM_WEAPON_TYPES

KIT_TYPE_AT						= 0
KIT_TYPE_ASSAULT					= 1
KIT_TYPE_ENGINEER					= 2
KIT_TYPE_MEDIC						= 3
KIT_TYPE_SPECOPS					= 4
KIT_TYPE_SUPPORT 					= 5
KIT_TYPE_SNIPER 					= 6
KIT_TYPE_AA 						= 7
KIT_TYPE_PILOT 						= 8
KIT_TYPE_CREWMAN 					= 9
KIT_TYPE_OFFICER 					= 10
KIT_TYPE_MORTAR 					= 11
KIT_TYPE_MARKSMAN 					= 12
KIT_TYPE_CIVILIAN 					= 13
NUM_KIT_TYPES 						= 14
KIT_TYPE_UNKNOWN					= NUM_KIT_TYPES

ARMY_USA						= 0
ARMY_MEC						= 1
ARMY_CHINESE						= 2
ARMY_SEALS						= 3
ARMY_SAS						= 4
ARMY_SPETZNAS						= 5
ARMY_MECSF						= 6
ARMY_REBELS						= 7
ARMY_INSURGENTS						= 8
ARMY_EURO						= 9
ARMY_BRITS 						= 10
ARMY_CANADA 						= 11
ARMY_GER						= 12
ARMY_UKR						= 13
ARMY_SE							= 14
ARMY_UN							= 15
ARMY_PEGLEG							=16
ARMY_UNDEATH						= 17
NUM_ARMIES						= 18
ARMY_UNKNOWN						= NUM_ARMIES

vehicleTypeMap = {
		"parachute" 				: VEHICLE_TYPE_PARACHUTE,
#-----------------------------------------------------------------------------------
# Soldier's - 	"objectname"				: VEHICLE_TYPE_SOLDIER,
#-----------------------------------------------------------------------------------
	# Battlefield2
		"us_soldier"				: VEHICLE_TYPE_SOLDIER,
		"us_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
		"us_light_soldier"			: VEHICLE_TYPE_SOLDIER,
		"mec_soldier"				: VEHICLE_TYPE_SOLDIER,
		"mec_light_soldier"			: VEHICLE_TYPE_SOLDIER,
		"mec_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
		"ch_soldier"				: VEHICLE_TYPE_SOLDIER,
		"ch_light_soldier"			: VEHICLE_TYPE_SOLDIER,
		"ch_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
	# SpecialForces	
		"seal_soldier"				: VEHICLE_TYPE_SOLDIER,
		"seal_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
		"sas_soldier"				: VEHICLE_TYPE_SOLDIER,
		"sas_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
		"spetz_soldier"				: VEHICLE_TYPE_SOLDIER,
		"spetz_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
		"mecsf_soldier"				: VEHICLE_TYPE_SOLDIER,
		"mecsf_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
		"chinsurgent_soldier"			: VEHICLE_TYPE_SOLDIER,
		"chinsurgent_heavy_soldier"		: VEHICLE_TYPE_SOLDIER,
		"meinsurgent_soldier"			: VEHICLE_TYPE_SOLDIER,
		"meinsurgent_heavy_soldier"		: VEHICLE_TYPE_SOLDIER,
	# Euroforces
		"eu_soldier"				: VEHICLE_TYPE_SOLDIER,
		"eu_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
	# ArmoredFury
	# POE 1.1.8
		"ger_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
		"ger_light_soldier"			: VEHICLE_TYPE_SOLDIER,
		"ukr_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
		"ukr_light_soldier"			: VEHICLE_TYPE_SOLDIER,
	# OPK 0.2
		"ge_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
		"ge_light_soldier"			: VEHICLE_TYPE_SOLDIER,
		"se_heavy_soldier"			: VEHICLE_TYPE_SOLDIER,
		"se_light_soldier"			: VEHICLE_TYPE_SOLDIER,
	# Project Reality 0.613
		"us_heavywhite_soldier" 		: VEHICLE_TYPE_SOLDIER,
		"us_lightarmor_soldier" 		: VEHICLE_TYPE_SOLDIER,
		"mec_lightarmor_soldier" 		: VEHICLE_TYPE_SOLDIER,
		"mec_medium_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"ch_lightarmor_soldier" 		: VEHICLE_TYPE_SOLDIER,
		"meinsurgent_civilian_body" 		: VEHICLE_TYPE_SOLDIER,
		"meinsurgent_medium_soldier" 		: VEHICLE_TYPE_SOLDIER,
		"gb_soldier" 				: VEHICLE_TYPE_SOLDIER,
		"gb_heavy_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"gb_lightarmor_soldier" 		: VEHICLE_TYPE_SOLDIER,
	# AiX 1.0
		"ch_support_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"ch_specops_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"ch_sniper_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"ch_medic_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"ch_engineer_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"ch_at_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"ch_assault_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"mec_support_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"mec_specops_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"mec_sniper_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"mec_medic_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"mec_engineer_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"mec_at_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"mec_assault_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"un_support_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"un_specops_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"un_sniper_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"un_medic_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"un_engineer_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"un_at_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"un_assault_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"us_support_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"us_specops_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"us_sniper_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"us_medic_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"us_engineer_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"us_at_soldier" 			: VEHICLE_TYPE_SOLDIER,
		"us_assault_soldier" 			: VEHICLE_TYPE_SOLDIER,
	# BF Pirates 2
#-----------------------------------------------------------------------------------
# Commander - 	"objectname" 				: VEHICLE_TYPE_COMMANDER,
#-----------------------------------------------------------------------------------
	# Battlefield2
	# SpecialForces	
	# Euroforces
	# ArmoredFury
	# POE 1.1.8
	# OPK 0.2
	# Project Reality 0.613
		"deployable_bunker" 			: VEHICLE_TYPE_COMMANDER,
		"deployable_firebase" 			: VEHICLE_TYPE_COMMANDER,
		"deployable_commandpost_us" 		: VEHICLE_TYPE_COMMANDER,
		"deployable_commandpost_gb" 		: VEHICLE_TYPE_COMMANDER,
		"deployable_commandpost_mec" 		: VEHICLE_TYPE_COMMANDER,
		"deployable_commandpost_ch" 		: VEHICLE_TYPE_COMMANDER,
	# AiX 1.0
		"uav_pred" 				: VEHICLE_TYPE_COMMANDER,
	# BF Pirates 2
#-----------------------------------------------------------------------------------
# Airdefence - 	"objectname"				: VEHICLE_TYPE_AIRDEFENSE,
#-----------------------------------------------------------------------------------	
	# Battlefield2
		"usaav_m6"				: VEHICLE_TYPE_AIRDEFENSE,
		"aav_tunguska"				: VEHICLE_TYPE_AIRDEFENSE,
		"aav_type95"				: VEHICLE_TYPE_AIRDEFENSE,
		"usaas_stinger"				: VEHICLE_TYPE_AIRDEFENSE,
		"igla_djigit"				: VEHICLE_TYPE_AIRDEFENSE,
		"wasp_defence_front"			: VEHICLE_TYPE_AIRDEFENSE,
		"wasp_defence_back"			: VEHICLE_TYPE_AIRDEFENSE,
	# SpecialForces
	# Euroforces
	# ArmoredFury
	# POE 1.1.8
		"aa_zu23"				: VEHICLE_TYPE_AIRDEFENSE,
		"ukraav_shilka"				: VEHICLE_TYPE_AIRDEFENSE,
		"ukraav_mtlb_sa13_v2"			: VEHICLE_TYPE_AIRDEFENSE,
		"geraav_gepard"				: VEHICLE_TYPE_AIRDEFENSE,
	# OPK 0.2
		"aas_phalanx"				: VEHICLE_TYPE_AIRDEFENSE,
		"aas_seasparrow"			: VEHICLE_TYPE_AIRDEFENSE,
		"sa3_position"				: VEHICLE_TYPE_AIRDEFENSE,
		"gepard"				: VEHICLE_TYPE_AIRDEFENSE,
		"bov3aa"				: VEHICLE_TYPE_AIRDEFENSE,
	# Project Reality 0.613
		"usaav_avenger" 			: VEHICLE_TYPE_AIRDEFENSE,
	# AiX 1.0
	"usaas_stinger_no_exit"				: VEHICLE_TYPE_AIRDEFENSE,
	# BF Pirates 2
#-----------------------------------------------------------------------------------
# Grounddefence - 	"ats_tow"			: VEHICLE_TYPE_GRNDDEFENSE,
#-----------------------------------------------------------------------------------	
	# Battlefield2
		"ats_tow"				: VEHICLE_TYPE_GRNDDEFENSE,
		"ats_hj8"				: VEHICLE_TYPE_GRNDDEFENSE,
		"hmg_m2hb"				: VEHICLE_TYPE_GRNDDEFENSE,
		"chhmg_kord"				: VEHICLE_TYPE_GRNDDEFENSE,
		"mec_bipod"				: VEHICLE_TYPE_GRNDDEFENSE,
		"us_bipod"				: VEHICLE_TYPE_GRNDDEFENSE,
		"ch_bipod"				: VEHICLE_TYPE_GRNDDEFENSE,
	# SpecialForces	
	# Euroforces
	# ArmoredFury
	# POE 1.1.8
		"gerartil_fh70"				: VEHICLE_TYPE_GRNDDEFENSE,
		"mg3_coax"				: VEHICLE_TYPE_GRNDDEFENSE,
		"remote_kord"				: VEHICLE_TYPE_GRNDDEFENSE,
		"remote_mg3"				: VEHICLE_TYPE_GRNDDEFENSE,
	# OPK 0.2
		"chhmg_type85"				: VEHICLE_TYPE_GRNDDEFENSE,
		"chlmg_type95_stationary"		: VEHICLE_TYPE_GRNDDEFENSE,
		"hmg_m134"				: VEHICLE_TYPE_GRNDDEFENSE,
		"hmg_m2hb_ammobox"			: VEHICLE_TYPE_GRNDDEFENSE,
		"kord_amobox"				: VEHICLE_TYPE_GRNDDEFENSE,
		"rulmg_rpk74_stationary"		: VEHICLE_TYPE_GRNDDEFENSE,
		"stationary_mg3"			: VEHICLE_TYPE_GRNDDEFENSE,
		"uslmg_m249saw_stationary"		: VEHICLE_TYPE_GRNDDEFENSE,
	# Project Reality 0.613
	# AiX 1.0
		"ch_hmg"				: VEHICLE_TYPE_GRNDDEFENSE,
		"hmg_m134b"				: VEHICLE_TYPE_GRNDDEFENSE,
		"kord"					: VEHICLE_TYPE_GRNDDEFENSE,
		"m2"					: VEHICLE_TYPE_GRNDDEFENSE,
		"m224_mortar"				: VEHICLE_TYPE_GRNDDEFENSE,
		"mec_hmg"				: VEHICLE_TYPE_GRNDDEFENSE,
		"t85"					: VEHICLE_TYPE_GRNDDEFENSE,
		"us_hmg"				: VEHICLE_TYPE_GRNDDEFENSE,
	# BF Pirates 2
#-----------------------------------------------------------------------------------
# Artillery - 	"objectname"				: VEHICLE_TYPE_ARTILLERY,
#-----------------------------------------------------------------------------------	
	# Battlefield2
		"usart_lw155"				: VEHICLE_TYPE_ARTILLERY,
		"ars_d30"				: VEHICLE_TYPE_ARTILLERY,
	# SpecialForces	
	# Euroforces
	# ArmoredFury
	# POE 1.1.8
		"gerartil_pzh2000"			: VEHICLE_TYPE_ARTILLERY,
		"ukrartil_m1974"			: VEHICLE_TYPE_ARTILLERY,
		"ukrartil_msta"				: VEHICLE_TYPE_ARTILLERY,
	# OPK 0.2
	# Project Reality 0.613
	# AiX 1.0
		"USART_LW155"				: VEHICLE_TYPE_ARTILLERY,
		"art_fieldcannon"			: VEHICLE_TYPE_ARTILLERY,
		"art_truckcannon"			: VEHICLE_TYPE_ARTILLERY,
	# BF Pirates 2
#-----------------------------------------------------------------------------------
# Aviators - 	"objectname"				: VEHICLE_TYPE_AVIATOR,
#-----------------------------------------------------------------------------------	
	# Battlefield2
		"usair_f18"				: VEHICLE_TYPE_AVIATOR,
		"ruair_mig29"				: VEHICLE_TYPE_AVIATOR,
		"air_j10"				: VEHICLE_TYPE_AVIATOR,
		"usair_f15"				: VEHICLE_TYPE_AVIATOR,
		"ruair_su34"				: VEHICLE_TYPE_AVIATOR,
		"air_su30mkk"				: VEHICLE_TYPE_AVIATOR,
		"air_f35b"				: VEHICLE_TYPE_AVIATOR,
	# SpecialForces	
	# Euroforces
		"xpak2_eurofighter"			: VEHICLE_TYPE_AVIATOR,
		"xpak2_harrier"				: VEHICLE_TYPE_AVIATOR,
	# ArmoredFury
		"air_a10"				: VEHICLE_TYPE_AVIATOR,
		"air_su39"				: VEHICLE_TYPE_AVIATOR,
		"xpak2_fantan"				: VEHICLE_TYPE_AVIATOR,
	# POE 1.1.8
		"gerair_ef2000"				: VEHICLE_TYPE_AVIATOR,
		"gerair_tornado"			: VEHICLE_TYPE_AVIATOR,
		"ukrair_mig25"				: VEHICLE_TYPE_AVIATOR,
		"ukrair_su24"				: VEHICLE_TYPE_AVIATOR,
		"ukrair_su25"				: VEHICLE_TYPE_AVIATOR,
	# OPK 0.2
		"f4phantom"				: VEHICLE_TYPE_AVIATOR,
		"tornado"				: VEHICLE_TYPE_AVIATOR,
		"mi24e"					: VEHICLE_TYPE_AVIATOR,
		"mig21"					: VEHICLE_TYPE_AVIATOR,
		"orao"					: VEHICLE_TYPE_AVIATOR,
	# Project Reality 0.613
		"ch_jet_fantan"				: VEHICLE_TYPE_AVIATOR,
		"gb_jet_eurofighter" 			: VEHICLE_TYPE_AVIATOR,
		"gbair_harrier" 			: VEHICLE_TYPE_AVIATOR,
		"iraqair_su25a" 			: VEHICLE_TYPE_AVIATOR,
		"ruair_mig29" 				: VEHICLE_TYPE_AVIATOR,
		"ruair_su34" 				: VEHICLE_TYPE_AVIATOR,
		"usair_a10a" 				: VEHICLE_TYPE_AVIATOR,
		"usair_f16" 				: VEHICLE_TYPE_AVIATOR,
		"v22" 					: VEHICLE_TYPE_AVIATOR,	
	# AiX 1.0
		"mig19farmer"				: VEHICLE_TYPE_AVIATOR,
		"fishbed"				: VEHICLE_TYPE_AVIATOR,
		"flagon"				: VEHICLE_TYPE_AVIATOR,
		"f5tiger"				: VEHICLE_TYPE_AVIATOR,
		"mirageiii"				: VEHICLE_TYPE_AVIATOR,
		"flogger"				: VEHICLE_TYPE_AVIATOR,
		"mirage2k"				: VEHICLE_TYPE_AVIATOR,
		"draken"				: VEHICLE_TYPE_AVIATOR,
		"f16"					: VEHICLE_TYPE_AVIATOR,
		"f16lg"					: VEHICLE_TYPE_AVIATOR,
		"aix_a10"				: VEHICLE_TYPE_AVIATOR,
		"aix_a10b"				: VEHICLE_TYPE_AVIATOR,
		"aix_av8b"				: VEHICLE_TYPE_AVIATOR,
		"aix_draken"				: VEHICLE_TYPE_AVIATOR,
		"aix_f117a"				: VEHICLE_TYPE_AVIATOR,
		"aix_f16"				: VEHICLE_TYPE_AVIATOR,
		"aix_f16lg"				: VEHICLE_TYPE_AVIATOR,
		"aix_f5tiger"				: VEHICLE_TYPE_AVIATOR,
		"aix_gr7"				: VEHICLE_TYPE_AVIATOR,
		"aix_mig19"				: VEHICLE_TYPE_AVIATOR,
		"aix_mig21"				: VEHICLE_TYPE_AVIATOR,
		"aix_mig23"				: VEHICLE_TYPE_AVIATOR,
		"aix_mirage_iii"			: VEHICLE_TYPE_AVIATOR,
		"aix_mirage2k"				: VEHICLE_TYPE_AVIATOR,
		"aix_su21"				: VEHICLE_TYPE_AVIATOR,
		"albatros_diii"				: VEHICLE_TYPE_AVIATOR,
		"fokker_dr1"				: VEHICLE_TYPE_AVIATOR,
		"fokker_eiii"				: VEHICLE_TYPE_AVIATOR,
		"hawkextras"				: VEHICLE_TYPE_AVIATOR,
		"mig21m"				: VEHICLE_TYPE_AVIATOR,
		"spad_xiii"				: VEHICLE_TYPE_AVIATOR,
		"AIX_Be12"				: VEHICLE_TYPE_AVIATOR,
		"AIX_Su47"				: VEHICLE_TYPE_AVIATOR,
		"AIX_Yak38"				: VEHICLE_TYPE_AVIATOR,
		"F16"					: VEHICLE_TYPE_AVIATOR,
		"MiG21"					: VEHICLE_TYPE_AVIATOR,
		"Mirage"				: VEHICLE_TYPE_AVIATOR,

	# BF Pirates 2
#-----------------------------------------------------------------------------------
# Helicopters - "objectname"				: VEHICLE_TYPE_HELICOPTER,
#-----------------------------------------------------------------------------------	
	# Battlefield2
		"usthe_uh60"				: VEHICLE_TYPE_HELICOPTER,
		"the_mi17"				: VEHICLE_TYPE_HELICOPTER,
		"chthe_z8"				: VEHICLE_TYPE_HELICOPTER,
		"ahe_ah1z"				: VEHICLE_TYPE_HELICOPTER,
		"ahe_havoc"				: VEHICLE_TYPE_HELICOPTER,
		"ahe_z10"				: VEHICLE_TYPE_HELICOPTER,
	# SpecialForces	
		"xpak_apache"				: VEHICLE_TYPE_HELICOPTER,
		"xpak_hind"				: VEHICLE_TYPE_HELICOPTER,
	# Euroforces
		"xpak2_tiger"				: VEHICLE_TYPE_HELICOPTER,
		"xpak2_lynx"				: VEHICLE_TYPE_HELICOPTER,
	# ArmoredFury
		"che_wz11"				: VEHICLE_TYPE_HELICOPTER,
		"she_ec635"				: VEHICLE_TYPE_HELICOPTER,
		"she_littlebird"			: VEHICLE_TYPE_HELICOPTER,
	# POE 1.1.8
		"ufo"					: VEHICLE_TYPE_HELICOPTER,
		"gerhe_nh90"				: VEHICLE_TYPE_HELICOPTER,
		"ukrhe_mi24p"				: VEHICLE_TYPE_HELICOPTER,
		"gerhe_eurotigerarh"			: VEHICLE_TYPE_HELICOPTER,
	# OPK 0.2
		"uh-1d"					: VEHICLE_TYPE_HELICOPTER,
		"tiger"					: VEHICLE_TYPE_HELICOPTER,
	# Project Reality 0.613
		"che_wz11" 				: VEHICLE_TYPE_HELICOPTER,
		"ahe_ah6" 				: VEHICLE_TYPE_HELICOPTER,
		"ahe_ah6a" 				: VEHICLE_TYPE_HELICOPTER,
		"ahe_mh6" 				: VEHICLE_TYPE_HELICOPTER,
		"gbthe_merlin" 				: VEHICLE_TYPE_HELICOPTER,
		"gb_ahe_apache" 			: VEHICLE_TYPE_HELICOPTER,
	# AiX 1.0
		"usahe_ah60" 				: VEHICLE_TYPE_HELICOPTER,
		"a8_extras" 				: VEHICLE_TYPE_HELICOPTER,
		"ahe_ah1x" 				: VEHICLE_TYPE_HELICOPTER,
		"ahe_ghost" 				: VEHICLE_TYPE_HELICOPTER,
		"ahe_roc" 				: VEHICLE_TYPE_HELICOPTER,
		"ahe_storm" 				: VEHICLE_TYPE_HELICOPTER,
		"ahe_v10" 				: VEHICLE_TYPE_HELICOPTER,
		"aix_ah64" 				: VEHICLE_TYPE_HELICOPTER,
		"aix_ah64gunship" 			: VEHICLE_TYPE_HELICOPTER,
		"aix_ka50" 				: VEHICLE_TYPE_HELICOPTER,
		"aix_notar_littlebird" 			: VEHICLE_TYPE_HELICOPTER,
		"aix_notar_littlebird_trans" 		: VEHICLE_TYPE_HELICOPTER,
		"blizzard" 				: VEHICLE_TYPE_HELICOPTER,
		"blizzardextras" 			: VEHICLE_TYPE_HELICOPTER,
		"chahe_a8" 				: VEHICLE_TYPE_HELICOPTER,
	# BF Pirates 2
#-----------------------------------------------------------------------------------
# Transports - 	"objectname"				: VEHICLE_TYPE_TRANSPORT,
#-----------------------------------------------------------------------------------	
	# Battlefield2
		"jeep_faav"				: VEHICLE_TYPE_TRANSPORT,
		"usjep_hmmwv"				: VEHICLE_TYPE_TRANSPORT,
		"jep_paratrooper"			: VEHICLE_TYPE_TRANSPORT,
		"jep_mec_paratrooper"			: VEHICLE_TYPE_TRANSPORT,
		"jep_vodnik"				: VEHICLE_TYPE_TRANSPORT,
		"jep_nanjing"				: VEHICLE_TYPE_TRANSPORT,
		"uslcr_lcac"				: VEHICLE_TYPE_TRANSPORT,
		"boat_rib"				: VEHICLE_TYPE_TRANSPORT,
	# SpecialForces
		"xpak_forklift"				: VEHICLE_TYPE_TRANSPORT,
		"xpak_atv"				: VEHICLE_TYPE_TRANSPORT,
		"xpak_civ1"				: VEHICLE_TYPE_TRANSPORT,
		"xpak_civ2"				: VEHICLE_TYPE_TRANSPORT,
		"xpak_jetski"				: VEHICLE_TYPE_TRANSPORT,
		"xpak_ailraider"			: VEHICLE_TYPE_TRANSPORT,
		"xpak_hummertow"			: VEHICLE_TYPE_TRANSPORT,
		"xpak_civ1_bomber" 			: VEHICLE_TYPE_TRANSPORT,
		"xpak_civ1_spawner" 			: VEHICLE_TYPE_TRANSPORT,
	# Euroforces
		"xpak2_vbl"				: VEHICLE_TYPE_TRANSPORT,
	# ArmoredFury
		"xpak2_musclecar"			: VEHICLE_TYPE_TRANSPORT,
		"xpak2_semi"				: VEHICLE_TYPE_TRANSPORT,
		"xpak2_semi" 				: VEHICLE_TYPE_TRANSPORT,
		"xpak2_semi_bomber" 			: VEHICLE_TYPE_TRANSPORT,
		"xpak2_vbl" 				: VEHICLE_TYPE_TRANSPORT,
	# POE 1.1.8
		"gerapc_boxerGTK"			: VEHICLE_TYPE_TRANSPORT,
		"gerjeep_dingo"				: VEHICLE_TYPE_TRANSPORT,
		"gerjeep_wolf"				: VEHICLE_TYPE_TRANSPORT,
		"gerjeep_wolfsoft"			: VEHICLE_TYPE_TRANSPORT,
		"snowmobile"				: VEHICLE_TYPE_TRANSPORT,
		"ukrapc_bmp2"				: VEHICLE_TYPE_TRANSPORT,
		"ukrapc_mtlb"				: VEHICLE_TYPE_TRANSPORT,
		"ukrjeep_dozer"				: VEHICLE_TYPE_TRANSPORT,
		"ukrjeep_uaz"				: VEHICLE_TYPE_TRANSPORT,
	# OPK 0.2
		"dingo"					: VEHICLE_TYPE_TRANSPORT,
		"wolf"					: VEHICLE_TYPE_TRANSPORT,
		"shmmwv_armed"				: VEHICLE_TYPE_TRANSPORT,
		"shmmwv"				: VEHICLE_TYPE_TRANSPORT,
		"puch"					: VEHICLE_TYPE_TRANSPORT,
	# Project Reality 0.613
		"chjep_uazsupport" 			: VEHICLE_TYPE_TRANSPORT,
		"ch_trk_support" 			: VEHICLE_TYPE_TRANSPORT,
		"civiliancar2" 				: VEHICLE_TYPE_TRANSPORT,
		"dirtbike" 				: VEHICLE_TYPE_TRANSPORT,
		"gb_jeep_landrover" 			: VEHICLE_TYPE_TRANSPORT,
		"gb_jeep_landrover_support" 		: VEHICLE_TYPE_TRANSPORT,
		"gb_saxon" 				: VEHICLE_TYPE_TRANSPORT,
		"gb_trk_support" 			: VEHICLE_TYPE_TRANSPORT,
		"iraqjep_gaz69" 			: VEHICLE_TYPE_TRANSPORT,
		"iraqjep_uazsupport" 			: VEHICLE_TYPE_TRANSPORT,
		"iraqtrk_ural4320" 			: VEHICLE_TYPE_TRANSPORT,	
		"jep_technical" 			: VEHICLE_TYPE_TRANSPORT,
		"mec_trk_support" 			: VEHICLE_TYPE_TRANSPORT,
		"mil_jeep_support" 			: VEHICLE_TYPE_TRANSPORT,
		"mil_jeep_technical" 			: VEHICLE_TYPE_TRANSPORT,
		"mil_trk_ural4320" 			: VEHICLE_TYPE_TRANSPORT,
		"mil_trk_support" 			: VEHICLE_TYPE_TRANSPORT,
		"suv_vip" 				: VEHICLE_TYPE_TRANSPORT,
		"truck1" 				: VEHICLE_TYPE_TRANSPORT,
		"usjep_hmmwvcrows" 			: VEHICLE_TYPE_TRANSPORT,
		"usjep_hmmwvsupport" 			: VEHICLE_TYPE_TRANSPORT,
		"usjep_hmmwvtow" 			: VEHICLE_TYPE_TRANSPORT,
		"ustrk_m35" 				: VEHICLE_TYPE_TRANSPORT,
		"us_trk_support" 			: VEHICLE_TYPE_TRANSPORT,
	# AiX 1.0
		"truck1" 				: VEHICLE_TYPE_TRANSPORT,
		"civiliancar2" 				: VEHICLE_TYPE_TRANSPORT,
		"jeep_faav" 				: VEHICLE_TYPE_TRANSPORT,
		"jeep_faav_hf" 				: VEHICLE_TYPE_TRANSPORT,
		"usjep_hmmwv"				: VEHICLE_TYPE_TRANSPORT,
		"aix_atv"				: VEHICLE_TYPE_TRANSPORT,
	# BF Pirates 2
#-----------------------------------------------------------------------------------	
# Armored Vehicles - "objectname"			: VEHICLE_TYPE_ARMOR,
#-----------------------------------------------------------------------------------	
	# Battlefield2
		"usapc_lav25"				: VEHICLE_TYPE_ARMOR,
		"apc_btr90"				: VEHICLE_TYPE_ARMOR,
		"apc_wz551"				: VEHICLE_TYPE_ARMOR,
		"ustnk_m1a2"				: VEHICLE_TYPE_ARMOR,
		"rutnk_t90"				: VEHICLE_TYPE_ARMOR,
		"tnk_type98"				: VEHICLE_TYPE_ARMOR,
	# SpecialForces
		"xpak_bmp3"				: VEHICLE_TYPE_ARMOR,	
	# Euroforces
		"xpak2_tnkl2a6"				: VEHICLE_TYPE_ARMOR,
		"xpak2_tnkc2"				: VEHICLE_TYPE_ARMOR,
	# ArmoredFury
	# POE 1.1.8
		"gerapc_marder1a5"			: VEHICLE_TYPE_ARMOR,
		"civsctr"				: VEHICLE_TYPE_ARMOR,
		"gertnk_leopard"			: VEHICLE_TYPE_ARMOR,
		"ukrtnk_oplot"				: VEHICLE_TYPE_ARMOR,
		"ukrtnk_t55"				: VEHICLE_TYPE_ARMOR,
	# OPK 0.2
		"marder1a5"				: VEHICLE_TYPE_ARMOR,
		"m84"					: VEHICLE_TYPE_ARMOR,
		"m80a"					: VEHICLE_TYPE_ARMOR,
		"leo2a6"				: VEHICLE_TYPE_ARMOR,
		"brdm2"					: VEHICLE_TYPE_ARMOR,
	# Project Reality 0.613
		"gb_apc_warrior" 			: VEHICLE_TYPE_ARMOR,
		"gb_tank_challenger" 			: VEHICLE_TYPE_ARMOR,
		"gb_tank_challenger_green" 		: VEHICLE_TYPE_ARMOR,
		"iraqapc_brdm2" 			: VEHICLE_TYPE_ARMOR,
		"iraqtnk_t62" 				: VEHICLE_TYPE_ARMOR,
		"mec_apc_bmp3" 				: VEHICLE_TYPE_ARMOR,
	# AiX 1.0
		"asset_pco" 				: VEHICLE_TYPE_ARMOR,
		"bradley" 				: VEHICLE_TYPE_ARMOR,
		"maws" 					: VEHICLE_TYPE_ARMOR,
		"rms" 					: VEHICLE_TYPE_ARMOR,
		"usapc_lav25" 				: VEHICLE_TYPE_ARMOR,
		"ustnk_m1a2" 				: VEHICLE_TYPE_ARMOR,
	# BF Pirates 2
#-----------------------------------------------------------------------------------                                                         
}


weaponTypeMap = {
#-------Possible Weapontypes--------------------------------------------------------
		# "objectname"				: WEAPON_TYPE_ASSAULT,
		# "objectname"				: WEAPON_TYPE_ASSAULTGRN,
		# "objectname"				: WEAPON_TYPE_CARBINE,
		# "objectname"				: WEAPON_TYPE_LMG,
		# "objectname"				: WEAPON_TYPE_SNIPER,
		# "objectname"				: WEAPON_TYPE_PISTOL,
		# "objectname"				: WEAPON_TYPE_ATAA,
		# "objectname"				: WEAPON_TYPE_SMG,
		# "objectname"				: WEAPON_TYPE_SHOTGUN,
		# "objectname"				: WEAPON_TYPE_KNIFE,
		# "objectname"				: WEAPON_TYPE_C4,
		# "objectname"				: WEAPON_TYPE_CLAYMORE,
		# "objectname"				: WEAPON_TYPE_HANDGRENADE,
		# "objectname"				: WEAPON_TYPE_SHOCKPAD,
		# "objectname"				: WEAPON_TYPE_ATMINE,
		# "objectname"				: WEAPON_TYPE_TARGETING,
		# "objectname"				: WEAPON_TYPE_GRAPPLINGHOOK,
		# "objectname"				: WEAPON_TYPE_ZIPLINE,
		# "objectname"				: WEAPON_TYPE_TACTICAL,
#-----------------------------------------------------------------------------------
	# Battlefield2	
		"usrif_m16a2"				: WEAPON_TYPE_ASSAULT,
		"rurif_ak101"				: WEAPON_TYPE_ASSAULT,
		"rurif_ak47"				: WEAPON_TYPE_ASSAULT,
		"usrif_sa80"				: WEAPON_TYPE_ASSAULT,
		"usrif_g3a3"				: WEAPON_TYPE_ASSAULT,
		"usrif_m203"				: WEAPON_TYPE_ASSAULT,
		"rurif_gp30"				: WEAPON_TYPE_ASSAULT,
		"rurif_gp25"				: WEAPON_TYPE_ASSAULT,
		"usrgl_m203"				: WEAPON_TYPE_ASSAULTGRN,
		"rurgl_gp30"				: WEAPON_TYPE_ASSAULTGRN,
		"rurgl_gp25"				: WEAPON_TYPE_ASSAULTGRN,
		"rurrif_ak74u"				: WEAPON_TYPE_CARBINE,
		"usrif_m4"				: WEAPON_TYPE_CARBINE,
		"rurif_ak74u"				: WEAPON_TYPE_CARBINE,
		"chrif_type95"				: WEAPON_TYPE_CARBINE,
		"usrif_g36c"				: WEAPON_TYPE_CARBINE,
		"uslmg_m249saw"				: WEAPON_TYPE_LMG,
		"rulmg_rpk74"				: WEAPON_TYPE_LMG,
		"chlmg_type95"				: WEAPON_TYPE_LMG,
		"rulmg_pkm"				: WEAPON_TYPE_LMG,
		"usrif_m24"				: WEAPON_TYPE_SNIPER,
		"rurif_dragunov"			: WEAPON_TYPE_SNIPER,
		"chsni_type88"				: WEAPON_TYPE_SNIPER,
		"ussni_m82a1"				: WEAPON_TYPE_SNIPER,
		"ussni_m95_barret"			: WEAPON_TYPE_SNIPER,
		"uspis_92fs"				: WEAPON_TYPE_PISTOL,
		"uspis_92fs_silencer"			: WEAPON_TYPE_PISTOL,
		"rupis_baghira"				: WEAPON_TYPE_PISTOL,
		"rupis_baghira_silencer"		: WEAPON_TYPE_PISTOL,
		"rupis_mp443"				: WEAPON_TYPE_PISTOL,
		"rupis_mp446s"				: WEAPON_TYPE_PISTOL,
		"chpis_qsz92"				: WEAPON_TYPE_PISTOL,
		"chpis_qsz92_silencer"			: WEAPON_TYPE_PISTOL,
		"usatp_predator"			: WEAPON_TYPE_ATAA,
		"chat_eryx"				: WEAPON_TYPE_ATAA,
		"usrif_mp5_a3"				: WEAPON_TYPE_SMG,
		"rurif_bizon"				: WEAPON_TYPE_SMG,
		"chrif_type85"				: WEAPON_TYPE_SMG,
		"usrif_remington11-87"			: WEAPON_TYPE_SHOTGUN,
		"rusht_saiga12"				: WEAPON_TYPE_SHOTGUN,
		"chsht_norinco982"			: WEAPON_TYPE_SHOTGUN,
		"chsht_protecta"			: WEAPON_TYPE_SHOTGUN,
		"ussht_jackhammer"			: WEAPON_TYPE_SHOTGUN,
		"kni_knife"				: WEAPON_TYPE_KNIFE,
		"c4_explosives"				: WEAPON_TYPE_C4,
		"ushgr_m67"				: WEAPON_TYPE_HANDGRENADE,
		"usmin_claymore"			: WEAPON_TYPE_CLAYMORE,
		"defibrillator"				: WEAPON_TYPE_SHOCKPAD,
		"at_mine"				: WEAPON_TYPE_ATMINE,
		"simrad"				: WEAPON_TYPE_TARGETING,	
	# SpecialForces stuff
		"xpak_grapplehook"			: WEAPON_TYPE_GRAPPLINGHOOK,
		"xpak_zipline" 				: WEAPON_TYPE_ZIPLINE,
		"nshgr_flashbang"			: WEAPON_TYPE_TACTICAL,
		"sasrif_teargas"			: WEAPON_TYPE_TACTICAL,
		"insgr_rpg"				: WEAPON_TYPE_ATAA,
		"nsrif_crossbow"			: WEAPON_TYPE_ZIPLINE,
		"rurif_oc14"				: WEAPON_TYPE_ASSAULT,
		"sasrif_fn2000"				: WEAPON_TYPE_ASSAULT,
		"sasgr_fn2000"				: WEAPON_TYPE_ASSAULTGRN,
		"sasrif_g36e"				: WEAPON_TYPE_ASSAULT,
		"sasrif_g36k"				: WEAPON_TYPE_ASSAULT,
		"sasrif_mg36"				: WEAPON_TYPE_LMG,
		"sasrif_mp7"				: WEAPON_TYPE_SMG,
		"spzrif_aps"				: WEAPON_TYPE_ASSAULT,
		"usrif_fnscarh"				: WEAPON_TYPE_ASSAULT,
		"usrif_fnscarl"				: WEAPON_TYPE_CARBINE,	
	# SpecialForces unlocks
		"rurif_oc14"				: WEAPON_TYPE_ASSAULT,
		"sasrif_fn2000"				: WEAPON_TYPE_ASSAULT,
		"sasgr_fn2000"				: WEAPON_TYPE_ASSAULTGRN,
		"sasrif_g36e"				: WEAPON_TYPE_ASSAULT,
		"sasrif_g36k"				: WEAPON_TYPE_ASSAULT,
		"sasrif_mg36"				: WEAPON_TYPE_LMG,
		"sasrif_mp7"				: WEAPON_TYPE_SMG,
		"spzrif_aps"				: WEAPON_TYPE_ASSAULT,
		"usrif_fnscarh"				: WEAPON_TYPE_ASSAULT,
		"usrif_fnscarl"				: WEAPON_TYPE_CARBINE,
	# Boosterpack
		"eurif_fnp90"				: WEAPON_TYPE_SMG,
		"eurif_hk53a3"				: WEAPON_TYPE_CARBINE,
		"gbrif_benelli_m4"			: WEAPON_TYPE_SHOTGUN,
		"gbrif_l96a1"				: WEAPON_TYPE_SNIPER,
		"eurif_famas"				: WEAPON_TYPE_ASSAULT,
		"gbrif_sa80a2_l85"			: WEAPON_TYPE_ASSAULT,
		"gbgr_sa80a2_l85"			: WEAPON_TYPE_ASSAULTGRN,
		"eurif_hk21"				: WEAPON_TYPE_LMG,
	# POE2 1.1.8
		"at_mine2"				: WEAPON_TYPE_ATMINE,
		"gergre_dm61"				: WEAPON_TYPE_HANDGRENADE,
		"gergrl_ag36"				: WEAPON_TYPE_ASSAULTGRN,
		"gerkni_km2000"				: WEAPON_TYPE_KNIFE,
		"gerlmg_mg3"				: WEAPON_TYPE_LMG,
		"gerlmg_mg36"				: WEAPON_TYPE_LMG,
		"gerpis_p8"				: WEAPON_TYPE_PISTOL,
		"gerrif_g36"				: WEAPON_TYPE_ASSAULT,
		"gerrif_g36c"				: WEAPON_TYPE_ASSAULT,
		"gerrif_g36k"				: WEAPON_TYPE_ASSAULT,
		"gerrif_msg90"				: WEAPON_TYPE_SNIPER,
		"gerroc_bunkerfaust"			: WEAPON_TYPE_ATAA,
		"gerroc_fliegerfaust2"			: WEAPON_TYPE_ATAA,
		"gerroc_panzerfaust3"			: WEAPON_TYPE_ATAA,
		"gerroc_panzerfaust3t"			: WEAPON_TYPE_ATAA,
		"gersni_g82"				: WEAPON_TYPE_CARBINE,
		"gergre_smoke"				: WEAPON_TYPE_TACTICAL,
		"gergre_smoke2"				: WEAPON_TYPE_TACTICAL,
		"katana"				: WEAPON_TYPE_KNIFE,
		"ruskni_expknife"			: WEAPON_TYPE_KNIFE,
		"ukrgre_rdg2"				: WEAPON_TYPE_ASSAULTGRN,
		"ukrgre_rdg2_2"				: WEAPON_TYPE_ASSAULTGRN,
		"ukrgre_rgd5"				: WEAPON_TYPE_ASSAULTGRN,
		"ukrgrl_gp25"				: WEAPON_TYPE_ASSAULTGRN,
		"ukrlmg_pkm"				: WEAPON_TYPE_LMG,
		"ukrlmg_rpk74"				: WEAPON_TYPE_LMG,
		"ukrpis_fort12"				: WEAPON_TYPE_PISTOL,
		"ukrpis_pb6p9"				: WEAPON_TYPE_PISTOL,
		"ukrrif_aks74u"				: WEAPON_TYPE_CARBINE,
		"ukrrif_pp2000"				: WEAPON_TYPE_SMG,
		"ukrrif_pp2000_2"			: WEAPON_TYPE_SMG,
		"ukrrif_svd"				: WEAPON_TYPE_SNIPER,
		"ukrrif_skorpion"			: WEAPON_TYPE_SNIPER,
		"ukrrif_vepr"				: WEAPON_TYPE_ASSAULT,
		"ukrrif_vintorez"			: WEAPON_TYPE_SNIPER,
		"ukrroc_rpgfrag"			: WEAPON_TYPE_ATAA,
		"ukrroc_rpgheat"			: WEAPON_TYPE_ATAA,
		"ukrroc_rpgtandem"			: WEAPON_TYPE_ATAA,
		"ukrroc_rpgthermo"			: WEAPON_TYPE_ATAA,
		"ukrroc_sa7"				: WEAPON_TYPE_ATAA,
		"ukrsht_toz194"				: WEAPON_TYPE_SHOTGUN,
		"ukrsmg_asval"				: WEAPON_TYPE_ASSAULT,
		"ukrsni_ntw20"				: WEAPON_TYPE_ASSAULT,
		"usasht_m1014"				: WEAPON_TYPE_SHOTGUN,
		"usasmg_mp7"				: WEAPON_TYPE_SMG,
		"usasmg_mp7_2"				: WEAPON_TYPE_SMG,
		"usasmg_mp7_scoped"			: WEAPON_TYPE_SMG,
		"usasmg_mp7_silenced"			: WEAPON_TYPE_SMG,
		"ushgr_m67"				: WEAPON_TYPE_HANDGRENADE,
		"usmin_claymore"			: WEAPON_TYPE_CLAYMORE,
		"usmin_claymore2"			: WEAPON_TYPE_CLAYMORE,
		"usrif_g36c"				: WEAPON_TYPE_ASSAULT,
	# OPK 0.2
		"ag36"					: WEAPON_TYPE_ASSAULT,
		"ag36_g"				: WEAPON_TYPE_ASSAULTGRN,
		"ammokit"				: WEAPON_TYPE_TACTICAL,
		"cz999"					: WEAPON_TYPE_PISTOL,
		"cz999_h"				: WEAPON_TYPE_PISTOL,
		"dm21" 					: WEAPON_TYPE_ATMINE,
		"dm51"					: WEAPON_TYPE_HANDGRENADE,
		"dm51_b"				: WEAPON_TYPE_TACTICAL,
		"g22"					: WEAPON_TYPE_SNIPER,
		"g36c"					: WEAPON_TYPE_CARBINE,
		"g36c_nosd"				: WEAPON_TYPE_CARBINE,
		"g36k"					: WEAPON_TYPE_ASSAULT,
		"g36"					: WEAPON_TYPE_ASSAULT,
		"g36_san"				: WEAPON_TYPE_ASSAULT,
		"g36_zf"				: WEAPON_TYPE_SNIPER,
		"g3a3"					: WEAPON_TYPE_ASSAULT,
		"gimlet"				: WEAPON_TYPE_ATAA,
		"grapplinghook"				: WEAPON_TYPE_GRAPPLINGHOOK,
		"halem"					: WEAPON_TYPE_TARGETING,
		"hgr_smoke"				: WEAPON_TYPE_TACTICAL,
		"klappspaten"				: WEAPON_TYPE_TACTICAL,
		"km2000"				: WEAPON_TYPE_KNIFE,
		"m21"					: WEAPON_TYPE_ASSAULT,
		"m21_g"					: WEAPON_TYPE_ASSAULTGRN,
		"m21_ngl"				: WEAPON_TYPE_ASSAULT,
		"m21_san"				: WEAPON_TYPE_ASSAULT,
		"m21_zf"				: WEAPON_TYPE_SNIPER,
		"m67"					: WEAPON_TYPE_HANDGRENADE,
		"m67_b"					: WEAPON_TYPE_TACTICAL,
		"m76"					: WEAPON_TYPE_SNIPER,
		"m77"					: WEAPON_TYPE_SNIPER,
		"m84mg"					: WEAPON_TYPE_LMG,
		"m85"					: WEAPON_TYPE_CARBINE,
		"m85_nosd"				: WEAPON_TYPE_CARBINE,
		"medikit"				: WEAPON_TYPE_TACTICAL,
		"mg3"					: WEAPON_TYPE_LMG,
		"mp2"					: WEAPON_TYPE_SMG,
		"mp5sd6"				: WEAPON_TYPE_SMG,
		"mp5"					: WEAPON_TYPE_SMG,
		"mp7"					: WEAPON_TYPE_SMG,
		"mp7_p"					: WEAPON_TYPE_SMG,
		"onetimeparachute"			: WEAPON_TYPE_TACTICAL,
		"osa"					: WEAPON_TYPE_SNIPER,
		"p12sd"					: WEAPON_TYPE_PISTOL,
		"p8"					: WEAPON_TYPE_PISTOL,
		"pzfst3"				: WEAPON_TYPE_ATAA,
		"serb_bajonett"				: WEAPON_TYPE_KNIFE,
		"stinger"				: WEAPON_TYPE_ATAA,
		"tmrp6" 				: WEAPON_TYPE_ATMINE,
		"vz61"					: WEAPON_TYPE_SMG,
		"vz61_p"				: WEAPON_TYPE_SMG,
		"wrench"				: WEAPON_TYPE_TACTICAL,
	# Project Reality 0.613
		"at_mine_idx4" 				: WEAPON_TYPE_ATMINE,
		"at_mine_usm19" 			: WEAPON_TYPE_ATMINE,
		"c4_carbomber"				: WEAPON_TYPE_C4,
		"c4_detonator" 				: WEAPON_TYPE_C4,
		"c4_large" 				: WEAPON_TYPE_C4,
		"c4_slam" 				: WEAPON_TYPE_C4,
		"chlat_pf89" 				: WEAPON_TYPE_ATAA,
		"chpis_qsz92_idx3" 			: WEAPON_TYPE_PISTOL,
		"chrif_gp25" 				: WEAPON_TYPE_ASSAULTGRN,
		"chrif_qbz95iron" 			: WEAPON_TYPE_ASSAULT,
		"chrif_qbz95scope" 			: WEAPON_TYPE_ASSAULT,
		"chrif_qbz95ugl"			: WEAPON_TYPE_ASSAULTGRN,
		"chsht_slugshot" 			: WEAPON_TYPE_SHOTGUN,
		"dual_micro_uzi" 			: WEAPON_TYPE_SMG,
		"f1grenade" 				: WEAPON_TYPE_TACTICAL,
		"gbhgr_l109" 				: WEAPON_TYPE_TACTICAL,
		"gblat_law80" 				: WEAPON_TYPE_ATAA,
		"gbpis_l9" 				: WEAPON_TYPE_PISTOL,
		"gbpis_l9_idx3" 			: WEAPON_TYPE_PISTOL,
		"gbrif_l85a2ag36" 			: WEAPON_TYPE_ASSAULT,
		"gbrif_l85a2ag36gl" 			: WEAPON_TYPE_ASSAULTGRN,
		"gbrif_l85a2ag36smoke" 			: WEAPON_TYPE_ASSAULTGRN,
		"gbrif_l85a2iron" 			: WEAPON_TYPE_ASSAULT,
		"gbrif_l85a2iron_6" 			: WEAPON_TYPE_ASSAULT,
		"gbrif_l85a2susat" 			: WEAPON_TYPE_ASSAULT,
		"gbrif_l86" 				: WEAPON_TYPE_SNIPER,
		"gbsht_benelli_m4" 			: WEAPON_TYPE_SHOTGUN,
		"gbsht_slugshot" 			: WEAPON_TYPE_SHOTGUN,
		"gbsmg_mp7" 				: WEAPON_TYPE_SMG,
		"gbsni_l115a1" 				: WEAPON_TYPE_SNIPER,
		"gbrif_benelli_m4" 			: WEAPON_TYPE_SHOTGUN,
		"gbrif_l96a1" 				: WEAPON_TYPE_SNIPER,
		"hgr_molotov" 				: WEAPON_TYPE_TACTICAL,
		"hgr_molotov_idx5" 			: WEAPON_TYPE_TACTICAL,
		"hgr_smoke" 				: WEAPON_TYPE_TACTICAL,
		"hgr_smoke_q1" 				: WEAPON_TYPE_TACTICAL,
		"hgr_smoke_signal" 			: WEAPON_TYPE_TACTICAL,
		"hgr_smoke_signalgreen" 		: WEAPON_TYPE_TACTICAL,
		"hgr_smoke_signalorange" 		: WEAPON_TYPE_TACTICAL,
		"hgr_smoke_idx4qty1" 			: WEAPON_TYPE_TACTICAL,
		"insrg_ak47" 				: WEAPON_TYPE_ASSAULT,
		"insrg_dragunov" 			: WEAPON_TYPE_SNIPER,
		"insrg_ied" 				: WEAPON_TYPE_C4,
		"insrg_ied_prox" 			: WEAPON_TYPE_ATMINE,
		"insrg_pkmkit" 				: WEAPON_TYPE_LMG,
		"iraq_scorpion" 			: WEAPON_TYPE_SMG,
		"iraq_smoke_nade" 			: WEAPON_TYPE_TACTICAL,
		"iraqaa_sa7" 				: WEAPON_TYPE_ATAA,
		"javelin" 				: WEAPON_TYPE_ATAA,
		"klappspaten" 				: WEAPON_TYPE_TACTICAL,
		"kni_kabar" 				: WEAPON_TYPE_KNIFE,
		"kni_knife"				: WEAPON_TYPE_KNIFE,
		"kni_sa80bayonet"			: WEAPON_TYPE_KNIFE,
		"m40a3" 				: WEAPON_TYPE_SNIPER,
		"mecrif_g3iron" 			: WEAPON_TYPE_ASSAULT,
		"mecrif_g3scope" 			: WEAPON_TYPE_ASSAULT,
		"medikit" 				: WEAPON_TYPE_SHOCKPAD,
		"medikit_idx4" 				: WEAPON_TYPE_SHOCKPAD,
		"mosinnagant" 				: WEAPON_TYPE_SNIPER,
		"mosinnagant_pu" 			: WEAPON_TYPE_SNIPER,
		"nvg" 					: WEAPON_TYPE_TACTICAL,
		"ppsh41" 				: WEAPON_TYPE_SMG,
		"rulat_rpg7" 				: WEAPON_TYPE_ATAA,
		"rupis_baghira_idx3" 			: WEAPON_TYPE_PISTOL,
		"rurgl_gp25_smoke" 			: WEAPON_TYPE_ASSAULTGRN,
		"rurgl_gp30_smoke" 			: WEAPON_TYPE_ASSAULTGRN,
		"rusht_slugshot"			: WEAPON_TYPE_SHOTGUN,
		"rusni_sv98" 				: WEAPON_TYPE_SNIPER,
		"simonov" 				: WEAPON_TYPE_ASSAULT,
		"sks" 					: WEAPON_TYPE_ASSAULT,
		"stone" 				: WEAPON_TYPE_TACTICAL,
		"tm62m_mine" 				: WEAPON_TYPE_ATMINE,
		"usaa_fm92a" 				: WEAPON_TYPE_ATAA,
		"usat_smaw" 				: WEAPON_TYPE_ATAA,
		"uslat_at4" 				: WEAPON_TYPE_ATAA,
		"uslmg_bipod" 				: WEAPON_TYPE_LMG,
		"usmin_claymore_idx4" 			: WEAPON_TYPE_CLAYMORE,
		"usmin_claymore_idx4qty3" 		: WEAPON_TYPE_CLAYMORE,
		"uspis_92fs_idx3" 			: WEAPON_TYPE_PISTOL,
		"uspis_p226" 				: WEAPON_TYPE_PISTOL,
		"usrgl_m203_smoke" 			: WEAPON_TYPE_ASSAULTGRN,
		"usrif_g3a3_5"				: WEAPON_TYPE_ASSAULT,
		"usrif_g3a3_6" 				: WEAPON_TYPE_ASSAULT,
		"usrif_m4_pilot" 			: WEAPON_TYPE_CARBINE,
		"usrif_m14" 				: WEAPON_TYPE_SNIPER,
		"usrif_m16a2" 				: WEAPON_TYPE_ASSAULT,
		"usrif_m16a2_6" 			: WEAPON_TYPE_ASSAULT,
		"usrif_m16a4" 				: WEAPON_TYPE_ASSAULT,
		"usrif_mk12" 				: WEAPON_TYPE_SNIPER,
		"ussht_slugshot" 			: WEAPON_TYPE_SHOTGUN,
	# AiX 1.0
#CARBINE
		"g36v"					: WEAPON_TYPE_CARBINE,
		"stg"					: WEAPON_TYPE_CARBINE,
		"tavor"					: WEAPON_TYPE_CARBINE,
		"steyr"					: WEAPON_TYPE_CARBINE,
		"ebr"					: WEAPON_TYPE_CARBINE,
#ATMINE
		"at_mine"				: WEAPON_TYPE_ATMINE,
		"at4_mine"				: WEAPON_TYPE_ATMINE,
#SHOCKPAD
		"defibrillator"				: WEAPON_TYPE_SHOCKPAD,
#KNIFE
		"kni_knife"				: WEAPON_TYPE_KNIFE,
		"throwknife"				: WEAPON_TYPE_KNIFE,
#PISTOL
		"aix_gsh"				: WEAPON_TYPE_PISTOL,
		"aix_gsh_silencer"			: WEAPON_TYPE_PISTOL,
		"aix_glock19"				: WEAPON_TYPE_PISTOL,
		"aix_glock19_silencer"			: WEAPON_TYPE_PISTOL,
		"rupis_baghira"				: WEAPON_TYPE_PISTOL,
		"rupis_baghira_silencer"		: WEAPON_TYPE_PISTOL,
		"uspis_92fs"				: WEAPON_TYPE_PISTOL,
		"uspis_92fs_silencer"			: WEAPON_TYPE_PISTOL,
		"kit_beretta"				: WEAPON_TYPE_PISTOL,
		"kit_gsh"				: WEAPON_TYPE_PISTOL,
		"kit_uspmatch"				: WEAPON_TYPE_PISTOL,
		"chpis_qsz92"				: WEAPON_TYPE_PISTOL,
		"chpis_qsz92_silencer"			: WEAPON_TYPE_PISTOL,
		"aix_uspmatch"				: WEAPON_TYPE_PISTOL,
		"aix_uspmatch_silencer"			: WEAPON_TYPE_PISTOL,
		"aix_beretta"				: WEAPON_TYPE_PISTOL,
		"aix_beretta_silencer"			: WEAPON_TYPE_PISTOL,
#GRAPPLINGHOOK
		"kit_grapple"				: WEAPON_TYPE_GRAPPLINGHOOK,
		"grapplinghook"				: WEAPON_TYPE_GRAPPLINGHOOK,
#HANDGRENADE
		"kit_grenade1"				: WEAPON_TYPE_HANDGRENADE,
		"ushgr_m67"				: WEAPON_TYPE_HANDGRENADE,
		"aix_grenade1"				: WEAPON_TYPE_HANDGRENADE,
#TACTICAL
		"ammokit"				: WEAPON_TYPE_TACTICAL,
		"mec_flaretrap"				: WEAPON_TYPE_TACTICAL,
		"medikit"				: WEAPON_TYPE_TACTICAL,
		"hgr_flashbang"				: WEAPON_TYPE_TACTICAL,
		"hgr_incendiary"			: WEAPON_TYPE_TACTICAL,
		"hgr_incendiary_sticky"			: WEAPON_TYPE_TACTICAL,
		"hgr_smoke_orange"			: WEAPON_TYPE_TACTICAL,
		"hgr_smoke_purple"			: WEAPON_TYPE_TACTICAL,
		"hgr_smoke_yellow"			: WEAPON_TYPE_TACTICAL,
		"hgr_teargas"				: WEAPON_TYPE_TACTICAL,
		"us_binocular"				: WEAPON_TYPE_TACTICAL,
		"us_flaretrap"				: WEAPON_TYPE_TACTICAL,
		"kit_flaretrap"				: WEAPON_TYPE_TACTICAL,
		"kit_incendiary"			: WEAPON_TYPE_TACTICAL,
		"kit_mecbinocs"				: WEAPON_TYPE_TACTICAL,
		"kit_mortar"				: WEAPON_TYPE_TACTICAL,
		"kit_us_binocs"				: WEAPON_TYPE_TACTICAL,
		"wrench"				: WEAPON_TYPE_TACTICAL,
		"binoculars_mec_ch"			: WEAPON_TYPE_TACTICAL,
		"ch_flaretrap"				: WEAPON_TYPE_TACTICAL,
#CLAYMORE
		"usmin_claymore"			: WEAPON_TYPE_CLAYMORE,
#C4
		"kit_timebomb"				: WEAPON_TYPE_C4,
		"c4_explosives"				: WEAPON_TYPE_C4,
		"c4_timebomb"				: WEAPON_TYPE_C4,
#ASSAULTGRN
		"sa80glgren"				: WEAPON_TYPE_ASSAULTGRN,
		"g36kgren"				: WEAPON_TYPE_ASSAULTGRN,
		"aix_g36k_gl"				: WEAPON_TYPE_ASSAULTGRN,
		"aix_mgl140"				: WEAPON_TYPE_ASSAULTGRN,
		"aix_scarl_gl"				: WEAPON_TYPE_ASSAULTGRN,
		"assault_gp25"				: WEAPON_TYPE_ASSAULTGRN,
		"assault_gp30"				: WEAPON_TYPE_ASSAULTGRN,
		"assault_m16_m203"			: WEAPON_TYPE_ASSAULTGRN,
		"at_mgl140"				: WEAPON_TYPE_ASSAULTGRN,
		"usrgl_m203"				: WEAPON_TYPE_ASSAULTGRN,
		"sasgr_fn2000"				: WEAPON_TYPE_ASSAULTGRN,
		"rurgl_gp25"				: WEAPON_TYPE_ASSAULTGRN,
		"rurgl_gp30"				: WEAPON_TYPE_ASSAULTGRN,
		"gbgr_sa80a2_l85"			: WEAPON_TYPE_ASSAULTGRN,
		"grenadelauncher"			: WEAPON_TYPE_ASSAULTGRN,
		"scargren"				: WEAPON_TYPE_ASSAULTGRN,
		"milkor"				: WEAPON_TYPE_ASSAULTGRN,
#ATAA
		"aix_strela2"				: WEAPON_TYPE_ATAA,
		"chat_eryx"				: WEAPON_TYPE_ATAA,
		"chat_eryx_lt"				: WEAPON_TYPE_ATAA,
		"rurpg_rpg7"				: WEAPON_TYPE_ATAA,
		"usatp_predator"			: WEAPON_TYPE_ATAA,
		"kit_fim"				: WEAPON_TYPE_ATAA,
		"kit_rpg7"				: WEAPON_TYPE_ATAA,
		"kit_strela2"				: WEAPON_TYPE_ATAA,
		"at_eryx_lt"				: WEAPON_TYPE_ATAA,
		"at_rpg7"				: WEAPON_TYPE_ATAA,
		"at_stinger"				: WEAPON_TYPE_ATAA,
		"at_strela2"				: WEAPON_TYPE_ATAA,
		"aix_fim92a"				: WEAPON_TYPE_ATAA,
		"aix_rpg7"				: WEAPON_TYPE_ATAA,
		"mortar_deployable"			: WEAPON_TYPE_ATAA,
#SHOTGUN
		"aix_m41a_shot"				: WEAPON_TYPE_SHOTGUN,
		"engineer_benelli_m4" 			: WEAPON_TYPE_SHOTGUN,
		"engineer_jackhammer" 			: WEAPON_TYPE_SHOTGUN,
		"engineer_norinco982"			: WEAPON_TYPE_SHOTGUN,
		"engineer_protecta"			: WEAPON_TYPE_SHOTGUN,
		"engineer_remington11-87"		: WEAPON_TYPE_SHOTGUN,
		"engineer_saiga12"			: WEAPON_TYPE_SHOTGUN,
#SMG
		"eurif_hk53a3"				: WEAPON_TYPE_SMG,
		"hk53a3"				: WEAPON_TYPE_SMG,
		"famas"					: WEAPON_TYPE_SMG,
		"aix_mac11"				: WEAPON_TYPE_SMG,
		"p220"					: WEAPON_TYPE_SMG,
		"rurif_ak101"				: WEAPON_TYPE_SMG,
		"rurif_ak101_b"				: WEAPON_TYPE_SMG,
		"rurif_bizon"				: WEAPON_TYPE_SMG,
		"rurrif_ak74u"				: WEAPON_TYPE_SMG,
		"sasrif_mp7"				: WEAPON_TYPE_SMG,
		"rurrif_ak74u_b"			: WEAPON_TYPE_SMG,
		"usrif_mp5_a3"				: WEAPON_TYPE_SMG,
		"kit_mac11"				: WEAPON_TYPE_SMG,
		"at_bizon"				: WEAPON_TYPE_SMG,
		"at_mp5"				: WEAPON_TYPE_SMG,
		"medic_ak101"				: WEAPON_TYPE_SMG,
		"specops_ak74u"				: WEAPON_TYPE_SMG,
		"specops_hk53a3"			: WEAPON_TYPE_SMG,
		"engineer_famas"			: WEAPON_TYPE_SMG,
		"aix_magpul"				: WEAPON_TYPE_SMG,
		"aix_Sig552SpecOps"			: WEAPON_TYPE_SMG,
#ASSAULT
		"sa80gl"				: WEAPON_TYPE_ASSAULT,	
		"sa80"					: WEAPON_TYPE_ASSAULT,	
		"g36k"					: WEAPON_TYPE_ASSAULT,
		"xm8"					: WEAPON_TYPE_ASSAULT,
		"scar"					: WEAPON_TYPE_ASSAULT,
		"aix_ak5_tactical"			: WEAPON_TYPE_ASSAULT,
		"aix_famas"				: WEAPON_TYPE_ASSAULT,
		"eu_famas"				: WEAPON_TYPE_ASSAULT,	
		"ak5"					: WEAPON_TYPE_ASSAULT,
		"sig552"				: WEAPON_TYPE_ASSAULT,
		"hk416"					: WEAPON_TYPE_ASSAULT,
		"f2000"					: WEAPON_TYPE_ASSAULT,
		"chrif_type95_b"			: WEAPON_TYPE_ASSAULT,
		"aix_fs2000"				: WEAPON_TYPE_ASSAULT,
		"gbrif_sa80a2_l85"			: WEAPON_TYPE_ASSAULT,
		"aix_mk14ebr"				: WEAPON_TYPE_ASSAULT,
		"aix_g36k_rif"				: WEAPON_TYPE_ASSAULT,
		"aix_g36v"				: WEAPON_TYPE_ASSAULT,
		"aix_hk416"				: WEAPON_TYPE_ASSAULT,
		"aix_m41a"				: WEAPON_TYPE_ASSAULT,
		"aix_scarl_rif"				: WEAPON_TYPE_ASSAULT,
		"aix_sig552"				: WEAPON_TYPE_ASSAULT,
		"aix_steyr_aug"				: WEAPON_TYPE_ASSAULT,
		"aix_xm8"				: WEAPON_TYPE_ASSAULT,
		"chlmg_type95"				: WEAPON_TYPE_ASSAULT,
		"chrif_type85"				: WEAPON_TYPE_ASSAULT,
		"chrif_type95"				: WEAPON_TYPE_ASSAULT,
		"eurif_famas"				: WEAPON_TYPE_ASSAULT,
		"eurif_fnp90"				: WEAPON_TYPE_ASSAULT,
		"rurif_ak47"				: WEAPON_TYPE_ASSAULT,
		"rurif_ak47_b"				: WEAPON_TYPE_ASSAULT,
		"rurif_gp25"				: WEAPON_TYPE_ASSAULT,
		"rurif_gp30"				: WEAPON_TYPE_ASSAULT,
		"sasrif_fn2000"				: WEAPON_TYPE_ASSAULT,
		"sasrif_g36e"				: WEAPON_TYPE_ASSAULT,
		"usrif_m4"				: WEAPON_TYPE_ASSAULT,
		"usrif_fnscarl"				: WEAPON_TYPE_ASSAULT,
		"usrif_g36c"				: WEAPON_TYPE_ASSAULT,
		"usrif_g3a3"				: WEAPON_TYPE_ASSAULT,
		"usrif_m203"				: WEAPON_TYPE_ASSAULT,
		"assault_ak5"				: WEAPON_TYPE_ASSAULT,
		"assault_fn_fal"			: WEAPON_TYPE_ASSAULT,
		"assault_fn2000"			: WEAPON_TYPE_ASSAULT,
		"assault_fnscarl"			: WEAPON_TYPE_ASSAULT,
		"assault_g36k"				: WEAPON_TYPE_ASSAULT,
		"assault_g3a3"				: WEAPON_TYPE_ASSAULT,
		"assault_m41a"				: WEAPON_TYPE_ASSAULT,
		"assault_sa80a2"			: WEAPON_TYPE_ASSAULT,
		"engineer_hk416"			: WEAPON_TYPE_ASSAULT,
		"engineer_mk14ebr"			: WEAPON_TYPE_ASSAULT,
		"engineer_tavor"			: WEAPON_TYPE_ASSAULT,
		"medic_ak47"				: WEAPON_TYPE_ASSAULT,
		"medic_fs2000"				: WEAPON_TYPE_ASSAULT,
		"medic_g36e"				: WEAPON_TYPE_ASSAULT,
		"medic_m16a2"				: WEAPON_TYPE_ASSAULT,
		"medic_sa80"				: WEAPON_TYPE_ASSAULT,
		"medic_steyr_aug"			: WEAPON_TYPE_ASSAULT,
		"specops_aix_famas"			: WEAPON_TYPE_ASSAULT,
		"specops_fnscarl"			: WEAPON_TYPE_ASSAULT,
		"specops_g36c"				: WEAPON_TYPE_ASSAULT,
		"specops_m4"				: WEAPON_TYPE_ASSAULT,
		"specops_sg552"				: WEAPON_TYPE_ASSAULT,
		"specops_type95"			: WEAPON_TYPE_ASSAULT,
		"specops_xm8"				: WEAPON_TYPE_ASSAULT,
#SNIPER
		"l96"					: WEAPON_TYPE_SNIPER,
		"tpg1"					: WEAPON_TYPE_SNIPER,
		"dsr"					: WEAPON_TYPE_SNIPER,
		"m109"					: WEAPON_TYPE_SNIPER,
		"aix_as50"				: WEAPON_TYPE_SNIPER,
		"aix_barrett_m109"			: WEAPON_TYPE_SNIPER,
		"aix_dsr"				: WEAPON_TYPE_SNIPER,
		"chsni_type88"				: WEAPON_TYPE_SNIPER,
		"gbrif_l96a1"				: WEAPON_TYPE_SNIPER,
		"rurif_dragunov"			: WEAPON_TYPE_SNIPER,
		"usrif_m24"				: WEAPON_TYPE_SNIPER,
		"sniper_as50"				: WEAPON_TYPE_SNIPER,
		"sniper_dragunov"			: WEAPON_TYPE_SNIPER,
		"sniper_dsr"				: WEAPON_TYPE_SNIPER,
		"sniper_l96a1"				: WEAPON_TYPE_SNIPER,
		"sniper_m109"				: WEAPON_TYPE_SNIPER,
		"sniper_m24"				: WEAPON_TYPE_SNIPER,
		"sniper_m82"				: WEAPON_TYPE_SNIPER,
		"sniper_m95_barret"			: WEAPON_TYPE_SNIPER,
		"sniper_tpg1"				: WEAPON_TYPE_SNIPER,
		"sniper_type88"				: WEAPON_TYPE_SNIPER,
		"kit_as50"				: WEAPON_TYPE_SNIPER,
		"aix_tpg1"				: WEAPON_TYPE_SNIPER,
#LMG	
		"hk21"					: WEAPON_TYPE_LMG,
		"minimec"				: WEAPON_TYPE_LMG,
		"mini"					: WEAPON_TYPE_LMG,
		"aix_stg58"				: WEAPON_TYPE_LMG,
		"eurif_hk21"				: WEAPON_TYPE_LMG,
		"sasrif_mg36"				: WEAPON_TYPE_LMG,
		"uslmg_m249saw"				: WEAPON_TYPE_LMG,
		"rulmg_pkm"				: WEAPON_TYPE_LMG,
		"rulmg_rpk74"				: WEAPON_TYPE_LMG,
		"support_hk21"				: WEAPON_TYPE_LMG,
		"support_m249saw"			: WEAPON_TYPE_LMG,
		"support_mg36"				: WEAPON_TYPE_LMG,
		"support_minigun"			: WEAPON_TYPE_LMG,
		"support_minigun_mec"			: WEAPON_TYPE_LMG,
		"support_pkm"				: WEAPON_TYPE_LMG,
		"support_rpk74"				: WEAPON_TYPE_LMG,
		"support_stg58"				: WEAPON_TYPE_LMG,
		"support_type95"			: WEAPON_TYPE_LMG,
		"aix_portableminigun"			: WEAPON_TYPE_LMG,
		"aix_portableminigun_mec"		: WEAPON_TYPE_LMG,
#-----------------------------------------------------------------------------------
}


kitTypeMap = {
#-------Possible Kittypes-----------------------------------------------------------
		# "objectname"				: KIT_TYPE_AT,
		# "objectname"				: KIT_TYPE_ASSAULT,
		# "objectname"				: KIT_TYPE_ENGINEER,
		# "objectname"				: KIT_TYPE_MEDIC,
		# "objectname"				: KIT_TYPE_SPECOPS,
		# "objectname"				: KIT_TYPE_SUPPORT,
		# "objectname"				: KIT_TYPE_SNIPER,
		# "objectname"				: KIT_TYPE_AA,
		# "objectname"				: KIT_TYPE_PILOT,
		# "objectname"				: KIT_TYPE_CREWMAN,
		# "objectname"				: KIT_TYPE_OFFICER,
		# "objectname"				: KIT_TYPE_MORTAR,
		# "objectname"				: KIT_TYPE_MARKSMAN,
		# "objectname"				: KIT_TYPE_CIVILIAN,
#-----------------------------------------------------------------------------------
	# Battlefield2
		"us_at"					: KIT_TYPE_AT,
		"us_assault"				: KIT_TYPE_ASSAULT,
		"us_engineer"				: KIT_TYPE_ENGINEER,
		"us_medic"				: KIT_TYPE_MEDIC,
		"us_specops"				: KIT_TYPE_SPECOPS,
		"us_support"				: KIT_TYPE_SUPPORT,
		"us_sniper"				: KIT_TYPE_SNIPER,
		"mec_at" 				: KIT_TYPE_AT,
		"mec_assault"				: KIT_TYPE_ASSAULT,
		"mec_engineer"				: KIT_TYPE_ENGINEER,
		"mec_medic"				: KIT_TYPE_MEDIC,
		"mec_specops"				: KIT_TYPE_SPECOPS,
		"mec_support"				: KIT_TYPE_SUPPORT,
		"mec_sniper"				: KIT_TYPE_SNIPER,
		"ch_at" 				: KIT_TYPE_AT,
		"ch_assault"				: KIT_TYPE_ASSAULT,
		"ch_engineer"				: KIT_TYPE_ENGINEER,
		"ch_medic"				: KIT_TYPE_MEDIC,
		"ch_specops"				: KIT_TYPE_SPECOPS,
		"ch_support"				: KIT_TYPE_SUPPORT,
		"ch_sniper"				: KIT_TYPE_SNIPER,
	# SpecialForces
		"seal_at" 				: KIT_TYPE_AT,
		"seal_assault"				: KIT_TYPE_ASSAULT,
		"seal_engineer"				: KIT_TYPE_ENGINEER,
		"seal_medic"				: KIT_TYPE_MEDIC,
		"seal_specops"				: KIT_TYPE_SPECOPS,
		"seal_support"				: KIT_TYPE_SUPPORT,
		"seal_sniper"				: KIT_TYPE_SNIPER,
		"sas_at" 				: KIT_TYPE_AT,
		"sas_assault"				: KIT_TYPE_ASSAULT,
		"sas_engineer"				: KIT_TYPE_ENGINEER,
		"sas_medic"				: KIT_TYPE_MEDIC,
		"sas_specops"				: KIT_TYPE_SPECOPS,
		"sas_support"				: KIT_TYPE_SUPPORT,
		"sas_sniper"				: KIT_TYPE_SNIPER,
		"spetsnaz_at" 				: KIT_TYPE_AT,
		"spetsnaz_assault"			: KIT_TYPE_ASSAULT,
		"spetsnaz_engineer"			: KIT_TYPE_ENGINEER,
		"spetsnaz_medic"			: KIT_TYPE_MEDIC,
		"spetsnaz_specops"			: KIT_TYPE_SPECOPS,
		"spetsnaz_support"			: KIT_TYPE_SUPPORT,
		"spetsnaz_sniper"			: KIT_TYPE_SNIPER,
		"mecsf_at" 				: KIT_TYPE_AT,
		"mecsf_assault"				: KIT_TYPE_ASSAULT,
		"mecsf_engineer"			: KIT_TYPE_ENGINEER,
		"mecsf_medic"				: KIT_TYPE_MEDIC,
		"mecsf_specops"				: KIT_TYPE_SPECOPS,
		"mecsf_support"				: KIT_TYPE_SUPPORT,
		"mecsf_sniper"				: KIT_TYPE_SNIPER,
		"chinsurgent_at" 			: KIT_TYPE_AT,
		"chinsurgent_assault"			: KIT_TYPE_ASSAULT,
		"chinsurgent_engineer"			: KIT_TYPE_ENGINEER,
		"chinsurgent_medic"			: KIT_TYPE_MEDIC,
		"chinsurgent_specops"			: KIT_TYPE_SPECOPS,
		"chinsurgent_support"			: KIT_TYPE_SUPPORT,
		"chinsurgent_sniper"			: KIT_TYPE_SNIPER,
		"meinsurgent_at" 			: KIT_TYPE_AT,
		"meinsurgent_assault"			: KIT_TYPE_ASSAULT,
		"meinsurgent_engineer"			: KIT_TYPE_ENGINEER,
		"meinsurgent_medic"			: KIT_TYPE_MEDIC,
		"meinsurgent_specops"			: KIT_TYPE_SPECOPS,
		"meinsurgent_support"			: KIT_TYPE_SUPPORT,
		"meinsurgent_sniper"			: KIT_TYPE_SNIPER,
		"mecsf_at_special" 			: KIT_TYPE_AT,
		"mecsf_assault_special"			: KIT_TYPE_ASSAULT,
		"mecsf_specops_special"			: KIT_TYPE_SPECOPS,
		"mecsf_sniper_special"			: KIT_TYPE_SNIPER,
		"sas_at_special" 			: KIT_TYPE_AT,
		"sas_assault_special"			: KIT_TYPE_ASSAULT,
		"sas_specops_special"			: KIT_TYPE_SPECOPS,
		"sas_sniper_special"			: KIT_TYPE_SNIPER,
	# Euroforces
		"eu_at" 				: KIT_TYPE_AT,
		"eu_assault"				: KIT_TYPE_ASSAULT,
		"eu_engineer"				: KIT_TYPE_ENGINEER,
		"eu_medic"				: KIT_TYPE_MEDIC,
		"eu_specops"				: KIT_TYPE_SPECOPS,
		"eu_support"				: KIT_TYPE_SUPPORT,
		"eu_sniper"				: KIT_TYPE_SNIPER,	
	# POE2 1.1.8
		"ger_assault"				: KIT_TYPE_ASSAULT,
		"ger_at"				: KIT_TYPE_AT,
		"ger_engineer"				: KIT_TYPE_ENGINEER,
		"ger_medic"				: KIT_TYPE_MEDIC,
		"ger_sniper"				: KIT_TYPE_SNIPER,
		"ger_specops"				: KIT_TYPE_SPECOPS,
		"ger_support"				: KIT_TYPE_SUPPORT,
		"ukr_at" 				: KIT_TYPE_AT,
		"ukr_assault"				: KIT_TYPE_ASSAULT,
		"ukr_engineer"				: KIT_TYPE_ENGINEER,
		"ukr_medic"				: KIT_TYPE_MEDIC,
		"ukr_specops"				: KIT_TYPE_SPECOPS,
		"ukr_support"				: KIT_TYPE_SUPPORT,
		"ukr_sniper"				: KIT_TYPE_SNIPER,
	# OPK 0.2
		"se_sturmsoldat_h"			: KIT_TYPE_ASSAULT,
		"se_sturmsoldat"			: KIT_TYPE_ASSAULT,
		"se_sschuetze_h"			: KIT_TYPE_SNIPER,
		"se_sschuetze"				: KIT_TYPE_SNIPER,
		"se_spezial_h"				: KIT_TYPE_SPECOPS,
		"se_spezial"				: KIT_TYPE_SPECOPS,
		"se_sani_h"				: KIT_TYPE_MEDIC,
		"se_sani"				: KIT_TYPE_MEDIC,
		"se_pzabw_h" 				: KIT_TYPE_AT,
		"se_pzabw" 				: KIT_TYPE_AT,
		"se_pilot"				: KIT_TYPE_PILOT,
		"se_nachschub"				: KIT_TYPE_SUPPORT,
		"se_mgschuetze"				: KIT_TYPE_SUPPORT,
		"ge_sturmsoldat_h"			: KIT_TYPE_ASSAULT,
		"ge_sturmsoldat"			: KIT_TYPE_ASSAULT,
		"ge_sschuetze_h"			: KIT_TYPE_SNIPER,
		"ge_sschuetze_falli"			: KIT_TYPE_SNIPER,
		"ge_sschuetze"				: KIT_TYPE_SNIPER,
		"ge_spezial_h"				: KIT_TYPE_SPECOPS,
		"ge_spezial_falli"			: KIT_TYPE_SPECOPS,
		"ge_spezial"				: KIT_TYPE_SPECOPS,
		"ge_sani_h"				: KIT_TYPE_MEDIC,
		"ge_sani_falli"				: KIT_TYPE_MEDIC,
		"ge_sani"				: KIT_TYPE_MEDIC,
		"ge_pzabw_h" 				: KIT_TYPE_AT,
		"ge_pzabw_falli" 			: KIT_TYPE_AT,
		"ge_pzabw" 				: KIT_TYPE_AT,
		"ge_pilot"				: KIT_TYPE_PILOT,
		"ge_nachschub_falli"			: KIT_TYPE_SUPPORT,
		"ge_nachschub"				: KIT_TYPE_SUPPORT,
		"ge_mgschuetze_falli"			: KIT_TYPE_SUPPORT,
		"ge_mgschuetze"				: KIT_TYPE_SUPPORT,
		"ge_falli"				: KIT_TYPE_ASSAULT,
		"pickupstinger"				: KIT_TYPE_AA,
		"pickuppilot_se"			: KIT_TYPE_PILOT,
		"pickuppilot_ge"			: KIT_TYPE_PILOT,
		"pickupgimlet"				: KIT_TYPE_AA,
	# Project Reality 0.613
		"chinsurgent_medic" 			: KIT_TYPE_MEDIC,
		"chinsurgent_mercenary" 		: KIT_TYPE_ASSAULT,
		"chinsurgent_militant" 			: KIT_TYPE_ASSAULT,
		"chinsurgent_officer" 			: KIT_TYPE_OFFICER,
		"chinsurgent_pilot" 			: KIT_TYPE_PILOT,
		"chinsurgent_sapper" 			: KIT_TYPE_ENGINEER,
		"chinsurgent_scout" 			: KIT_TYPE_SPECOPS,
		"chinsurgent_tanker" 			: KIT_TYPE_CREWMAN,
		"ch_assault" 				: KIT_TYPE_ASSAULT,
		"ch_at" 				: KIT_TYPE_AT,
		"ch_engineer" 				: KIT_TYPE_ENGINEER,
		"ch_medic" 				: KIT_TYPE_MEDIC,
		"ch_rifleman" 				: KIT_TYPE_ASSAULT,
		"ch_riflemanaa" 			: KIT_TYPE_AA,
		"ch_riflemanat" 			: KIT_TYPE_AT,
		"ch_sniper" 				: KIT_TYPE_SNIPER,
		"ch_specops" 				: KIT_TYPE_SPECOPS,
		"ch_support" 				: KIT_TYPE_SUPPORT,
		"ch_marksman" 				: KIT_TYPE_MARKSMAN,
		"ch_mortarman" 				: KIT_TYPE_MORTAR,
		"ch_pilot" 				: KIT_TYPE_PILOT,
		"ch_officer" 				: KIT_TYPE_OFFICER,
		"ch_tanker" 				: KIT_TYPE_CREWMAN,
		"eu_assault" 				: KIT_TYPE_ASSAULT,
		"eu_at" 				: KIT_TYPE_AT,
		"eu_engineer" 				: KIT_TYPE_ENGINEER,
		"eu_medic" 				: KIT_TYPE_MEDIC,
		"eu_sniper" 				: KIT_TYPE_SNIPER,
		"eu_specops" 				: KIT_TYPE_SPECOPS,
		"eu_support" 				: KIT_TYPE_SUPPORT,
		"gb_assault" 				: KIT_TYPE_ASSAULT,
		"gb_at" 				: KIT_TYPE_AT,
		"gb_engineer" 				: KIT_TYPE_ENGINEER,
		"gb_medic" 				: KIT_TYPE_MEDIC,
		"gb_rifleman" 				: KIT_TYPE_ASSAULT,
		"gb_riflemanaa" 			: KIT_TYPE_AA,
		"gb_riflemanat" 			: KIT_TYPE_AT,
		"gb_sniper" 				: KIT_TYPE_SNIPER,
		"gb_specops" 				: KIT_TYPE_SPECOPS,
		"gb_support" 				: KIT_TYPE_SUPPORT,
		"gb_marksman" 				: KIT_TYPE_MARKSMAN,
		"gb_mortarman" 				: KIT_TYPE_MORTAR,
		"gb_pilot" 				: KIT_TYPE_PILOT,
		"gb_officer" 				: KIT_TYPE_OFFICER,
		"gb_tanker" 				: KIT_TYPE_CREWMAN,
		"mecsf_assault" 			: KIT_TYPE_ASSAULT,
		"mecsf_at" 				: KIT_TYPE_AT,
		"mecsf_engineer" 			: KIT_TYPE_ENGINEER,
		"mecsf_medic" 				: KIT_TYPE_MEDIC,
		"mecsf_sniper" 				: KIT_TYPE_SNIPER,
		"mecsf_specops" 			: KIT_TYPE_SPECOPS,
		"mecsf_support" 			: KIT_TYPE_SUPPORT,
		"mec_assault" 				: KIT_TYPE_ASSAULT,
		"mec_at" 				: KIT_TYPE_AT,
		"mec_engineer" 				: KIT_TYPE_ENGINEER,
		"mec_medic" 				: KIT_TYPE_MEDIC,
		"mec_rifleman" 				: KIT_TYPE_ASSAULT,
		"mec_riflemanaa" 			: KIT_TYPE_AA,
		"mec_riflemanat" 			: KIT_TYPE_AT,
		"mec_sniper" 				: KIT_TYPE_SNIPER,
		"mec_specops" 				: KIT_TYPE_SPECOPS,
		"mec_support" 				: KIT_TYPE_SUPPORT,
		"mec_marksman" 				: KIT_TYPE_MARKSMAN,
		"mec_mortarman" 			: KIT_TYPE_MORTAR,
		"mec_pilot" 				: KIT_TYPE_PILOT,
		"mec_officer" 				: KIT_TYPE_OFFICER,
		"mec_tanker" 				: KIT_TYPE_CREWMAN,
		"meinsurgent_civilian" 			: KIT_TYPE_CIVILIAN,
		"meinsurgent_machinegunner" 		: KIT_TYPE_SUPPORT,
		"meinsurgent_warveteran" 		: KIT_TYPE_ASSAULT,
		"meinsurgent_ambusher" 			: KIT_TYPE_ENGINEER,
		"meinsurgent_insurgent" 		: KIT_TYPE_ASSAULT,
		"meinsurgent_officer" 			: KIT_TYPE_OFFICER,
		"sas_assault" 				: KIT_TYPE_ASSAULT,
		"sas_at" 				: KIT_TYPE_AT,
		"sas_engineer" 				: KIT_TYPE_ENGINEER,
		"sas_medic" 				: KIT_TYPE_MEDIC,
		"sas_sniper" 				: KIT_TYPE_SNIPER,
		"sas_specops" 				: KIT_TYPE_SPECOPS,
		"sas_support" 				: KIT_TYPE_SUPPORT,
		"seal_assault" 				: KIT_TYPE_ASSAULT,
		"seal_at" 				: KIT_TYPE_AT,
		"seal_engineer" 			: KIT_TYPE_ENGINEER,
		"seal_medic" 				: KIT_TYPE_MEDIC,
		"seal_sniper" 				: KIT_TYPE_SNIPER,
		"seal_specops" 				: KIT_TYPE_SPECOPS,
		"seal_support" 				: KIT_TYPE_SUPPORT,
		"spetsnaz_assault" 			: KIT_TYPE_ASSAULT,
		"spetsnaz_at" 				: KIT_TYPE_AT,
		"spetsnaz_engineer" 			: KIT_TYPE_ENGINEER,
		"spetsnaz_medic" 			: KIT_TYPE_MEDIC,
		"spetsnaz_sniper" 			: KIT_TYPE_SNIPER,
		"spetsnaz_specops" 			: KIT_TYPE_SPECOPS,
		"spetsnaz_support" 			: KIT_TYPE_SUPPORT,
		"us_assault" 				: KIT_TYPE_ASSAULT,
		"us_at" 				: KIT_TYPE_AT,
		"us_engineer" 				: KIT_TYPE_ENGINEER,
		"us_medic"				: KIT_TYPE_MEDIC,
		"us_rifleman" 				: KIT_TYPE_ASSAULT,
		"us_riflemanaa" 			: KIT_TYPE_AA,
		"us_riflemanat" 			: KIT_TYPE_AT,
		"us_sniper" 				: KIT_TYPE_SNIPER,
		"us_specops" 				: KIT_TYPE_SPECOPS,
		"us_support" 				: KIT_TYPE_SUPPORT,
		"us_marksman" 				: KIT_TYPE_MARKSMAN,
		"us_mortarman" 				: KIT_TYPE_MORTAR,
		"us_pilot" 				: KIT_TYPE_PILOT,
		"us_officer" 				: KIT_TYPE_OFFICER,
		"us_tanker" 				: KIT_TYPE_CREWMAN,
	# AiX 1.0
		"un_assault" 				: KIT_TYPE_ASSAULT,
		"un_at" 				: KIT_TYPE_AT,
		"un_engineer" 				: KIT_TYPE_ENGINEER,
		"un_medic"				: KIT_TYPE_MEDIC,
		"un_sniper" 				: KIT_TYPE_SNIPER,
		"un_specops" 				: KIT_TYPE_SPECOPS,
		"un_support" 				: KIT_TYPE_SUPPORT,
	# BF Pirates 2
#-----------------------------------------------------------------------------------
}


armyMap = {
#-------Possible Weapontypes--------------------------------------------------------
		# "objectname"				: ARMY_USA,
		# "objectname"				: ARMY_MEC
		# "objectname"				: ARMY_CHINESE
		# "objectname"				: ARMY_SEALS
		# "objectname"				: ARMY_SAS
		# "objectname"				: ARMY_SPETZNAS
		# "objectname"				: ARMY_MECSF
		# "objectname"				: ARMY_REBELS
		# "objectname"				: ARMY_INSURGENTS
		# "objectname"				: ARMY_EURO
		# "objectname"				: ARMY_BRITS
		# "objectname"				: ARMY_CANADA
		# "objectname"				: ARMY_GER
		# "objectname"				: ARMY_UKR
		# "objectname"				: ARMY_SE
		# "objectname"				: ARMY_UN
		# "objectname"				: ARMY_PEGLEG
		# "objectname"				: ARMY_UNDEATH
#-----------------------------------------------------------------------------------
	# Battlefield2
		"us"					: ARMY_USA,
		"mec"					: ARMY_MEC,
		"ch"					: ARMY_CHINESE,
	# SpecialForces 
		"seal"					: ARMY_SEALS,
		"sas"					: ARMY_SAS,
		"spetz"					: ARMY_SPETZNAS,
		"mecsf"					: ARMY_MECSF,
		"chinsurgent"				: ARMY_REBELS,
		"meinsurgent"   			: ARMY_INSURGENTS,
	# Euroforces
		"eu"					: ARMY_EURO,
	# POE2 1.1.8
		"ger"					: ARMY_GER,
		"ukr"					: ARMY_UKR,
	# OPK 0.2
		"ge"					: ARMY_GER,
		"se"					: ARMY_SE,
	# Project Reality 0.613
		"gb" 					: ARMY_BRITS,
		"cf" 					: ARMY_CANADA,
	# AiX 1.0
		"un" 					: ARMY_UN,
	# BF Pirates 2
		"peg" 					: ARMY_PEGLEG,
		"und" 					: ARMY_UNDEATH,
#-----------------------------------------------------------------------------------
}


mapMap = {
#-----------------------------------------------------------------------------------
	# Battlefield2
		# Middle Eastern Theater
		"kubra_dam"				: "0",
		"mashtuur_city"				: "1",
		"operation_clean_sweep" 		: "2",
		"zatar_wetlands"			: "3",
		"strike_at_karkand"			: "4",
		"sharqi_peninsula"			: "5",
		"gulf_of_oman"				: "6",
		"operationsmokescreen"  		: "10",
		"taraba_quarry"				: "11",
		"road_to_jalalabad"			: "12",
		"highway_tampa"				: "13",
		# Asian Theater
		"daqing_oilfields"			: "100",
		"dalian_plant"				: "101",
		"dragon_valley"				: "102",
		"fushe_pass"				: "103",
		"hingan_hills"				: "104",
		"songhua_stalemate"			: "105",
		"greatwall"				: "110",	
		# US Theatre
		"midnight_sun"				: "200",
		"operationroadrage"			: "201",
		"operationharvest"			: "202",
		# Special maps
		"wake_island_2007"			: "601",
	# SpecialForces 
		"devils_perch"				: "300",
		"iron_gator"				: "301",
		"night_flight"				: "302",
		"warlord"				: "303",
		"leviathan"				: "304",
		"mass_destruction"			: "305",
		"surge"					: "306",
		"ghost_town"				: "307",
	# POE2 1.1.8 GSID 1001 - 1100
		"battle_of_sambir"			: "1001",
		"carpathian_mountains"			: "1002",
		"dnipro_sunrise"			: "1003",
		"dnister_river_valley"			: "1004",
		"fallen"				: "1005",
		"first_snow"				: "1006",
		"guardian"				: "1007",
		"highway_to_hell"			: "1008",
		"lutsk"					: "1009",
		"orel"					: "1010",
		"rivne"					: "1011",
		"rolling_thunder"			: "1012",
		"zhytomyr"				: "1013",
		"spies_like_us"				: "1014",
		"berezan_island"			: "1015",
		"berezne"				: "1016",
		"blue_nile"				: "1017",
		"crimea"				: "1018",
		"odessa"				: "1019",
		"olesko_keep"				: "1020",
		"operationacorn"			: "1021",
		#"red_dawn"				: "1022",
	# OPK 0.2 GSID 1101 - 1200
		"borders_infiltration"			: "1101",
		"opk_airfield_assault"			: "1102",
		"opk_ambush"				: "1103",
		"opk_battle_of_bogovina"		: "1104",
		"opk_battle_of_last_outpost"		: "1105",
		"opk_battle_of_tutin"			: "1106",
		"opk_blockade_policy"			: "1107",
		"opk_bordercontrol"			: "1108",
		"opk_code_bravo"			: "1109",
		"opk_harbour_sabotage"			: "1110",
		"opk_hill_of_the_dead"			: "1111",
		"opk_monastari_zogosiji"		: "1112",
		"opk_red_on_eleven"			: "1113",
		"opk_village"				: "1114",
		"opk_wildgans"				: "1115",
		"out_of_reach"				: "1116",
	# Project Reality 0.613 GSID 1201 - 1300
		"7gates"				: "1201",
		"al_kufrah_oilfield"			: "1202",
		"albasrah"				: "1203",
		"assault_on_mestia"			: "1204",
		"bi_ming"				: "1205",
		"daqing_oilfields"			: "1206",
		"ejod_desert_6"				: "1207",
		"helmand_province"			: "1208",
		"hills_of_hamgyong"			: "1209",
		"jabal"					: "1210",
		"kashan_desert"				: "1211",
		"operation_ghost_train"			: "1212",
		"operation_phoenix"			: "1213",
		"qwai1"					: "1214",
		"road_to_kyongan_ni"			: "1215",
		"street"				: "1216",
		"sunset_city"				: "1217",
	# Allied Intent 0.2 - AiX GSID 1301 - 1400
		"abandoned_uranium_works"		: "1301",
		"codename_cascade"			: "1302",
		"dalian_64_sunset"			: "1303",
		"europa_island"				: "1304",
		"liberation"				: "1305",
		"operation_night_sweep"			: "1306",
		"oxbow_lakes"				: "1307",
		"processing_plant"			: "1308",
		"surrounded_2"				: "1309",
		#"the_push_day"				: "1310",
		"the_push_night"			: "1311",
		"aix_archipelago"			: "1312",
		"aix_damocles"				: "1313",
		"aix_refinery"				: "1314",
		"aix_runningman"			: "1315",
		"daqing_dawn"				: "1316",
		"dragon_valley_moon"			: "1317",
		"falklands"				: "1318",
		"karkand_stormfront"			: "1319",
		"processing_plant"			: "1320",
		"the_push_day"				: "1321",
		"urban_jungle"				: "1322",
		"wake_twilight"				: "1323",
		"zatar_wetlands_ii"			: "1324",
		"zzz_easter_island"			: "1325",
		"end_of_the_line"			: "1326",
		"kursk"					: "1327",
		"marauders_at_midnight"			: "1328",
		"midway"				: "1329",
		"snowy_park"				: "1330",
		"snowy_park_day"			: "1331",
		"snowy_park_summer"			: "1332",
		"solomon_showdown"			: "1333",
		"operation_fox"				: "1334",
		"iron_thunder"				: "1335",
		"invasion_of_the_philippines"		: "1336",
		"husky"					: "1337",
		"battle_of_kirkuk_oilfields"		: "1338",
		"aix_abandoned_uranium_works"		: "1339",
		"aix_wake_island_2007"			: "1340",
		"eagles_nest"				: "1341",
		"iwo_jima"				: "1342",
		"manamoc_island"			: "1343",
		"rebellion"				: "1344",
		"red_dawn"				: "1345",
		"tobruk"				: "1346",
		"clean_sweep_ii"			: "1347",
	# BF Pirates 2 GSID 2001 - 2100
		"bluebayou"				: "2001",
		"dead_calm"				: "2002",
		"pelican_point"				: "2003",
		"shallow_draft"				: "2004",
		"shiver_me_timbers"			: "2005",
		"storm_the_bastion"			: "2006",
#-----------------------------------------------------------------------------------
}
UNKNOWN_MAP = 99


gameModeMap = {
#-----------------------------------------------------------------------------------
		"gpm_cq"				: 0,
		"gpm_sl"				: 1,
		"gpm_coop"				: 2,
		"gpm_tdm"				: 3,
		"gpm_ctf"       			: 4,
	    	"gpm_obj"       			: 5,
	    	"gpm_dom"       			: 6,
		"gpm_fl"				: 7,
		"gpm_nuke"				: 8,
		"gpm_inc"				: 9,
		"gpm_insurgency"			: 10,
		"gpm_xtract"				: 11,
		"gpm_zm"				: 12,
#-----------------------------------------------------------------------------------
}
UNKNOWN_GAMEMODE = 99


def getVehicleType(templateName):
	try:
		vehicleType = vehicleTypeMap[string.lower(templateName)]
	except KeyError:
		return VEHICLE_TYPE_UNKNOWN
	return vehicleType

	
def getWeaponType(templateName):
	try:
		weaponType = weaponTypeMap[string.lower(templateName)]
	except KeyError:
		return WEAPON_TYPE_UNKNOWN
	return weaponType	

		
def getKitType(templateName):	
	try:
		kitType = kitTypeMap[string.lower(templateName)]
	except KeyError:
		return KIT_TYPE_UNKNOWN
	return kitType	

	
def getArmy(templateName):
	try:
		army = armyMap[string.lower(templateName)]
	except KeyError:
		return ARMY_UNKNOWN
	return army


def getMapId(mapName):
	try:
		mapId = mapMap[string.lower(mapName)]
	except KeyError:
		return UNKNOWN_MAP
	return mapId


def getGameModeId(gameMode):
	try:
		gameModeId = gameModeMap[string.lower(gameMode)]
	except KeyError:
		return UNKNOWN_GAMEMODE
	return gameModeId


def getRootParent(obj):
	parent = obj.getParent()
	if parent == None:
		return obj
	return getRootParent(parent)


if g_debug: print "Stat constants loaded"