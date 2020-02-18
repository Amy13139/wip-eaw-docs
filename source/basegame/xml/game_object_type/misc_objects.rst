.. _xml_type_template:
.. Template to use for XML type documentation

*********************
Miscellaneous Objects
*********************


About
=====
*Description*: This Type/Subtype does something!


Structure
=========
MiscObjects
-----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``MiscObject``                                                    ``Name``
================================================================= =================================================================

|

MiscObject
^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Affiliation
	Ref; *Description Here*

- Beacon_Lifetime_In_Secs
	Float; *Description Here*

- Beacon_Radar_Map_Event_Name
	Ref; *Description Here*

- Behavior
	Ref, Ref; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool T/F; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Lua_Script
	Ref; *Description Here*

- Model_Name
	File; *Description Here*

- Radar_Icon_Name
	File; *Description Here*

- Radar_Icon_Size
	Ref; *Description Here*

- SFXEvent_Beacon_Placed
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Tactical_Health
	Ref; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Variant_Of_Existing_Type
	Ref; *Description Here*

SpecialStructures
-----------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpecialStructure``                                              ``Name``
================================================================= =================================================================

|

SpecialStructure
^^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

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

- Autoresolve_Health
	Int; *Description Here*

- Barrel_Bone_Name
	Ref; *Description Here*

- Base_Level_Available
	Int; *Description Here*

- Base_Position
	Ref; *Description Here*

- Base_Shield_Always_Off
	Ref; *Description Here*

- Base_Shield_Radius
	Int; *Description Here*

- Behavior
	Ref, Ref; *Description Here*

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Bombing_Run_Prevention_Radius
	Int; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Max_Instances_Per_Planet
	Ref; *Description Here*

- Build_Requires_Initial_Placement
	Bool t/f; *Description Here*

- Build_Tab_Special_Structures
	Bool Y/N; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- Can_Contain_Heroes_During_Ground_Battle
	Ref; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Soft_Footprint_Radius
	Ref; *Description Here*

- Damage
	Int; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Clone_Is_Obstacle
	Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Destruction_Survivors
	Ref, Float; *Description Here*

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
	Bool Y/N; *Description Here*

- Fire_Inaccuracy_Distance
	Ref, Float; *Description Here*

- GUI_Bounds_Scale
	Float; *Description Here*

- GUI_Bracket_Height
	Int; *Description Here*

- GUI_Bracket_Size
	Int; *Description Here*

- GUI_Bracket_Width
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

- Galactic_Influence_Range
	Float; *Description Here*

- Gravity_Control_Field_Range
	Float; *Description Here*

- HQ_Win_Condition_Relevant
	Bool y/n; *Description Here*

- Has_Land_Evaluator
	Bool T/F; *Description Here*

- Has_Space_Evaluator
	Bool T/F; *Description Here*

- Hyperspace_Fleet_Reveal_Range
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Influences_Capture_Point
	Bool T/F; *Description Here*

- Initial_State_Visible_Under_FOW
	Bool T/F; *Description Here*

- Is_Community_Property
	Bool Y/N; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Is_Impassable_Asteroid
	Ref; *Description Here*

- Is_Interdictor
	Bool Y/N; *Description Here*

- Is_Special_Weapon_In_Space
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Land_Damage_Alternates
	Int, Int, Int; *Description Here*

- Land_Damage_SFX
	Ref, Ref, Ref; *Description Here*

- Land_Damage_Thresholds
	Int, Float, Float; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Land_Victory_Relevant
	Bool Y/N; *Description Here*

- Last_State_Visible_Under_FOW
	Ref; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Lobbing_Superweapon_Chargeup_Frames
	Int; *Description Here*

- Lobbing_Superweapon_Chargeup_Particle
	Ref; *Description Here*

- Lobbing_Superweapon_Chargeup_Particle_Bone_Name
	Ref; *Description Here*

- Lobbing_Superweapon_SFXEvent_Chargeup
	Ref; *Description Here*

- Lobbing_Superweapon_SFXEvent_Fire
	Ref; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- MP_Encyclopedia_Text
	Ref, Ref; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Modifies_Reveal_Range
	Bool y/n; *Description Here*

- Movie_Object
	Bool t/f; *Description Here*

- Multisample_FOW_Check
	Bool Y/N; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

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

- Place_At_Every_Specific_Marker_Position
	Bool T/F; *Description Here*

- Place_Other_Type_At_Every_Specific_Marker_Position
	Ref; *Description Here*

- Political_Control
	Int; *Description Here*

- Prevents_Blockade_Run_Attrition
	Bool T/F; *Description Here*

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

- Radar_Icon_Name
	None; *Description Here*

- Radar_Icon_Size
	Ref; *Description Here*

- Radar_Range_Icon_Name
	File; *Description Here*

- Radar_Show_Facing
	Bool Y/N; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Reinforcement_Prevention_Radius
	Int; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Planets
	None; *Description Here*

- Required_Special_Structures
	None; *Description Here*

- Required_Star_Base_Level
	Int; *Description Here*

- Required_Timeline
	Int; *Description Here*

- Requires_Base_Power
	Bool T/F; *Description Here*

- Reserve_Spawned_Units_Tech_0
	Ref, Ref; *Description Here*

- Reveal_During_Setup_Phase
	Ref; *Description Here*

- Reveal_Range_Modifier
	Float; *Description Here*

- SFXEvent_Ambient_Loop
	Ref; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Powered_Active_Loop
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Sold_Tactical
	Ref; *Description Here*

- SFXEvent_Special_Weapon_Ready
	Ref; *Description Here*

- SFXEvent_Turret_Rotating_Loop
	Ref; *Description Here*

- SFXEvent_Unit_Lost
	Ref; *Description Here*

- SFXEvent_Unit_Under_Attack
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- SecondaryOccupationPassability
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Shield_Normal_Color
	Float, Float, Float, Float; *Description Here*

- Shield_Off_Anim
	Ref; *Description Here*

- Shield_On_Anim
	Ref; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Shield_Upgraded_Color
	Float, Float, Float, Float; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- Slice_Cost_Credits
	Int; *Description Here*

- SpaceAutoResolveHitRate
	Int; *Description Here*

- SpaceAutoResolveStunRate
	Int; *Description Here*

- SpaceBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Space_Obstacle_Offset
	Ref; *Description Here*

- Space_Victory_Relevant
	Bool Y/N; *Description Here*

- Spawn_Garrison_On_Load
	Bool T/F; *Description Here*

- Spawned_Squadron_Delay_Seconds
	Int; *Description Here*

- Spawned_Squadron_Location_Bones
	Ref; *Description Here*

- Spawned_Squadron_Location_Flyout_Distances
	Float; *Description Here*

- Special_Weapon_Index
	Int; *Description Here*

- Special_Weapon_Target_Action_Index
	Ref; *Description Here*

- Special_Weapon_Valid_Targets
	Ref | Ref | Ref | Ref | Ref; *Description Here*

- Starting_Spawned_Units_Tech_0
	Ref, Int; *Description Here*

- Tactical_Additional_Structure_Type
	Ref; *Description Here*

- Tactical_Buildable_Objects_Campaign
	Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Tactical_Buildable_Objects_Multiplayer
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Tactical_Sell_Credits
	Ref; *Description Here*

- Targeting_Fire_Inaccuracy
	Ref, Float; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Min_Attack_Distance
	Ref; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Tech_Level
	Int; *Description Here*

- Terrain_Texture_Modifier_Join_Distance
	Float; *Description Here*

- Terrain_Texture_Modifier_Material
	Int; *Description Here*

- Terrain_Texture_Modifier_Square
	Bool t/f; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Turret_Bone_Name
	Ref; *Description Here*

- Turret_Elevate_Extent_Degrees
	Int; *Description Here*

- Turret_Rest_Angle
	Float, Float, Float; *Description Here*

- Turret_Rotate_Extent_Degrees
	Int; *Description Here*

- Turret_Rotate_Speed
	Float; *Description Here*

- Turret_Targets_Air_Vehicles
	Ref; *Description Here*

- Turret_Targets_Anything_Else
	Ref; *Description Here*

- Turret_Targets_Ground_Infantry
	Ref; *Description Here*

- Turret_Targets_Ground_Vehicles
	Ref; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- Weapon_Quantity
	Int; *Description Here*

- Weapon_Type
	Ref; *Description Here*

TechBuildings
-------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``TechBuilding``                                                  ``Name``
================================================================= =================================================================

|

TechBuilding
^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Affiliation
	Ref; *Description Here*

- Behavior
	None; *Description Here*

- Build_Advances_Tech_Level
	Int; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Limit_Current_Per_Player
	Int; *Description Here*

- Build_Tab_Special_Structures
	Bool Y/N; *Description Here*

- Build_Time_Reduced_By_Multiple_Factories
	Ref; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- GUI_Row
	Ref; *Description Here*

- Icon_Name
	File; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Special_Structures
	Ref; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

UpgradeObjects
--------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``UpgradeObject``                                                 ``Name``
================================================================= =================================================================

|

UpgradeObject
^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Behavior
	Ref; *Description Here*

- Build_Limit_Current_For_All_Allies
	Int; *Description Here*

- Build_Limit_Current_Per_Player
	Int; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Destroy_Previous_Upgrade_Level
	Bool Y/N; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Icon_Name
	File; *Description Here*

- Is_Skirmish_Tactical_Super_Weapon
	Bool t/f; *Description Here*

- Next_Upgrade_Level_Type
	None; *Description Here*

- Previous_Upgrade_Level_Type
	None; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Special_Weapon_Ready
	Ref; *Description Here*

- Show_In_Sidebar_When_Complete
	Ref; *Description Here*

- Show_In_Sidebar_While_Building
	Ref; *Description Here*

- Tactical_Build_Cost_Campaign
	Int; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Ref; *Description Here*

- Tactical_Build_Increments_Tech_Level
	Ref; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Ref; *Description Here*

- Tactical_Destruction_Decrements_Tech_Level
	Ref; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Variant_Of_Existing_Type
	Ref; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
