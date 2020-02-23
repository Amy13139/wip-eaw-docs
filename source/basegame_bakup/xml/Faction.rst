.. _xml_faction:
.. Template to use for XML type documentation

*******
Faction
*******


About
=====
Stores faction-specific information


Structure
=========
Faction_Files
-------------
- File
	File; A file to load, has the same type as this file

Factions
--------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Faction``                                                       ``Name``
================================================================= =================================================================

|

Faction
^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Allies
	Ref; *Description Here*

- Alternate_Icon_Name
	Ref; *Description Here*

- Alternate_Icon_Prefix
	Ref; *Description Here*

- Automatic_Planetary_Corruption_Upgrade_Type
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Basic_AI
	Ref; *Description Here*

- Benefits_From_Corruption
	Ref; *Description Here*

- Big_Fleet_Color
	Int, Int, Int, Int; *Description Here*

- Bombardment_Blob_Size
	Float; *Description Here*

- Bombardment_Initial_Delay
	Float; *Description Here*

- Bombardment_Lighting_Color_List
	Float, Float, Float, Float, Float, Float; *Description Here*

- Bombardment_Lighting_Intensity_List
	Ref; *Description Here*

- Bombardment_Lighting_Seconds_List
	Ref; *Description Here*

- Bombardment_Number_Of_Salvos
	Ref; *Description Here*

- Bombardment_Particle
	Ref; *Description Here*

- Bombardment_Projectile
	Ref; *Description Here*

- Bombardment_Required_Orbital_Ships
	Ref, Ref, ...; *Description Here*

- Bombardment_Salvo_Delay
	Ref; *Description Here*

- Bombardment_Shadow_Blob_Material_Name
	Ref; *Description Here*

- Bombardment_Shot_Delay
	Float; *Description Here*

- Bombardment_Shots_Per_Salvo
	Ref; *Description Here*

- Bombing_Run_Blob_Size
	Float; *Description Here*

- Bombing_Run_Shadow_Blob_Material_Name
	Ref; *Description Here*

- Bribed_Color
	Int, Int, Int, Int; *Description Here*

- Can_Control_Planets
	Bool t/f; *Description Here*

- Can_Win_By_Destroying_Super_Weapon
	Bool Y/N; *Description Here*

- Carrier_Icon_Name
	File; *Description Here*

- Color
	Int, Int, Int, Int; *Description Here*

- Corruption_Galactic_Production_Price_Multipliers
	Float, Float; *Description Here*

- Corruption_Galactic_Production_Time_Multipliers
	Float, Float; *Description Here*

- Corruption_Tactical_Build_Pad_Price_Multipliers
	Float, Float; *Description Here*

- Corruption_Tactical_Build_Pad_Time_Multipliers
	Float, Float; *Description Here*

- Corruption_Tactical_Production_Price_Multipliers
	Float, Float; *Description Here*

- Corruption_Tactical_Production_Time_Multipliers
	Float, Float; *Description Here*

- Corvette_Icon_Name
	File; *Description Here*

- Create_Player_In_Multiplayer_Games
	Ref; *Description Here*

- Credits_Accumulation_Factor
	Float; *Description Here*

- Debug_Ground_Structures
	Ref; *Description Here*

- Default_Transmission_Message
	Ref; *Description Here*

- Defeat_Text
	Ref; *Description Here*

- Display_Font_Color
	Int, Int, Int, Int; *Description Here*

- Displayed_Tech_Level_Adjustment
	Ref; *Description Here*

- Easily_Bribed
	Ref; *Description Here*

- Enemies
	Ref, Ref, ...; *Description Here*

- Faction_Leader
	Ref; *Description Here*

- Faction_Leader_Company
	Ref; *Description Here*

- Faction_Super_Weapon
	Ref; *Description Here*

- Fighter_Icon_Name
	File; *Description Here*

- Finale_Movie
	Ref; *Description Here*

- Finale_Movie_2
	Ref; *Description Here*

- Fleet_Icon_Name
	Ref; *Description Here*

- Force_Alignment
	Ref; *Description Here*

- Frigate_Icon_Name
	File; *Description Here*

- Galactic_Advisor_Hints
	Ref, Ref, ...; *Description Here*

- Garrison_Reinforcement_Delay_Seconds
	Float; *Description Here*

- Generic_Win_Movie
	Ref; *Description Here*

- Ground_Base_Icon_Name
	Ref; *Description Here*

- Ground_Transport_Icon_Name
	Ref; *Description Here*

- Helper_Icon_Name
	File; *Description Here*

- Home_Planet
	Ref; *Description Here*

- Hyperspace_Speed_Factor
	Float; *Description Here*

- Icon_Name
	Ref; *Description Here*

- Infantry_Icon_Name
	File; *Description Here*

- Is_Debug_Switchable_To
	Ref; *Description Here*

- Is_Neutral
	Ref; *Description Here*

- Is_Playable
	Bool t/f; *Description Here*

- Land_Ability_Targeting_Range_Overlay_Material_Name
	Ref; *Description Here*

- Land_Ability_Targeting_Range_Overlay_RGBA
	Int, Int, Int, Int; *Description Here*

- Land_Ability_Targeting_Range_Overlay_Scale_Factor
	Float; *Description Here*

- Land_Advisor_Hints
	Ref, Ref, ...; *Description Here*

- Land_Area_Effect_Range_Overlay_Material_Name
	Ref; *Description Here*

- Land_Area_Effect_Range_Overlay_RGBA
	Int, Int, Int, Int; *Description Here*

- Land_Area_Effect_Range_Overlay_Scale_Factor
	Float; *Description Here*

- Land_Lose_Image
	File; *Description Here*

- Land_Mode_Garrison_Selection_Blob_Material_Name
	Ref; *Description Here*

- Land_Mode_Selection_Blob_Material_Name
	Ref; *Description Here*

- Land_Retreat_Begin_SFXEvent
	Ref; *Description Here*

- Land_Retreat_Cancel_SFXEvent
	Ref; *Description Here*

- Land_Retreat_Countdown_Color_RGBA
	Int, Int, Int, Int; *Description Here*

- Land_Retreat_Countdown_Seconds
	Float; *Description Here*

- Land_Retreat_Countdown_Text_ID
	Ref; *Description Here*

- Land_Retreat_Enemy_Begin_SFXEvent
	Ref; *Description Here*

- Land_Retreat_Not_Allowed_Reason_1_SFXEvent
	Ref; *Description Here*

- Land_Retreat_Not_Allowed_Reason_2_SFXEvent
	Ref; *Description Here*

- Land_Retreat_Not_Allowed_Reason_3_SFXEvent
	Ref; *Description Here*

- Land_Retreat_Not_Allowed_SFXEvent
	Ref; *Description Here*

- Land_Retreat_Pursue_Max_Speed_Mod_Factor
	Float; *Description Here*

- Land_Retreat_Units_Damaged_Mod_Factor
	Float; *Description Here*

- Land_Skirmish_AI_Default_Forces
	Ref, Ref; *Description Here*

- Land_Skirmish_Unit_Buy_Credits
	Ref; *Description Here*

- Land_Skirmish_Unit_Cap_By_Player_Count
	Int, Int, Int, Int, Int, Int, Ref; *Description Here*

- Land_Surrender_SFXEvent
	Ref; *Description Here*

- Land_Win_Image
	File; *Description Here*

- Maintenance_Cost
	Float; *Description Here*

- Minimum_Visible_Base_Level
	Int; *Description Here*

- Multiplayer_Beacon_Type
	Ref; *Description Here*

- Multiplayer_Campaign_Heroes
	Ref, Ref, ...; *Description Here*

- Multiplayer_Map_Preview_Icon
	File; *Description Here*

- Music_Event_Battle_Load_Screen
	Ref; *Description Here*

- Music_Event_Land_Ambient_Super_Weapon
	Ref; *Description Here*

- Music_Event_Land_Battle_Super_Weapon
	Ref; *Description Here*

- Music_Event_List_Ambient
	Ref, Ref; *Description Here*

- Music_Event_List_Battle
	Ref, Ref; *Description Here*

- Music_Event_Space_Ambient_Super_Weapon
	Ref; *Description Here*

- Music_Event_Space_Battle_Super_Weapon
	Ref; *Description Here*

- Music_Event_Strategic_Lose
	Ref; *Description Here*

- Music_Event_Strategic_Lose_Vs_Faction
	Ref, Ref; *Description Here*

- Music_Event_Strategic_Win
	Ref; *Description Here*

- Music_Event_Strategic_Win_Vs_Faction
	Ref, Ref; *Description Here*

- Music_Event_Tactical_Land_Battle_Pending
	Ref; *Description Here*

- Music_Event_Tactical_Lose
	Ref; *Description Here*

- Music_Event_Tactical_Lose_Vs_Faction
	Ref, Ref; *Description Here*

- Music_Event_Tactical_Space_Battle_Pending
	Ref; *Description Here*

- Music_Event_Tactical_Win
	Ref; *Description Here*

- Music_Event_Tactical_Win_Vs_Faction
	Ref, Ref; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- Planet_Icon_Offset
	Float, Float, Float; *Description Here*

- Planet_Icon_Scale
	Float; *Description Here*

- Post_Credits_Movie
	None; *Description Here*

- Primary_Enemy
	Ref; *Description Here*

- Reinforcements_Cancelled_SFXEvent
	Ref; *Description Here*

- Reinforcements_Enroute_SFXEvent
	Ref; *Description Here*

- Reinforcements_Pick_Landing_Zone_SFXEvent
	Ref; *Description Here*

- Reinforcements_Ready_SFXEvent
	Ref; *Description Here*

- Reinforcements_Requesting_SFXEvent
	Ref; *Description Here*

- Reinforcements_Selection_SFXEvent
	Ref; *Description Here*

- Reinforcements_Shadow_Blob_Material_Name
	Ref; *Description Here*

- SFXEvent_Arrive_From_Hyperspace
	Ref; *Description Here*

- SFXEvent_Base_Shield_Absorb_Damage
	Ref; *Description Here*

- SFXEvent_Bombard_Ally_Available
	Ref; *Description Here*

- SFXEvent_Bombard_Available
	Ref; *Description Here*

- SFXEvent_Bombard_Cancelled
	Ref; *Description Here*

- SFXEvent_Bombard_Enemy_Available
	Ref; *Description Here*

- SFXEvent_Bombing_Run_Ally_Available
	Ref; *Description Here*

- SFXEvent_Bombing_Run_Available
	Ref; *Description Here*

- SFXEvent_Bombing_Run_Begin_Crosstalk
	Ref; *Description Here*

- SFXEvent_Bombing_Run_Cancelled
	Ref; *Description Here*

- SFXEvent_Bombing_Run_Enemy_Available
	Ref; *Description Here*

- SFXEvent_Build_Impossible_Location_Blockaded
	Ref; *Description Here*

- SFXEvent_Bunker_Garrisoned
	Ref; *Description Here*

- SFXEvent_Bunker_Vacated
	Ref; *Description Here*

- SFXEvent_Corruption_Removed
	Ref; *Description Here*

- SFXEvent_Enemy_Fleet_Approaching_Planet
	Ref; *Description Here*

- SFXEvent_Enemy_Spotted
	Ref; *Description Here*

- SFXEvent_Exit_Into_Hyperspace
	Ref; *Description Here*

- SFXEvent_GUI_Enemy_Toggle_Non_Hero_Ability_Off
	Ref, Ref; *Description Here*

- SFXEvent_GUI_Enemy_Toggle_Non_Hero_Ability_On
	Ref, Ref; *Description Here*

- SFXEvent_GUI_Start_Campaign
	Ref; *Description Here*

- SFXEvent_GUI_Toggle_Non_Hero_Ability_Off
	Ref, Ref; *Description Here*

- SFXEvent_GUI_Toggle_Non_Hero_Ability_On
	Ref, Ref; *Description Here*

- SFXEvent_HUD_Advisor_Hint
	Ref; *Description Here*

- SFXEvent_HUD_Advisor_Message
	Ref; *Description Here*

- SFXEvent_HUD_Advisor_Urgent
	Ref; *Description Here*

- SFXEvent_HUD_Base_Shield_Offline
	Ref; *Description Here*

- SFXEvent_HUD_Base_Shield_Online
	Ref; *Description Here*

- SFXEvent_HUD_Base_Shield_Penetrated
	Ref; *Description Here*

- SFXEvent_HUD_Build_Pad_Captured
	Ref; *Description Here*

- SFXEvent_HUD_Build_Pad_Lost
	Ref; *Description Here*

- SFXEvent_HUD_Enemy_Base_Shield_Offline
	Ref; *Description Here*

- SFXEvent_HUD_Enemy_Base_Shield_Online
	Ref; *Description Here*

- SFXEvent_HUD_Enemy_Base_Shield_Penetrated
	Ref; *Description Here*

- SFXEvent_HUD_Enemy_Special_Weapon_Charging
	Ref; *Description Here*

- SFXEvent_HUD_Enemy_Special_Weapon_Firing
	Ref; *Description Here*

- SFXEvent_HUD_Enemy_Special_Weapon_Ready
	Ref; *Description Here*

- SFXEvent_HUD_Gravity_Control_Generator_Off
	Ref; *Description Here*

- SFXEvent_HUD_Gravity_Control_Generator_On
	Ref; *Description Here*

- SFXEvent_HUD_Landing_Zone_Captured
	Ref; *Description Here*

- SFXEvent_HUD_Landing_Zone_Lost
	Ref; *Description Here*

- SFXEvent_HUD_Last_Landing_Zone_Lost
	Ref; *Description Here*

- SFXEvent_HUD_Lost_Land_Battle
	Ref; *Description Here*

- SFXEvent_HUD_Lost_Land_Battle_Enemy_TSW_Present
	Ref; *Description Here*

- SFXEvent_HUD_Lost_Space_Battle
	Ref; *Description Here*

- SFXEvent_HUD_Lost_Space_Battle_Enemy_TSW_Present
	Ref; *Description Here*

- SFXEvent_HUD_Lost_Tactical_Corruption_Mission
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Ally_Owned_05_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Ally_Owned_15_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Ally_Owned_30_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Ally_Owned_60_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Contested
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_05_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_15_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_30_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Enemy_Owned_60_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Owned_05_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Owned_15_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Owned_30_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Reinforcement_Point_Owned_60_Seconds
	Ref; *Description Here*

- SFXEvent_HUD_Repairing
	Ref; *Description Here*

- SFXEvent_HUD_Special_Weapon_Charging
	Ref; *Description Here*

- SFXEvent_HUD_Special_Weapon_Firing
	Ref; *Description Here*

- SFXEvent_HUD_Special_Weapon_Ready
	Ref; *Description Here*

- SFXEvent_HUD_Tactical_Victory_Near
	Ref; *Description Here*

- SFXEvent_HUD_Won_Land_Battle
	Ref; *Description Here*

- SFXEvent_HUD_Won_Land_Battle_Enemy_TSW_Present
	Ref; *Description Here*

- SFXEvent_HUD_Won_Space_Battle
	Ref; *Description Here*

- SFXEvent_HUD_Won_Space_Battle_Enemy_TSW_Present
	Ref; *Description Here*

- SFXEvent_HUD_Won_Tactical_Corruption_Mission
	Ref; *Description Here*

- SFXEvent_Hack_Success
	Ref; *Description Here*

- SFXEvent_Land_Base_Under_Attack_Announcement
	Ref; *Description Here*

- SFXEvent_Land_Invasion_Commencing
	Ref; *Description Here*

- SFXEvent_Max_Credits_Limit_Reached
	Ref; *Description Here*

- SFXEvent_Mission_Added
	Ref; *Description Here*

- SFXEvent_New_Construction_Options_Available
	Ref; *Description Here*

- SFXEvent_Planet_Corrupted
	Ref; *Description Here*

- SFXEvent_Planet_Gained_Control
	Ref; *Description Here*

- SFXEvent_Planet_Lost_Control
	Ref; *Description Here*

- SFXEvent_Player_Taunt
	Ref; *Description Here*

- SFXEvent_Sabotage_Success
	Ref; *Description Here*

- SFXEvent_Slice_Failure
	Ref; *Description Here*

- SFXEvent_Slice_Success
	Ref; *Description Here*

- SFXEvent_Space_Base_Under_Attack_Announcement
	Ref; *Description Here*

- SFXEvent_Starbase_Ally_Upgraded
	Ref; *Description Here*

- SFXEvent_Starbase_Enemy_Upgraded
	Ref; *Description Here*

- SFXEvent_Starbase_Upgraded
	Ref; *Description Here*

- SFXEvent_Strategic_Pop_Cap_Reached
	Ref; *Description Here*

- SFXEvent_Tactical_Corruption_Mission_Commencing
	Ref; *Description Here*

- SFXEvent_Tactical_Gain_Enemy_Control
	Ref, Ref; *Description Here*

- SFXEvent_Tactical_Gain_Friendly_Control
	Ref, Ref; *Description Here*

- SFXEvent_Tactical_Lose_Enemy_Control
	Ref, Ref; *Description Here*

- SFXEvent_Tactical_Lose_Friendly_Control
	Ref, Ref; *Description Here*

- SFXEvent_Tactical_Object_Building_Complete
	Ref; *Description Here*

- SFXEvent_Tactical_Object_Building_Loop
	Ref; *Description Here*

- SFXEvent_Tactical_Object_Building_Started
	Ref; *Description Here*

- SFXEvent_Tactical_Object_Sold
	Ref; *Description Here*

- SFXEvent_Tactical_Pop_Cap_Reached
	Ref; *Description Here*

- SFXEvent_Tactical_Unit_Cap_Reached
	Ref; *Description Here*

- SFXEvent_Unit_Type_Spotted
	Ref, Ref; *Description Here*

- SFXEvent_Weather_Begin
	Ref, Ref; *Description Here*

- SFXEvent_Weather_End
	Ref, Ref; *Description Here*

- SFX_Event_Tactical_Land_Battle_Pending
	Ref; *Description Here*

- SFX_Event_Tactical_Space_Battle_Pending
	Ref; *Description Here*

- Scatters_From_Crushers
	Ref; *Description Here*

- Selection_Blob_RGBA
	Int, Int, Int, Int; *Description Here*

- Ship_Icon_Name
	Ref; *Description Here*

- Skirmish_Land_Bomber
	Ref; *Description Here*

- Space_Advisor_Hints
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_Forced_Retreat_Due_To_Superweapon
	Ref; *Description Here*

- Space_Lose_Image
	File; *Description Here*

- Space_Mode_Garrison_Selection_Blob_Material_Name
	Ref; *Description Here*

- Space_Mode_Selection_Blob_Material_Name
	Ref; *Description Here*

- Space_Retreat_Begin_SFXEvent
	Ref; *Description Here*

- Space_Retreat_Cancel_SFXEvent
	Ref; *Description Here*

- Space_Retreat_Countdown_Color_RGBA
	Int, Int, Int, Int; *Description Here*

- Space_Retreat_Countdown_Seconds
	Float; *Description Here*

- Space_Retreat_Countdown_Text_ID
	Ref; *Description Here*

- Space_Retreat_Enemy_Begin_SFXEvent
	Ref; *Description Here*

- Space_Retreat_Flight_Increment
	Float; *Description Here*

- Space_Retreat_Flight_Move_Increment
	Float; *Description Here*

- Space_Retreat_Not_Allowed_Reason_1_SFXEvent
	Ref; *Description Here*

- Space_Retreat_Not_Allowed_Reason_2_SFXEvent
	Ref; *Description Here*

- Space_Retreat_Not_Allowed_Reason_3_SFXEvent
	Ref; *Description Here*

- Space_Retreat_Not_Allowed_SFXEvent
	Ref; *Description Here*

- Space_Retreat_Off_Map_Dest_Pos
	Float, Float, Float; *Description Here*

- Space_Retreat_Pursue_Max_Speed_Mod_Factor
	Float; *Description Here*

- Space_Retreat_Unit_Increment_Wait_Frames
	Ref; *Description Here*

- Space_Retreat_Units_Damaged_Mod_Factor
	Float; *Description Here*

- Space_Skirmish_AI_Default_Forces
	Ref, Ref; *Description Here*

- Space_Skirmish_Unit_Buy_Credits
	Ref; *Description Here*

- Space_Surrender_SFXEvent
	Ref; *Description Here*

- Space_Tactical_Unit_Cap
	Int; *Description Here*

- Space_Win_Image
	File; *Description Here*

- SpeechEvent_Super_Weapon_Enemy_Moved_Into_Range
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Enemy_Moving_Into_Range
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Enemy_Moving_Range_05_Seconds
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Enemy_Moving_Range_15_Seconds
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Enemy_Moving_Range_30_Seconds
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Enemy_Moving_Range_60_Seconds
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Moved_Into_Range
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Moving_Into_Range
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Moving_Range_05_Seconds
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Moving_Range_15_Seconds
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Moving_Range_30_Seconds
	Ref; *Description Here*

- SpeechEvent_Super_Weapon_Moving_Range_60_Seconds
	Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Land_Attacker
	Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Land_Attacker_Conditional_Or
	Ref, Ref, Ref, Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Land_Attacker_Last_Location
	Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Land_Defender
	Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Land_Defender_Conditional_Or
	Ref, Ref, Ref, Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Land_Defender_Last_Location
	Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Land_Raid_Attacker
	Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Land_Raid_Defender
	Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Space_Attacker
	Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Space_Attacker_Conditional_And
	Ref, Ref, Ref, Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Space_Attacker_Conditional_Or
	Ref, Ref, Ref, Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Space_Defender
	Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Space_Defender_Conditional_And
	Ref, Ref, Ref, Ref; *Description Here*

- SpeechEvent_Tactical_Intro_Space_Defender_Conditional_Or
	Ref, Ref, Ref, Ref; *Description Here*

- Squadron_Icon_Name
	Ref; *Description Here*

- Standalone_Space_Maps_Special_Weapon_A
	Ref; *Description Here*

- Standalone_Space_Maps_Special_Weapon_B
	Ref; *Description Here*

- Star_Base_Icon_Name
	Ref; *Description Here*

- Strategic_Map_Music_Event
	Ref; *Description Here*

- Superweapon_Win_Movie
	Ref; *Description Here*

- Tactical_Intro_Command_Bar_Movie_Name
	Ref; *Description Here*

- Tech_Level_Icon_Name
	Ref; *Description Here*

- Tech_Tree_Dialog_Name
	Ref; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Text_Nickname_ID
	Ref; *Description Here*

- Vehicle_Icon_Name
	File; *Description Here*

- Victory_Text
	Ref; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
