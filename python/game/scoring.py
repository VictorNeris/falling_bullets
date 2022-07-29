

SCORING_TYPE_UNKNOWN		= 0
SCORING_TYPE_SNIPER		= 1
SCORING_TYPE_MELEE		= 2

objects = {

#SNIPER
		"m40a3"				: SCORING_TYPE_SNIPER,
		"chsni_type88"				: SCORING_TYPE_SNIPER,
		"rurif_dragunov"			: SCORING_TYPE_SNIPER,
		"cs_lr4"				: SCORING_TYPE_SNIPER,
		"rurif_sv98"				: SCORING_TYPE_SNIPER,
		"sr_jng90"			: SCORING_TYPE_SNIPER,
		"m40a3_sd"				: SCORING_TYPE_SNIPER,
		"chsni_type88_sd"				: SCORING_TYPE_SNIPER,
		"rurif_dragunov_sd"			: SCORING_TYPE_SNIPER,
		"cs_lr4"				: SCORING_TYPE_SNIPER,
		"rurif_sv98"				: SCORING_TYPE_SNIPER,
		"sr_jng90_sd"			: SCORING_TYPE_SNIPER,

# MELEE
		"defibrillator"				: SCORING_TYPE_MELEE,
		"kni_knife"				: SCORING_TYPE_MELEE,

}

def getscoringtype(object):
	if object == None: return SCORING_TYPE_UNKNOWN

	template = object.templateName.lower()
	if objects.has_key(template):
		return objects[template]
	else:
		return SCORING_TYPE_UNKNOWN


