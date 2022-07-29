#add sp maps you want to play as rush mode

class Rushv2Config:
	def __init__(self, disableAtkBaseAfterFirstRush=True):
		self.disableAtkBaseAfterFirstRush = disableAtkBaseAfterFirstRush

RUSH_MAPS=[
	'strike_at_karkand_rush',
	'sharqi_peninsula_rush',
	'road_to_jalalabad_rush',
	'wake_island_2007_rush',
	'warlord_rush',
	'devils_perch_rush'
]

RUSHV2_MAPS={
	'strike_at_karkand_rushv2' : Rushv2Config(),
	'sharqi_peninsula_rushv2' : Rushv2Config(),
	'road_to_jalalabad_rushv2' : Rushv2Config(),
	'greatwall_rushv2' : Rushv2Config(),
	'operation_blue_pearl_rushv2' : Rushv2Config(),
	'operation_clean_sweep_rushv2' : Rushv2Config(),
	'dragon_valley_rushv2' : Rushv2Config(),
	'mashtuur_city_rushv2' : Rushv2Config(),
}