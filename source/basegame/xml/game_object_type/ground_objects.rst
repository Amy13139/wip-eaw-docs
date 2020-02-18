.. _xml_type_template:
.. Template to use for XML type documentation

**************
Ground Objects
**************


About
=====
*Description*: This Type/Subtype does something!


Structure
=========
GroundBases
-----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GroundBase``                                                    ``Name``
================================================================= =================================================================

|

GroundBase
^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Affiliation
	Ref; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Base_Level
	Int; *Description Here*

- Behavior
	Ref; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Tab_Outpost
	Bool Y/N; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Damage
	Int; *Description Here*

- GUI_Distance
	Int; *Description Here*

- GUI_Model_Name
	File; *Description Here*

- GUI_Offset
	Ref; *Description Here*

- GUI_Row
	Ref; *Description Here*

- GUI_Velocity
	Int; *Description Here*

- Icon_Name
	File; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Next_Level_Base
	None; *Description Here*

- Prev_Level_Base
	None; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Star_Base_Level
	Int; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Victory_Relevant
	Bool y/n; *Description Here*


|


|
|

GroundBuildables
----------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GroundBuildable``                                               ``Name``
``SpecialStructure``                                              ``Name``
================================================================= =================================================================

|

GroundBuildable
^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Base_Level_Available
	Ref; *Description Here*

- Base_Position
	Ref; *Description Here*

- Base_Shield_Always_Off
	Ref; *Description Here*

- Behavior
	Ref, Ref, ...; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Capture_Point_Radius
	Int; *Description Here*

- Capture_Point_Transition_Time_Seconds
	Float; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Ref; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Soft_Footprint_Radius
	Float; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Exclude_From_Distance_Fade
	Bool t/f; *Description Here*

- Fine_Tune_Occupied_Passability
	Ref; *Description Here*

- GUI_Bounds_Scale
	Float; *Description Here*

- GUI_Bracket_Height
	Ref; *Description Here*

- GUI_Bracket_Size
	Ref; *Description Here*

- GUI_Bracket_Width
	Ref; *Description Here*

- Has_Land_Evaluator
	Bool T/F; *Description Here*

- Hides_When_Built_On
	Bool T/F; *Description Here*

- Icon_Name
	File; *Description Here*

- Immune_To_Damage
	Bool T/F; *Description Here*

- Influences_Capture_Point
	Ref; *Description Here*

- Initial_State_Visible_Under_FOW
	Bool T/F; *Description Here*

- Is_Community_Property
	Bool Y/N; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Ref; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Damage_Alternates
	Int, Int, Int, Int; *Description Here*

- Land_Damage_SFX
	Ref, Ref, Ref, Ref; *Description Here*

- Land_Damage_Thresholds
	Int, Float, Float, Int; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Name
	Ref; *Description Here*

- Last_State_Visible_Under_FOW
	Ref; *Description Here*

- Loop_Idle_Anim_00
	Ref; *Description Here*

- MP_Encyclopedia_Text
	Ref; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Minimum_Time_Before_Pad_Can_Build_Again
	Float; *Description Here*

- Movie_Object
	Bool t/f; *Description Here*

- No_Reflection_Below_Detail_Level
	Ref; *Description Here*

- No_Refraction_Below_Detail_Level
	Ref; *Description Here*

- Obstacle_Height
	Float; *Description Here*

- Obstacle_Proxy_Type
	Ref; *Description Here*

- Obstacle_Width
	Float; *Description Here*

- Obstacle_X_Offset
	Float; *Description Here*

- Obstacle_Y_Offset
	Float; *Description Here*

- Ownership_Sticks
	Bool Y/N; *Description Here*

- Political_Control
	Int; *Description Here*

- Property_Flags
	Ref; *Description Here*

- Radar_Icon_Name
	File; *Description Here*

- Radar_Icon_Size
	Ref; *Description Here*

- Radar_Show_Facing
	Bool Y/N; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Required_Ground_Base_Level
	Ref; *Description Here*

- Reveal_During_Setup_Phase
	Ref; *Description Here*

- Reveal_During_Setup_Phase_Only
	Ref; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Sold_Tactical
	Ref; *Description Here*

- SFXEvent_Special_Weapon_Ready
	Ref; *Description Here*

- SFXEvent_Unit_Lost
	Ref; *Description Here*

- SFXEvent_Unit_Under_Attack
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Select_Box_Scale
	Ref; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Shield_Points
	Ref; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Size_Value
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Tactical_Build_Cost_Campaign
	Int; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Ref; *Description Here*

- Tactical_Build_Start_Lower_Z
	Ref; *Description Here*

- Tactical_Build_Time_Seconds
	Ref; *Description Here*

- Tactical_Buildable_Constructed
	Ref; *Description Here*

- Tactical_Buildable_Objects_Campaign
	Ref, Ref, ...; *Description Here*

- Tactical_Buildable_Objects_Multiplayer
	Ref, Ref, ...; *Description Here*

- Tactical_Health
	Ref; *Description Here*

- Tactical_Sell_Credits
	Ref; *Description Here*

- Terrain_Texture_Modifier_Join_Distance
	Float; *Description Here*

- Terrain_Texture_Modifier_Material
	Int; *Description Here*

- Terrain_Texture_Modifier_Square
	Bool t/f; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- UnitCollisionClass
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Ref; *Description Here*

- Visible_To_Enemies_When_Empty
	Ref; *Description Here*


|

SpecialStructure
^^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Affiliation
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Base_Position
	Ref; *Description Here*

- Behavior
	Ref, Ref, Ref; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Encyclopedia_Text
	Ref, Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- GUI_Bounds_Scale
	Float; *Description Here*

- GUI_Bracket_Size
	Int; *Description Here*

- Has_Land_Evaluator
	Bool T/F; *Description Here*

- Icon_Name
	File; *Description Here*

- Influences_Capture_Point
	Ref; *Description Here*

- Initial_State_Visible_Under_FOW
	Bool T/F; *Description Here*

- Is_Community_Property
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref; *Description Here*

- Land_Damage_Alternates
	Int, Int, Int, Int; *Description Here*

- Land_Damage_SFX
	Ref, Ref, Ref, Ref; *Description Here*

- Land_Damage_Thresholds
	Int, Float, Float, Int; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Last_State_Visible_Under_FOW
	Ref; *Description Here*

- MP_Encyclopedia_Text
	Ref; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Obstacle_Proxy_Type
	Ref; *Description Here*

- Radar_Icon_Size
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Reveal_During_Setup_Phase
	Ref; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Size_Value
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Ref; *Description Here*

- Tactical_Build_Start_Lower_Z
	Float; *Description Here*

- Tactical_Build_Time_Seconds
	Ref; *Description Here*

- Tactical_Buildable_Constructed
	Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Terrain_Texture_Modifier_Square
	Bool t/f; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations


|


|
|

GroundStructures
----------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GroundStructure``                                               ``Name``
================================================================= =================================================================

|

GroundStructure
^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Ref; *Description Here*

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Apply_Y_Turret_Rotate_To_Axis
	Int; *Description Here*

- Apply_Z_Turret_Rotate_To_Axis
	Int; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Attack_Category_Restrictions
	Ref; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Barrel_Bone_Name
	Ref; *Description Here*

- Base_Level_Available
	Ref; *Description Here*

- Behavior
	Ref; *Description Here*

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Ref; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Damage_Type
	Ref; *Description Here*

- Death_Clone_Is_Obstacle
	Bool y/n; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Enemy_Spawn_Text
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Facing_Adjust
	Float, Float, Float; *Description Here*

- Friendly_Spawn_Text
	Ref; *Description Here*

- GUI_Bounds_Scale
	Float; *Description Here*

- GUI_Bracket_Height
	Ref; *Description Here*

- GUI_Bracket_Size
	Ref; *Description Here*

- GUI_Bracket_Width
	Ref; *Description Here*

- GUI_Hide_Health_Bar
	Bool t/f; *Description Here*

- Has_Land_Evaluator
	Bool T/F; *Description Here*

- Icon_Name
	File; *Description Here*

- Influences_Capture_Point
	Ref; *Description Here*

- Initial_State_Visible_Under_FOW
	Bool T/F; *Description Here*

- Is_Branched_Map_Discardable
	Bool T/F; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Is_Discardable
	Bool Y/N; *Description Here*

- Is_Squashable_By_Supercrusher
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Damage_Alternates
	Int, Int, ...; *Description Here*

- Land_Damage_SFX
	Ref, Ref, ...; *Description Here*

- Land_Damage_Thresholds
	Float, Float, Float, Float; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Name
	Ref; *Description Here*

- Last_State_Visible_Under_FOW
	Ref; *Description Here*

- Loads_When_Faction_Present
	Ref; *Description Here*

- Loop_Idle_Anim_00
	Ref; *Description Here*

- Lua_Script
	Ref; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Distance_From_Spawner
	Int; *Description Here*

- Multisample_FOW_Check
	Bool Y/N; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- No_Reflection_Below_Detail_Level
	Ref; *Description Here*

- No_Refraction_Below_Detail_Level
	Ref; *Description Here*

- Obstacle_Height
	Float; *Description Here*

- Obstacle_Proxy_Type
	Ref; *Description Here*

- Obstacle_Width
	Float; *Description Here*

- Obstacle_X_Offset
	Float; *Description Here*

- Obstacle_Y_Offset
	Float; *Description Here*

- OverridePassability
	Ref; *Description Here*

- Projectile_Damage
	Float; *Description Here*

- Projectile_Fire_Pulse_Count
	Int; *Description Here*

- Projectile_Fire_Pulse_Delay_Seconds
	Float; *Description Here*

- Projectile_Fire_Recharge_Seconds
	Float; *Description Here*

- Projectile_Types
	Ref; *Description Here*

- Property_Flags
	Ref | Ref; *Description Here*

- Radar_Icon_Size
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Required_Ground_Base_Level
	Ref; *Description Here*

- Required_Special_Structures
	Ref; *Description Here*

- Reveal_During_Setup_Phase
	Ref; *Description Here*

- SFXEvent_Ambient_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Sold_Tactical
	Ref; *Description Here*

- SFXEvent_Turret_Rotating_Loop
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Select_Box_Scale
	Ref; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Shield_Points
	Ref; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Space_Obstacle_Offset
	Ref; *Description Here*

- Spawn_Indigenous_Units_Chance
	Floatf; *Description Here*

- Spawn_Indigenous_Units_In_Packs
	Bool Y/N; *Description Here*

- Spawn_Indigenous_Units_Radius
	Floatf; *Description Here*

- Spawned_Indigenous_Pack_Type
	Ref; *Description Here*

- Spawned_Indigenous_Units_Delay_Seconds
	Float; *Description Here*

- Spawned_Indigenous_Units_Quantity
	Int; *Description Here*

- Spawned_Indigenous_Units_Type
	Ref; *Description Here*

- Tactical_Health
	Ref; *Description Here*

- Tactical_Sell_Credits
	Ref; *Description Here*

- Targeting_Fire_Inaccuracy
	Ref, Float; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Min_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Targeting_Stickiness_Time_Threshold
	Float; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Turret_Bone_Name
	Ref; *Description Here*

- Turret_Elevate_Extent_Degrees
	Int; *Description Here*

- Turret_Rotate_Extent_Degrees
	Int; *Description Here*

- Turret_Rotate_Speed
	Float; *Description Here*

- UnitCollisionClass
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Ref; *Description Here*

LandPrimarySkydomes
-------------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``LandPrimarySkydome``                                            ``Name``
================================================================= =================================================================

|

LandPrimarySkydome
^^^^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Behavior
	Ref; *Description Here*

- Exclude_From_Distance_Fade
	Bool t/f; *Description Here*

- Galactic_Model_Name
	None; *Description Here*

- In_Background
	Bool y/n; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Text_ID
	None; The in-game name of this unit, references a .DAT file to allow from translations


|


|
|

LandSecondarySkydomes
---------------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``LandSecondarySkydome``                                          ``Name``
================================================================= =================================================================

|

LandSecondarySkydome
^^^^^^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Behavior
	None; *Description Here*

- Exclude_From_Distance_Fade
	Bool t/f; *Description Here*

- Galactic_Model_Name
	None; *Description Here*

- In_Background
	Bool y/n; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Text_ID
	None; The in-game name of this unit, references a .DAT file to allow from translations


EaW-Godot Port Connection
=========================
This file is imported into a thing
