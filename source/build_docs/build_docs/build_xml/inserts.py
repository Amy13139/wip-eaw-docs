# This file contains the non-Auto-Generated text for the Auto-XML Generator in the form of Python variables.
from os.path import join
from typing import Dict

# Template file paths, from "/source/" directory
TEMPLATE_TYPE: str = join("_templates", "xml", "xml_type_auto.rst")
TEMPLATE_ROOT: str = join("_templates", "xml", "xml_root_auto.rst")

# Each type template file"s "{}"s will be replaced with the following, in order from the top of the file:
# XML Type Name
# About Section (Non-Auto)
# Root Docs Directory Name/* (Used for table of contents)
# EaW-Godot Context (Non-Auto)
# Node Name List
# SubNode Name List

# Each root template file"s "{}"s will be replaced with the following, in order from the top of the file:
# XML Type Name
# About Section (Non-Auto)
# Structure (includes given Node and SubNode descriptions)
# EaW-Godot Context (Non-Auto)

#############################
# Start About Sections
#############################
# Sections in the form of: RootNodeName/XmlTypeName: """*Insert About Text Here*""",


DESCRIPTION_TYPE: Dict[str, str] = {
	# XML Type Descriptions (About Section)
	
	# This is used when the requested key is not in the dictionary or the value is an empty string
	"default": "*Description*: This XMLType does something!",

	"GameObjectType":
		"""
	*If you want to find something that isn"t in the other XML types, it"s here... It"s all here... -luke13139*

The GameObjectType stores information related to anything the game considers and "object". This includes units, props, 
projectiles, particles, and heroes, to name a few. This XML Type accounts for more than any other XML type, and holds
more than every other XML type put together. Many RootNodes in this class contain duplicate information, but only  
Nodes/SubNodes used in a RootNode will appear under its documentation.
		""",

	"HeroClashType":
		"""
	*Probably just something about Vader HAND-ling Luke if they get into a duel. -luke13139*

Unknown, but it may contain information related to hero-on-hero battles, such as what animations to use for
lightsaber battles
		""",

	"SFXEvent":
		"""
Contains events that play sound effects. These events contain the file to play and related audio settings.
		""",

	# "TerrainDecalFX":
	# 	"""
	# 	""",

	"LightningTypeManager":
		"""
	*Palpatine may just go with plaid lightning to mix up his style, ya"know? -luke13139*
	
Unknown, but it may contain information related to the different lightning effects in the game, which include those from
abilities (such as Palpatine"s Force Lightning), weather, and ionized nebulae.
		""",

	# "DynamicTrackFX":
	# 	"""
	# 	""",

	"MusicEvent":
		"""
Contains events that play music/trigger music changes. They may loop, and only 1 music event may be active at a time 
(except while switching tracks, where the previous event can fade out while the new music fades in)
		""",

	"SpeechEvent":
		"""
	*Not sound effects, all sound effects are SFXEvents. These are SpeechEvents. Very different. -luke13139*
	
Similar to SFXEvents, but only contains voice recordings.
		""",

	"GameConstants":
		"""
Stores a variety of miscellaneous values for the game. Many of these are visual information and default settings.
		""",

	"CommandBarComponent":
		"""
Stores data for the buttons on the command bar.
		""",

	"TradeRoute":
		"""
	*Does not include lines. -luke13139*
	
Unknown, but may contain information related to the planet-to-planet hyperlane connections on the Galactic Conquest Map
		""",

	"TradeRouteLines":
		"""
	*Probably doesn"t have trade routes, but it probably does have lines! -luke13139*
	
Unknown, but may contain information related to the lines used to show hyperlanes on the Galactic Conquest Map.
		""",

	"RadarMap":
		"""
	*Why they needed a dedicated XML type for this is beyond mortal comprehension. -luke13139*

Contains some colors and textures to use for displays on the minimap. This includes the visual indicators for unit 
deaths, issued commands, and pings.
		""",

	"Draw3DTextCrawl":
		"""
	*Text?!?! Crawling?!?! -luke13139*

Unknown, but may contain information related to the in-game version of the iconic Star Wars text crawl introduction.
		""",

	"WeatherPattern":
		"""
	*Bringing out the inner meteorologist in imperial officers, rebel kamikazes, and wanted mercenaries. -luke13139*
		""",

	"HardPoint":
		"""
Stores the individual parts of larger units. May or may not be targetable and destroyable. Most weapons in space are 
fired from hardpoints, with the notable exception of fighters and other small craft.
		""",

	"Campaign":
		"""
Stores campaign information.
		""",

	"Faction":
		"""
Stores information specific to factions in the game.

Base EaW Factions:

- Rebel
- Empire
- Pirates
- Neutral
- Hostile
- Sarlacc

Base FoC Factions (Excluding EaW Factions):

- Underworld
- Hutts

		""",

	"TacticalCameraConstants":
		"""
	*Why? Shouldn"t this have been under GameConstants or just about anywhere else? Why?!?! -luke13139*

Unknown, but it may contain information related to the movements of the normal camera view, cinematic camera view, 
and/or BattleCam view.
		""",

	"LightSource":  # TODO: Remove LightSource Description joke, at some point
		"""
Lights.
		""",

	"BinkMovie":
		"""
References .BIK Movie files, giving them a name attribute which can be referenced.
		""",

	"TargetingPrioritySet":
		"""
Targeting priorities for units, used for controlling auto-targeting.
		""",

	"DifficultyAdjustment":
		"""
	*Answers the age-old question of how hard "Hard" is. -luke13139*
		""",

	"WeatherAudioManager":
		"""
	*Combine with LightningTypeManager for a realistic thunderstorm! A lightning storm... in... space? -luke13139*
		""",
}

# Default RootNodes by XML Type:
# GameObjectType: [
# 	"CIN_FighterUnits", "CIN_GroundInfantry_Units", "CIN_GroundVehicles", "CIN_Projectiles", "CIN_SpaceCorvettes",
# 	"CIN_SpaceProps", "CIN_SpaceUnitsCapital", "CIN_SpaceUnitsFrigates", "Cin_GroundProps", "Cin_GroundStructures",
#   "Cin_TransportUnits", "Containers", "EmpireGroundCompanies", "FighterUnits", "Game_Object_Files", 
#   "GenericHeroUnits", "GroundBases", "GroundBuildables", "GroundInfantry_Units", "GroundStructures", "GroundVehicles",
#   "HeroCompanies", "HeroUnits", "Indigenous_Companies", "Indigenous_Units", "LandBombingRunUnits", 
#   "LandPrimarySkydomes", "LandSecondarySkydomes", "MOV_Cinematics", "Markers", "MiscObjects", "Particles", "Planets", 
#   "Projectiles", "Prop_Forest", "Props_Desert", "Props_Generic", "Props_Snow", "Props_Story", "Props_Swamp", 
#   "Props_Temperate", "Props_Urban", "Props_Volcanic", "RebelGroundCompanies", "ScriptMarkers", "SecondaryStructures", 
#   "SpaceBuildables", "SpaceCorvettes", "SpacePrimarySkydomes", "SpaceProps", "SpaceSecondarySkydomes", 
#   "SpaceUnitsCapital", "SpaceUnitsFrigates", "SpaceUnitsSupers", "SpecialEffects", "SpecialStructures", 
#   "Squadrons", "StarBases", "TechBuildings", "TransportUnits", "UniqueUnits", "UpgradeObjects"
# ]
# HeroClashType: ["Hero_Clashes"]
# SFXEvent: ["SFXEvent_Files", "SFXEvents"]
# TerrainDecalFX: ["TerrainDecals"]
# LightningTypeManager: ["LightningEffects"]
# DynamicTrackFX: ["DynamicTracks"]
# MusicEvent: ["MusicEvents"]
# SpeechEvent: ["SpeechEvents"]
# GameConstants: ["GameConstants"]
# CommandBarComponent: ["CommandBarComponents", "CommandBar_Component_Files"]
# TradeRoute: ["TradeRoutes", "Trade_Route_Files"]
# TradeRouteLines: ["TradeRouteLines"]
# RadarMap: ["RadarMap"]
# Draw3DTextCrawl: ["StarWars3DTextScroll"]
# WeatherPattern: ["Weather_Scenarios"]
# HardPoint: ["HardPoints"]
# Campaign: ["Campaign_Files", "Campaigns", "Story", "Story_Mode_Plots"]
# Faction: ["Faction_Files", "Factions"]
# TacticalCameraConstants: ["TacticalCameras"]
# LightSource: ["LightSources"]
# BinkMovie: ["Movies"]
# TargetingPrioritySet: ["Targeting_Priority_Set_Files", "Targeting_Priority_Sets"]
# DifficultyAdjustment: ["Difficulty_Adjustments"]
# WeatherAudioManager: ["WeatherAudio"]


DESCRIPTION_ROOT: Dict[str, str] = {
	# RootNode Descriptions (About Section)
	
	# This is used when the requested key is not in the dictionary or the value is an empty string
	"default": "This is a RootNode with no description, but please feel free to give it one through GitHub!",

	# GameObjectType Roots
	"CIN_FighterUnits": "Cinematic Fighter Units",
	"CIN_GroundInfantry_Units": "Cinematic Infantry Units",
	"CIN_GroundVehicles": "Cinematic Ground Vehicle Units",
	"CIN_Projectiles": "Cinematic Projectiles",
	"CIN_SpaceCorvettes": "Cinematic Corvette-Class Units",
	"CIN_SpaceProps": "Cinematic Space Props",
	"CIN_SpaceUnitsCapital": "Cinematic Capital-Class Units",
	"CIN_SpaceUnitsFrigates": "Cinematic Frigate-Class Units",
	"Cin_GroundProps": "Cinematic Ground Props",
	"Cin_GroundStructures": "Cinematic Ground Structures",
	"Cin_TransportUnits": "Cinematic Transport Units",
	"Containers": "",
	"EmpireGroundCompanies": "",
	"FighterUnits": "",
	"Game_Object_Files": "",
	"GenericHeroUnits": "",
	"GroundBases": "",
	"GroundBuildables": "",
	"GroundInfantry_Units": "",
	"GroundStructures": "",
	"GroundVehicles": "",
	"HeroCompanies": "",
	"HeroUnits": "",
	"Indigenous_Companies": "",
	"Indigenous_Units": "",
	"LandBombingRunUnits": "",
	"LandPrimarySkydomes": "",
	"LandSecondarySkydomes": "",
	"MOV_Cinematics": "",
	"Markers": "",
	"MiscObjects": "",
	"Particles": "",
	"Planets": "",
	"Projectiles": "",
	"Prop_Forest": "",
	"Props_Desert": "",
	"Props_Generic": "",
	"Props_Snow": "",
	"Props_Story": "",
	"Props_Swamp": "",
	"Props_Temperate": "",
	"Props_Urban": "",
	"Props_Volcanic": "",
	"RebelGroundCompanies": "",
	"ScriptMarkers": "",
	"SecondaryStructures": "",
	"SpaceBuildables": "",
	"SpaceCorvettes": "",
	"SpacePrimarySkydomes": "",
	"SpaceProps": "",
	"SpaceSecondarySkydomes": "",
	"SpaceUnitsCapital": "",
	"SpaceUnitsFrigates": "",
	"SpaceUnitsSupers": "",
	"SpecialEffects": "",
	"SpecialStructures": "",
	"Squadrons": "",
	"StarBases": "",
	"TechBuildings": "",
	"TransportUnits": "",
	"UniqueUnits": "",
	"UpgradeObjects": "",

	# HeroClashType Roots
	"Hero_Clashes": "",

	# SFXEvent Roots
	"SFXEvent_Files": "",
	"SFXEvents": "",

	# TerrainDecalFX Roots
	"TerrainDecals": "",

	# LightningTypeManager Roots
	"LightningEffects": "",

	# DynamicTrackFX Roots
	"DynamicTracks": "",

	# MusicEvent Roots
	"MusicEvents": "",

	# SpeechEvent Roots
	"SpeechEvents": "",

	# GameConstants Roots
	"GameConstants": "",

	# CommandBarComponent Roots
	"CommandBarComponents": "",
	"CommandBar_Component_Files": "",

	# TradeRoute Roots
	"TradeRoutes": "",
	"Trade_Route_Files": "",

	# TradeRouteLines Roots
	"TradeRouteLines": "",

	# RadarMap Roots
	"RadarMap": "",

	# Draw3DTextCrawl Roots
	"StarWars3DTextScroll": "",

	# WeatherPattern Roots
	"Weather_Scenarios": "",

	# HardPoint Roots
	"HardPoints": "",

	# Campaign Roots
	"Campaign_Files": "",
	"Campaigns": "",
	"Story": "",
	"Story_Mode_Plots": "",

	# Faction Roots
	"Faction_Files": "",
	"Factions": "",

	# TacticalCameraConstants Roots
	"TacticalCameras": "",

	# LightSource Roots
	"LightSources": "",

	# BinkMovie Roots
	"Movies": "",

	# TargetingPrioritySet Roots:
	"Targeting_Priority_Set_Files": "",
	"Targeting_Priority_Sets": "",

	# DifficultyAdjustment Roots
	"Difficulty_Adjustments": "",

	# WeatherAudioManager Roots
	"WeatherAudio": "",

}


#############################
# End About Sections
#############################


#############################
# Start Contexts
#############################
# Sections in the form of: RootNodeName/XmlTypeName: "*Insert Context Here*",

# TODO: Add contexts
CONTEXT_TYPE: Dict[str, str] = {
	# XML Type Contexts
	
	# This is used when the requested key is not in the dictionary or the value is an empty string
	"default": "*Description*: This XMLType does something!",

	"GameObjectType":
		"""
	*If you want to find something that isn"t in the other XML types, it"s here... It"s all here... -luke13139*

The GameObjectType stores information related to anything the game considers and "object". This includes units, props, 
projectiles, particles, and heroes, to name a few. This XML Type accounts for more than any other XML type, and holds
more than every other XML type put together. Many RootNodes in this class contain duplicate information, but only  
Nodes/SubNodes used in a RootNode will appear under its documentation.
		""",

	"HeroClashType":
		"""
	*Probably just something about Vader HAND-ling Luke if they get into a duel. -luke13139*

Unknown, but it may contain information related to hero-on-hero battles, such as what animations to use for
lightsaber battles
		""",

	"SFXEvent":
		"""
Contains events that play sound effects. These events contain the file to play and related audio settings.
		""",

	# "TerrainDecalFX":
	# 	"""
	# 	""",

	"LightningTypeManager":
		"""
	*Palpatine may just go with plaid lightning to mix up his style, ya"know? -luke13139*

Unknown, but it may contain information related to the different lightning effects in the game, which include those from
abilities (such as Palpatine"s Force Lightning), weather, and ionized nebulae.
		""",

	# "DynamicTrackFX":
	# 	"""
	# 	""",

	"MusicEvent":
		"""
Contains events that play music/trigger music changes. They may loop, and only 1 music event may be active at a time 
(except while switching tracks, where the previous event can fade out while the new music fades in)
		""",

	"SpeechEvent":
		"""
	*Not sound effects, all sound effects are SFXEvents. These are SpeechEvents. Very different. -luke13139*

Similar to SFXEvents, but only contains voice recordings.
		""",

	"GameConstants":
		"""
Stores a variety of miscellaneous values for the game. Many of these are visual information and default settings.
		""",

	"CommandBarComponent":
		"""
Stores data for the buttons on the command bar.
		""",

	"TradeRoute":
		"""
	*Does not include lines. -luke13139*

Unknown, but may contain information related to the planet-to-planet hyperlane connections on the Galactic Conquest Map
		""",

	"TradeRouteLines":
		"""
	*Probably doesn"t have trade routes, but it probably does have lines! -luke13139*

Unknown, but may contain information related to the lines used to show hyperlanes on the Galactic Conquest Map.
		""",

	"RadarMap":
		"""
	*Why they needed a dedicated XML type for this is beyond mortal comprehension. -luke13139*

Contains some colors and textures to use for displays on the minimap. This includes the visual indicators for unit 
deaths, issued commands, and pings.
		""",

	"Draw3DTextCrawl":
		"""
	*Text?!?! Crawling?!?! -luke13139*

Unknown, but may contain information related to the in-game version of the iconic Star Wars text crawl introduction.
		""",

	"WeatherPattern":
		"""
	*Bringing out the inner meteorologist in imperial officers, rebel kamikazes, and wanted mercenaries. -luke13139*
		""",

	"HardPoint":
		"""
Stores the individual parts of larger units. May or may not be targetable and destroyable. Most weapons in space are 
fired from hardpoints, with the notable exception of fighters and other small craft.
		""",

	"Campaign":
		"""
Stores campaign information.
		""",

	"Faction":
		"""
Stores information specific to factions in the game.

Base EaW Factions:

- Rebel
- Empire
- Pirates
- Neutral
- Hostile
- Sarlacc

Base FoC Factions (Excluding EaW Factions):

- Underworld
- Hutts

		""",

	"TacticalCameraConstants":
		"""
	*Why? Shouldn"t this have been under GameConstants or just about anywhere else? Why?!?! -luke13139*

Unknown, but it may contain information related to the movements of the normal camera view, cinematic camera view, 
and/or BattleCam view.
		""",

	"LightSource":  # TODO: Remove LightSource Description joke, at some point
		"""
Lights.
		""",

	"BinkMovie":
		"""
References .BIK Movie files, giving them a name attribute which can be referenced.
		""",

	"TargetingPrioritySet":
		"""
Targeting priorities for units, used for controlling auto-targeting.
		""",

	"DifficultyAdjustment":
		"""
	*Answers the age-old question of how hard "Hard" is. -luke13139*
		""",

	"WeatherAudioManager":
		"""
	*Combine with LightningTypeManager for a realistic thunderstorm! A lightning storm... in... space? -luke13139*
		""",
}


# Default RootNodes by XML Type:
# GameObjectType: [
# 	"CIN_FighterUnits", "CIN_GroundInfantry_Units", "CIN_GroundVehicles", "CIN_Projectiles", "CIN_SpaceCorvettes",
# 	"CIN_SpaceProps", "CIN_SpaceUnitsCapital", "CIN_SpaceUnitsFrigates", "Cin_GroundProps", "Cin_GroundStructures",
#   "Cin_TransportUnits", "Containers", "EmpireGroundCompanies", "FighterUnits", "Game_Object_Files",
#   "GenericHeroUnits", "GroundBases", "GroundBuildables", "GroundInfantry_Units", "GroundStructures", "GroundVehicles",
#   "HeroCompanies", "HeroUnits", "Indigenous_Companies", "Indigenous_Units", "LandBombingRunUnits",
#   "LandPrimarySkydomes", "LandSecondarySkydomes", "MOV_Cinematics", "Markers", "MiscObjects", "Particles", "Planets",
#   "Projectiles", "Prop_Forest", "Props_Desert", "Props_Generic", "Props_Snow", "Props_Story", "Props_Swamp",
#   "Props_Temperate", "Props_Urban", "Props_Volcanic", "RebelGroundCompanies", "ScriptMarkers", "SecondaryStructures",
#   "SpaceBuildables", "SpaceCorvettes", "SpacePrimarySkydomes", "SpaceProps", "SpaceSecondarySkydomes",
#   "SpaceUnitsCapital", "SpaceUnitsFrigates", "SpaceUnitsSupers", "SpecialEffects", "SpecialStructures",
#   "Squadrons", "StarBases", "TechBuildings", "TransportUnits", "UniqueUnits", "UpgradeObjects"
# ]
# HeroClashType: ["Hero_Clashes"]
# SFXEvent: ["SFXEvent_Files", "SFXEvents"]
# TerrainDecalFX: ["TerrainDecals"]
# LightningTypeManager: ["LightningEffects"]
# DynamicTrackFX: ["DynamicTracks"]
# MusicEvent: ["MusicEvents"]
# SpeechEvent: ["SpeechEvents"]
# GameConstants: ["GameConstants"]
# CommandBarComponent: ["CommandBarComponents", "CommandBar_Component_Files"]
# TradeRoute: ["TradeRoutes", "Trade_Route_Files"]
# TradeRouteLines: ["TradeRouteLines"]
# RadarMap: ["RadarMap"]
# Draw3DTextCrawl: ["StarWars3DTextScroll"]
# WeatherPattern: ["Weather_Scenarios"]
# HardPoint: ["HardPoints"]
# Campaign: ["Campaign_Files", "Campaigns", "Story", "Story_Mode_Plots"]
# Faction: ["Faction_Files", "Factions"]
# TacticalCameraConstants: ["TacticalCameras"]
# LightSource: ["LightSources"]
# BinkMovie: ["Movies"]
# TargetingPrioritySet: ["Targeting_Priority_Set_Files", "Targeting_Priority_Sets"]
# DifficultyAdjustment: ["Difficulty_Adjustments"]
# WeatherAudioManager: ["WeatherAudio"]


CONTEXT_ROOT: Dict[str, str] = {
	# RootNode Contexts
	
	# This is used when the requested key is not in the dictionary or the value is an empty string
	"default": "This is a RootNode with no description, but please feel free to give it one through GitHub!",

	# GameObjectType Roots
	"CIN_FighterUnits": "Cinematic Fighter Units",
	"CIN_GroundInfantry_Units": "Cinematic Infantry Units",
	"CIN_GroundVehicles": "Cinematic Ground Vehicle Units",
	"CIN_Projectiles": "Cinematic Projectiles",
	"CIN_SpaceCorvettes": "Cinematic Corvette-Class Units",
	"CIN_SpaceProps": "Cinematic Space Props",
	"CIN_SpaceUnitsCapital": "Cinematic Capital-Class Units",
	"CIN_SpaceUnitsFrigates": "Cinematic Frigate-Class Units",
	"Cin_GroundProps": "Cinematic Ground Props",
	"Cin_GroundStructures": "Cinematic Ground Structures",
	"Cin_TransportUnits": "Cinematic Transport Units",
	"Containers": "",
	"EmpireGroundCompanies": "",
	"FighterUnits": "",
	"Game_Object_Files": "",
	"GenericHeroUnits": "",
	"GroundBases": "",
	"GroundBuildables": "",
	"GroundInfantry_Units": "",
	"GroundStructures": "",
	"GroundVehicles": "",
	"HeroCompanies": "",
	"HeroUnits": "",
	"Indigenous_Companies": "",
	"Indigenous_Units": "",
	"LandBombingRunUnits": "",
	"LandPrimarySkydomes": "",
	"LandSecondarySkydomes": "",
	"MOV_Cinematics": "",
	"Markers": "",
	"MiscObjects": "",
	"Particles": "",
	"Planets": "",
	"Projectiles": "",
	"Prop_Forest": "",
	"Props_Desert": "",
	"Props_Generic": "",
	"Props_Snow": "",
	"Props_Story": "",
	"Props_Swamp": "",
	"Props_Temperate": "",
	"Props_Urban": "",
	"Props_Volcanic": "",
	"RebelGroundCompanies": "",
	"ScriptMarkers": "",
	"SecondaryStructures": "",
	"SpaceBuildables": "",
	"SpaceCorvettes": "",
	"SpacePrimarySkydomes": "",
	"SpaceProps": "",
	"SpaceSecondarySkydomes": "",
	"SpaceUnitsCapital": "",
	"SpaceUnitsFrigates": "",
	"SpaceUnitsSupers": "",
	"SpecialEffects": "",
	"SpecialStructures": "",
	"Squadrons": "",
	"StarBases": "",
	"TechBuildings": "",
	"TransportUnits": "",
	"UniqueUnits": "",
	"UpgradeObjects": "",

	# HeroClashType Roots
	"Hero_Clashes": "",

	# SFXEvent Roots
	"SFXEvent_Files": "",
	"SFXEvents": "",

	# TerrainDecalFX Roots
	"TerrainDecals": "",

	# LightningTypeManager Roots
	"LightningEffects": "",

	# DynamicTrackFX Roots
	"DynamicTracks": "",

	# MusicEvent Roots
	"MusicEvents": "",

	# SpeechEvent Roots
	"SpeechEvents": "",

	# GameConstants Roots
	"GameConstants": "",

	# CommandBarComponent Roots
	"CommandBarComponents": "",
	"CommandBar_Component_Files": "",

	# TradeRoute Roots
	"TradeRoutes": "",
	"Trade_Route_Files": "",

	# TradeRouteLines Roots
	"TradeRouteLines": "",

	# RadarMap Roots
	"RadarMap": "",

	# Draw3DTextCrawl Roots
	"StarWars3DTextScroll": "",

	# WeatherPattern Roots
	"Weather_Scenarios": "",

	# HardPoint Roots
	"HardPoints": "",

	# Campaign Roots
	"Campaign_Files": "",
	"Campaigns": "",
	"Story": "",
	"Story_Mode_Plots": "",

	# Faction Roots
	"Faction_Files": "",
	"Factions": "",

	# TacticalCameraConstants Roots
	"TacticalCameras": "",

	# LightSource Roots
	"LightSources": "",

	# BinkMovie Roots
	"Movies": "",

	# TargetingPrioritySet Roots:
	"Targeting_Priority_Set_Files": "",
	"Targeting_Priority_Sets": "",

	# DifficultyAdjustment Roots
	"Difficulty_Adjustments": "",

	# WeatherAudioManager Roots
	"WeatherAudio": "",

}


#############################
# End Contexts
#############################


#############################
# Start Descriptions
#############################
# Sections in the form of: NodeType/SubNodeType: "*Insert Description Here*",

# Node Names by XML Type:
# GameObjectType: [
# 	"CIN_GroundInfantry", "CIN_SpaceProp", "CIN_SpaceUnit", "Cin_GroundProp", "Cin_GroundStructure", 
# 	"Cin_GroundVehicle", "Cin_Projectile", "Cin_SpaceUnit", "Cin_TransportUnit", "Container", "GenericHeroUnit", 
# 	"GroundBase", "GroundBuildable", "GroundCompany", "GroundInfantry", "GroundStructure", "GroundVehicle", 
# 	"HeroCompany", "HeroUnit", "Indigenous_Unit", "LandBombingUnit", "LandPrimarySkydome", "LandSecondarySkydome", 
# 	"MOV_Cinematic", "Marker", "MiscObject", "Particle", "Planet", "Projectile", "Prop_Desert", "Prop_Forest", 
# 	"Props_Generic", "Props_Snow", "Props_Story", "Props_Swamp", "Props_Temperate", "Props_Urban", "Props_Volcanic", 
# 	"ScriptMarker", "SecondaryStructure", "SpaceBuildable", "SpacePrimarySkydome", "SpaceProp", "SpaceSecondarySkydome", 
# 	"SpaceUnit", "SpecialEffect", "SpecialStructure", "Squadron", "StarBase", "TechBuilding", "TransportUnit", 
# 	"UniqueUnit", "UpgradeObject"
# ]
# HeroClashType: ["Hero_Clash"]
# SFXEvent: ["SFXEvent"]
# TerrainDecalFX: ["Decal"]
# LightningTypeManager: ["LightningEffect"]
# DynamicTrackFX: ["DynamicTrack"]
# MusicEvent: ["MusicEvent"]
# SpeechEvent: ["SpeechEvent"]
# GameConstants: []
# CommandBarComponent: ["CommandBarComponent"]
# TradeRoute: ["TradeRoute"]
# TradeRouteLines: ["TradeRouteLine"]
# RadarMap: ["RadarMapEvents"]
# Draw3DTextCrawl: ["TextScroll"]
# WeatherPattern: ["Weather_Scenario"]
# HardPoint: ["HardPoint"]
# Campaign: ["Campaign", "Event"]
# Faction: ["Faction"]
# TacticalCameraConstants: ["TacticalCamera"]
# LightSource: ["LightSource"]
# BinkMovie: ["Movie"]
# TargetingPrioritySet: ["Priority_Set"]
# DifficultyAdjustment: ["Difficulty_Adjustment"]
# WeatherAudioManager: []

DESCRIPTION_NODE: Dict[str, str] = {
	# Node Descriptions
	
	# This is used when the requested key is not in the dictionary or the value is an empty string
	"default": "No description currently, but please feel free to give it one through GitHub!",

	# GameObjectType Nodes
	"CIN_GroundInfantry": "",
	"CIN_SpaceProp": "",
	"CIN_SpaceUnit": "",
	"Cin_GroundProp": "",
	"Cin_GroundStructure": "", 
	"Cin_GroundVehicle": "",
	"Cin_Projectile": "",
	"Cin_SpaceUnit": "",
	"Cin_TransportUnit": "",
	"Container": "",
	"GenericHeroUnit": "", 
	"GroundBase": "",
	"GroundBuildable": "",
	"GroundCompany": "",
	"GroundInfantry": "",
	"GroundStructure": "",
	"GroundVehicle": "", 
	"HeroCompany": "",
	"HeroUnit": "",
	"Indigenous_Unit": "",
	"LandBombingUnit": "",
	"LandPrimarySkydome": "",
	"LandSecondarySkydome": "", 
	"MOV_Cinematic": "",
	"Marker": "",
	"MiscObject": "",
	"Particle": "",
	"Planet": "",
	"Projectile": "",
	"Prop_Desert": "",
	"Prop_Forest": "", 
	"Props_Generic": "",
	"Props_Snow": "",
	"Props_Story": "",
	"Props_Swamp": "",
	"Props_Temperate": "",
	"Props_Urban": "",
	"Props_Volcanic": "", 
	"ScriptMarker": "",
	"SecondaryStructure": "",
	"SpaceBuildable": "", 
	"SpacePrimarySkydome": "",
	"SpaceProp": "",
	"SpaceSecondarySkydome": "", 
	"SpaceUnit": "",
	"SpecialEffect": "",
	"SpecialStructure": "",
	"Squadron": "",
	"StarBase": "",
	"TechBuilding": "",
	"TransportUnit": "", 
	"UniqueUnit": "",
	"UpgradeObject": "",

	# HeroClashType Nodes
	"Hero_Clash": "",

	# SFXEvent Nodes
	"SFXEvent": "",

	# TerrainDecalFX Nodes
	"Decal": "",

	# LightningTypeManager Nodes
	"LightningEffect": "",

	# DynamicTrackFX Nodes
	"DynamicTrack": "",

	# MusicEvent Nodes
	"MusicEvent": "",

	# SpeechEvent Nodes
	"SpeechEvent": "",

	# GameConstants Nodes
	# N/A

	# CommandBarComponent Nodes
	"CommandBarComponent": "",

	# TradeRoute Nodes
	"TradeRoute": "",

	# TradeRouteLines Nodes
	"TradeRouteLine": "",

	# RadarMap Nodes
	"RadarMapEvents": "",

	# Draw3DTextCrawl Nodes
	"TextScroll": "",

	# WeatherPattern Nodes
	"Weather_Scenario": "",

	# HardPoint Nodes
	"HardPoint": "",

	# Campaign Nodes
	"Campaign": "",
	"Event": "",

	# Faction Nodes
	"Faction": "",

	# TacticalCameraConstants Nodes
	"TacticalCamera": "",

	# LightSource Nodes
	"LightSource": "",

	# BinkMovie Nodes
	"Movie": "",

	# TargetingPrioritySet Nodes:
	"Priority_Set": "",

	# DifficultyAdjustment Nodes
	"Difficulty_Adjustment": "",

	# WeatherAudioManager Nodes
	# N/A

}

# Default SubNodes and Attributes by XML Type:
# GameObjectType: [
# 	"Attribute - Description", "Attribute - Name", "Attribute - Subobjectlist", "AI_Combat_Power", "Activation_Style",
# 	"Additional_Population_Capacity", "Affiliation", "Air_Vehicle_Turret_Target", "Alternate_Max_Rate_Of_Turn",
# 	"Alternate_Max_Speed", "Always_Instantiate_Galactic", "Always_Spawn_In_Orbit", "Applicable_Unit_Categories",
# 	"Applicable_Unit_Types", "Apply_Y_Turret_Rotate_To_Axis", "Apply_Z_Turret_Rotate_To_Axis", "Armor_Type",
# 	"Asteroid_Damage_Hit_Particles", "Attach_To_Flagship_During_Space_Battle", "Attack_Animation_Is_Overlay",
# 	"Attack_Move_Response_Range", "Auto_Deploys", "Autonomous_Move_Extension_Vs_Attacker", "Autoresolve_Health",
# 	"Bank_Turn_Angle", "Barrel_Bone_Name", "Base_Level", "Base_Level_Available", "Base_Position",
# 	"Base_Shield_Penetration_Particle", "Begin_Turn_Towards_Distance", "Behavior", "Blob_Shadow_Below_Detail_Level",
# 	"Blob_Shadow_Bone_Name", "Blob_Shadow_Material_Name", "Blob_Shadow_Scale", "Bomb_Countdown_Seconds",
# 	"Build_Advances_Tech_Level", "Build_Can_Be_Unlocked_By_Slicer", "Build_Cost_Credits", "Build_Countdown_Text_ID",
# 	"Build_Countdown_Text_RGBA", "Build_Countdown_Timer", "Build_Initially_Locked",
# 	"Build_Limit_Current_For_All_Allies", "Build_Limit_Current_Per_Player", "Build_Limit_Lifetime_For_All_Allies",
# 	"Build_Limit_Lifetime_Per_Player", "Build_Max_Instances_Per_Planet", "Build_Music_Completed",
# 	"Build_Speech_Completed", "Build_Speech_Countdowns", "Build_Speech_Stopped", "Build_Speech_Underway",
# 	"Build_Tab_Heroes", "Build_Tab_Land_Units", "Build_Tab_Outpost", "Build_Tab_Space_Station", "Build_Tab_Space_Units",
# 	"Build_Tab_Special_Structures", "Build_Time_Reduced_By_Multiple_Factories", "Build_Time_Seconds",
# 	"Burning_Damage_Per_Second", "Cache_Crusher_Boxes", "Camera_Aligned", "CanCellStack",
# 	"Can_Be_Neutralized_By_Major_Heroes", "Can_Be_Neutralized_By_Minor_Heroes",
# 	"Can_Hyperspace_Without_Activating_Ability", "Capture_Point_Radius", "Capture_Point_Transition_Time_Seconds",
# 	"CategoryMask", "Cinematic_Anim_Blend_Seconds", "Cinematic_Anim_Index", "Cinematic_Anim_Speed",
# 	"Cinematic_Object_Only", "Collidable_By_Projectile_Dead", "Collidable_By_Projectile_Living",
# 	"Collision_Box_Modifier", "Combat_Power_Value", "Company_Transport_Unit", "Company_Units",
# 	"Conversion_Ability_Changes_To_Enemy", "Converted_To_Enemy_Die_Time_Seconds", "Create_Team", "Create_Team_Type",
# 	"Custom_Footprint_Radius", "Custom_Hard_XExtent", "Custom_Hard_XExtent_Offset", "Custom_Hard_YExtent",
# 	"Custom_Hard_YExtent_Offset", "Custom_Soft_Footprint_Radius", "Damage", "Damage_Hit_Particles", "Damage_Type",
# 	"Damaged_Smoke_Asset_Name", "Death_By_TSW_Replacements", "Death_Clone", "Death_Clone_Is_Obstacle",
# 	"Death_Explosions", "Death_Fade_Time", "Death_Leave_Hulk_Behind", "Death_Persistence_Duration",
# 	"Death_SFXEvent_Start_Die", "Dense_FOW_Reveal_Range_Multiplier", "Deploys", "Destruction_Survivors",
# 	"Effective_Radius", "Encyclopedia_Good_Against", "Encyclopedia_Text", "Encyclopedia_Unit_Class",
# 	"Encyclopedia_Vulnerable_To", "Enemy_Spawn_Text", "Energy_Capacity", "Energy_Refresh_Rate",
# 	"Evade_Detection_Chance", "Exclude_From_Distance_Fade", "Exit_Door_Angle_Degrees",
# 	"Exit_Door_Distance", "Expiration_Seconds", "File", "Fire_Category_Restrictions", "Fire_Inaccuracy_Distance",
# 	"Fires_Forward", "FormationGrouping", "FormationOrder", "FormationSpacing", "Formation_Priority",
# 	"Formation_Prority", "Friendly_Spawn_Text", "GUI_Activated_Ability_Name", "GUI_Angles", "GUI_Bounds_Scale",
# 	"GUI_Bracket_Height", "GUI_Bracket_Size", "GUI_Bracket_Width", "GUI_Distance", "GUI_Model", "GUI_Model_Name",
# 	"GUI_Offset", "GUI_Row", "GUI_Velocity", "GUI_X_Rot", "GalacticBehavior", "Galactic_Fleet_Override_Icon_Index",
# 	"Galactic_Fleet_Override_Model_Name", "Galactic_Model_Name", "Galactic_Position", "Ground_Infantry_Turret_Target",
# 	"Ground_Vehicle_Turret_Target", "Guard_Chase_Range", "HardPoints", "Hardpoints", "Has_Land_Evaluator",
# 	"Has_Pre_Turn_Anim", "Has_Space_Evaluator", "Heal_Amount", "Heal_Interval_In_Secs", "Heal_Percent", "Heal_Range",
# 	"Highlight_Blob_Material_Name", "Hover_Offset", "Hyperspace", "Hyperspace_Speed", "Icon_Name",
# 	"Idle_Anim_00_Rate_Mod", "Idle_Chase_Range", "Immune_To_Damage", "In_Background", "Influences_Capture_Point",
# 	"Initial_State_Visible_Under_FOW", "IsBuildable", "Is_Affected_By_Gravity_Control_Field", "Is_Bomber",
# 	"Is_Branched_Map_Discardable", "Is_Combustible", "Is_Community_Property", "Is_Decoration", "Is_Discardable",
# 	"Is_Dummy", "Is_Editor_Placed", "Is_Escort", "Is_Generic_Hero", "Is_Marker", "Is_Named_Hero", "Is_Pulsing",
# 	"Is_Special_Weapon_In_Space", "Is_Sprite", "Is_Squashable", "Is_Squashable_By_Supercrusher", "Is_Stealth_Company",
# 	"Is_Supercrusher", "Is_Visible_On_Radar", "LOD_Bias", "LandBehavior", "Land_Damage_Alternates", "Land_Damage_SFX",
# 	"Land_Damage_Thresholds", "Land_FOW_Reveal_Range", "Land_Model_Anim_Override_Name", "Land_Model_Name",
# 	"Land_Victory_Relevant", "Landing_Transport_Variant", "Last_State_Visible_Under_FOW", "LateralAcceleration",
# 	"Layer_Z_Adjust", "Locomotor_Has_Animation_Priority", "Loop_Idle_Anim_00", "Lua_Script", "MP_Encyclopedia_Text",
# 	"Maintenance_Cost", "Mass", "MaxFacingLookAheadFrames", "Max_Distance_From_Spawner", "Max_Ground_Base", "Max_Lift",
# 	"Max_Num_Spawned_Objects", "Max_Number_Of_Pulses", "Max_Rate_Of_Roll", "Max_Rate_Of_Turn", "Max_Space_Base",
# 	"Max_Speed", "Max_Squad_Size", "Max_Thrust", "Maximum_Destruction_Survivor_Count", "Min_Speed",
# 	"Min_Speed_Fraction_For_Turn", "MinimumPushReturnDistance", "Minimum_Destruction_Survivor_Count",
# 	"Minimum_Follow_Distance", "Mod_Multiplier", "Mouse_Collide_Override_Sphere_Radius", "MovementBoxExpansionFactor",
# 	"MovementClass", "MovementPredictionInterval", "Movement_Animation_Speed", "Movie_Object", "Multisample_FOW_Check",
# 	"Name_Adjust", "Neutralization_Cost", "Next_Level_Base", "Next_Upgrade_Level_Type", "No_Colorization_Color",
# 	"No_Reflection_Below_Detail_Level", "No_Refraction_Below_Detail_Level", "Number_per_Squadron", "Obstacle_Height",
# 	"Obstacle_Width", "Obstacle_X_Offset", "Obstacle_Y_Offset", "Occlusion_Silhouette_Enabled", "OccupationStyle",
# 	"On_Fire_Speed_Modifier", "Out_Of_Combat_Defense_Adjustment", "Overall_Length", "Overall_Width",
# 	"OverrideAcceleration", "OverrideDeceleration", "Owner_Attachment_Bone", "Owner_Light_Effect_Color",
# 	"Owner_Light_Effect_Color2", "Owner_Light_Effect_Duration", "Owner_Light_Effect_Pulse_Count",
# 	"Owner_Light_Effect_Type", "Owner_Particle_Bone_Name", "Ownership_Sticks", "Particle_Effect",
# 	"Particle_Lifetime_Frames", "Pause_During_Cinematic_Anim", "Planet_Credit_Value", "Play_SFXEvent_On_Sighting",
# 	"Political_Control", "Political_Faction", "Population_Value", "Pre_Lit", "Prepare_Strafe_Height", "Prev_Level_Base",
# 	"Prevents_Blockade_Run_Attrition", "Prevents_Story_Campaign_Autoresolve", "Previous_Upgrade_Level_Type",
# 	"Primary_Locomotor_Name", "Projectile_Absorbed_By_Shields_Particle", "Projectile_Appearance_Delay_Frames",
# 	"Projectile_Category", "Projectile_Custom_Render", "Projectile_Damage", "Projectile_Does_Energy_Damage",
# 	"Projectile_Does_Hitpoint_Damage", "Projectile_Does_Shield_Damage", "Projectile_Fire_Pulse_Count",
# 	"Projectile_Fire_Pulse_Delay_Seconds", "Projectile_Fire_Recharge_Seconds", "Projectile_Ground_Detonation_Particle",
# 	"Projectile_Ground_Detonation_SurfaceFX", "Projectile_Length", "Projectile_Lifetime_Detonation_Particle",
# 	"Projectile_Max_Flight_Distance", "Projectile_Max_Scan_Range",
# 	"Projectile_Object_Armor_Reduced_Detonation_Particle", "Projectile_Object_Detonation_Particle",
# 	"Projectile_SFXEvent_Detonate_Reduced_By_Armor", "Projectile_Types", "Projectile_Width", "Property_Flags",
# 	"Pulse_Frequency_Secs", "Radar_Clip_To_Visible_Region", "Radar_Icon_Name", "Radar_Icon_Scale_Land",
# 	"Radar_Icon_Scale_Space", "Radar_Icon_Size", "Radar_Register_As_Foreground_Object", "Ranged_Target_Z_Adjust",
# 	"Ranking_In_Category", "Recharge_Seconds", "Reinforcement_Prevention_Radius", "Remove_Upon_Death",
# 	"Required_Ground_Base_Level", "Required_Planets", "Required_Special_Structures", "Required_Star_Base_Level",
# 	"Required_Timeline", "Reserve_Spawned_Units_Tech_0", "Retreat_Self_Destruct_Explosion", "Reveal_During_Setup_Phase",
# 	"Reveal_During_Setup_Phase_Only", "Reveal_For_Attacker", "Rotation_Animation_Speed", "SFXEvent_Ambient_Loop",
# 	"SFXEvent_Ambient_Moving", "SFXEvent_Ambient_Moving_Max_Delay_Seconds", "SFXEvent_Ambient_Moving_Min_Delay_Seconds",
# 	"SFXEvent_Assist_Attack", "SFXEvent_Assist_Move", "SFXEvent_Attack", "SFXEvent_Attack_Hardpoint",
# 	"SFXEvent_Barrage", "SFXEvent_Bomb_Run_Incoming", "SFXEvent_Bomb_Run_Select_Target", "SFXEvent_Build_Cancelled",
# 	"SFXEvent_Build_Complete", "SFXEvent_Build_Started", "SFXEvent_Damaged_By_Asteroid", "SFXEvent_Deploy",
# 	"SFXEvent_Enemy_Damaged_Health_Critical_Warning", "SFXEvent_Enemy_Damaged_Health_Low_Warning",
# 	"SFXEvent_Engine_Cinematic_Focus_Loop", "SFXEvent_Engine_Idle_Loop", "SFXEvent_Engine_Moving_Loop", "SFXEvent_Fire",
# 	"SFXEvent_Fleet_Move", "SFXEvent_GUI_Unit_Ability_Activated", "SFXEvent_GUI_Unit_Ability_Deactivated",
# 	"SFXEvent_Group_Attack", "SFXEvent_Group_Move", "SFXEvent_Guard", "SFXEvent_Hardpoint_All_Weapons_Destroyed",
# 	"SFXEvent_Hardpoint_Destroyed", "SFXEvent_Health_Critical_Warning", "SFXEvent_Health_Low_Warning", "SFXEvent_Move",
# 	"SFXEvent_Move_Into_Asteroid_Field", "SFXEvent_Move_Into_Nebula", "SFXEvent_Select",
# 	"SFXEvent_Special_Ability_Loop", "SFXEvent_Special_Weapon_Ready", "SFXEvent_Stop",
# 	"SFXEvent_Tactical_Build_Cancelled", "SFXEvent_Tactical_Build_Complete", "SFXEvent_Tactical_Build_Started",
# 	"SFXEvent_Target_Ability", "SFXEvent_Target_Affected", "SFXEvent_Turret_Rotating_Loop", "SFXEvent_Unit_Lost",
# 	"SFXEvent_Unit_Under_Attack", "Scale_Factor", "Score_Cost_Credits", "Secondary_Locomotor_Name",
# 	"Secondary_Objective", "Select_Box_Scale", "Select_Box_Z_Adjust", "Selection_Blob_Material_Name", "Sensor_Range",
# 	"Shield_Armor_Type", "Shield_Hit_Particles", "Shield_Points", "Shield_Refresh_Rate", "Ship_Class",
# 	"Show_In_Sidebar_When_Complete", "Show_In_Sidebar_While_Building", "Show_Name", "Single_Target_Heal", "Size_Value",
# 	"Slice_Cost_Credits", "Sort_Order_Adjust", "SpaceAutoResolveStunRate", "SpaceBehavior", "Space_Escort_Unit_Types",
# 	"Space_FOW_Reveal_Range", "Space_Full_Stop_Command", "Space_Layer", "Space_Model_Name", "Space_Obstacle_Offset",
# 	"Space_Override_Population_Value", "Space_Victory_Relevant", "Spawn_Indigenous_Units_Chance",
# 	"Spawn_Indigenous_Units_In_Packs", "Spawn_Indigenous_Units_Radius", "Spawned_Indigenous_Pack_Type",
# 	"Spawned_Indigenous_Units_Delay_Seconds", "Spawned_Indigenous_Units_Quantity", "Spawned_Indigenous_Units_Type",
# 	"Spawned_Object_Type", "Spawned_Squadron_Delay_Seconds", "Special_Structures", "Special_Weapon_Index",
# 	"Special_Weapon_Target_Action_Index", "Special_Weapon_Valid_Targets", "Spin_Away_On_Death",
# 	"Spin_Away_On_Death_Chance", "Spin_Away_On_Death_Explosion", "Spin_Away_On_Death_SFXEvent_Start_Die",
# 	"Spin_Away_On_Death_Time", "Squadron_Capacity", "Squadron_Formation_Error_Tolerance", "Squadron_Offsets",
# 	"Squadron_Units", "Starting_Spawned_Units_Tech_0", "Stay_In_Transport_During_Ground_Battle", "Stealth_Capable",
# 	"Stopped_Rate_Of_Turn", "Strafe_Distance", "SurfaceFX_Name", "Surface_Type_Cover_Damage_Shield",
# 	"TSW_Attack_Anim_Duration_Seconds", "TSW_Attack_Distance_From_Target", "TSW_Explosion_Debris_Creation_Frame_Delay",
# 	"TSW_MusicEvent_Activation_Start", "TSW_Post_Destruction_Wait_Frames", "TSW_Post_Music_Wait_Frames",
# 	"TSW_Power_Up_Countdown_Seconds", "TSW_SFXEvent_Activate_Voice", "TSW_SFXEvent_GUI_Bttton_Press",
# 	"TSW_SFXEvent_Weapon_Power_Up", "TSW_Start_Distance_From_Target", "TSW_Start_Pos_Match_Targets_Z",
# 	"TSW_Z_Adjust_Relative_To_Target_Pos", "TacticalBehavior", "Tactical_Additional_Structure_Type",
# 	"Tactical_Build_Cost_Campaign", "Tactical_Build_Cost_Multiplayer", "Tactical_Build_Prerequisites",
# 	"Tactical_Build_Time_Seconds", "Tactical_Buildable_Objects_Campaign", "Tactical_Buildable_Objects_Multiplayer",
# 	"Tactical_Health", "Tactical_Production_Queue", "Target_Bones", "Target_Particle_Bone_Name",
# 	"Target_Particle_Effect", "Target_Types", "Targeting_Allowed_When_Burning", "Targeting_Fire_Inaccuracy",
# 	"Targeting_Max_Attack_Distance", "Targeting_Min_Attack_Distance", "Targeting_Priority_Set", "Targeting_Scan_Range",
# 	"Targeting_Stickiness_Time_Threshold", "Tech_Level", "Terrain", "Text_ID", "Transport_Capacity", "Turret_Bone_Name",
# 	"Turret_Elevate_Extent_Degrees", "Turret_Rotate_Extent_Degrees", "Turret_Rotate_Speed",
# 	"Turret_Targets_Air_Vehicles", "Turret_Targets_Anything_Else", "Turret_Targets_Ground_Infantry",
# 	"Turret_Targets_Ground_Vehicles", "Type", "UnitCollisionClass", "Use_Special_Submit_Rules", "User_Bound_Max",
# 	"User_Bound_Min", "Uses_Multiple_Locomotors", "Variant_Of_Existing_Type", "Vehicle_Thief_Inside_Clone",
# 	"Victory_Relevant", "Visible_On_Radar_When_Fogged", "Visible_To_Enemies_When_Empty", "Walk_Transition",
# 	"Weapon_Quantity", "Weapon_Type", "Weather_Category", "Wind_Disturbance_Radius", "Wind_Disturbance_Sphere_Alpha",
# 	"Wind_Disturbance_Strength"
# ]
#
# HeroClashType: [
# 	"Attribute - Name", "Clash_Range", "Clash_Type", "Combat_Distance", "Damage_Amount", "Damage_Percentage",
# 	"First_Hero_Conversation_Anim_Type", "First_Hero_Damage_Multiplier", "First_Hero_Draw_Anim_Type",
# 	"First_Hero_Lose_Anim_Type", "First_Hero_Type", "First_Hero_Win_Anim_Type", "First_Hero_Win_Exchange_Chance",
# 	"First_Hero_Win_Speech", "Involved_Hero_Types", "Play_Conversation_Events", "Second_Hero_Conversation_Anim_Type",
# 	"Second_Hero_Damage_Multiplier", "Second_Hero_Draw_Anim_Type", "Second_Hero_Lose_Anim_Type", "Second_Hero_Type",
# 	"Second_Hero_Win_Anim_Type", "Second_Hero_Win_Exchange_Chance", "Second_Hero_Win_Speech"
# ]
#
# SFXEvent: [
# 	"Attribute - Name", "Chained_SFXEvent", "File", "Is_2D", "Is_3D", "Is_GUI", "Is_Preset", "Localize",
# 	"Max_Instances", "Max_Pitch", "Max_Predelay", "Max_Volume", "Min_Pitch", "Min_Predelay", "Min_Volume",
# 	"Overlap_Test", "Play_Count", "Play_Sequentially", "Priority", "Probability", "Samples", "Text_ID",
# 	"Use_Preset", "Volume_Saturation_Distance"
# ]
#
# TerrainDecalFX: [
# 	"Attribute - Name", "Category", "Fadeout_Time", "Intensity", "Permanent", "Render_Mode", "Scale", "UV_Slot",
# 	"Z_Angle"
# ]
#
# LightningTypeManager: [
# 	"Attribute - Name", "Bolt_Creation_Interval_Max", "Bolt_Creation_Interval_Min", "Color_End", "Color_Start",
# 	"Detail", "Displace", "Fadeout_Time_Max", "Fadeout_Time_Min", "Number_Bolts", "Texture_Name", "Texture_Repeat",
# 	"Texture_Scroll", "Width_Max", "Width_Min"
# ]
#
# DynamicTrackFX: ["Attribute - Name", "Render_Mode", "fade_begin_distance", "fade_distance_per_second",
# 	"fade_end_distance", "min_geometry_lod", "opacity", "segment_length", "texture_name", "width"
# ]
#
# MusicEvent: ["Attribute - Name", "Fade_In_Seconds", "Fade_Out_Previous_Seconds", "Files", "Loop", "Volume_Percent"]
# SpeechEvent: ["Attribute - Name", "Files", "Text_ID", "Volume_Percent"]
# GameConstants: [
# 	"AITechLevelProductionTimeWeight", "AIUsesFogOfWarGalactic", "AIUsesFogOfWarLand", "AIUsesFogOfWarSpace",
# 	"AI_BuildTaskReservationSeconds", "AI_FogCellsPerThreatCell", "AI_LandAreaThreatScaleFactor",
# 	"AI_LandEvaluatorRegionSize", "AI_LandThreatDistanceFactor", "AI_LandThreatLookAheadTime",
# 	"AI_LandThreatTurnRateFactor", "AI_SpaceAreaThreatScaleFactor", "AI_SpaceEvaluatorRegionSize",
# 	"AI_SpaceThreatDecayStep", "AI_SpaceThreatDistanceFactor", "AI_SpaceThreatLookAheadTime",
# 	"AI_SpaceThreatTurnRateFactor", "Activated_Destroy_Planet_Ability_Names", "Activated_Neutralize_Hero_Ability_Names",
# 	"Activated_Sabotage_Ability_Names", "Activated_Siphon_Credits_Ability_Names", "Activated_Slice_Ability_Names",
# 	"Activated_System_Spy_Ability_Names", "Advisor_Hint_Duration", "Advisor_Hint_Interval",
# 	"Allow_Reinforcement_Percentage_Normalized", "AlwaysBypassAutoResolve", "Animate_During_Galactic_Mode_Pause",
# 	"ApproximationForwardDistance", "ApproximationSmoothCosAngle", "Armor_Types", "Asteroid_Field_Damage",
# 	"Asteroid_Field_Damage_Rate", "AutoResolveAttritionAllowanceFactor", "AutoResolveDisplayTime",
# 	"AutoResolveLoserAttrition", "AutoResolveTransportLosses", "AutoResolveVoteDefaultTimeOut",
# 	"AutoResolveVoteDefaultToTactical", "AutoResolveWinnerAttrition", "Auto_Resolve_Tactical_Multiplier",
# 	"Auto_Rotate_For_Space_Targeting", "AutomaticAutoResolve", "Base_Land_Targeting_Arc_Angle_Coefficient",
# 	"Base_Shield_Delay_Time", "Base_Shield_Speed_Modifier", "Base_Shield_Vulnerability_Modifier",
# 	"Battle_Load_Planet_Ambient", "Battle_Load_Planet_Direction", "Battle_Load_Planet_Viewport",
# 	"Battle_Pending_Message_Color", "Battle_Pending_Message_Font", "Battle_Pending_Message_Font_Size",
# 	"Battle_Pending_Message_Pos_X", "Battle_Pending_Message_Pos_Y", "Battle_Pending_Timeout_Seconds",
# 	"BeaconPlaceDelay", "BetweenFormationSpacing", "Bink_Player_Caption_Font_Name", "Bink_Player_Caption_Font_Size",
# 	"Black_Market_Income_Mult_Max", "Black_Market_Income_Mult_Min", "Blockade_Run_Attrition_Factor",
# 	"Bombing_Run_Reduction_Per_Squadron_Percent", "CB_Flash_Count", "CB_Flash_Duration", "CB_Movie_Color",
# 	"CB_Movie_Offset", "Camera_FX_Manager_Letterbox_Height", "Camera_Stop_Left", "Camera_Stop_Right",
# 	"Camera_Z_Position", "CloseEnoughAngleForMoveStart", "Command_Bar_Default_Font_Name",
# 	"Command_Bar_Default_Font_Size", "Control_Point_Domination_Victory_Time_In_Secs", "Countdowns_Font_Name",
# 	"Countdowns_Font_Size", "Credit_Cap_Per_Planet", "Credits_Bottom_Color", "Credits_Display_Font_Name",
# 	"Credits_Display_Font_Size", "Credits_Font", "Credits_Font_Size", "Credits_Header_Bottom_Color",
# 	"Credits_Header_Top_Color", "Credits_Logo_1_Height", "Credits_Logo_1_Name", "Credits_Logo_1_Width",
# 	"Credits_Logo_1_Y_Offset", "Credits_Logo_2_Height", "Credits_Logo_2_Name", "Credits_Logo_2_Width",
# 	"Credits_Logo_2_Y_Offset", "Credits_Logo_3_Height", "Credits_Logo_3_Name", "Credits_Logo_3_Width",
# 	"Credits_Logo_3_Y_Offset", "Credits_Margin", "Credits_Scroll_Rate", "Credits_Spacing", "Credits_Top_Color",
# 	"CrouchIdleWalkBlendTime", "CrouchMoveBlendTime", "Crouch_Move_Fire_Angle_Cutoff",
# 	"CurrentPathCostCoefficientSpace", "Damage_To_Armor_Mod", "Damage_Types", "Default_Defense_Adjust",
# 	"Default_Hero_Respawn_Time", "Demo_Attract_Map_Cycle_Delay_Seconds", "Demo_Attract_Maps",
# 	"Demo_Attract_Start_Timeout_Seconds", "Depleted_Shield_Damage_Increment", "Depleted_Shield_Disable_Time",
# 	"Depleted_Shield_Regen_Cap", "DesiredLandFOWCellSize", "DesiredSpaceFOWCellSize",
# 	"DestinationSearchRadiusIncrementSpace", "Destination_Collision_Query_Extension", "Diminishing_Firepower",
# 	"Display_Bink_Movie_Frames", "Distribute_Credit_Quantum", "DoubleClickMoveMaxSpeedRatio", "Droid_Date_Color",
# 	"Droid_Encyclopedia_Offset", "Droid_Seperator_Color", "Droid_Text_Color", "DynamicAvoidanceRectangleBound",
# 	"DynamicLandComplexityQuota", "DynamicLandQuotaResetInterval", "DynamicObstacleOverlapPenalty",
# 	"Earthquake_Shake_Magnitude", "Earthquake_Shake_Speed", "Earthquake_Transition_Time",
# 	"Elevated_Vulnerability_Duration", "Elevated_Vulnerability_Factor", "Encyclopedia_Class_Y_Offset",
# 	"Encyclopedia_Cost_Offset", "Encyclopedia_Delay", "Encyclopedia_Fade_Rate", "Encyclopedia_Icon_X_Offset",
# 	"Encyclopedia_Icon_Y_Offset", "Encyclopedia_Min_Display_Time", "Encyclopedia_Name_Offset",
# 	"Encyclopedia_Population_Offset", "Enemy_Color", "EnergyRechargeIntervalInSecs", "EnergyToShieldExchangeRate",
# 	"Energy_Beam_Color", "Energy_Beam_Frames", "Energy_Beam_Texture", "Energy_Beam_Width",
# 	"Engines_Disabled_Speed_Modifier", "Event_Message_Default_Font_Name", "Event_Message_Default_Font_Size",
# 	"Evil_Side_Leader_Name", "Evil_Side_Name", "FinalFacing180Penalty", "FinalFormationFacingDeltaCoefficient",
# 	"FinalFormationFacingMinimumAngle", "Fiscal_Cycle_Time_In_Secs", "Fleeing_Infantry_Speed_Bonus",
# 	"Fleet_Hyperspace_Band_Texture_Name", "Fleet_Maintenance_Update_Delay_Seconds", "Fleet_Movement_Line_Texture_Name",
# 	"FormationMaximumSideError", "FormationMinimumSideError", "FramesPerCollisionCheck",
# 	"FramesPerPositionApproximationRebuild", "GMC_Battle_Fade_Time", "GMC_Battle_Zoom_Time",
# 	"GMC_InitialPitchAngleDegrees", "GMC_InitialPullbackDistance", "GMC_ZoomTime", "GMC_ZoomedPitchAngleDegrees",
# 	"GMC_ZoomedPositionOffsetPlanetRadiusFractions", "GMC_ZoomedPullbackPlanetRadiusFraction",
# 	"GUI_Attack_Move_Command_Ack_Effect", "GUI_Attack_Movement_Click_Radar_Event_Name", "GUI_Cycle_Color",
# 	"GUI_Cycle_Speed", "GUI_Darken_Level", "GUI_Double_Click_Move_Command_Ack_Effect", "GUI_Flash_Duration",
# 	"GUI_Flash_Level", "GUI_Guard_Move_Command_Ack_Effect", "GUI_Hilite_Level", "GUI_Move_Acknowledge_Scale_Land",
# 	"GUI_Move_Acknowledge_Scale_Space", "GUI_Move_Command_Ack_Effect", "GUI_Movement_Click_Radar_Event_Name",
# 	"GUI_Movement_Double_Click_Radar_Event_Name", "GUI_Planet_Fade_Duration", "GUI_Planet_Flash_Level",
# 	"GUI_Rapid_Flash_Duration", "GUI_Strategic_Countdown_Timers_Screen_Spacing",
# 	"GUI_Strategic_Countdown_Timers_Screen_X", "GUI_Strategic_Countdown_Timers_Screen_Y",
# 	"GUI_Tactical_Countdown_Timers_Screen_Spacing", "GUI_Tactical_Countdown_Timers_Screen_X",
# 	"GUI_Tactical_Countdown_Timers_Screen_Y", "Galactic_Right_Button_Scroll_Speed_Factor",
# 	"Galactic_Scroll_Plane", "Galactic_Zoom_Acceleration", "Galactic_Zoom_In_Light_Angle",
# 	"Galactic_Zoom_In_Station_Offset", "Galactic_Zoom_In_Station_Rotation", "Galactic_Zoom_Light_Level",
# 	"Galactic_Zoom_Out_Light_Angle", "Game_Object_Name_Font_Name", "Game_Object_Name_Font_Size",
# 	"Game_Scoring_Script_Name", "Good_Ground_Color_Tint", "Good_Side_Leader_Name", "Good_Side_Name",
# 	"GripperCombatGridSnapDistance", "HardPoint_Target_Reticle_Enemy_Screen_Size",
# 	"HardPoint_Target_Reticle_Enemy_Texture", "HardPoint_Target_Reticle_Enemy_Tracked_Texture",
# 	"HardPoint_Target_Reticle_Friendly_Disabled_Texture", "HardPoint_Target_Reticle_Friendly_Disabled_Tracked_Texture",
# 	"HardPoint_Target_Reticle_Friendly_Repairing_Texture", "HardPoint_Target_Reticle_Friendly_Screen_Size",
# 	"HardPoint_Target_Reticle_Friendly_Texture", "HardPoint_Target_Reticle_Friendly_Tracked_Texture",
# 	"Hardpoint_Recharge_Cutoff_For_Opportunity_Fire", "Health_Bar_Scale", "Health_Bar_Spacing",
# 	"Health_Critical_Percent_Threshold", "Health_Low_Percent_Threshold", "High_Threat_Reachability_Tolerance",
# 	"Hint_Text_Color", "Hull_Vs_Hard_Points_Health_Constraint", "Icons_Per_Column", "IdleMovementFrames",
# 	"IdleWalkBlendTime", "In_Game_Cinematics", "In_Game_Message_Default_Font_Name", "In_Game_Message_Default_Font_Size",
# 	"Income_Redistribution", "Indigenous_Spawn_Destruction_Reward", "InfantryFormationRecruitmentDistance",
# 	"InfantryTurnBlendTime", "Ion_Storm_Shield_Disable_Time", "Japanese_Line_Percent", "Japanese_ST_Line_Percent",
# 	"LandDestinationProximity", "LandFOWColor", "LandFOWRegrowTime", "LandObjectTrackingInterval",
# 	"LandObjectTrackingTreeCount", "LandPredictionTimeInterval", "LandTemporaryDestinationProximity",
# 	"LandWaitOperatorSpeedCoefficient", "Land_Auto_Resolve_Delay_Seconds", "Land_Base_Destruction_Forces_Retreat",
# 	"Land_Capture_Allowed_Countdown_Seconds", "Land_Collidable_Grid_Cull_Size", "Land_Guard_Range",
# 	"Land_Health_Bar_Scale", "Land_Retreat_Allowed_Countdown_Seconds", "Land_Retreat_Attrition_Factor",
# 	"Land_Tactical_Camera_Locked", "Large_Coin_Stack_Size", "Laser_Beam_Z_Scale_Factor", "Laser_Kite_Z_Scale_Factor",
# 	"Left_Queue_Tint", "Localized_Menu_Overlay", "Localized_Splash_Screen", "Localized_UK_English_Splash_Screen",
# 	"Long_Encyclopedia_Delay", "LoopWaypointLineTextureName", "Lose_Message_Color", "Low_Threat_Reachability_Tolerance",
# 	"MP_Color_Blue", "MP_Color_Cyan", "MP_Color_Gray", "MP_Color_Green", "MP_Color_Orange", "MP_Color_Purple",
# 	"MP_Color_Red", "MP_Color_Yellow", "MP_Default_Allow_Auto_Resolve", "MP_Default_Allow_Heroes",
# 	"MP_Default_Allow_Random_Events", "MP_Default_Allow_SuperWeapons", "MP_Default_Credits",
# 	"MP_Default_Free_Starting_Units", "MP_Default_Game_Timer", "MP_Default_Land_Tactical_Win_Condition",
# 	"MP_Default_Max_Tech_Level", "MP_Default_Pre_Built_Base", "MP_Default_Space_Tactical_Win_Condition",
# 	"MP_Default_Start_Tech_Level", "MP_Default_Win_Condition", "MP_Default_Win_Condition_Float_Param", "
# 	MP_Default_Win_Condition_Int_Param", "Main_Menu_Demo_Attract_Mode", "Map_Preview_Image_Size",
# 	"MatchFacingDeltaSpace", "MaxCombatAccuracyAlignmentBonus", "MaxCombatDamageAlignmentBonus",
# 	"MaxCombatSensorRangeAlignmentBonus", "MaxCreditIncomeAlignmentBonus", "MaxCreditIncomeAlignmentPenalty",
# 	"MaxInfluenceTransitionAlignmentBonus", "MaxInfluenceTransitionAlignmentPenalty", "MaxLandFormationFormupFrames",
# 	"MaxObstacleCostLand", "MaxObstacleCostSpace", "MaxRotationsSpace", "MaxWaypointsPerPath",
# 	"Max_Bombing_Run_Interval_Seconds", "Max_Formation_Area", "Max_Galactic_Zoom_Distance", "Max_Galactic_Zoom_Speed",
# 	"Max_Ground_Forces_On_Planet", "Max_Move_Frame_Delay", "Max_Skirmish_Credits", "MaximumFleetMovementDistance",
# 	"MaximumGroundbaseLevel", "MaximumPoliticalControl", "MaximumSpecialStructures", "MaximumSpecialStructuresLand",
# 	"MaximumSpecialStructuresSpace", "MaximumStarbaseLevel", "Medium_Coin_Stack_Size",
# 	"Medium_Threat_Reachability_Tolerance", "Melee_Cutoff_Range", "Message_Of_The_Day_URL", "MinLandPredictionDistance",
# 	"MinObstacleCostLand", "MinObstacleCostSpace", "Min_Accuracy_For_Icon", "Min_Bombing_Run_Interval_Seconds",
# 	"Min_Galactic_Zoom_Speed", "Min_Health_Bar_Scale", "Min_Sight_Range_For_Icon", "Min_Skirmish_Credits",
# 	"MinimumDragDistance", "MinimumDragSelectDistance", "MinimumStoppedVsStoppedOverlapCoefficient",
# 	"Minimum_Tactical_Overrun_Time_In_Secs", "Mouse_Over_Highlight_Scale", "MoveBlendTime",
# 	"MovementReevaluationFrameCount", "MovingVsMovingLookAheadTime", "Multiplayer_Losing_Team_Bonus_Credit_Percentage",
# 	"Nebula_Ability_Disable_Time", "Nebula_Effect_Color", "Neutral_UI_Color", "Num_Structures_For_Large_Planet_Name",
# 	"Num_Structures_For_Medium_Planet_Name", "Object_Max_Health_Multiplier_Land", "Object_Max_Health_Multiplier_Space",
# 	"Object_Max_Speed_Multiplier_Galactic", "Object_Max_Speed_Multiplier_Land", "Object_Max_Speed_Multiplier_Space",
# 	"Object_Visual_Status_Particle_Attach_Bone_Names", "ObstacleAreaOverlapForMaxSpace", "Occlusion_Silhouettes_Enabled",
# 	"OccupationRadiusCoefficientSpace", "OffMapCostPenalty", "Override_Death_Persistence_Duration", "Pay_As_You_Go",
# 	"Planet_Ability_Icon_Names", "Planet_Ability_RGBs", "Planet_Ability_Text_IDs", "Planet_Reveal_Delay_Time",
# 	"PlayModeSwitchMovies", "Player_Color", "Political_Control_Change_Time_Seconds", "Political_Income_Curve",
# 	"Preferred_Pathfinder_Types", "Production_Speed_Factor", "Production_Speed_Mod_Base_Vs_Tech_0",
# 	"Production_Speed_Mod_Base_Vs_Tech_1", "Production_Speed_Mod_Base_Vs_Tech_2", "Production_Speed_Mod_Base_Vs_Tech_3",
# 	"Production_Speed_Mod_Base_Vs_Tech_4", "Progressive_Taxation", "Push_Scroll_Speed_Modifier",
# 	"Quickmatch_Map_Exclusion_List", "Radar_Colorize_Multiplayer_Enemy", "Radar_Colorize_Selected_Units",
# 	"Radar_Multiplayer_Enemy_Color", "Radar_Selected_Units_Color", "Raid_Force_Free_Object_Category_Mask",
# 	"Raid_Force_Limited_Object_Category_Mask", "Raid_Force_Max_Heros", "Raid_Force_Max_Limited_Objects",
# 	"Raid_Force_Required_Faction", "Random_Story_Empire_Construction", "Random_Story_Empire_Destroy",
# 	"Random_Story_Max_Triggers", "Random_Story_Rebel_Construction", "Random_Story_Rebel_Destroy",
# 	"Random_Story_Reward_Empire_Buildable", "Random_Story_Reward_Empire_Unit", "Random_Story_Reward_Rebel_Buildable",
# 	"Random_Story_Reward_Rebel_Unit", "Random_Story_Rewards", "Random_Story_Triggers", "ReinforcementOverlayBadColor",
# 	"ReinforcementOverlayGoodColor", "RepushDistance", "RetreatAutoResolveLoserAttrition",
# 	"RetreatAutoResolveWinnerAttrition", "Right_Queue_Tint", "Rotate_Formation_Facing_Moves", "Saliency_Health",
# 	"Saliency_Power", "Saliency_Size", "Saliency_Speed", "Saliency_Targets", "Saliency_X", "Saliency_Y",
# 	"Scroll_Acceleration_Factor", "Scroll_Deceleration_Factor", "SetupPhaseCountdownSeconds", "SetupPhaseEnabled",
# 	"SetupPhaseFOWColor", "SetupPhaseInvalidDragColor", "ShieldRechargeIntervalInSecs", "Shield_Flash_Duration",
# 	"Shield_Flash_Scale", "ShipNameTextFiles", "Ships_Per_Stack", "Short_Range_Attack_Formation_Coefficient",
# 	"ShouldDisplayPotentialPath", "ShouldDisplayPredictionPaths", "ShouldDisplaySyncedPaths",
# 	"ShouldInfantryTeamsSplitAcrossFormations", "ShouldSkipLandFormup", "ShouldUseSpaceIdleMovement",
# 	"ShowUnitAIPlanAttachment", "Skirmish_Buy_Credits", "Skirmish_Reinforcement_Delay_Frames", "Solo_Attack_Range",
# 	"SpaceFOWColor", "SpaceFOWHeight", "SpaceFOWRegrowTime", "SpaceIdleMovementSpeed", "SpaceIdlePathCullCoefficient",
# 	"SpaceLocomotorFacingLookaheadAcc", "SpaceObjectTrackingInterval", "SpaceObjectTrackingTreeCount",
# 	"SpacePathFailureDistanceCutoffCoefficient", "SpacePathFailureForwardExpansionIncrement",
# 	"SpacePathFailureMaxExpansionsCoefficient", "SpacePathFailureRotationExpansionIncrement",
# 	"SpacePathfindFrameDelayDelta", "SpacePathfindMaxExpansions", "SpacePathingTries", "SpaceReinforceFOWColor",
# 	"SpaceReinforceFeedbackOnlyWhileDragging", "SpaceStaticObstacleAvoidanceBonusDistance",
# 	"Space_Auto_Resolve_Delay_Seconds", "Space_Capture_Allowed_Countdown_Seconds", "Space_Collidable_Grid_Cull_Size",
# 	"Space_Elevated_Vulnerability_Duration", "Space_Elevated_Vulnerability_Factor", "Space_Guard_Range",
# 	"Space_Large_Ship_Grid_Cull_Size", "Space_Reinforcement_Collision_Check_Distance",
# 	"Space_Retreat_Allowed_Countdown_Seconds", "Space_Retreat_Attrition_Factor",
# 	"Space_Station_Destruction_Forces_Retreat", "Space_Tactical_Camera_Locked", "SpecialAlignedOperatorBonus",
# 	"Speech_Text_Color", "Spread_Out_Spacing_Coefficient", "Star_Wars_Crawl_Start_Fadeout_Frame", "
# 	Starting_Galactic_Camera_Position", "Strategic_Edge_Scroll_Region", "Strategic_Max_Scroll_Speed",
# 	"Strategic_Min_Scroll_Speed", "Strategic_Offscreen_Scroll_Region", "Strategic_Queue_Tactical_Battles",
# 	"SyncedFrameInterval", "System_Text_Color", "Tactical_Build_Time_Multiplier", "Tactical_Edge_Scroll_Region",
# 	"Tactical_Max_Scroll_Speed", "Tactical_Min_Scroll_Speed", "Tactical_Offscreen_Scroll_Region",
# 	"Tactical_Overrun_Multiple", "Task_Text_Color", "TeamCrouchMoveBlendTime", "TeamMoveBlendTime",
# 	"Team_Healthbar_Offset", "Telekinesis_Hover_Height", "Telekinesis_Max_Bob_Height", "Telekinesis_Max_Wobble_Angle",
# 	"Telekinesis_Transition_Time", "Telekinesis_Wobble_Cycle_Time", "Telekinesis_Wobble_Fade_Time",
# 	"Terrain_Resurface_Rand", "Terrain_Resurface_Tolerance", "Text_Button_Default_Font_Name",
# 	"Text_Button_Default_Font_Size", "Text_Reveal_Rate", "ThreatExpansionDistance", "Tool_Tip_Font_Name",
# 	"Tool_Tip_Font_Size", "Tool_Tip_Small_Font_Name", "Tool_Tip_Small_Font_Size", "Tooltip_Delay", "Tractor_Beam_Color",
# 	"Tractor_Beam_Frames", "Tractor_Beam_Texture", "Tractor_Beam_Width", "TradeRouteMovementFactor",
# 	"TurnInPlaceSlowdownCapital", "TurnInPlaceSlowdownCorvette", "TurnInPlaceSlowdownFrigate",
# 	"Under_Construction_Damage_Multiplier", "Unit_Command_Rankings_By_Category", "UseLinearCollisionChecks",
# 	"Use_Neutral_UI_Color", "Use_Reinforcement_Points", "VehicleFormationRecruitmentDistance",
# 	"WaitOperatorBaseFrameTime", "WaitOperatorCostCoefficient", "WaitOperatorSpeedCoefficient", "WalkAnimationCutoff",
# 	"Water_Clip_Plane_Offset", "Water_Render_Target_Resolution", "WaypointFlagModelName", "WaypointLineLandDashLength",
# 	"WaypointLineLandDashVelocity", "WaypointLineLandGapLength", "WaypointLineTextureName", "Win_Lose_Message_Font",
# 	"Win_Lose_Message_Font_Size", "Win_Message_Color", "XYExpansionDistanceLand", "XYExpansionDistanceSpace"
# ]
#
# CommandBarComponent: [
# 	"Attribute - Name", "Disabled", "File", "Group", "Hidden", "Manual_Offset", "Mega_Texture_Name", "Model_Name",
# 	"Model_Offset_X", "Model_Offset_Y", "Type"
# ]
#
# TradeRoute: [
# 	"Attribute - Name", "Credit_Gain_Factor", "File", "HS_Speed_Factor", "Point_A", "Point_B", "Political_Control_Gain",
# 	"Visible_Line_Name"
# ]
#
# TradeRouteLines: ["Attribute - Name", "Color_Zoomed_In", "Color_Zoomed_Out", "Render_Mode", "Width"]
# RadarMap: ["Attribute - Name", "Event_Duration", "Event_Model_Name", "Event_Model_Scale", "Event_Single_Instance"]
# Draw3DTextCrawl: [
# 	"Attribute - Language", "Attribute - Name", "Fadein_End_Frame", "Fadein_Start_Frame", "Fadeout_Start_Frame",
# 	"Font_Character_Padding", "Font_Name", "Font_Size", "Font_Stretch_Factor", "Has_Header", "Header_Font_Name",
# 	"Header_Font_Size", "Header_Text_IDs", "Header_Texture_Height_Pow_2", "Header_Texture_Width_Pow_2",
# 	"Model_Camera_Bone_Name", "Model_Name", "Polygon_Shader_Name", "Polygon_Tex_Param_Name", "Text_IDs",
# 	"Texture_Height_Pow_2", "Texture_Width_Pow_2"
# ]
#
# WeatherPattern: ["Attribute - Name", "Duration", "Ease_Out_Duration", "Emitter_Intensity", "Lightning_Intensity"]
# HardPoint: [
# 	"Attribute - Name", "Attachment_Bone", "Collision_Mesh", "Damage_Decal", "Damage_Particles", "Damage_Type",
# 	"Death_Breakoff_Prop", "Death_Explosion_Particles", "Death_Explosion_SFXEvent", "Fire_Bone_A", "Fire_Bone_B",
# 	"Fire_Cone_Height", "Fire_Cone_Width", "Fire_Inaccuracy_Distance", "Fire_Max_Recharge_Seconds",
# 	"Fire_Min_Recharge_Seconds", "Fire_Projectile_Type", "Fire_Pulse_Count", "Fire_Pulse_Delay_Seconds",
# 	"Fire_Range_Distance", "Fire_SFXEvent", "Health", "Is_Destroyable", "Is_Targetable", "Model_To_Attach",
# 	"Tooltip_Text", "Type"
# ]
#
# Campaign: [
# 	"Attribute - Name", "AI_Player_Control", "Active_Plot", "Autoresolve_Exclusion_Locations", "Camera_Distance",
# 	"Camera_Shift_X", "Camera_Shift_Y", "Campaign_Set", "Description_Text", "Empire_Story_Name", "Event_Param1",
# 	"Event_Param2", "Event_Param3", "Event_Type", "Evil_Victory_Conditions", "File", "Good_Victory_Conditions",
# 	"Home_Location", "Is_Autoresolve_Allowed", "Is_Listed", "Is_Multiplayer", "Is_Story_Campaign", "Locations",
# 	"Lua_Script", "Markup_Filename", "Max_Tech_Level", "Planet_Auto_Reveal", "Rebel_Story_Name", "Show_Completed_Tab",
# 	"Special_Case_Production", "Starting_Active_Player", "Starting_Credits", "Starting_Forces", "Starting_Tech_Level",
# 	"Story_Chapter", "Story_Dialog", "Story_Dialog_Popup", "Story_Tag", "Supports_Custom_Settings", "Suspended_Plot",
# 	"Text_ID", "Trade_Routes", "Tutorial"
# ]
# Faction: [
# 	"Attribute - Name", "Allies", "Alternate_Icon_Name", "Basic_AI", "Big_Fleet_Color", "Bombing_Run_Blob_Size",
# 	"Bombing_Run_Shadow_Blob_Material_Name", "Can_Control_Planets", "Can_Win_By_Destroying_Super_Weapon",
# 	"Carrier_Icon_Name", "Color", "Corvette_Icon_Name", "Create_Player_In_Multiplayer_Games",
# 	"Credits_Accumulation_Factor", "Debug_Ground_Structures", "Default_Transmission_Message", "Defeat_Text",
# 	"Display_Font_Color", "Displayed_Tech_Level_Adjustment", "Enemies", "Faction_Leader", "Faction_Leader_Company",
# 	"Faction_Super_Weapon", "Fighter_Icon_Name", "File", "Finale_Movie", "Fleet_Icon_Name", "Force_Alignment",
# 	"Frigate_Icon_Name", "Galactic_Advisor_Hints", "Garrison_Reinforcement_Delay_Seconds", "Generic_Win_Movie",
# 	"Ground_Base_Icon_Name", "Ground_Transport_Icon_Name", "Helper_Icon_Name", "Hyperspace_Speed_Factor", "Icon_Name",
# 	"Infantry_Icon_Name", "Is_Debug_Switchable_To", "Is_Neutral", "Is_Playable",
# 	"Land_Ability_Targeting_Range_Overlay_Material_Name", "Land_Ability_Targeting_Range_Overlay_RGBA",
# 	"Land_Ability_Targeting_Range_Overlay_Scale_Factor", "Land_Advisor_Hints",
# 	"Land_Area_Effect_Range_Overlay_Material_Name", "Land_Area_Effect_Range_Overlay_RGBA",
# 	"Land_Area_Effect_Range_Overlay_Scale_Factor", "Land_Lose_Image", "Land_Mode_Garrison_Selection_Blob_Material_Name",
# 	"Land_Mode_Selection_Blob_Material_Name", "Land_Retreat_Begin_SFXEvent", "Land_Retreat_Cancel_SFXEvent",
# 	"Land_Retreat_Countdown_Color_RGBA", "Land_Retreat_Countdown_Seconds", "Land_Retreat_Countdown_Text_ID",
# 	"Land_Retreat_Enemy_Begin_SFXEvent", "Land_Retreat_Not_Allowed_Reason_1_SFXEvent",
# 	"Land_Retreat_Not_Allowed_Reason_2_SFXEvent", "Land_Retreat_Not_Allowed_Reason_3_SFXEvent",
# 	"Land_Retreat_Not_Allowed_SFXEvent", "Land_Retreat_Pursue_Max_Speed_Mod_Factor",
# 	"Land_Retreat_Units_Damaged_Mod_Factor", "Land_Skirmish_AI_Default_Forces", "Land_Skirmish_Unit_Buy_Credits",
# 	"Land_Skirmish_Unit_Cap_By_Player_Count", "Land_Surrender_SFXEvent", "Land_Win_Image", "Maintenance_Cost",
# 	"Minimum_Visible_Base_Level", "Multiplayer_Beacon_Type", "Multiplayer_Campaign_Heroes",
# 	"Music_Event_Battle_Load_Screen", "Music_Event_Land_Ambient_Super_Weapon", "Music_Event_Land_Battle_Super_Weapon",
# 	"Music_Event_List_Ambient", "Music_Event_List_Battle", "Music_Event_Space_Ambient_Super_Weapon",
# 	"Music_Event_Space_Battle_Super_Weapon", "Music_Event_Strategic_Lose", "Music_Event_Strategic_Win",
# 	"Music_Event_Tactical_Land_Battle_Pending", "Music_Event_Tactical_Lose",
# 	"Music_Event_Tactical_Space_Battle_Pending", "Music_Event_Tactical_Win", "No_Colorization_Color",
# 	"Planet_Icon_Offset", "Planet_Icon_Scale", "Primary_Enemy", "Reinforcements_Cancelled_SFXEvent",
# 	"Reinforcements_Enroute_SFXEvent", "Reinforcements_Pick_Landing_Zone_SFXEvent", "Reinforcements_Ready_SFXEvent",
# 	"Reinforcements_Requesting_SFXEvent", "Reinforcements_Selection_SFXEvent",
# 	"Reinforcements_Shadow_Blob_Material_Name", "SFXEvent_Arrive_From_Hyperspace", "SFXEvent_Base_Shield_Absorb_Damage",
# 	"SFXEvent_Bombing_Run_Ally_Available", "SFXEvent_Bombing_Run_Available", "SFXEvent_Bombing_Run_Begin_Crosstalk",
# 	"SFXEvent_Bombing_Run_Cancelled", "SFXEvent_Bombing_Run_Enemy_Available",
# 	"SFXEvent_Build_Impossible_Location_Blockaded", "SFXEvent_Enemy_Fleet_Approaching_Planet", "SFXEvent_Enemy_Spotted",
# 	"SFXEvent_Exit_Into_Hyperspace", "SFXEvent_GUI_Enemy_Toggle_Non_Hero_Ability_Off",
# 	"SFXEvent_GUI_Enemy_Toggle_Non_Hero_Ability_On", "SFXEvent_GUI_Start_Campaign",
# 	"SFXEvent_GUI_Toggle_Non_Hero_Ability_Off", "SFXEvent_GUI_Toggle_Non_Hero_Ability_On", "SFXEvent_HUD_Advisor_Hint",
# 	"SFXEvent_HUD_Advisor_Message", "SFXEvent_HUD_Advisor_Urgent", "SFXEvent_HUD_Base_Shield_Offline",
# 	"SFXEvent_HUD_Base_Shield_Online", "SFXEvent_HUD_Base_Shield_Penetrated", "SFXEvent_HUD_Build_Pad_Captured",
# 	"SFXEvent_HUD_Build_Pad_Lost", "SFXEvent_HUD_Enemy_Base_Shield_Offline", "SFXEvent_HUD_Enemy_Base_Shield_Online",
# 	"SFXEvent_HUD_Enemy_Base_Shield_Penetrated", "SFXEvent_HUD_Enemy_Special_Weapon_Charging",
# 	"SFXEvent_HUD_Enemy_Special_Weapon_Firing", "SFXEvent_HUD_Enemy_Special_Weapon_Ready",
# 	"SFXEvent_HUD_Gravity_Control_Generator_Off", "SFXEvent_HUD_Gravity_Control_Generator_On",
# 	"SFXEvent_HUD_Landing_Zone_Captured", "SFXEvent_HUD_Landing_Zone_Lost", "SFXEvent_HUD_Last_Landing_Zone_Lost",
# 	"SFXEvent_HUD_Lost_Land_Battle", "SFXEvent_HUD_Lost_Land_Battle_Enemy_TSW_Present",
# 	"SFXEvent_HUD_Lost_Space_Battle", "SFXEvent_HUD_Lost_Space_Battle_Enemy_TSW_Present",
# 	"SFXEvent_HUD_Reinforcement_Point_Ally_Owned_05_Seconds", "SFXEvent_HUD_Reinforcement_Point_Ally_Owned_15_Seconds",
# 	"SFXEvent_HUD_Reinforcement_Point_Ally_Owned_30_Seconds", "SFXEvent_HUD_Reinforcement_Point_Ally_Owned_60_Seconds",
# 	"SFXEvent_HUD_Reinforcement_Point_Contested", "SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_05_Seconds",
# 	"SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_15_Seconds",
# 	"SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_30_Seconds",
# 	"SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_60_Seconds", "SFXEvent_HUD_Reinforcement_Point_Owned_05_Seconds",
# 	"SFXEvent_HUD_Reinforcement_Point_Owned_15_Seconds", "SFXEvent_HUD_Reinforcement_Point_Owned_30_Seconds",
# 	"SFXEvent_HUD_Reinforcement_Point_Owned_60_Seconds", "SFXEvent_HUD_Repairing",
# 	"SFXEvent_HUD_Special_Weapon_Charging", "SFXEvent_HUD_Special_Weapon_Firing",
# 	"SFXEvent_HUD_Special_Weapon_Ready", "SFXEvent_HUD_Tactical_Victory_Near", "SFXEvent_HUD_Won_Land_Battle",
# 	"SFXEvent_HUD_Won_Land_Battle_Enemy_TSW_Present", "SFXEvent_HUD_Won_Space_Battle",
# 	"SFXEvent_HUD_Won_Space_Battle_Enemy_TSW_Present", "SFXEvent_Land_Base_Under_Attack_Announcement",
# 	"SFXEvent_Land_Invasion_Commencing", "SFXEvent_Max_Credits_Limit_Reached", "SFXEvent_Mission_Added",
# 	"SFXEvent_New_Construction_Options_Available", "SFXEvent_Planet_Gained_Control", "SFXEvent_Planet_Lost_Control",
# 	"SFXEvent_Player_Taunt", "SFXEvent_Slice_Failure", "SFXEvent_Slice_Success",
# 	"SFXEvent_Space_Base_Under_Attack_Announcement", "SFXEvent_Starbase_Ally_Upgraded",
# 	"SFXEvent_Starbase_Enemy_Upgraded", "SFXEvent_Starbase_Upgraded", "SFXEvent_Strategic_Pop_Cap_Reached",
# 	"SFXEvent_Tactical_Gain_Friendly_Control", "SFXEvent_Tactical_Lose_Friendly_Control",
# 	"SFXEvent_Tactical_Object_Building_Complete", "SFXEvent_Tactical_Object_Building_Loop",
# 	"SFXEvent_Tactical_Object_Building_Started", "SFXEvent_Tactical_Object_Sold", "SFXEvent_Tactical_Pop_Cap_Reached",
# 	"SFXEvent_Tactical_Unit_Cap_Reached", "SFXEvent_Unit_Type_Spotted", "SFXEvent_Weather_Begin",
# 	"SFXEvent_Weather_End", "SFX_Event_Tactical_Land_Battle_Pending", "SFX_Event_Tactical_Space_Battle_Pending",
# 	"Scatters_From_Crushers", "Selection_Blob_RGBA", "Ship_Icon_Name", "Skirmish_Land_Bomber", "Space_Advisor_Hints",
# 	"Space_Forced_Retreat_Due_To_Superweapon", "Space_Lose_Image", "Space_Mode_Garrison_Selection_Blob_Material_Name",
# 	"Space_Mode_Selection_Blob_Material_Name", "Space_Retreat_Begin_SFXEvent", "Space_Retreat_Cancel_SFXEvent",
# 	"Space_Retreat_Countdown_Color_RGBA", "Space_Retreat_Countdown_Seconds", "Space_Retreat_Countdown_Text_ID",
# 	"Space_Retreat_Enemy_Begin_SFXEvent", "Space_Retreat_Flight_Move_Increment",
# 	"Space_Retreat_Not_Allowed_Reason_1_SFXEvent", "Space_Retreat_Not_Allowed_Reason_2_SFXEvent",
# 	"Space_Retreat_Not_Allowed_Reason_3_SFXEvent", "Space_Retreat_Not_Allowed_SFXEvent",
# 	"Space_Retreat_Off_Map_Dest_Pos", "Space_Retreat_Pursue_Max_Speed_Mod_Factor",
# 	"Space_Retreat_Unit_Increment_Wait_Frames", "Space_Retreat_Units_Damaged_Mod_Factor",
# 	"Space_Skirmish_AI_Default_Forces", "Space_Skirmish_Unit_Buy_Credits", "Space_Surrender_SFXEvent",
# 	"Space_Tactical_Unit_Cap", "Space_Win_Image", "SpeechEvent_Super_Weapon_Enemy_Moved_Into_Range",
# 	"SpeechEvent_Super_Weapon_Enemy_Moving_Into_Range", "SpeechEvent_Super_Weapon_Enemy_Moving_Range_05_Seconds",
# 	"SpeechEvent_Super_Weapon_Enemy_Moving_Range_15_Seconds", "SpeechEvent_Super_Weapon_Enemy_Moving_Range_30_Seconds",
# 	"SpeechEvent_Super_Weapon_Enemy_Moving_Range_60_Seconds", "SpeechEvent_Super_Weapon_Moved_Into_Range",
# 	"SpeechEvent_Super_Weapon_Moving_Into_Range", "SpeechEvent_Super_Weapon_Moving_Range_05_Seconds",
# 	"SpeechEvent_Super_Weapon_Moving_Range_15_Seconds", "SpeechEvent_Super_Weapon_Moving_Range_30_Seconds",
# 	"SpeechEvent_Super_Weapon_Moving_Range_60_Seconds", "SpeechEvent_Tactical_Intro_Land_Attacker",
# 	"SpeechEvent_Tactical_Intro_Land_Attacker_Last_Location", "SpeechEvent_Tactical_Intro_Land_Defender",
# 	"SpeechEvent_Tactical_Intro_Land_Defender_Conditional_Or", "SpeechEvent_Tactical_Intro_Land_Defender_Last_Location",
# 	"SpeechEvent_Tactical_Intro_Land_Raid_Attacker", "SpeechEvent_Tactical_Intro_Land_Raid_Defender",
# 	"SpeechEvent_Tactical_Intro_Space_Attacker", "SpeechEvent_Tactical_Intro_Space_Attacker_Conditional_And",
# 	"SpeechEvent_Tactical_Intro_Space_Attacker_Conditional_Or", "SpeechEvent_Tactical_Intro_Space_Defender",
# 	"SpeechEvent_Tactical_Intro_Space_Defender_Conditional_And",
# 	"SpeechEvent_Tactical_Intro_Space_Defender_Conditional_Or", "Squadron_Icon_Name",
# 	"Standalone_Space_Maps_Special_Weapon_A", "Standalone_Space_Maps_Special_Weapon_B", "Star_Base_Icon_Name",
# 	"Strategic_Map_Music_Event", "Superweapon_Win_Movie", "Tactical_Intro_Command_Bar_Movie_Name",
# 	"Tech_Tree_Dialog_Name", "Text_ID", "Vehicle_Icon_Name", "Victory_Text"
# ]
#
# TacticalCameraConstants: [
# 	"Attribute - Name", "Bottom_Bounds_Buffer", "Distance_Default", "Distance_Max", "Distance_Min",
# 	"Distance_Per_Mouse_Unit", "Distance_Smooth_Time", "Distance_Spline", "Far_Clip", "Fov_Default",
# 	"Fov_Max", "Fov_Min", "Fov_Per_Mouse_Unit", "Fov_Smooth_Time", "Location_Follows_Terrain",
# 	"Location_Height_Down_Smooth_Time", "Location_Height_Up_Smooth_Time", "Min_Height_Above_Terrain", "Near_Clip",
# 	"Object_Fade_Begin", "Object_Fade_End", "Pitch_Default", "Pitch_Max", "Pitch_Min", "Pitch_Per_Mouse_Unit",
# 	"Pitch_Per_Zoom_Unit", "Pitch_Spline", "Pitch_When_Zoomed_In", "Pitch_Zoom_Begin_Fraction", "Side_Bounds_Buffer",
# 	"Spline_Steps", "Tactical_Overview_Click_Time", "Tactical_Overview_Clicks", "Tactical_Overview_Distance",
# 	"Tactical_Overview_Distance2", "Tactical_Overview_FOV", "Tactical_Overview_FOV2", "Tactical_Overview_Pitch",
# 	"Tactical_Overview_Pitch2", "Top_Bounds_Buffer", "Use_Splines", "Yaw_Default", "Yaw_Max", "Yaw_Min",
# 	"Yaw_Per_Mouse_Unit"
# ]
#
# LightSource: [
# 	"Attribute - Name", "Auto_Destruct_Fade_Time", "Auto_Destruct_Time", "Blob_Color", "Blob_Intensity", "Blob_Radius",
# 	"Diffuse", "Falloff_Start", "Intensity", "Radius"
# ]
#
# BinkMovie: ["Attribute - Name", "Cannot_Skip", "Movie_File"]
# TargetingPrioritySet: [
# 	"Attribute - Name", "Attack_Priorities", "Category_Exclusions", "File", "Property_Exclusions", "Unit_Exclusions"
# ]
#
# DifficultyAdjustment: ["Attribute - Name", "Credit_Multiplier", "Damage_Multiplier",
# 	"Galactic_AI_Contrast_Multiplier", "Galactic_AI_Goal_Cycle_Sleep_Duration", "Galactic_Build_Time_Multiplier",
# 	"Land_AI_Contrast_Multiplier", "Land_AI_Goal_Cycle_Sleep_Duration", "Land_Build_Time_Multiplier",
# 	"Space_AI_Contrast_Multiplier", "Space_AI_Goal_Cycle_Sleep_Duration", "Space_Build_Time_Multiplier"
# ]
#
# WeatherAudioManager: ["Ambient_SFXEvent_Intermittent", "Weather_SFXEvent_Intermittent", "Weather_SFXEvent_Loop"]


DESCRIPTION_SUBNODE: Dict[str, str] = {
	# SubNode Descriptions
	
	# This is used when the requested key is not in the dictionary or the value is an empty string
	"default": "No description currently, but please feel free to give it one through GitHub!",

	# Identically Named Subnodes are in this section, all other usages commented out
	"Attribute - Name": "",
	"Damage_Type": "",
	"File": "",
	"Files": "",
	"Fire_Inaccuracy_Distance": "",
	"Icon_Name": "",
	"Intensity": "",
	"Lua_Script": "",
	"Maintenance_Cost": "",
	"Model_Name": "",
	"No_Colorization_Color": "",
	"Render_Mode": "",
	"Text_ID": "",
	"Type": "",
	"Volume_Percent": "",

	# GameObjectType SubNodes
	"Attribute - Description": "",
	# "Attribute - Name": "",
	"Attribute - Subobjectlist": "",
	"AI_Combat_Power": "",
	"Activation_Style": "",
	"Additional_Population_Capacity": "",
	"Affiliation": "",
	"Air_Vehicle_Turret_Target": "",
	"Alternate_Max_Rate_Of_Turn": "",
	"Alternate_Max_Speed": "",
	"Always_Instantiate_Galactic": "",
	"Always_Spawn_In_Orbit": "",
	"Applicable_Unit_Categories": "",
	"Applicable_Unit_Types": "",
	"Apply_Y_Turret_Rotate_To_Axis": "",
	"Apply_Z_Turret_Rotate_To_Axis": "",
	"Armor_Type": "",
	"Asteroid_Damage_Hit_Particles": "",
	"Attach_To_Flagship_During_Space_Battle": "",
	"Attack_Animation_Is_Overlay": "",
	"Attack_Move_Response_Range": "",
	"Auto_Deploys": "",
	"Autonomous_Move_Extension_Vs_Attacker": "",
	"Autoresolve_Health": "",
	"Bank_Turn_Angle": "",
	"Barrel_Bone_Name": "",
	"Base_Level": "",
	"Base_Level_Available": "",
	"Base_Position": "",
	"Base_Shield_Penetration_Particle": "",
	"Begin_Turn_Towards_Distance": "",
	"Behavior": "",
	"Blob_Shadow_Below_Detail_Level": "",
	"Blob_Shadow_Bone_Name": "",
	"Blob_Shadow_Material_Name": "",
	"Blob_Shadow_Scale": "",
	"Bomb_Countdown_Seconds": "",
	"Build_Advances_Tech_Level": "",
	"Build_Can_Be_Unlocked_By_Slicer": "",
	"Build_Cost_Credits": "",
	"Build_Countdown_Text_ID": "",
	"Build_Countdown_Text_RGBA": "",
	"Build_Countdown_Timer": "",
	"Build_Initially_Locked": "",
	"Build_Limit_Current_For_All_Allies": "",
	"Build_Limit_Current_Per_Player": "",
	"Build_Limit_Lifetime_For_All_Allies": "",
	"Build_Limit_Lifetime_Per_Player": "",
	"Build_Max_Instances_Per_Planet": "",
	"Build_Music_Completed": "",
	"Build_Speech_Completed": "",
	"Build_Speech_Countdowns": "",
	"Build_Speech_Stopped": "",
	"Build_Speech_Underway": "",
	"Build_Tab_Heroes": "",
	"Build_Tab_Land_Units": "",
	"Build_Tab_Outpost": "",
	"Build_Tab_Space_Station": "",
	"Build_Tab_Space_Units": "",
	"Build_Tab_Special_Structures": "",
	"Build_Time_Reduced_By_Multiple_Factories": "",
	"Build_Time_Seconds": "",
	"Burning_Damage_Per_Second": "",
	"Cache_Crusher_Boxes": "",
	"Camera_Aligned": "",
	"CanCellStack": "",
	"Can_Be_Neutralized_By_Major_Heroes": "",
	"Can_Be_Neutralized_By_Minor_Heroes": "",
	"Can_Hyperspace_Without_Activating_Ability": "",
	"Capture_Point_Radius": "",
	"Capture_Point_Transition_Time_Seconds": "",
	"CategoryMask": "",
	"Cinematic_Anim_Blend_Seconds": "",
	"Cinematic_Anim_Index": "",
	"Cinematic_Anim_Speed": "",
	"Cinematic_Object_Only": "",
	"Collidable_By_Projectile_Dead": "",
	"Collidable_By_Projectile_Living": "",
	"Collision_Box_Modifier": "",
	"Combat_Power_Value": "",
	"Company_Transport_Unit": "",
	"Company_Units": "",
	"Conversion_Ability_Changes_To_Enemy": "",
	"Converted_To_Enemy_Die_Time_Seconds": "",
	"Create_Team": "",
	"Create_Team_Type": "",
	"Custom_Footprint_Radius": "",
	"Custom_Hard_XExtent": "",
	"Custom_Hard_XExtent_Offset": "",
	"Custom_Hard_YExtent": "",
	"Custom_Hard_YExtent_Offset": "",
	"Custom_Soft_Footprint_Radius": "",
	"Damage": "",
	"Damage_Hit_Particles": "",
	# "Damage_Type": "",
	"Damaged_Smoke_Asset_Name": "",
	"Death_By_TSW_Replacements": "",
	"Death_Clone": "",
	"Death_Clone_Is_Obstacle": "",
	"Death_Explosions": "",
	"Death_Fade_Time": "",
	"Death_Leave_Hulk_Behind": "",
	"Death_Persistence_Duration": "",
	"Death_SFXEvent_Start_Die": "",
	"Dense_FOW_Reveal_Range_Multiplier": "",
	"Deploys": "",
	"Destruction_Survivors": "",
	"Effective_Radius": "",
	"Encyclopedia_Good_Against": "",
	"Encyclopedia_Text": "",
	"Encyclopedia_Unit_Class": "",
	"Encyclopedia_Vulnerable_To": "",
	"Enemy_Spawn_Text": "",
	"Energy_Capacity": "",
	"Energy_Refresh_Rate": "",
	"Evade_Detection_Chance": "",
	"Exclude_From_Distance_Fade": "",
	"Exit_Door_Angle_Degrees": "",
	"Exit_Door_Distance": "",
	"Expiration_Seconds": "",
	# "File": "",
	"Fire_Category_Restrictions": "",
	# "Fire_Inaccuracy_Distance": "",
	"Fires_Forward": "",
	"FormationGrouping": "",
	"FormationOrder": "",
	"FormationSpacing": "",
	"Formation_Priority": "",
	"Formation_Prority": "",
	"Friendly_Spawn_Text": "",
	"GUI_Activated_Ability_Name": "",
	"GUI_Angles": "",
	"GUI_Bounds_Scale": "",
	"GUI_Bracket_Height": "",
	"GUI_Bracket_Size": "",
	"GUI_Bracket_Width": "",
	"GUI_Distance": "",
	"GUI_Model": "",
	"GUI_Model_Name": "",
	"GUI_Offset": "",
	"GUI_Row": "",
	"GUI_Velocity": "",
	"GUI_X_Rot": "",
	"GalacticBehavior": "",
	"Galactic_Fleet_Override_Icon_Index": "",
	"Galactic_Fleet_Override_Model_Name": "",
	"Galactic_Model_Name": "",
	"Galactic_Position": "",
	"Ground_Infantry_Turret_Target": "",
	"Ground_Vehicle_Turret_Target": "",
	"Guard_Chase_Range": "",
	"HardPoints": "",
	"Hardpoints": "",
	"Has_Land_Evaluator": "",
	"Has_Pre_Turn_Anim": "",
	"Has_Space_Evaluator": "",
	"Heal_Amount": "",
	"Heal_Interval_In_Secs": "",
	"Heal_Percent": "",
	"Heal_Range": "",
	"Highlight_Blob_Material_Name": "",
	"Hover_Offset": "",
	"Hyperspace": "",
	"Hyperspace_Speed": "",
	# "Icon_Name": "",
	"Idle_Anim_00_Rate_Mod": "",
	"Idle_Chase_Range": "",
	"Immune_To_Damage": "",
	"In_Background": "",
	"Influences_Capture_Point": "",
	"Initial_State_Visible_Under_FOW": "",
	"IsBuildable": "",
	"Is_Affected_By_Gravity_Control_Field": "",
	"Is_Bomber": "",
	"Is_Branched_Map_Discardable": "",
	"Is_Combustible": "",
	"Is_Community_Property": "",
	"Is_Decoration": "",
	"Is_Discardable": "",
	"Is_Dummy": "",
	"Is_Editor_Placed": "",
	"Is_Escort": "",
	"Is_Generic_Hero": "",
	"Is_Marker": "",
	"Is_Named_Hero": "",
	"Is_Pulsing": "",
	"Is_Special_Weapon_In_Space": "",
	"Is_Sprite": "",
	"Is_Squashable": "",
	"Is_Squashable_By_Supercrusher": "",
	"Is_Stealth_Company": "",
	"Is_Supercrusher": "",
	"Is_Visible_On_Radar": "",
	"LOD_Bias": "",
	"LandBehavior": "",
	"Land_Damage_Alternates": "",
	"Land_Damage_SFX": "",
	"Land_Damage_Thresholds": "",
	"Land_FOW_Reveal_Range": "",
	"Land_Model_Anim_Override_Name": "",
	"Land_Model_Name": "",
	"Land_Victory_Relevant": "",
	"Landing_Transport_Variant": "",
	"Last_State_Visible_Under_FOW": "",
	"LateralAcceleration": "",
	"Layer_Z_Adjust": "",
	"Locomotor_Has_Animation_Priority": "",
	"Loop_Idle_Anim_00": "",
	# "Lua_Script": "",
	"MP_Encyclopedia_Text": "",
	# "Maintenance_Cost": "",
	"Mass": "",
	"MaxFacingLookAheadFrames": "",
	"Max_Distance_From_Spawner": "",
	"Max_Ground_Base": "",
	"Max_Lift": "",
	"Max_Num_Spawned_Objects": "",
	"Max_Number_Of_Pulses": "",
	"Max_Rate_Of_Roll": "",
	"Max_Rate_Of_Turn": "",
	"Max_Space_Base": "",
	"Max_Speed": "",
	"Max_Squad_Size": "",
	"Max_Thrust": "",
	"Maximum_Destruction_Survivor_Count": "",
	"Min_Speed": "",
	"Min_Speed_Fraction_For_Turn": "",
	"MinimumPushReturnDistance": "",
	"Minimum_Destruction_Survivor_Count": "",
	"Minimum_Follow_Distance": "",
	"Mod_Multiplier": "",
	"Mouse_Collide_Override_Sphere_Radius": "",
	"MovementBoxExpansionFactor": "",
	"MovementClass": "",
	"MovementPredictionInterval": "",
	"Movement_Animation_Speed": "",
	"Movie_Object": "",
	"Multisample_FOW_Check": "",
	"Name_Adjust": "",
	"Neutralization_Cost": "",
	"Next_Level_Base": "",
	"Next_Upgrade_Level_Type": "",
	# "No_Colorization_Color": "",
	"No_Reflection_Below_Detail_Level": "",
	"No_Refraction_Below_Detail_Level": "",
	"Number_per_Squadron": "",
	"Obstacle_Height": "",
	"Obstacle_Width": "",
	"Obstacle_X_Offset": "",
	"Obstacle_Y_Offset": "",
	"Occlusion_Silhouette_Enabled": "",
	"OccupationStyle": "",
	"On_Fire_Speed_Modifier": "",
	"Out_Of_Combat_Defense_Adjustment": "",
	"Overall_Length": "",
	"Overall_Width": "",
	"OverrideAcceleration": "",
	"OverrideDeceleration": "",
	"Owner_Attachment_Bone": "",
	"Owner_Light_Effect_Color": "",
	"Owner_Light_Effect_Color2": "",
	"Owner_Light_Effect_Duration": "",
	"Owner_Light_Effect_Pulse_Count": "",
	"Owner_Light_Effect_Type": "",
	"Owner_Particle_Bone_Name": "",
	"Ownership_Sticks": "",
	"Particle_Effect": "",
	"Particle_Lifetime_Frames": "",
	"Pause_During_Cinematic_Anim": "",
	"Planet_Credit_Value": "",
	"Play_SFXEvent_On_Sighting": "",
	"Political_Control": "",
	"Political_Faction": "",
	"Population_Value": "",
	"Pre_Lit": "",
	"Prepare_Strafe_Height": "",
	"Prev_Level_Base": "",
	"Prevents_Blockade_Run_Attrition": "",
	"Prevents_Story_Campaign_Autoresolve": "",
	"Previous_Upgrade_Level_Type": "",
	"Primary_Locomotor_Name": "",
	"Projectile_Absorbed_By_Shields_Particle": "",
	"Projectile_Appearance_Delay_Frames": "",
	"Projectile_Category": "",
	"Projectile_Custom_Render": "",
	"Projectile_Damage": "",
	"Projectile_Does_Energy_Damage": "",
	"Projectile_Does_Hitpoint_Damage": "",
	"Projectile_Does_Shield_Damage": "",
	"Projectile_Fire_Pulse_Count": "",
	"Projectile_Fire_Pulse_Delay_Seconds": "",
	"Projectile_Fire_Recharge_Seconds": "",
	"Projectile_Ground_Detonation_Particle": "",
	"Projectile_Ground_Detonation_SurfaceFX": "",
	"Projectile_Length": "",
	"Projectile_Lifetime_Detonation_Particle": "",
	"Projectile_Max_Flight_Distance": "",
	"Projectile_Max_Scan_Range": "",
	"Projectile_Object_Armor_Reduced_Detonation_Particle": "",
	"Projectile_Object_Detonation_Particle": "",
	"Projectile_SFXEvent_Detonate_Reduced_By_Armor": "",
	"Projectile_Types": "",
	"Projectile_Width": "",
	"Property_Flags": "",
	"Pulse_Frequency_Secs": "",
	"Radar_Clip_To_Visible_Region": "",
	"Radar_Icon_Name": "",
	"Radar_Icon_Scale_Land": "",
	"Radar_Icon_Scale_Space": "",
	"Radar_Icon_Size": "",
	"Radar_Register_As_Foreground_Object": "",
	"Ranged_Target_Z_Adjust": "",
	"Ranking_In_Category": "",
	"Recharge_Seconds": "",
	"Reinforcement_Prevention_Radius": "",
	"Remove_Upon_Death": "",
	"Required_Ground_Base_Level": "",
	"Required_Planets": "",
	"Required_Special_Structures": "",
	"Required_Star_Base_Level": "",
	"Required_Timeline": "",
	"Reserve_Spawned_Units_Tech_0": "",
	"Retreat_Self_Destruct_Explosion": "",
	"Reveal_During_Setup_Phase": "",
	"Reveal_During_Setup_Phase_Only": "",
	"Reveal_For_Attacker": "",
	"Rotation_Animation_Speed": "",
	"SFXEvent_Ambient_Loop": "",
	"SFXEvent_Ambient_Moving": "",
	"SFXEvent_Ambient_Moving_Max_Delay_Seconds": "",
	"SFXEvent_Ambient_Moving_Min_Delay_Seconds": "",
	"SFXEvent_Assist_Attack": "",
	"SFXEvent_Assist_Move": "",
	"SFXEvent_Attack": "",
	"SFXEvent_Attack_Hardpoint": "",
	"SFXEvent_Barrage": "",
	"SFXEvent_Bomb_Run_Incoming": "",
	"SFXEvent_Bomb_Run_Select_Target": "",
	"SFXEvent_Build_Cancelled": "",
	"SFXEvent_Build_Complete": "",
	"SFXEvent_Build_Started": "",
	"SFXEvent_Damaged_By_Asteroid": "",
	"SFXEvent_Deploy": "",
	"SFXEvent_Enemy_Damaged_Health_Critical_Warning": "",
	"SFXEvent_Enemy_Damaged_Health_Low_Warning": "",
	"SFXEvent_Engine_Cinematic_Focus_Loop": "",
	"SFXEvent_Engine_Idle_Loop": "",
	"SFXEvent_Engine_Moving_Loop": "",
	"SFXEvent_Fire": "",
	"SFXEvent_Fleet_Move": "",
	"SFXEvent_GUI_Unit_Ability_Activated": "",
	"SFXEvent_GUI_Unit_Ability_Deactivated": "",
	"SFXEvent_Group_Attack": "",
	"SFXEvent_Group_Move": "",
	"SFXEvent_Guard": "",
	"SFXEvent_Hardpoint_All_Weapons_Destroyed": "",
	"SFXEvent_Hardpoint_Destroyed": "",
	"SFXEvent_Health_Critical_Warning": "",
	"SFXEvent_Health_Low_Warning": "",
	"SFXEvent_Move": "",
	"SFXEvent_Move_Into_Asteroid_Field": "",
	"SFXEvent_Move_Into_Nebula": "",
	"SFXEvent_Select": "",
	"SFXEvent_Special_Ability_Loop": "",
	"SFXEvent_Special_Weapon_Ready": "",
	"SFXEvent_Stop": "",
	"SFXEvent_Tactical_Build_Cancelled": "",
	"SFXEvent_Tactical_Build_Complete": "",
	"SFXEvent_Tactical_Build_Started": "",
	"SFXEvent_Target_Ability": "",
	"SFXEvent_Target_Affected": "",
	"SFXEvent_Turret_Rotating_Loop": "",
	"SFXEvent_Unit_Lost": "",
	"SFXEvent_Unit_Under_Attack": "",
	"Scale_Factor": "",
	"Score_Cost_Credits": "",
	"Secondary_Locomotor_Name": "",
	"Secondary_Objective": "",
	"Select_Box_Scale": "",
	"Select_Box_Z_Adjust": "",
	"Selection_Blob_Material_Name": "",
	"Sensor_Range": "",
	"Shield_Armor_Type": "",
	"Shield_Hit_Particles": "",
	"Shield_Points": "",
	"Shield_Refresh_Rate": "",
	"Ship_Class": "",
	"Show_In_Sidebar_When_Complete": "",
	"Show_In_Sidebar_While_Building": "",
	"Show_Name": "",
	"Single_Target_Heal": "",
	"Size_Value": "",
	"Slice_Cost_Credits": "",
	"Sort_Order_Adjust": "",
	"SpaceAutoResolveStunRate": "",
	"SpaceBehavior": "",
	"Space_Escort_Unit_Types": "",
	"Space_FOW_Reveal_Range": "",
	"Space_Full_Stop_Command": "",
	"Space_Layer": "",
	"Space_Model_Name": "",
	"Space_Obstacle_Offset": "",
	"Space_Override_Population_Value": "",
	"Space_Victory_Relevant": "",
	"Spawn_Indigenous_Units_Chance": "",
	"Spawn_Indigenous_Units_In_Packs": "",
	"Spawn_Indigenous_Units_Radius": "",
	"Spawned_Indigenous_Pack_Type": "",
	"Spawned_Indigenous_Units_Delay_Seconds": "",
	"Spawned_Indigenous_Units_Quantity": "",
	"Spawned_Indigenous_Units_Type": "",
	"Spawned_Object_Type": "",
	"Spawned_Squadron_Delay_Seconds": "",
	"Special_Structures": "",
	"Special_Weapon_Index": "",
	"Special_Weapon_Target_Action_Index": "",
	"Special_Weapon_Valid_Targets": "",
	"Spin_Away_On_Death": "",
	"Spin_Away_On_Death_Chance": "",
	"Spin_Away_On_Death_Explosion": "",
	"Spin_Away_On_Death_SFXEvent_Start_Die": "",
	"Spin_Away_On_Death_Time": "",
	"Squadron_Capacity": "",
	"Squadron_Formation_Error_Tolerance": "",
	"Squadron_Offsets": "",
	"Squadron_Units": "",
	"Starting_Spawned_Units_Tech_0": "",
	"Stay_In_Transport_During_Ground_Battle": "",
	"Stealth_Capable": "",
	"Stopped_Rate_Of_Turn": "",
	"Strafe_Distance": "",
	"SurfaceFX_Name": "",
	"Surface_Type_Cover_Damage_Shield": "",
	"TSW_Attack_Anim_Duration_Seconds": "",
	"TSW_Attack_Distance_From_Target": "",
	"TSW_Explosion_Debris_Creation_Frame_Delay": "",
	"TSW_MusicEvent_Activation_Start": "",
	"TSW_Post_Destruction_Wait_Frames": "",
	"TSW_Post_Music_Wait_Frames": "",
	"TSW_Power_Up_Countdown_Seconds": "",
	"TSW_SFXEvent_Activate_Voice": "",
	"TSW_SFXEvent_GUI_Bttton_Press": "",
	"TSW_SFXEvent_Weapon_Power_Up": "",
	"TSW_Start_Distance_From_Target": "",
	"TSW_Start_Pos_Match_Targets_Z": "",
	"TSW_Z_Adjust_Relative_To_Target_Pos": "",
	"TacticalBehavior": "",
	"Tactical_Additional_Structure_Type": "",
	"Tactical_Build_Cost_Campaign": "",
	"Tactical_Build_Cost_Multiplayer": "",
	"Tactical_Build_Prerequisites": "",
	"Tactical_Build_Time_Seconds": "",
	"Tactical_Buildable_Objects_Campaign": "",
	"Tactical_Buildable_Objects_Multiplayer": "",
	"Tactical_Health": "",
	"Tactical_Production_Queue": "",
	"Target_Bones": "",
	"Target_Particle_Bone_Name": "",
	"Target_Particle_Effect": "",
	"Target_Types": "",
	"Targeting_Allowed_When_Burning": "",
	"Targeting_Fire_Inaccuracy": "",
	"Targeting_Max_Attack_Distance": "",
	"Targeting_Min_Attack_Distance": "",
	"Targeting_Priority_Set": "",
	"Targeting_Scan_Range": "",
	"Targeting_Stickiness_Time_Threshold": "",
	"Tech_Level": "",
	"Terrain": "",
	# "Text_ID": "",
	"Transport_Capacity": "",
	"Turret_Bone_Name": "",
	"Turret_Elevate_Extent_Degrees": "",
	"Turret_Rotate_Extent_Degrees": "",
	"Turret_Rotate_Speed": "",
	"Turret_Targets_Air_Vehicles": "",
	"Turret_Targets_Anything_Else": "",
	"Turret_Targets_Ground_Infantry": "",
	"Turret_Targets_Ground_Vehicles": "",
	# "Type": "",
	"UnitCollisionClass": "",
	"Use_Special_Submit_Rules": "",
	"User_Bound_Max": "",
	"User_Bound_Min": "",
	"Uses_Multiple_Locomotors": "",
	"Variant_Of_Existing_Type": "",
	"Vehicle_Thief_Inside_Clone": "",
	"Victory_Relevant": "",
	"Visible_On_Radar_When_Fogged": "",
	"Visible_To_Enemies_When_Empty": "",
	"Walk_Transition": "",
	"Weapon_Quantity": "",
	"Weapon_Type": "",
	"Weather_Category": "",
	"Wind_Disturbance_Radius": "",
	"Wind_Disturbance_Sphere_Alpha": "",
	"Wind_Disturbance_Strength": "",

	# HeroClashType SubNodes
	# "Attribute - Name": "",
	"Clash_Range": "",
	"Clash_Type": "",
	"Combat_Distance": "",
	"Damage_Amount": "",
	"Damage_Percentage": "",
	"First_Hero_Conversation_Anim_Type": "",
	"First_Hero_Damage_Multiplier": "",
	"First_Hero_Draw_Anim_Type": "",
	"First_Hero_Lose_Anim_Type": "",
	"First_Hero_Type": "",
	"First_Hero_Win_Anim_Type": "",
	"First_Hero_Win_Exchange_Chance": "",
	"First_Hero_Win_Speech": "",
	"Involved_Hero_Types": "",
	"Play_Conversation_Events": "",
	"Second_Hero_Conversation_Anim_Type": "",
	"Second_Hero_Damage_Multiplier": "",
	"Second_Hero_Draw_Anim_Type": "",
	"Second_Hero_Lose_Anim_Type": "",
	"Second_Hero_Type": "",
	"Second_Hero_Win_Anim_Type": "",
	"Second_Hero_Win_Exchange_Chance": "",
	"Second_Hero_Win_Speech": "",

	# SFXEvent SubNodes
	# "Attribute - Name": "",
	"Chained_SFXEvent": "",
	# "File": "",
	"Is_2D": "",
	"Is_3D": "",
	"Is_GUI": "",
	"Is_Preset": "",
	"Localize": "",
	"Max_Instances": "",
	"Max_Pitch": "",
	"Max_Predelay": "",
	"Max_Volume": "",
	"Min_Pitch": "",
	"Min_Predelay": "",
	"Min_Volume": "",
	"Overlap_Test": "",
	"Play_Count": "",
	"Play_Sequentially": "",
	"Priority": "",
	"Probability": "",
	"Samples": "",
	# "Text_ID": "",
	"Use_Preset": "",
	"Volume_Saturation_Distance": "",

	# TerrainDecalFX SubNodes
	# "Attribute - Name": "",
	"Category": "",
	"Fadeout_Time": "",
	# "Intensity": "",
	"Permanent": "",
	# "Render_Mode": "",
	"Scale": "",
	"UV_Slot": "",
	"Z_Angle": "",

	# LightningTypeManager SubNodes
	# "Attribute - Name": "",
	"Bolt_Creation_Interval_Max": "",
	"Bolt_Creation_Interval_Min": "",
	"Color_End": "",
	"Color_Start": "",
	"Detail": "",
	"Displace": "",
	"Fadeout_Time_Max": "",
	"Fadeout_Time_Min": "",
	"Number_Bolts": "",
	"Texture_Name": "",
	"Texture_Repeat": "",
	"Texture_Scroll": "",
	"Width_Max": "",
	"Width_Min": "",


	# DynamicTrackFX SubNodes
	# "Attribute - Name": "",
	# "Render_Mode": "",
	"fade_begin_distance": "",
	"fade_distance_per_second": "",
	"fade_end_distance": "",
	"min_geometry_lod": "",
	"opacity": "",
	"segment_length": "",
	"texture_name": "",
	"width": "",

	# MusicEvent SubNodes
	# "Attribute - Name": "",
	"Fade_In_Seconds": "",
	"Fade_Out_Previous_Seconds": "",
	# "Files": "",
	"Loop": "",
	# "Volume_Percent": "",

	# SpeechEvent SubNodes
	# "Attribute - Name": "",
	# "Files": "",
	# "Text_ID": "",
	# "Volume_Percent": "",

	# GameConstants SubNodes
	"AITechLevelProductionTimeWeight": "",
	"AIUsesFogOfWarGalactic": "",
	"AIUsesFogOfWarLand": "",
	"AIUsesFogOfWarSpace": "",
	"AI_BuildTaskReservationSeconds": "",
	"AI_FogCellsPerThreatCell": "",
	"AI_LandAreaThreatScaleFactor": "",
	"AI_LandEvaluatorRegionSize": "",
	"AI_LandThreatDistanceFactor": "",
	"AI_LandThreatLookAheadTime": "",
	"AI_LandThreatTurnRateFactor": "",
	"AI_SpaceAreaThreatScaleFactor": "",
	"AI_SpaceEvaluatorRegionSize": "",
	"AI_SpaceThreatDecayStep": "",
	"AI_SpaceThreatDistanceFactor": "",
	"AI_SpaceThreatLookAheadTime": "",
	"AI_SpaceThreatTurnRateFactor": "",
	"Activated_Destroy_Planet_Ability_Names": "",
	"Activated_Neutralize_Hero_Ability_Names": "",
	"Activated_Sabotage_Ability_Names": "",
	"Activated_Siphon_Credits_Ability_Names": "",
	"Activated_Slice_Ability_Names": "",
	"Activated_System_Spy_Ability_Names": "",
	"Advisor_Hint_Duration": "",
	"Advisor_Hint_Interval": "",
	"Allow_Reinforcement_Percentage_Normalized": "",
	"AlwaysBypassAutoResolve": "",
	"Animate_During_Galactic_Mode_Pause": "",
	"ApproximationForwardDistance": "",
	"ApproximationSmoothCosAngle": "",
	"Armor_Types": "",
	"Asteroid_Field_Damage": "",
	"Asteroid_Field_Damage_Rate": "",
	"AutoResolveAttritionAllowanceFactor": "",
	"AutoResolveDisplayTime": "",
	"AutoResolveLoserAttrition": "",
	"AutoResolveTransportLosses": "",
	"AutoResolveVoteDefaultTimeOut": "",
	"AutoResolveVoteDefaultToTactical": "",
	"AutoResolveWinnerAttrition": "",
	"Auto_Resolve_Tactical_Multiplier": "",
	"Auto_Rotate_For_Space_Targeting": "",
	"AutomaticAutoResolve": "",
	"Base_Land_Targeting_Arc_Angle_Coefficient": "",
	"Base_Shield_Delay_Time": "",
	"Base_Shield_Speed_Modifier": "",
	"Base_Shield_Vulnerability_Modifier": "",
	"Battle_Load_Planet_Ambient": "",
	"Battle_Load_Planet_Direction": "",
	"Battle_Load_Planet_Viewport": "",
	"Battle_Pending_Message_Color": "",
	"Battle_Pending_Message_Font": "",
	"Battle_Pending_Message_Font_Size": "",
	"Battle_Pending_Message_Pos_X": "",
	"Battle_Pending_Message_Pos_Y": "",
	"Battle_Pending_Timeout_Seconds": "",
	"BeaconPlaceDelay": "",
	"BetweenFormationSpacing": "",
	"Bink_Player_Caption_Font_Name": "",
	"Bink_Player_Caption_Font_Size": "",
	"Black_Market_Income_Mult_Max": "",
	"Black_Market_Income_Mult_Min": "",
	"Blockade_Run_Attrition_Factor": "",
	"Bombing_Run_Reduction_Per_Squadron_Percent": "",
	"CB_Flash_Count": "",
	"CB_Flash_Duration": "",
	"CB_Movie_Color": "",
	"CB_Movie_Offset": "",
	"Camera_FX_Manager_Letterbox_Height": "",
	"Camera_Stop_Left": "",
	"Camera_Stop_Right": "",
	"Camera_Z_Position": "",
	"CloseEnoughAngleForMoveStart": "",
	"Command_Bar_Default_Font_Name": "",
	"Command_Bar_Default_Font_Size": "",
	"Control_Point_Domination_Victory_Time_In_Secs": "",
	"Countdowns_Font_Name": "",
	"Countdowns_Font_Size": "",
	"Credit_Cap_Per_Planet": "",
	"Credits_Bottom_Color": "",
	"Credits_Display_Font_Name": "",
	"Credits_Display_Font_Size": "",
	"Credits_Font": "",
	"Credits_Font_Size": "",
	"Credits_Header_Bottom_Color": "",
	"Credits_Header_Top_Color": "",
	"Credits_Logo_1_Height": "",
	"Credits_Logo_1_Name": "",
	"Credits_Logo_1_Width": "",
	"Credits_Logo_1_Y_Offset": "",
	"Credits_Logo_2_Height": "",
	"Credits_Logo_2_Name": "",
	"Credits_Logo_2_Width": "",
	"Credits_Logo_2_Y_Offset": "",
	"Credits_Logo_3_Height": "",
	"Credits_Logo_3_Name": "",
	"Credits_Logo_3_Width": "",
	"Credits_Logo_3_Y_Offset": "",
	"Credits_Margin": "",
	"Credits_Scroll_Rate": "",
	"Credits_Spacing": "",
	"Credits_Top_Color": "",
	"CrouchIdleWalkBlendTime": "",
	"CrouchMoveBlendTime": "",
	"Crouch_Move_Fire_Angle_Cutoff": "",
	"CurrentPathCostCoefficientSpace": "",
	"Damage_To_Armor_Mod": "",
	"Damage_Types": "",
	"Default_Defense_Adjust": "",
	"Default_Hero_Respawn_Time": "",
	"Demo_Attract_Map_Cycle_Delay_Seconds": "",
	"Demo_Attract_Maps": "",
	"Demo_Attract_Start_Timeout_Seconds": "",
	"Depleted_Shield_Damage_Increment": "",
	"Depleted_Shield_Disable_Time": "",
	"Depleted_Shield_Regen_Cap": "",
	"DesiredLandFOWCellSize": "",
	"DesiredSpaceFOWCellSize": "",
	"DestinationSearchRadiusIncrementSpace": "",
	"Destination_Collision_Query_Extension": "",
	"Diminishing_Firepower": "",
	"Display_Bink_Movie_Frames": "",
	"Distribute_Credit_Quantum": "",
	"DoubleClickMoveMaxSpeedRatio": "",
	"Droid_Date_Color": "",
	"Droid_Encyclopedia_Offset": "",
	"Droid_Seperator_Color": "",
	"Droid_Text_Color": "",
	"DynamicAvoidanceRectangleBound": "",
	"DynamicLandComplexityQuota": "",
	"DynamicLandQuotaResetInterval": "",
	"DynamicObstacleOverlapPenalty": "",
	"Earthquake_Shake_Magnitude": "",
	"Earthquake_Shake_Speed": "",
	"Earthquake_Transition_Time": "",
	"Elevated_Vulnerability_Duration": "",
	"Elevated_Vulnerability_Factor": "",
	"Encyclopedia_Class_Y_Offset": "",
	"Encyclopedia_Cost_Offset": "",
	"Encyclopedia_Delay": "",
	"Encyclopedia_Fade_Rate": "",
	"Encyclopedia_Icon_X_Offset": "",
	"Encyclopedia_Icon_Y_Offset": "",
	"Encyclopedia_Min_Display_Time": "",
	"Encyclopedia_Name_Offset": "",
	"Encyclopedia_Population_Offset": "",
	"Enemy_Color": "",
	"EnergyRechargeIntervalInSecs": "",
	"EnergyToShieldExchangeRate": "",
	"Energy_Beam_Color": "",
	"Energy_Beam_Frames": "",
	"Energy_Beam_Texture": "",
	"Energy_Beam_Width": "",
	"Engines_Disabled_Speed_Modifier": "",
	"Event_Message_Default_Font_Name": "",
	"Event_Message_Default_Font_Size": "",
	"Evil_Side_Leader_Name": "",
	"Evil_Side_Name": "",
	"FinalFacing180Penalty": "",
	"FinalFormationFacingDeltaCoefficient": "",
	"FinalFormationFacingMinimumAngle": "",
	"Fiscal_Cycle_Time_In_Secs": "",
	"Fleeing_Infantry_Speed_Bonus": "",
	"Fleet_Hyperspace_Band_Texture_Name": "",
	"Fleet_Maintenance_Update_Delay_Seconds": "",
	"Fleet_Movement_Line_Texture_Name": "",
	"FormationMaximumSideError": "",
	"FormationMinimumSideError": "",
	"FramesPerCollisionCheck": "",
	"FramesPerPositionApproximationRebuild": "",
	"GMC_Battle_Fade_Time": "",
	"GMC_Battle_Zoom_Time": "",
	"GMC_InitialPitchAngleDegrees": "",
	"GMC_InitialPullbackDistance": "",
	"GMC_ZoomTime": "",
	"GMC_ZoomedPitchAngleDegrees": "",
	"GMC_ZoomedPositionOffsetPlanetRadiusFractions": "",
	"GMC_ZoomedPullbackPlanetRadiusFraction": "",
	"GUI_Attack_Move_Command_Ack_Effect": "",
	"GUI_Attack_Movement_Click_Radar_Event_Name": "",
	"GUI_Cycle_Color": "",
	"GUI_Cycle_Speed": "",
	"GUI_Darken_Level": "",
	"GUI_Double_Click_Move_Command_Ack_Effect": "",
	"GUI_Flash_Duration": "",
	"GUI_Flash_Level": "",
	"GUI_Guard_Move_Command_Ack_Effect": "",
	"GUI_Hilite_Level": "",
	"GUI_Move_Acknowledge_Scale_Land": "",
	"GUI_Move_Acknowledge_Scale_Space": "",
	"GUI_Move_Command_Ack_Effect": "",
	"GUI_Movement_Click_Radar_Event_Name": "",
	"GUI_Movement_Double_Click_Radar_Event_Name": "",
	"GUI_Planet_Fade_Duration": "",
	"GUI_Planet_Flash_Level": "",
	"GUI_Rapid_Flash_Duration": "",
	"GUI_Strategic_Countdown_Timers_Screen_Spacing": "",
	"GUI_Strategic_Countdown_Timers_Screen_X": "",
	"GUI_Strategic_Countdown_Timers_Screen_Y": "",
	"GUI_Tactical_Countdown_Timers_Screen_Spacing": "",
	"GUI_Tactical_Countdown_Timers_Screen_X": "",
	"GUI_Tactical_Countdown_Timers_Screen_Y": "",
	"Galactic_Right_Button_Scroll_Speed_Factor": "",
	"Galactic_Scroll_Plane": "",
	"Galactic_Zoom_Acceleration": "",
	"Galactic_Zoom_In_Light_Angle": "",
	"Galactic_Zoom_In_Station_Offset": "",
	"Galactic_Zoom_In_Station_Rotation": "",
	"Galactic_Zoom_Light_Level": "",
	"Galactic_Zoom_Out_Light_Angle": "",
	"Game_Object_Name_Font_Name": "",
	"Game_Object_Name_Font_Size": "",
	"Game_Scoring_Script_Name": "",
	"Good_Ground_Color_Tint": "",
	"Good_Side_Leader_Name": "",
	"Good_Side_Name": "",
	"GripperCombatGridSnapDistance": "",
	"HardPoint_Target_Reticle_Enemy_Screen_Size": "",
	"HardPoint_Target_Reticle_Enemy_Texture": "",
	"HardPoint_Target_Reticle_Enemy_Tracked_Texture": "",
	"HardPoint_Target_Reticle_Friendly_Disabled_Texture": "",
	"HardPoint_Target_Reticle_Friendly_Disabled_Tracked_Texture": "",
	"HardPoint_Target_Reticle_Friendly_Repairing_Texture": "",
	"HardPoint_Target_Reticle_Friendly_Screen_Size": "",
	"HardPoint_Target_Reticle_Friendly_Texture": "",
	"HardPoint_Target_Reticle_Friendly_Tracked_Texture": "",
	"Hardpoint_Recharge_Cutoff_For_Opportunity_Fire": "",
	"Health_Bar_Scale": "",
	"Health_Bar_Spacing": "",
	"Health_Critical_Percent_Threshold": "",
	"Health_Low_Percent_Threshold": "",
	"High_Threat_Reachability_Tolerance": "",
	"Hint_Text_Color": "",
	"Hull_Vs_Hard_Points_Health_Constraint": "",
	"Icons_Per_Column": "",
	"IdleMovementFrames": "",
	"IdleWalkBlendTime": "",
	"In_Game_Cinematics": "",
	"In_Game_Message_Default_Font_Name": "",
	"In_Game_Message_Default_Font_Size": "",
	"Income_Redistribution": "",
	"Indigenous_Spawn_Destruction_Reward": "",
	"InfantryFormationRecruitmentDistance": "",
	"InfantryTurnBlendTime": "",
	"Ion_Storm_Shield_Disable_Time": "",
	"Japanese_Line_Percent": "",
	"Japanese_ST_Line_Percent": "",
	"LandDestinationProximity": "",
	"LandFOWColor": "",
	"LandFOWRegrowTime": "",
	"LandObjectTrackingInterval": "",
	"LandObjectTrackingTreeCount": "",
	"LandPredictionTimeInterval": "",
	"LandTemporaryDestinationProximity": "",
	"LandWaitOperatorSpeedCoefficient": "",
	"Land_Auto_Resolve_Delay_Seconds": "",
	"Land_Base_Destruction_Forces_Retreat": "",
	"Land_Capture_Allowed_Countdown_Seconds": "",
	"Land_Collidable_Grid_Cull_Size": "",
	"Land_Guard_Range": "",
	"Land_Health_Bar_Scale": "",
	"Land_Retreat_Allowed_Countdown_Seconds": "",
	"Land_Retreat_Attrition_Factor": "",
	"Land_Tactical_Camera_Locked": "",
	"Large_Coin_Stack_Size": "",
	"Laser_Beam_Z_Scale_Factor": "",
	"Laser_Kite_Z_Scale_Factor": "",
	"Left_Queue_Tint": "",
	"Localized_Menu_Overlay": "",
	"Localized_Splash_Screen": "",
	"Localized_UK_English_Splash_Screen": "",
	"Long_Encyclopedia_Delay": "",
	"LoopWaypointLineTextureName": "",
	"Lose_Message_Color": "",
	"Low_Threat_Reachability_Tolerance": "",
	"MP_Color_Blue": "",
	"MP_Color_Cyan": "",
	"MP_Color_Gray": "",
	"MP_Color_Green": "",
	"MP_Color_Orange": "",
	"MP_Color_Purple": "",
	"MP_Color_Red": "",
	"MP_Color_Yellow": "",
	"MP_Default_Allow_Auto_Resolve": "",
	"MP_Default_Allow_Heroes": "",
	"MP_Default_Allow_Random_Events": "",
	"MP_Default_Allow_SuperWeapons": "",
	"MP_Default_Credits": "",
	"MP_Default_Free_Starting_Units": "",
	"MP_Default_Game_Timer": "",
	"MP_Default_Land_Tactical_Win_Condition": "",
	"MP_Default_Max_Tech_Level": "",
	"MP_Default_Pre_Built_Base": "",
	"MP_Default_Space_Tactical_Win_Condition": "",
	"MP_Default_Start_Tech_Level": "",
	"MP_Default_Win_Condition": "",
	"MP_Default_Win_Condition_Float_Param": "",
	"MP_Default_Win_Condition_Int_Param": "",
	"Main_Menu_Demo_Attract_Mode": "",
	"Map_Preview_Image_Size": "",
	"MatchFacingDeltaSpace": "",
	"MaxCombatAccuracyAlignmentBonus": "",
	"MaxCombatDamageAlignmentBonus": "",
	"MaxCombatSensorRangeAlignmentBonus": "",
	"MaxCreditIncomeAlignmentBonus": "",
	"MaxCreditIncomeAlignmentPenalty": "",
	"MaxInfluenceTransitionAlignmentBonus": "",
	"MaxInfluenceTransitionAlignmentPenalty": "",
	"MaxLandFormationFormupFrames": "",
	"MaxObstacleCostLand": "",
	"MaxObstacleCostSpace": "",
	"MaxRotationsSpace": "",
	"MaxWaypointsPerPath": "",
	"Max_Bombing_Run_Interval_Seconds": "",
	"Max_Formation_Area": "",
	"Max_Galactic_Zoom_Distance": "",
	"Max_Galactic_Zoom_Speed": "",
	"Max_Ground_Forces_On_Planet": "",
	"Max_Move_Frame_Delay": "",
	"Max_Skirmish_Credits": "",
	"MaximumFleetMovementDistance": "",
	"MaximumGroundbaseLevel": "",
	"MaximumPoliticalControl": "",
	"MaximumSpecialStructures": "",
	"MaximumSpecialStructuresLand": "",
	"MaximumSpecialStructuresSpace": "",
	"MaximumStarbaseLevel": "",
	"Medium_Coin_Stack_Size": "",
	"Medium_Threat_Reachability_Tolerance": "",
	"Melee_Cutoff_Range": "",
	"Message_Of_The_Day_URL": "",
	"MinLandPredictionDistance": "",
	"MinObstacleCostLand": "",
	"MinObstacleCostSpace": "",
	"Min_Accuracy_For_Icon": "",
	"Min_Bombing_Run_Interval_Seconds": "",
	"Min_Galactic_Zoom_Speed": "",
	"Min_Health_Bar_Scale": "",
	"Min_Sight_Range_For_Icon": "",
	"Min_Skirmish_Credits": "",
	"MinimumDragDistance": "",
	"MinimumDragSelectDistance": "",
	"MinimumStoppedVsStoppedOverlapCoefficient": "",
	"Minimum_Tactical_Overrun_Time_In_Secs": "",
	"Mouse_Over_Highlight_Scale": "",
	"MoveBlendTime": "",
	"MovementReevaluationFrameCount": "",
	"MovingVsMovingLookAheadTime": "",
	"Multiplayer_Losing_Team_Bonus_Credit_Percentage": "",
	"Nebula_Ability_Disable_Time": "",
	"Nebula_Effect_Color": "",
	"Neutral_UI_Color": "",
	"Num_Structures_For_Large_Planet_Name": "",
	"Num_Structures_For_Medium_Planet_Name": "",
	"Object_Max_Health_Multiplier_Land": "",
	"Object_Max_Health_Multiplier_Space": "",
	"Object_Max_Speed_Multiplier_Galactic": "",
	"Object_Max_Speed_Multiplier_Land": "",
	"Object_Max_Speed_Multiplier_Space": "",
	"Object_Visual_Status_Particle_Attach_Bone_Names": "",
	"ObstacleAreaOverlapForMaxSpace": "",
	"Occlusion_Silhouettes_Enabled": "",
	"OccupationRadiusCoefficientSpace": "",
	"OffMapCostPenalty": "",
	"Override_Death_Persistence_Duration": "",
	"Pay_As_You_Go": "",
	"Planet_Ability_Icon_Names": "",
	"Planet_Ability_RGBs": "",
	"Planet_Ability_Text_IDs": "",
	"Planet_Reveal_Delay_Time": "",
	"PlayModeSwitchMovies": "",
	"Player_Color": "",
	"Political_Control_Change_Time_Seconds": "",
	"Political_Income_Curve": "",
	"Preferred_Pathfinder_Types": "",
	"Production_Speed_Factor": "",
	"Production_Speed_Mod_Base_Vs_Tech_0": "",
	"Production_Speed_Mod_Base_Vs_Tech_1": "",
	"Production_Speed_Mod_Base_Vs_Tech_2": "",
	"Production_Speed_Mod_Base_Vs_Tech_3": "",
	"Production_Speed_Mod_Base_Vs_Tech_4": "",
	"Progressive_Taxation": "",
	"Push_Scroll_Speed_Modifier": "",
	"Quickmatch_Map_Exclusion_List": "",
	"Radar_Colorize_Multiplayer_Enemy": "",
	"Radar_Colorize_Selected_Units": "",
	"Radar_Multiplayer_Enemy_Color": "",
	"Radar_Selected_Units_Color": "",
	"Raid_Force_Free_Object_Category_Mask": "",
	"Raid_Force_Limited_Object_Category_Mask": "",
	"Raid_Force_Max_Heros": "",
	"Raid_Force_Max_Limited_Objects": "",
	"Raid_Force_Required_Faction": "",
	"Random_Story_Empire_Construction": "",
	"Random_Story_Empire_Destroy": "",
	"Random_Story_Max_Triggers": "",
	"Random_Story_Rebel_Construction": "",
	"Random_Story_Rebel_Destroy": "",
	"Random_Story_Reward_Empire_Buildable": "",
	"Random_Story_Reward_Empire_Unit": "",
	"Random_Story_Reward_Rebel_Buildable": "",
	"Random_Story_Reward_Rebel_Unit": "",
	"Random_Story_Rewards": "",
	"Random_Story_Triggers": "",
	"ReinforcementOverlayBadColor": "",
	"ReinforcementOverlayGoodColor": "",
	"RepushDistance": "",
	"RetreatAutoResolveLoserAttrition": "",
	"RetreatAutoResolveWinnerAttrition": "",
	"Right_Queue_Tint": "",
	"Rotate_Formation_Facing_Moves": "",
	"Saliency_Health": "",
	"Saliency_Power": "",
	"Saliency_Size": "",
	"Saliency_Speed": "",
	"Saliency_Targets": "",
	"Saliency_X": "",
	"Saliency_Y": "",
	"Scroll_Acceleration_Factor": "",
	"Scroll_Deceleration_Factor": "",
	"SetupPhaseCountdownSeconds": "",
	"SetupPhaseEnabled": "",
	"SetupPhaseFOWColor": "",
	"SetupPhaseInvalidDragColor": "",
	"ShieldRechargeIntervalInSecs": "",
	"Shield_Flash_Duration": "",
	"Shield_Flash_Scale": "",
	"ShipNameTextFiles": "",
	"Ships_Per_Stack": "",
	"Short_Range_Attack_Formation_Coefficient": "",
	"ShouldDisplayPotentialPath": "",
	"ShouldDisplayPredictionPaths": "",
	"ShouldDisplaySyncedPaths": "",
	"ShouldInfantryTeamsSplitAcrossFormations": "",
	"ShouldSkipLandFormup": "",
	"ShouldUseSpaceIdleMovement": "",
	"ShowUnitAIPlanAttachment": "",
	"Skirmish_Buy_Credits": "",
	"Skirmish_Reinforcement_Delay_Frames": "",
	"Solo_Attack_Range": "",
	"SpaceFOWColor": "",
	"SpaceFOWHeight": "",
	"SpaceFOWRegrowTime": "",
	"SpaceIdleMovementSpeed": "",
	"SpaceIdlePathCullCoefficient": "",
	"SpaceLocomotorFacingLookaheadAcc": "",
	"SpaceObjectTrackingInterval": "",
	"SpaceObjectTrackingTreeCount": "",
	"SpacePathFailureDistanceCutoffCoefficient": "",
	"SpacePathFailureForwardExpansionIncrement": "",
	"SpacePathFailureMaxExpansionsCoefficient": "",
	"SpacePathFailureRotationExpansionIncrement": "",
	"SpacePathfindFrameDelayDelta": "",
	"SpacePathfindMaxExpansions": "",
	"SpacePathingTries": "",
	"SpaceReinforceFOWColor": "",
	"SpaceReinforceFeedbackOnlyWhileDragging": "",
	"SpaceStaticObstacleAvoidanceBonusDistance": "",
	"Space_Auto_Resolve_Delay_Seconds": "",
	"Space_Capture_Allowed_Countdown_Seconds": "",
	"Space_Collidable_Grid_Cull_Size": "",
	"Space_Elevated_Vulnerability_Duration": "",
	"Space_Elevated_Vulnerability_Factor": "",
	"Space_Guard_Range": "",
	"Space_Large_Ship_Grid_Cull_Size": "",
	"Space_Reinforcement_Collision_Check_Distance": "",
	"Space_Retreat_Allowed_Countdown_Seconds": "",
	"Space_Retreat_Attrition_Factor": "",
	"Space_Station_Destruction_Forces_Retreat": "",
	"Space_Tactical_Camera_Locked": "",
	"SpecialAlignedOperatorBonus": "",
	"Speech_Text_Color": "",
	"Spread_Out_Spacing_Coefficient": "",
	"Star_Wars_Crawl_Start_Fadeout_Frame": "",
	"Starting_Galactic_Camera_Position": "",
	"Strategic_Edge_Scroll_Region": "",
	"Strategic_Max_Scroll_Speed": "",
	"Strategic_Min_Scroll_Speed": "",
	"Strategic_Offscreen_Scroll_Region": "",
	"Strategic_Queue_Tactical_Battles": "",
	"SyncedFrameInterval": "",
	"System_Text_Color": "",
	"Tactical_Build_Time_Multiplier": "",
	"Tactical_Edge_Scroll_Region": "",
	"Tactical_Max_Scroll_Speed": "",
	"Tactical_Min_Scroll_Speed": "",
	"Tactical_Offscreen_Scroll_Region": "",
	"Tactical_Overrun_Multiple": "",
	"Task_Text_Color": "",
	"TeamCrouchMoveBlendTime": "",
	"TeamMoveBlendTime": "",
	"Team_Healthbar_Offset": "",
	"Telekinesis_Hover_Height": "",
	"Telekinesis_Max_Bob_Height": "",
	"Telekinesis_Max_Wobble_Angle": "",
	"Telekinesis_Transition_Time": "",
	"Telekinesis_Wobble_Cycle_Time": "",
	"Telekinesis_Wobble_Fade_Time": "",
	"Terrain_Resurface_Rand": "",
	"Terrain_Resurface_Tolerance": "",
	"Text_Button_Default_Font_Name": "",
	"Text_Button_Default_Font_Size": "",
	"Text_Reveal_Rate": "",
	"ThreatExpansionDistance": "",
	"Tool_Tip_Font_Name": "",
	"Tool_Tip_Font_Size": "",
	"Tool_Tip_Small_Font_Name": "",
	"Tool_Tip_Small_Font_Size": "",
	"Tooltip_Delay": "",
	"Tractor_Beam_Color": "",
	"Tractor_Beam_Frames": "",
	"Tractor_Beam_Texture": "",
	"Tractor_Beam_Width": "",
	"TradeRouteMovementFactor": "",
	"TurnInPlaceSlowdownCapital": "",
	"TurnInPlaceSlowdownCorvette": "",
	"TurnInPlaceSlowdownFrigate": "",
	"Under_Construction_Damage_Multiplier": "",
	"Unit_Command_Rankings_By_Category": "",
	"UseLinearCollisionChecks": "",
	"Use_Neutral_UI_Color": "",
	"Use_Reinforcement_Points": "",
	"VehicleFormationRecruitmentDistance": "",
	"WaitOperatorBaseFrameTime": "",
	"WaitOperatorCostCoefficient": "",
	"WaitOperatorSpeedCoefficient": "",
	"WalkAnimationCutoff": "",
	"Water_Clip_Plane_Offset": "",
	"Water_Render_Target_Resolution": "",
	"WaypointFlagModelName": "",
	"WaypointLineLandDashLength": "",
	"WaypointLineLandDashVelocity": "",
	"WaypointLineLandGapLength": "",
	"WaypointLineTextureName": "",
	"Win_Lose_Message_Font": "",
	"Win_Lose_Message_Font_Size": "",
	"Win_Message_Color": "",
	"XYExpansionDistanceLand": "",
	"XYExpansionDistanceSpace": "",

	# CommandBarComponent SubNodes
	# "Attribute - Name": "",
	"Disabled": "",
	# "File": "",
	"Group": "",
	"Hidden": "",
	"Manual_Offset": "",
	"Mega_Texture_Name": "",
	# "Model_Name": "",
	"Model_Offset_X": "",
	"Model_Offset_Y": "",
	# "Type": "",

	# TradeRoute SubNodes
	# "Attribute - Name": "",
	"Credit_Gain_Factor": "",
	# "File": "",
	"HS_Speed_Factor": "",
	"Point_A": "",
	"Point_B": "",
	"Political_Control_Gain": "",
	"Visible_Line_Name": "",

	# TradeRouteLines SubNodes
	# "Attribute - Name": "",
	"Color_Zoomed_In": "",
	"Color_Zoomed_Out": "",
	# "Render_Mode": "",
	"Width": "",

	# RadarMap SubNodes
	# "Attribute - Name": "",
	"Event_Duration": "",
	"Event_Model_Name": "",
	"Event_Model_Scale": "",
	"Event_Single_Instance": "",

	# Draw3DTextCrawl SubNodes
	"Attribute - Language": "",
	# "Attribute - Name": "",
	"Fadein_End_Frame": "",
	"Fadein_Start_Frame": "",
	"Fadeout_Start_Frame": "",
	"Font_Character_Padding": "",
	"Font_Name": "",
	"Font_Size": "",
	"Font_Stretch_Factor": "",
	"Has_Header": "",
	"Header_Font_Name": "",
	"Header_Font_Size": "",
	"Header_Text_IDs": "",
	"Header_Texture_Height_Pow_2": "",
	"Header_Texture_Width_Pow_2": "",
	"Model_Camera_Bone_Name": "",
	# "Model_Name": "",
	"Polygon_Shader_Name": "",
	"Polygon_Tex_Param_Name": "",
	"Text_IDs": "",
	"Texture_Height_Pow_2": "",
	"Texture_Width_Pow_2": "",

	# WeatherPattern SubNodes
	# "Attribute - Name": "",
	"Duration": "",
	"Ease_Out_Duration": "",
	"Emitter_Intensity": "",
	"Lightning_Intensity": "",

	# HardPoint SubNodes
	# "Attribute - Name": "",
	"Attachment_Bone": "",
	"Collision_Mesh": "",
	"Damage_Decal": "",
	"Damage_Particles": "",
	# "Damage_Type": "",
	"Death_Breakoff_Prop": "",
	"Death_Explosion_Particles": "",
	"Death_Explosion_SFXEvent": "",
	"Fire_Bone_A": "",
	"Fire_Bone_B": "",
	"Fire_Cone_Height": "",
	"Fire_Cone_Width": "",
	# "Fire_Inaccuracy_Distance": "",
	"Fire_Max_Recharge_Seconds": "",
	"Fire_Min_Recharge_Seconds": "",
	"Fire_Projectile_Type": "",
	"Fire_Pulse_Count": "",
	"Fire_Pulse_Delay_Seconds": "",
	"Fire_Range_Distance": "",
	"Fire_SFXEvent": "",
	"Health": "",
	"Is_Destroyable": "",
	"Is_Targetable": "",
	"Model_To_Attach": "",
	"Tooltip_Text": "",
	# "Type": "",


	# Campaign SubNodes
	# "Attribute - Name": "",
	"AI_Player_Control": "",
	"Active_Plot": "",
	"Autoresolve_Exclusion_Locations": "",
	"Camera_Distance": "",
	"Camera_Shift_X": "",
	"Camera_Shift_Y": "",
	"Campaign_Set": "",
	"Description_Text": "",
	"Empire_Story_Name": "",
	"Event_Param1": "",
	"Event_Param2": "",
	"Event_Param3": "",
	"Event_Type": "",
	"Evil_Victory_Conditions": "",
	# "File": "",
	"Good_Victory_Conditions": "",
	"Home_Location": "",
	"Is_Autoresolve_Allowed": "",
	"Is_Listed": "",
	"Is_Multiplayer": "",
	"Is_Story_Campaign": "",
	"Locations": "",
	# "Lua_Script": "",
	"Markup_Filename": "",
	"Max_Tech_Level": "",
	"Planet_Auto_Reveal": "",
	"Rebel_Story_Name": "",
	"Show_Completed_Tab": "",
	"Special_Case_Production": "",
	"Starting_Active_Player": "",
	"Starting_Credits": "",
	"Starting_Forces": "",
	"Starting_Tech_Level": "",
	"Story_Chapter": "",
	"Story_Dialog": "",
	"Story_Dialog_Popup": "",
	"Story_Tag": "",
	"Supports_Custom_Settings": "",
	"Suspended_Plot": "",
	# "Text_ID": "",
	"Trade_Routes": "",
	"Tutorial": "",


	# Faction SubNodes
	# "Attribute - Name": "",
	"Allies": "",
	"Alternate_Icon_Name": "",
	"Basic_AI": "",
	"Big_Fleet_Color": "",
	"Bombing_Run_Blob_Size": "",
	"Bombing_Run_Shadow_Blob_Material_Name": "",
	"Can_Control_Planets": "",
	"Can_Win_By_Destroying_Super_Weapon": "",
	"Carrier_Icon_Name": "",
	"Color": "",
	"Corvette_Icon_Name": "",
	"Create_Player_In_Multiplayer_Games": "",
	"Credits_Accumulation_Factor": "",
	"Debug_Ground_Structures": "",
	"Default_Transmission_Message": "",
	"Defeat_Text": "",
	"Display_Font_Color": "",
	"Displayed_Tech_Level_Adjustment": "",
	"Enemies": "",
	"Faction_Leader": "",
	"Faction_Leader_Company": "",
	"Faction_Super_Weapon": "",
	"Fighter_Icon_Name": "",
	# "File": "",
	"Finale_Movie": "",
	"Fleet_Icon_Name": "",
	"Force_Alignment": "",
	"Frigate_Icon_Name": "",
	"Galactic_Advisor_Hints": "",
	"Garrison_Reinforcement_Delay_Seconds": "",
	"Generic_Win_Movie": "",
	"Ground_Base_Icon_Name": "",
	"Ground_Transport_Icon_Name": "",
	"Helper_Icon_Name": "",
	"Hyperspace_Speed_Factor": "",
	# "Icon_Name": "",
	"Infantry_Icon_Name": "",
	"Is_Debug_Switchable_To": "",
	"Is_Neutral": "",
	"Is_Playable": "",
	"Land_Ability_Targeting_Range_Overlay_Material_Name": "",
	"Land_Ability_Targeting_Range_Overlay_RGBA": "",
	"Land_Ability_Targeting_Range_Overlay_Scale_Factor": "",
	"Land_Advisor_Hints": "",
	"Land_Area_Effect_Range_Overlay_Material_Name": "",
	"Land_Area_Effect_Range_Overlay_RGBA": "",
	"Land_Area_Effect_Range_Overlay_Scale_Factor": "",
	"Land_Lose_Image": "",
	"Land_Mode_Garrison_Selection_Blob_Material_Name": "",
	"Land_Mode_Selection_Blob_Material_Name": "",
	"Land_Retreat_Begin_SFXEvent": "",
	"Land_Retreat_Cancel_SFXEvent": "",
	"Land_Retreat_Countdown_Color_RGBA": "",
	"Land_Retreat_Countdown_Seconds": "",
	"Land_Retreat_Countdown_Text_ID": "",
	"Land_Retreat_Enemy_Begin_SFXEvent": "",
	"Land_Retreat_Not_Allowed_Reason_1_SFXEvent": "",
	"Land_Retreat_Not_Allowed_Reason_2_SFXEvent": "",
	"Land_Retreat_Not_Allowed_Reason_3_SFXEvent": "",
	"Land_Retreat_Not_Allowed_SFXEvent": "",
	"Land_Retreat_Pursue_Max_Speed_Mod_Factor": "",
	"Land_Retreat_Units_Damaged_Mod_Factor": "",
	"Land_Skirmish_AI_Default_Forces": "",
	"Land_Skirmish_Unit_Buy_Credits": "",
	"Land_Skirmish_Unit_Cap_By_Player_Count": "",
	"Land_Surrender_SFXEvent": "",
	"Land_Win_Image": "",
	# "Maintenance_Cost": "",
	"Minimum_Visible_Base_Level": "",
	"Multiplayer_Beacon_Type": "",
	"Multiplayer_Campaign_Heroes": "",
	"Music_Event_Battle_Load_Screen": "",
	"Music_Event_Land_Ambient_Super_Weapon": "",
	"Music_Event_Land_Battle_Super_Weapon": "",
	"Music_Event_List_Ambient": "",
	"Music_Event_List_Battle": "",
	"Music_Event_Space_Ambient_Super_Weapon": "",
	"Music_Event_Space_Battle_Super_Weapon": "",
	"Music_Event_Strategic_Lose": "",
	"Music_Event_Strategic_Win": "",
	"Music_Event_Tactical_Land_Battle_Pending": "",
	"Music_Event_Tactical_Lose": "",
	"Music_Event_Tactical_Space_Battle_Pending": "",
	"Music_Event_Tactical_Win": "",
	# "No_Colorization_Color": "",
	"Planet_Icon_Offset": "",
	"Planet_Icon_Scale": "",
	"Primary_Enemy": "",
	"Reinforcements_Cancelled_SFXEvent": "",
	"Reinforcements_Enroute_SFXEvent": "",
	"Reinforcements_Pick_Landing_Zone_SFXEvent": "",
	"Reinforcements_Ready_SFXEvent": "",
	"Reinforcements_Requesting_SFXEvent": "",
	"Reinforcements_Selection_SFXEvent": "",
	"Reinforcements_Shadow_Blob_Material_Name": "",
	"SFXEvent_Arrive_From_Hyperspace": "",
	"SFXEvent_Base_Shield_Absorb_Damage": "",
	"SFXEvent_Bombing_Run_Ally_Available": "",
	"SFXEvent_Bombing_Run_Available": "",
	"SFXEvent_Bombing_Run_Begin_Crosstalk": "",
	"SFXEvent_Bombing_Run_Cancelled": "",
	"SFXEvent_Bombing_Run_Enemy_Available": "",
	"SFXEvent_Build_Impossible_Location_Blockaded": "",
	"SFXEvent_Enemy_Fleet_Approaching_Planet": "",
	"SFXEvent_Enemy_Spotted": "",
	"SFXEvent_Exit_Into_Hyperspace": "",
	"SFXEvent_GUI_Enemy_Toggle_Non_Hero_Ability_Off": "",
	"SFXEvent_GUI_Enemy_Toggle_Non_Hero_Ability_On": "",
	"SFXEvent_GUI_Start_Campaign": "",
	"SFXEvent_GUI_Toggle_Non_Hero_Ability_Off": "",
	"SFXEvent_GUI_Toggle_Non_Hero_Ability_On": "",
	"SFXEvent_HUD_Advisor_Hint": "",
	"SFXEvent_HUD_Advisor_Message": "",
	"SFXEvent_HUD_Advisor_Urgent": "",
	"SFXEvent_HUD_Base_Shield_Offline": "",
	"SFXEvent_HUD_Base_Shield_Online": "",
	"SFXEvent_HUD_Base_Shield_Penetrated": "",
	"SFXEvent_HUD_Build_Pad_Captured": "",
	"SFXEvent_HUD_Build_Pad_Lost": "",
	"SFXEvent_HUD_Enemy_Base_Shield_Offline": "",
	"SFXEvent_HUD_Enemy_Base_Shield_Online": "",
	"SFXEvent_HUD_Enemy_Base_Shield_Penetrated": "",
	"SFXEvent_HUD_Enemy_Special_Weapon_Charging": "",
	"SFXEvent_HUD_Enemy_Special_Weapon_Firing": "",
	"SFXEvent_HUD_Enemy_Special_Weapon_Ready": "",
	"SFXEvent_HUD_Gravity_Control_Generator_Off": "",
	"SFXEvent_HUD_Gravity_Control_Generator_On": "",
	"SFXEvent_HUD_Landing_Zone_Captured": "",
	"SFXEvent_HUD_Landing_Zone_Lost": "",
	"SFXEvent_HUD_Last_Landing_Zone_Lost": "",
	"SFXEvent_HUD_Lost_Land_Battle": "",
	"SFXEvent_HUD_Lost_Land_Battle_Enemy_TSW_Present": "",
	"SFXEvent_HUD_Lost_Space_Battle": "",
	"SFXEvent_HUD_Lost_Space_Battle_Enemy_TSW_Present": "",
	"SFXEvent_HUD_Reinforcement_Point_Ally_Owned_05_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Ally_Owned_15_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Ally_Owned_30_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Ally_Owned_60_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Contested": "",
	"SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_05_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_15_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_30_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_60_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Owned_05_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Owned_15_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Owned_30_Seconds": "",
	"SFXEvent_HUD_Reinforcement_Point_Owned_60_Seconds": "",
	"SFXEvent_HUD_Repairing": "",
	"SFXEvent_HUD_Special_Weapon_Charging": "",
	"SFXEvent_HUD_Special_Weapon_Firing": "",
	"SFXEvent_HUD_Special_Weapon_Ready": "",
	"SFXEvent_HUD_Tactical_Victory_Near": "",
	"SFXEvent_HUD_Won_Land_Battle": "",
	"SFXEvent_HUD_Won_Land_Battle_Enemy_TSW_Present": "",
	"SFXEvent_HUD_Won_Space_Battle": "",
	"SFXEvent_HUD_Won_Space_Battle_Enemy_TSW_Present": "",
	"SFXEvent_Land_Base_Under_Attack_Announcement": "",
	"SFXEvent_Land_Invasion_Commencing": "",
	"SFXEvent_Max_Credits_Limit_Reached": "",
	"SFXEvent_Mission_Added": "",
	"SFXEvent_New_Construction_Options_Available": "",
	"SFXEvent_Planet_Gained_Control": "",
	"SFXEvent_Planet_Lost_Control": "",
	"SFXEvent_Player_Taunt": "",
	"SFXEvent_Slice_Failure": "",
	"SFXEvent_Slice_Success": "",
	"SFXEvent_Space_Base_Under_Attack_Announcement": "",
	"SFXEvent_Starbase_Ally_Upgraded": "",
	"SFXEvent_Starbase_Enemy_Upgraded": "",
	"SFXEvent_Starbase_Upgraded": "",
	"SFXEvent_Strategic_Pop_Cap_Reached": "",
	"SFXEvent_Tactical_Gain_Friendly_Control": "",
	"SFXEvent_Tactical_Lose_Friendly_Control": "",
	"SFXEvent_Tactical_Object_Building_Complete": "",
	"SFXEvent_Tactical_Object_Building_Loop": "",
	"SFXEvent_Tactical_Object_Building_Started": "",
	"SFXEvent_Tactical_Object_Sold": "",
	"SFXEvent_Tactical_Pop_Cap_Reached": "",
	"SFXEvent_Tactical_Unit_Cap_Reached": "",
	"SFXEvent_Unit_Type_Spotted": "",
	"SFXEvent_Weather_Begin": "",
	"SFXEvent_Weather_End": "",
	"SFX_Event_Tactical_Land_Battle_Pending": "",
	"SFX_Event_Tactical_Space_Battle_Pending": "",
	"Scatters_From_Crushers": "",
	"Selection_Blob_RGBA": "",
	"Ship_Icon_Name": "",
	"Skirmish_Land_Bomber": "",
	"Space_Advisor_Hints": "",
	"Space_Forced_Retreat_Due_To_Superweapon": "",
	"Space_Lose_Image": "",
	"Space_Mode_Garrison_Selection_Blob_Material_Name": "",
	"Space_Mode_Selection_Blob_Material_Name": "",
	"Space_Retreat_Begin_SFXEvent": "",
	"Space_Retreat_Cancel_SFXEvent": "",
	"Space_Retreat_Countdown_Color_RGBA": "",
	"Space_Retreat_Countdown_Seconds": "",
	"Space_Retreat_Countdown_Text_ID": "",
	"Space_Retreat_Enemy_Begin_SFXEvent": "",
	"Space_Retreat_Flight_Move_Increment": "",
	"Space_Retreat_Not_Allowed_Reason_1_SFXEvent": "",
	"Space_Retreat_Not_Allowed_Reason_2_SFXEvent": "",
	"Space_Retreat_Not_Allowed_Reason_3_SFXEvent": "",
	"Space_Retreat_Not_Allowed_SFXEvent": "",
	"Space_Retreat_Off_Map_Dest_Pos": "",
	"Space_Retreat_Pursue_Max_Speed_Mod_Factor": "",
	"Space_Retreat_Unit_Increment_Wait_Frames": "",
	"Space_Retreat_Units_Damaged_Mod_Factor": "",
	"Space_Skirmish_AI_Default_Forces": "",
	"Space_Skirmish_Unit_Buy_Credits": "",
	"Space_Surrender_SFXEvent": "",
	"Space_Tactical_Unit_Cap": "",
	"Space_Win_Image": "",
	"SpeechEvent_Super_Weapon_Enemy_Moved_Into_Range": "",
	"SpeechEvent_Super_Weapon_Enemy_Moving_Into_Range": "",
	"SpeechEvent_Super_Weapon_Enemy_Moving_Range_05_Seconds": "",
	"SpeechEvent_Super_Weapon_Enemy_Moving_Range_15_Seconds": "",
	"SpeechEvent_Super_Weapon_Enemy_Moving_Range_30_Seconds": "",
	"SpeechEvent_Super_Weapon_Enemy_Moving_Range_60_Seconds": "",
	"SpeechEvent_Super_Weapon_Moved_Into_Range": "",
	"SpeechEvent_Super_Weapon_Moving_Into_Range": "",
	"SpeechEvent_Super_Weapon_Moving_Range_05_Seconds": "",
	"SpeechEvent_Super_Weapon_Moving_Range_15_Seconds": "",
	"SpeechEvent_Super_Weapon_Moving_Range_30_Seconds": "",
	"SpeechEvent_Super_Weapon_Moving_Range_60_Seconds": "",
	"SpeechEvent_Tactical_Intro_Land_Attacker": "",
	"SpeechEvent_Tactical_Intro_Land_Attacker_Last_Location": "",
	"SpeechEvent_Tactical_Intro_Land_Defender": "",
	"SpeechEvent_Tactical_Intro_Land_Defender_Conditional_Or": "",
	"SpeechEvent_Tactical_Intro_Land_Defender_Last_Location": "",
	"SpeechEvent_Tactical_Intro_Land_Raid_Attacker": "",
	"SpeechEvent_Tactical_Intro_Land_Raid_Defender": "",
	"SpeechEvent_Tactical_Intro_Space_Attacker": "",
	"SpeechEvent_Tactical_Intro_Space_Attacker_Conditional_And": "",
	"SpeechEvent_Tactical_Intro_Space_Attacker_Conditional_Or": "",
	"SpeechEvent_Tactical_Intro_Space_Defender": "",
	"SpeechEvent_Tactical_Intro_Space_Defender_Conditional_And": "",
	"SpeechEvent_Tactical_Intro_Space_Defender_Conditional_Or": "",
	"Squadron_Icon_Name": "",
	"Standalone_Space_Maps_Special_Weapon_A": "",
	"Standalone_Space_Maps_Special_Weapon_B": "",
	"Star_Base_Icon_Name": "",
	"Strategic_Map_Music_Event": "",
	"Superweapon_Win_Movie": "",
	"Tactical_Intro_Command_Bar_Movie_Name": "",
	"Tech_Tree_Dialog_Name": "",
	# "Text_ID": "",
	"Vehicle_Icon_Name": "",
	"Victory_Text": "",

	# TacticalCameraConstants SubNodes
	# "Attribute - Name": "",
	"Bottom_Bounds_Buffer": "",
	"Distance_Default": "",
	"Distance_Max": "",
	"Distance_Min": "",
	"Distance_Per_Mouse_Unit": "",
	"Distance_Smooth_Time": "",
	"Distance_Spline": "",
	"Far_Clip": "",
	"Fov_Default": "",
	"Fov_Max": "",
	"Fov_Min": "",
	"Fov_Per_Mouse_Unit": "",
	"Fov_Smooth_Time": "",
	"Location_Follows_Terrain": "",
	"Location_Height_Down_Smooth_Time": "",
	"Location_Height_Up_Smooth_Time": "",
	"Min_Height_Above_Terrain": "",
	"Near_Clip": "",
	"Object_Fade_Begin": "",
	"Object_Fade_End": "",
	"Pitch_Default": "",
	"Pitch_Max": "",
	"Pitch_Min": "",
	"Pitch_Per_Mouse_Unit": "",
	"Pitch_Per_Zoom_Unit": "",
	"Pitch_Spline": "",
	"Pitch_When_Zoomed_In": "",
	"Pitch_Zoom_Begin_Fraction": "",
	"Side_Bounds_Buffer": "",
	"Spline_Steps": "",
	"Tactical_Overview_Click_Time": "",
	"Tactical_Overview_Clicks": "",
	"Tactical_Overview_Distance": "",
	"Tactical_Overview_Distance2": "",
	"Tactical_Overview_FOV": "",
	"Tactical_Overview_FOV2": "",
	"Tactical_Overview_Pitch": "",
	"Tactical_Overview_Pitch2": "",
	"Top_Bounds_Buffer": "",
	"Use_Splines": "",
	"Yaw_Default": "",
	"Yaw_Max": "",
	"Yaw_Min": "",
	"Yaw_Per_Mouse_Unit": "",

	# LightSource SubNodes
	# "Attribute - Name": "",
	"Auto_Destruct_Fade_Time": "",
	"Auto_Destruct_Time": "",
	"Blob_Color": "",
	"Blob_Intensity": "",
	"Blob_Radius": "",
	"Diffuse": "",
	"Falloff_Start": "",
	# "Intensity": "",
	"Radius": "",

	# BinkMovie SubNodes
	# "Attribute - Name": "",
	"Cannot_Skip": "",
	"Movie_File": "",

	# TargetingPrioritySet SubNodes:
	# "Attribute - Name": "",
	"Attack_Priorities": "",
	"Category_Exclusions": "",
	# "File": "",
	"Property_Exclusions": "",
	"Unit_Exclusions": "",

	# DifficultyAdjustment SubNodes
	# "Attribute - Name": "",
	"Credit_Multiplier": "",
	"Damage_Multiplier": "",
	"Galactic_AI_Contrast_Multiplier": "",
	"Galactic_AI_Goal_Cycle_Sleep_Duration": "",
	"Galactic_Build_Time_Multiplier": "",
	"Land_AI_Contrast_Multiplier": "",
	"Land_AI_Goal_Cycle_Sleep_Duration": "",
	"Land_Build_Time_Multiplier": "",
	"Space_AI_Contrast_Multiplier": "",
	"Space_AI_Goal_Cycle_Sleep_Duration": "",
	"Space_Build_Time_Multiplier": "",


	# WeatherAudioManager SubNodes
	"Ambient_SFXEvent_Intermittent": "",
	"Weather_SFXEvent_Intermittent": "",
	"Weather_SFXEvent_Loop": "",

}

#############################
# End Descriptions
#############################
