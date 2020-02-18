.. _xml_game_object_type_unit:
.. Template to use for XML type documentation

****
Unit
****


About
=====
This category covers all top-level nodes that indicate unit information, usually having a suffix of ``Units``. Subnodes and nodes specific to a top-level node will be in its respective page, while all shared subnodes and nodes will be in this document.


Structure
===============
FighterUnits
------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpaceUnit``                                                     ``Name``
================================================================= =================================================================

|

SpaceUnit
^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Affiliation
	Ref; *Description Here*

- Air_Vehicle_Turret_Target
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Asteroid_Damage_Hit_Particles
	Ref; *Description Here*

- Avoid_Enemy_Exclusion_Range
	Float; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Begin_Turn_Towards_Distance
	Float; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- CategoryMask
	Ref | Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Collision_Box_Modifier
	Float; *Description Here*

- Create_Team
	Bool Y/N; *Description Here*

- Custom_Footprint_Radius
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Damage_Type
	Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Fire_Inaccuracy_Distance
	Ref, Float; *Description Here*

- Fires_Forward
	Bool y/n; *Description Here*

- FormationOrder
	Int; *Description Here*

- Formation_Priority
	Int; *Description Here*

- HardPoints
	Ref, Ref; *Description Here*

- Hyperspace
	Bool Y/N; *Description Here*

- Hyperspace_Speed
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Is_Bomber
	Bool y/n; *Description Here*

- Is_Escort
	Bool y/n; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- Land_Bomber_Type
	Ref; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Maintenance_Cost
	Float; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Lift
	Int; *Description Here*

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- Min_Speed
	Float; *Description Here*

- Min_Speed_Fraction_For_Turn
	Float; *Description Here*

- Minimum_Follow_Distance
	Float; *Description Here*

- Mouse_Collide_Override_Sphere_Radius
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- Number_per_Squadron
	Int; *Description Here*

- Out_Of_Combat_Defense_Adjustment
	Float; *Description Here*

- Political_Control
	Int; *Description Here*

- Population_Value
	Int; *Description Here*

- Projectile_Fire_Pulse_Count
	Int; *Description Here*

- Projectile_Fire_Pulse_Delay_Seconds
	Float; *Description Here*

- Projectile_Fire_Recharge_Seconds
	Float; *Description Here*

- Projectile_Types
	Ref; *Description Here*

- Property_Flags
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Int; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Star_Base_Level
	Int; *Description Here*

- SFXEvent_Ambient_Moving
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Max_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Min_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Assist_Attack
	Ref; *Description Here*

- SFXEvent_Assist_Move
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Attack_Hardpoint
	Ref, Ref; *Description Here*

- SFXEvent_Enemy_Damaged_Health_Critical_Warning
	Ref; *Description Here*

- SFXEvent_Enemy_Damaged_Health_Low_Warning
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Hardpoint
	Ref; *Description Here*

- SFXEvent_Health_Critical_Warning
	Ref; *Description Here*

- SFXEvent_Health_Low_Warning
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Move_Into_Asteroid_Field
	Ref; *Description Here*

- SFXEvent_Move_Into_Nebula
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Shield_Armor_Type
	Ref; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- SpaceBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Spin_Away_On_Death
	Bool Y/N; *Description Here*

- Spin_Away_On_Death_Chance
	Float; *Description Here*

- Spin_Away_On_Death_Explosion
	Ref; *Description Here*

- Spin_Away_On_Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Spin_Away_On_Death_Time
	Floatf; *Description Here*

- Squadron_Capacity
	Int; *Description Here*

- Strafe_Distance
	Float; *Description Here*

- Surface_Bombardment_Capable
	Bool y/n; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Targeting_Stickiness_Time_Threshold
	Float; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Turret_Elevate_Extent_Degrees
	Int; *Description Here*

- Turret_Rotate_Extent_Degrees
	Int; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

GenericHeroUnits
----------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GenericHeroUnit``                                               ``Name``
================================================================= =================================================================

|

GenericHeroUnit
^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Always_Spawn_In_Orbit
	Bool Y/N; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Attach_To_Flagship_During_Space_Battle
	Bool Y/N; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Behavior
	Ref; *Description Here*

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Bone_Name
	Ref; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- CanCellStack
	Bool y/n; *Description Here*

- Can_Be_Neutralized_By_Major_Heroes
	Bool Y/N; *Description Here*

- Can_Be_Neutralized_By_Minor_Heroes
	Bool Y/N; *Description Here*

- Can_Hyperspace_Without_Activating_Ability
	Bool Y/N; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Create_Team
	Bool Y/N; *Description Here*

- Crouch_Animation_Speed
	Float; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Soft_Footprint_Radius
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Death_Fade_Time
	Float; *Description Here*

- Death_Persistence_Duration
	Float; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Execute_Script_On_Type
	Bool t/f; *Description Here*

- FormationOrder
	Ref; *Description Here*

- FormationRaggedness
	Float; *Description Here*

- FormationSpacing
	Float; *Description Here*

- GUI_Row
	Ref; *Description Here*

- Ground_Infantry_Turret_Target
	Ref; *Description Here*

- Guard_Chase_Range
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Is_Generic_Hero
	Bool Y/N; *Description Here*

- Is_Sprite
	Bool Y/N; *Description Here*

- Is_Squashable
	Ref; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Anim_Override_Name
	File; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Lua_Script
	Ref; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- MaxJiggleDistance
	Ref; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- Movement_Animation_Speed
	Float; *Description Here*

- Neutralization_Cost
	Float; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Occlusion_Silhouette_Enabled
	Int; *Description Here*

- OccupationStyle
	Ref; *Description Here*

- OverrideAcceleration
	Float; *Description Here*

- OverrideDeceleration
	Float; *Description Here*

- Play_SFXEvent_On_Sighting
	Bool T/F; *Description Here*

- Political_Control
	Int; *Description Here*

- Projectile_Fire_Recharge_Seconds
	Float; *Description Here*

- Projectile_Types
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Ranking_In_Category
	Ref; *Description Here*

- Rotation_Animation_Speed
	Float; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Group_Attack
	Ref; *Description Here*

- SFXEvent_Group_Move
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Show_Hero_Head
	Bool Y/N; *Description Here*

- Size_Value
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Stay_In_Transport_During_Ground_Battle
	Bool Y/N; *Description Here*

- SurfaceFX_Name
	Ref, Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Targeting_Fire_Inaccuracy
	Ref, Float; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Targeting_Stickiness_Time_Threshold
	Float; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Type
	Ref; *Description Here*

- UnitCollisionClass
	Ref; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- Walk_Animation_Speed
	Float; *Description Here*


GroundInfantry_Units
--------------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GroundInfantry``                                                ``Name``
================================================================= =================================================================

|

GroundInfantry
^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Base_Shield_Penetration_Particle
	Ref; *Description Here*

- Behavior
	Ref; *Description Here*

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Bone_Name
	Ref; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- Burning_Damage_Per_Second
	Float; *Description Here*

- CanCellStack
	Bool y/n; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Cinematic_Anim_Blend_Seconds
	Float; *Description Here*

- Cinematic_Anim_Index
	Int; *Description Here*

- Cinematic_Anim_Speed
	Float; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Conversion_Ability_Changes_To_Enemy
	Ref; *Description Here*

- Create_Team
	Bool Y/N; *Description Here*

- Crouch_Animation_Speed
	Float; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Soft_Footprint_Radius
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_Fade_Time
	Float; *Description Here*

- Death_Persistence_Duration
	Float; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Deploys
	Bool Y/N; *Description Here*

- Destruction_Survivors
	Ref, Float; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Fire_Category_Restrictions
	Ref; *Description Here*

- FormationGrouping
	Ref; *Description Here*

- FormationOrder
	Ref; *Description Here*

- FormationRaggedness
	Float; *Description Here*

- FormationSpacing
	Float; *Description Here*

- Formation_Formup_Wait_Style
	Ref; *Description Here*

- GUI_Bracket_Height
	Int; *Description Here*

- GUI_Bracket_Size
	Int; *Description Here*

- GUI_Bracket_Width
	Int; *Description Here*

- Ground_Infantry_Turret_Target
	Ref; *Description Here*

- Guard_Chase_Range
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Influences_Capture_Point
	Ref; *Description Here*

- IsBuildable
	Bool Y/N; *Description Here*

- Is_Affected_By_Gravity_Control_Field
	Ref; *Description Here*

- Is_Combustible
	Bool y/n; *Description Here*

- Is_Squashable
	Ref; *Description Here*

- Is_Squashable_By_Supercrusher
	Bool Y/N; *Description Here*

- Is_Stationary_When_Attacking
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Land_Damage_Alternates
	Int, Int, Int; *Description Here*

- Land_Damage_SFX
	Ref, Ref, Ref; *Description Here*

- Land_Damage_Thresholds
	Int, Float, Float; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Anim_Override_Name
	File; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Land_Terrain_Model_Mapping
	Ref, File, Ref, File, Ref, File, Ref, File, Ref, File, Ref, File, Ref, File; *Description Here*

- LateralAcceleration
	Float; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Lua_Script
	Ref; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- MaxJiggleDistance
	Float; *Description Here*

- Max_Rate_Of_Roll
	Int; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Ref; *Description Here*

- Min_Speed_Fraction_For_Turn
	Ref; *Description Here*

- MinimumPushReturnDistance
	Ref; *Description Here*

- Mouse_Collide_Override_Sphere_Radius
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- Movement_Animation_Speed
	Float; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Occlusion_Silhouette_Enabled
	Int; *Description Here*

- OccupationStyle
	Ref; *Description Here*

- On_Fire_Speed_Modifier
	Floatf; *Description Here*

- OverrideAcceleration
	Float; *Description Here*

- OverrideDeceleration
	Float; *Description Here*

- Pause_During_Cinematic_Anim
	Bool y/n; *Description Here*

- Political_Control
	Int; *Description Here*

- Presence_Induced_Animations
	Ref, Ref, Ref, Ref; *Description Here*

- Projectile_Appearance_Delay_Frames
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
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Required_Timeline
	Int; *Description Here*

- Rotation_Animation_Speed
	Float; *Description Here*

- SFXEvent_Ambient_Moving
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Max_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Min_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Assist_Attack
	Ref; *Description Here*

- SFXEvent_Assist_Move
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Complete
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Started
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Sensor_Range
	Int; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Size_Value
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Specific_Death_Anim_Index
	None; *Description Here*

- Specific_Death_Anim_Type
	Ref; *Description Here*

- Stealth_Capable
	Bool Y/N; *Description Here*

- SurfaceFX_Name
	Ref, Ref; *Description Here*

- Surface_Type_Cover_Damage_Shield
	Float; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	Ref; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Targeting_Allowed_When_Burning
	Bool y/n; *Description Here*

- Targeting_Fire_Inaccuracy
	Ref, Float; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Targeting_Stickiness_Time_Threshold
	Float; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Turret_Elevate_Extent_Degrees
	Float; *Description Here*

- Turret_Rotate_Extent_Degrees
	Float; *Description Here*

- Type
	Ref; *Description Here*

- UnitCollisionClass
	Ref; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- WaitsForFormationFormup
	Bool t/f; *Description Here*

- Walk_Animation_Speed
	Float; *Description Here*

- Walk_Transition
	Bool Y/N; *Description Here*

- Weather_Category
	Ref; *Description Here*

- Wind_Disturbance_Radius
	Int; *Description Here*

- Wind_Disturbance_Sphere_Alpha
	Float; *Description Here*

- Wind_Disturbance_Strength
	Int; *Description Here*

GroundVehicles
--------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GroundVehicle``                                                 ``Name``
================================================================= =================================================================

|

GroundVehicle
^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Air_Vehicle_Turret_Target
	Ref; *Description Here*

- Apply_Y_Turret_Rotate_To_Axis
	Int; *Description Here*

- Apply_Z_Turret_Rotate_To_Axis
	Int; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Asteroid_Damage_Hit_Particles
	Ref; *Description Here*

- Attack_Animation_Is_Overlay
	Bool y/n; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Auto_Deploys
	Bool Y/N; *Description Here*

- Autonomous_Move_Extension_Vs_Attacker
	Float; *Description Here*

- Autoresolve_Health
	Float; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Barrel_Bone_Name
	Ref; *Description Here*

- Base_Shield_Penetration_Particle
	Ref; *Description Here*

- Behavior
	Ref, Ref; *Description Here*

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Bone_Name
	Ref; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Cache_Crusher_Boxes
	Bool Y/N; *Description Here*

- CanCellStack
	Bool y/n; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Close_Enough_Angle_For_Move_Start
	Ref; *Description Here*

- Collidable_By_Projectile_Dead
	Bool Y/N; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Converted_To_Enemy_Die_Time_Seconds
	Int; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_XExtent_Offset
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Hard_YExtent_Deployed
	Float; *Description Here*

- Custom_Hard_YExtent_Offset
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Damage_Type
	Ref; *Description Here*

- Damaged_Smoke_Asset_Name
	File; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Clone_Is_Obstacle
	Bool y/n; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_Explosions_End
	Ref; *Description Here*

- Death_Fade_Time
	Float; *Description Here*

- Death_Persistence_Duration
	Float; *Description Here*

- Death_SFXEvent_End_Die
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Deployment_Anim_Rate
	Float; *Description Here*

- Deploys
	Bool Y/N; *Description Here*

- Destruction_Survivors
	Ref, Float; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Exit_Door_Angle_Degrees
	Float; *Description Here*

- Exit_Door_Distance
	Float; *Description Here*

- Fire_Category_Restrictions
	Ref; *Description Here*

- Fire_Weapon_When_Deployed
	Bool Y/N; *Description Here*

- Fire_Weapon_When_In_Normal_Attack_Mode
	Bool Y/N; *Description Here*

- Fire_Weapon_When_In_Rocket_Attack_Mode
	Bool Y/N; *Description Here*

- Fire_Weapon_When_Undeployed
	Bool Y/N; *Description Here*

- Fires_Forward
	Bool y/n; *Description Here*

- FormationGrouping
	Ref; *Description Here*

- FormationOrder
	Ref; *Description Here*

- FormationRaggedness
	Ref; *Description Here*

- FormationSpacing
	Float; *Description Here*

- GUI_Bounds_Scale
	Float; *Description Here*

- GUI_Bracket_Size
	Int; *Description Here*

- Glory_Cinematics
	Ref, Ref, Ref; *Description Here*

- Ground_Infantry_Turret_Target
	Ref; *Description Here*

- Ground_Vehicle_Turret_Target
	Ref; *Description Here*

- Guard_Chase_Range
	Float; *Description Here*

- HardPoints
	Ref; *Description Here*

- Hardpoints
	Ref; *Description Here*

- Has_Land_Evaluator
	Bool Y/N; *Description Here*

- Has_Pre_Turn_Anim
	Ref; *Description Here*

- Hover_Offset
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Influences_Capture_Point
	Ref; *Description Here*

- IsDeathClone
	Ref; *Description Here*

- IsDeathCloneObstacle
	Ref; *Description Here*

- Is_Affected_By_Gravity_Control_Field
	Ref; *Description Here*

- Is_Sprite
	Bool Y/N; *Description Here*

- Is_Squashable
	Ref; *Description Here*

- Is_Squashable_By_Supercrusher
	Bool Y/N; *Description Here*

- Is_Supercrusher
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

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

- Layer_Z_Adjust
	Float; *Description Here*

- Locomotor_Has_Animation_Priority
	Bool y/n; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Lua_Script
	Ref; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- MaxFacingLookAheadFrames
	Float; *Description Here*

- MaxJiggleDistance
	Ref; *Description Here*

- MaxSecondaryTurnROTCoefficient
	Float; *Description Here*

- Max_Lift
	Float; *Description Here*

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- MinSecondaryTurnROTCoefficient
	Float; *Description Here*

- Min_Speed
	Float; *Description Here*

- Min_Speed_Fraction_For_Turn
	Float; *Description Here*

- MinimumPushReturnDistance
	Ref; *Description Here*

- Mouse_Collide_Override_Sphere_Radius
	Float; *Description Here*

- MovementBoxExpansionFactor
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- MovementPredictionInterval
	Float; *Description Here*

- Movement_Animation_Speed
	Float; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Occlusion_Silhouette_Enabled
	Int; *Description Here*

- OccupationStyle
	Ref; *Description Here*

- Overall_Length
	Float; *Description Here*

- Overall_Width
	Float; *Description Here*

- OverrideAcceleration
	Float; *Description Here*

- OverrideDeceleration
	Float; *Description Here*

- PathFrameDelay
	Ref; *Description Here*

- Political_Control
	Int; *Description Here*

- Prepare_Strafe_Height
	Float; *Description Here*

- Presence_Range
	Float; *Description Here*

- Projectile_Appearance_Delay_Frames
	Int, Int; *Description Here*

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
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Ranking_In_Category
	Int; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Required_Timeline
	Int; *Description Here*

- Rotation_Animation_Speed
	Float; *Description Here*

- SFXEvent_Ambient_Loop
	Ref; *Description Here*

- SFXEvent_Ambient_Moving
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Max_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Min_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Assist_Attack
	Ref; *Description Here*

- SFXEvent_Assist_Move
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Idle_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Complete
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Started
	Ref; *Description Here*

- SFXEvent_Turret_Rotating_Loop
	Ref; *Description Here*

- SFXEvent_Unit_Lost
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- SecondaryTurnAngle
	Ref; *Description Here*

- SecondaryTurnInPlaceROTCoefficient
	Float; *Description Here*

- SecondaryTurnLookaheadDistance
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Selt_Destruct_SFXEvent_Start_Die
	Ref; *Description Here*

- Sensor_Range
	Int; *Description Here*

- Shield_Armor_Type
	Ref; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Should_Cause_Limited_Turrets_To_Turn
	Ref; *Description Here*

- Should_Reinforcements_Move
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Specific_Death_Anim_Index
	None; *Description Here*

- Specific_Death_Anim_Type
	Ref; *Description Here*

- Spin_Away_On_Death
	Bool Y/N; *Description Here*

- Spin_Away_On_Death_Chance
	Float; *Description Here*

- Spin_Away_On_Death_Explosion
	Ref; *Description Here*

- Spin_Away_On_Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Spin_Away_On_Death_Time
	Floatf; *Description Here*

- Stationary_Space_Layer
	Ref; *Description Here*

- Stealth_Capable
	Bool Y/N; *Description Here*

- Stopped_Rate_Of_Turn
	Float; *Description Here*

- SurfaceFX_Name
	Ref; *Description Here*

- Surface_Type_Cover_Damage_Shield
	Float; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Target_Bones
	Ref, Ref, Ref; *Description Here*

- Targeting_Fire_Inaccuracy
	Ref, Float; *Description Here*

- Targeting_Fire_Inaccuracy_Fixed_Radius
	Ref; *Description Here*

- Targeting_Land_Model_Stay_Horiz_Flat
	Ref; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Min_Attack_Distance
	Ref; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Targeting_Stickiness_Time_Threshold
	Float; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Tread_Scroll_Rate
	Float; *Description Here*

- Turret_Bone_Name
	Ref; *Description Here*

- Turret_Deployed_Rest_Angle
	Float, Float, Float; *Description Here*

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

- Type
	Ref; *Description Here*

- UnitCollisionClass
	Ref; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- UseSecondaryFacing
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Vehicle_Thief_Inside_Clone
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- Walk_Transition
	Bool Y/N; *Description Here*

- Weather_Category
	Ref; *Description Here*

- Wind_Disturbance_Radius
	Int; *Description Here*

- Wind_Disturbance_Sphere_Alpha
	Float; *Description Here*

- Wind_Disturbance_Strength
	Int; *Description Here*

HeroUnits
---------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``HeroUnit``                                                      ``Name``
================================================================= =================================================================

|

HeroUnit
^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Alternate_Max_Rate_Of_Turn
	Float; *Description Here*

- Alternate_Max_Speed
	Float; *Description Here*

- Always_Spawn_In_Orbit
	Bool Y/N; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Attach_To_Flagship_During_Space_Battle
	Bool Y/N; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Autonomous_Move_Extension_Vs_Attacker
	Float; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Bone_Name
	Ref; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- CanCellStack
	Bool y/n; *Description Here*

- Can_Be_Neutralized_By_Major_Heroes
	Bool Y/N; *Description Here*

- Can_Be_Neutralized_By_Minor_Heroes
	Bool Y/N; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Ref; *Description Here*

- Create_Team
	Ref; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Soft_Footprint_Radius
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Damage_Type
	Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_Fade_Time
	Float; *Description Here*

- Death_Persistence_Duration
	Float; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Deploys
	Bool Y/N; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- FormationOrder
	Ref; *Description Here*

- FormationRaggedness
	Float; *Description Here*

- FormationSpacing
	Float; *Description Here*

- GUI_Bracket_Height
	Int; *Description Here*

- GUI_Bracket_Size
	Int; *Description Here*

- GUI_Bracket_Width
	Int; *Description Here*

- GalacticBehavior
	Ref; *Description Here*

- Galactic_Influence_Range
	Float; *Description Here*

- Ground_Infantry_Turret_Target
	Ref; *Description Here*

- Guard_Chase_Range
	Float; *Description Here*

- Has_Land_Evaluator
	Bool T/F; *Description Here*

- Highlight_Blob_Material_Name
	Ref; *Description Here*

- Holster_Disable_Engine_Loops
	Ref; *Description Here*

- Holster_Drawn_Bone_Translation
	Float, Float, Float; *Description Here*

- Holster_Holstered_Bone_Translation
	Float, Float, Float; *Description Here*

- Holster_Minimum_Drawn_Time_In_Secs
	Float; *Description Here*

- Holster_Transition_Time_In_Secs
	Float; *Description Here*

- Holster_Weapon_Bone_Name
	Ref; *Description Here*

- Hover_Offset
	Float; *Description Here*

- Hyperspace_Fleet_Reveal_Range
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- IsBuildable
	Bool Y/N; *Description Here*

- Is_Force_Sensitive
	Bool Y/N; *Description Here*

- Is_Named_Hero
	Bool Y/N; *Description Here*

- Is_Squashable
	Ref; *Description Here*

- Is_Stationary_When_Attacking
	Bool Y/N; *Description Here*

- Is_Super_Weapon_Killer
	Bool Y/N; *Description Here*

- Is_Visible_On_Enemy_Radar
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Lua_Script
	Ref; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- MaxJiggleDistance
	Float; *Description Here*

- Max_Lift
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Min_Speed
	Float; *Description Here*

- MinimumPushReturnDistance
	Ref; *Description Here*

- Mouse_Collide_Override_Sphere_Radius
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- Movement_Animation_Speed
	Float; *Description Here*

- Neutralization_Cost
	Float; *Description Here*

- Occlusion_Silhouette_Enabled
	Int; *Description Here*

- OccupationStyle
	Ref; *Description Here*

- OverrideAcceleration
	Float; *Description Here*

- OverrideDeceleration
	Float; *Description Here*

- Play_SFXEvent_On_Sighting
	Bool T/F; *Description Here*

- Political_Control
	Int; *Description Here*

- Political_Faction
	Ref; *Description Here*

- Presence_Range
	Float; *Description Here*

- Primary_Locomotor_Name
	Ref; *Description Here*

- Projectile_Appearance_Delay_Frames
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

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Ranking_In_Category
	Ref; *Description Here*

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

- Respawn_Whole_Team_When_Killed
	Bool Y/N; *Description Here*

- Rotation_Animation_Speed
	Float; *Description Here*

- SFXEvent_Ambient_Moving
	Ref; *Description Here*

- SFXEvent_Announce
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Attacked
	Ref; *Description Here*

- SFXEvent_Deploy
	Ref; *Description Here*

- SFXEvent_Draw_Weapon
	Ref; *Description Here*

- SFXEvent_Enemy_Health_Critical_Warning
	Ref; *Description Here*

- SFXEvent_Enemy_Health_Low_Warning
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Idle_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Group_Attack
	Ref; *Description Here*

- SFXEvent_Group_Move
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Health_Critical_Warning
	Ref; *Description Here*

- SFXEvent_Health_Low_Warning
	Ref; *Description Here*

- SFXEvent_Holster_Weapon
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Complete
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Started
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Secondary_Locomotor_Name
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Selection_Blob_Material_Name
	Ref; *Description Here*

- Sensor_Range
	Int; *Description Here*

- Share_Damage_With_Teammates
	Bool Y/N; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Size_Value
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Spawn_Planet
	Ref; *Description Here*

- Stay_In_Transport_During_Ground_Battle
	Bool Y/N; *Description Here*

- Stealth_Capable
	Bool Y/N; *Description Here*

- SurfaceFX_Name
	Ref, Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Targeting_Fire_Inaccuracy
	Ref, Float; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Targeting_Stickiness_Time_Threshold
	Float; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Type
	Ref; *Description Here*

- Unique_Ground_Unit
	Ref; *Description Here*

- Unique_Space_Unit
	Ref; *Description Here*

- UnitCollisionClass
	Ref; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- Uses_Multiple_Locomotors
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- WaitsForFormationFormup
	Bool t/f; *Description Here*

- Walk_Animation_Speed
	Float; *Description Here*

Indigenous_Units
----------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Indigenous_Unit``                                               ``Name``
================================================================= =================================================================

|

Indigenous_Unit
^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Air_Vehicle_Turret_Target
	Ref; *Description Here*

- Allow_Idle_When_Moving
	Bool Y/N; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Avoidance_Disabled
	Ref; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Base_Shield_Penetration_Particle
	Ref; *Description Here*

- Begin_Turn_Towards_Distance
	Float; *Description Here*

- Behavior
	Ref; *Description Here*

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Bone_Name
	Ref; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- Burning_Damage_Per_Second
	Float; *Description Here*

- CanCellStack
	Bool y/n; *Description Here*

- Can_Indigenous_Unit_Stop
	Bool Y/N; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Close_Enough_Angle_For_Move_Start
	Float; *Description Here*

- Collidable_By_Projectile_Dead
	Bool Y/N; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Create_Team
	Bool T/F; *Description Here*

- Create_Team_Type
	Ref; *Description Here*

- Crouch_Animation_Speed
	Float; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_XExtent_Offset
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Soft_Footprint_Radius
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Clone_Is_Obstacle
	Bool y/n; *Description Here*

- Death_Fade_Time
	Float; *Description Here*

- Death_Persistence_Duration
	Float; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Deploys
	Bool Y/N; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Fire_Category_Restrictions
	Ref, Ref; *Description Here*

- FormationGrouping
	Ref; *Description Here*

- FormationOrder
	Ref; *Description Here*

- FormationRaggedness
	Float; *Description Here*

- FormationSpacing
	Float; *Description Here*

- GUI_Bracket_Height
	Int; *Description Here*

- GUI_Bracket_Size
	Int; *Description Here*

- GUI_Bracket_Width
	Int; *Description Here*

- Ground_Infantry_Turret_Target
	Ref; *Description Here*

- Guard_Chase_Range
	Float; *Description Here*

- Harass_Enemy_Exclusion_Range
	Float; *Description Here*

- Has_Pre_Turn_Anim
	Ref; *Description Here*

- Hover_Offset
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Influences_Capture_Point
	Ref; *Description Here*

- IsBuildable
	Bool Y/N; *Description Here*

- IsDeathCloneObstacle
	Ref; *Description Here*

- Is_Combustible
	Bool y/n; *Description Here*

- Is_Squashable
	Ref; *Description Here*

- Is_Stationary_When_Attacking
	Bool Y/N; *Description Here*

- Is_Valid_Target
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Anim_Override_Name
	File; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- MaxFacingLookAheadFrames
	Float; *Description Here*

- MaxJiggleDistance
	Ref; *Description Here*

- Max_Lift
	Int; *Description Here*

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- Min_Speed
	Float; *Description Here*

- Min_Speed_Fraction_For_Turn
	Float; *Description Here*

- MinimumPushReturnDistance
	Ref; *Description Here*

- Mouse_Collide_Override_Sphere_Radius
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- Movement_Animation_Speed
	Float; *Description Here*

- Movie_Object
	Bool t/f; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Occlusion_Silhouette_Enabled
	Int; *Description Here*

- OccupationStyle
	Ref; *Description Here*

- On_Fire_Speed_Modifier
	Floatf; *Description Here*

- OverrideAcceleration
	Float; *Description Here*

- OverrideDeceleration
	Float; *Description Here*

- Political_Control
	Int; *Description Here*

- Prepare_Strafe_Height
	Float; *Description Here*

- Projectile_Appearance_Delay_Frames
	Ref; *Description Here*

- Projectile_Fire_Pulse_Count
	Int; *Description Here*

- Projectile_Fire_Pulse_Delay_Seconds
	Float; *Description Here*

- Projectile_Fire_Recharge_Seconds
	Int; *Description Here*

- Projectile_Types
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Planets
	None; *Description Here*

- Required_Special_Structures
	None; *Description Here*

- Required_Star_Base_Level
	Int; *Description Here*

- Required_Tech_Structure
	None; *Description Here*

- Required_Timeline
	Int; *Description Here*

- Rotation_Animation_Speed
	Float; *Description Here*

- SFXEvent_Ambient_Moving
	None; *Description Here*

- SFXEvent_Ambient_Moving_Max_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Min_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Assist_Attack
	Ref; *Description Here*

- SFXEvent_Assist_Move
	Ref; *Description Here*

- SFXEvent_Attack
	None; *Description Here*

- SFXEvent_Engine_Idle_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Move
	None; *Description Here*

- SFXEvent_Select
	None; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Int; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Sensor_Range
	Int; *Description Here*

- Size_Value
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Specific_Death_Anim_Index
	Ref; *Description Here*

- Specific_Death_Anim_Type
	Ref; *Description Here*

- Squash_Damage_Type
	Ref; *Description Here*

- SurfaceFX_Name
	Ref, Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Targeting_Allowed_When_Burning
	Bool y/n; *Description Here*

- Targeting_Fire_Inaccuracy
	Ref, Float; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Min_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

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

- Turret_Targets_Air_Vehicles
	Ref; *Description Here*

- Turret_Targets_Anything_Else
	Ref; *Description Here*

- Turret_Targets_Ground_Infantry
	Ref; *Description Here*

- Turret_Targets_Ground_Vehicles
	Ref; *Description Here*

- Turret_XY_Only
	Bool Y/N; *Description Here*

- Type
	Ref; *Description Here*

- UnitCollisionClass
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- Walk_Animation_Speed
	Float; *Description Here*

- Walk_Transition
	Bool Y/N; *Description Here*

- Weather_Category
	Ref; *Description Here*

- Wind_Disturbance_Radius
	Int; *Description Here*

- Wind_Disturbance_Sphere_Alpha
	Float; *Description Here*

- Wind_Disturbance_Strength
	Int; *Description Here*

LandBombingRunUnits
-------------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``LandBombingUnit``                                               ``Name``
================================================================= =================================================================

|

LandBombingUnit
^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Affiliation
	Ref; *Description Here*

- Air_Vehicle_Turret_Target
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Autoresolve_Health
	Float; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Behavior
	Ref; *Description Here*

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Material_Name
	None; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Damage
	Int; *Description Here*

- Damage_Hit_Particles
	Ref; *Description Here*

- Damaged_Smoke_Asset_Name
	File; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Deploys
	Bool Y/N; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Fires_Forward
	Bool y/n; *Description Here*

- Guard_Chase_Range
	Float; *Description Here*

- Hover_Offset
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- MaxFacingLookAheadFrames
	Float; *Description Here*

- Max_Lift
	Float; *Description Here*

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- Min_Speed
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- OccupationStyle
	Ref; *Description Here*

- Prepare_Strafe_Height
	Float; *Description Here*

- Projectile_Fire_Pulse_Count
	Int; *Description Here*

- Projectile_Fire_Pulse_Delay_Seconds
	Float; *Description Here*

- Projectile_Fire_Recharge_Seconds
	Float; *Description Here*

- Projectile_Types
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- SFXEvent_Ambient_Moving
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Max_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Min_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Bomb_Run_Incoming
	Ref; *Description Here*

- SFXEvent_Bomb_Run_Select_Target
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Hardpoint
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Shield_Hit_Particles
	Ref; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Size_Value
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Spin_Away_On_Death
	Bool Y/N; *Description Here*

- Spin_Away_On_Death_Chance
	Float; *Description Here*

- Spin_Away_On_Death_Explosion
	Ref; *Description Here*

- Spin_Away_On_Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Spin_Away_On_Death_Time
	Floatf; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Turret_Elevate_Extent_Degrees
	Int; *Description Here*

- Turret_Rotate_Extent_Degrees
	Int; *Description Here*

- Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- XSFXEvent_Ambient_Loop
	Ref; *Description Here*

SpaceCorvettes
--------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpaceUnit``                                                     ``Name``
================================================================= =================================================================

|

SpaceUnit
^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Affiliation
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Autonomous_Move_Extension_Vs_Attacker
	Float; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Behavior
	Ref, Ref, Ref, Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Tab_Space_Units
	Bool Y/N; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- CategoryMask
	Ref | Ref | Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Collision_Box_Modifier
	Float; *Description Here*

- Custom_Footprint_Radius
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Fire_Inaccuracy_Distance
	Ref, Float; *Description Here*

- Fires_Forward
	Bool y/n; *Description Here*

- FormationOrder
	Int; *Description Here*

- FormationPriority
	Int; *Description Here*

- Formation_Priority
	Int; *Description Here*

- GUI_Bracket_Size
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

- Guard_Chase_Range
	Float; *Description Here*

- HardPoints
	Ref, Ref, Ref; *Description Here*

- Hardpoints
	Ref, Ref, Ref, Ref, Ref; *Description Here*

- Has_Space_Evaluator
	Bool T/F; *Description Here*

- Hyperspace
	Bool Y/N; *Description Here*

- Hyperspace_Speed
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Is_Bomber
	Bool y/n; *Description Here*

- Is_Escort
	Bool Y/N; *Description Here*

- Is_Interdictor
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Maintenance_Cost
	Float; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Lift
	Float; *Description Here*

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- Min_Speed
	Float; *Description Here*

- Min_Speed_Fraction_For_Turn
	Float; *Description Here*

- Minimum_Follow_Distance
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- Number_per_Squadron
	Int; *Description Here*

- Out_Of_Combat_Defense_Adjustment
	Float; *Description Here*

- OverrideAcceleration
	Float; *Description Here*

- OverrideDeceleration
	Float; *Description Here*

- Political_Control
	Int; *Description Here*

- Population_Value
	Int; *Description Here*

- Projectile_Fire_Pulse_Count
	Int; *Description Here*

- Projectile_Fire_Pulse_Delay_Seconds
	Float; *Description Here*

- Projectile_Fire_Recharge_Seconds
	Int; *Description Here*

- Projectile_Types
	Ref; *Description Here*

- Property_Flags
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Int; *Description Here*

- Ranking_In_Category
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

- SFXEvent_Ambient_Loop
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Attack_Hardpoint
	Ref, Ref; *Description Here*

- SFXEvent_Attack_With_Non_Hero_Ability
	Ref; *Description Here*

- SFXEvent_Barrage
	Ref; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Idle_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Move_Into_Nebula
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Stop
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Complete
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Started
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Ref; *Description Here*

- Shield_Armor_Type
	Ref; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Should_Attacker_Hold_Fire_For_Special_Ability
	Bool T/F; *Description Here*

- Size_Value
	Int; *Description Here*

- Slice_Cost_Credits
	Int; *Description Here*

- SpaceBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Squadron_Capacity
	Int; *Description Here*

- Surface_Bombardment_Capable
	Bool Y/N; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Targeting_Fire_Inaccuracy_Fixed_Radius
	Ref; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Min_Attack_Distance
	Int; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Targeting_Stickiness_Time_Threshold
	Float; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Transport_Capacity
	Int; *Description Here*

- Turret_Elevate_Extent_Degrees
	Int; *Description Here*

- Turret_Rotate_Extent_Degrees
	Int; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- xxxSpace_Model_Name
	File; *Description Here*


SpaceUnitsCapital
-----------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpaceUnit``                                                     ``Name``
================================================================= =================================================================

|

SpaceUnit
^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Asteroid_Damage_Hit_Particles
	Ref; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Behavior
	Ref, Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Tab_Space_Units
	Bool Y/N; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- CategoryMask
	Ref | Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Damage
	Int; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Formation_Priority
	Int; *Description Here*

- GUI_Bracket_Height
	Int; *Description Here*

- GUI_Bracket_Size
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

- Glory_Cinematics
	Ref; *Description Here*

- Guard_Chase_Range
	Float; *Description Here*

- HardPoints
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Has_Space_Evaluator
	Bool T/F; *Description Here*

- Hyperspace
	Bool Y/N; *Description Here*

- Hyperspace_Speed
	Int; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Maintenance_Cost
	Float; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- Multisample_FOW_Check
	Bool Y/N; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- OverrideAcceleration
	Float; *Description Here*

- OverrideDeceleration
	Float; *Description Here*

- Political_Faction
	Ref; *Description Here*

- Population_Value
	Int; *Description Here*

- Radar_Icon_Name
	File; *Description Here*

- Radar_Icon_Scale_Land
	Float; *Description Here*

- Radar_Icon_Scale_Space
	Float; *Description Here*

- Ranking_In_Category
	Int; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Planets
	Ref, Ref, Ref, Ref; *Description Here*

- Required_Special_Structures
	None; *Description Here*

- Required_Star_Base_Level
	Int; *Description Here*

- Required_Timeline
	Int; *Description Here*

- Reserve_Spawned_Units_Tech_0
	Ref, Int; *Description Here*

- SFXEvent_Ambient_Loop
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Attack_Hardpoint
	Ref, Ref; *Description Here*

- SFXEvent_Barrage
	Ref; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Damaged_By_Asteroid
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Idle_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Hardpoint_Destroyed
	Ref, Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Move_Into_Asteroid_Field
	Ref; *Description Here*

- SFXEvent_Move_Into_Nebula
	Ref; *Description Here*

- SFXEvent_Move_Opposite
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Stop
	Ref; *Description Here*

- Scale_Factor
	Int; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Ref; *Description Here*

- Shield_Armor_Type
	Ref; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- Slice_Cost_Credits
	Int; *Description Here*

- SpaceBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Full_Stop_Command
	Ref; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Spawned_Squadron_Delay_Seconds
	Int; *Description Here*

- Squadron_Capacity
	Int; *Description Here*

- Starting_Spawned_Units_Tech_0
	Ref, Int; *Description Here*

- Surface_Bombardment_Capable
	Bool y/n; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Targeting_Stickiness_Time_Threshold
	Float; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- Visible_On_Radar_When_Fogged
	Bool t/f; *Description Here*

- xxxSpace_Model_Name
	File; *Description Here*


|


|
|

SpaceUnitsFrigates
------------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpaceUnit``                                                     ``Name``
================================================================= =================================================================

|

SpaceUnit
^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Affiliation
	Ref, Ref, Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Asteroid_Damage_Hit_Particles
	Ref; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Behavior
	Ref, Ref, Ref, Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Tab_Space_Units
	Bool Y/N; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- CategoryMask
	Ref | Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Damage
	Int; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_Leave_Hulk_Behind
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Disallows_Hyperspace_Retreat
	Ref; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Formation_Priority
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

- Guard_Chase_Range
	Float; *Description Here*

- HardPoints
	Ref; *Description Here*

- Has_Space_Evaluator
	Bool T/F; *Description Here*

- Hyperspace
	Bool Y/N; *Description Here*

- Hyperspace_Speed
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Is_Bomber
	Bool y/n; *Description Here*

- Is_Escort
	Bool y/n; *Description Here*

- Is_Interdictor
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Lua_Script
	Ref; *Description Here*

- Maintenance_Cost
	Float; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- Moniker
	Ref; *Description Here*

- MovementClass
	Ref; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- Number_per_Squadron
	Int; *Description Here*

- OverrideAcceleration
	Float; *Description Here*

- OverrideDeceleration
	Float; *Description Here*

- Play_SFXEvent_On_Sighting
	Bool T/F; *Description Here*

- Political_Control
	Int; *Description Here*

- Population_Value
	Int; *Description Here*

- Radar_Icon_Scale_Land
	Float; *Description Here*

- Radar_Icon_Scale_Space
	Float; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Ranking_In_Category
	Int; *Description Here*

- Reinforcement_Prevention_Radius
	Ref; *Description Here*

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

- Reserve_Spawned_Units_Tech_0
	Ref, Int; *Description Here*

- SFXEvent_Ambient_Loop
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Attack_Hardpoint
	Ref, Ref; *Description Here*

- SFXEvent_Barrage
	Ref; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Damaged_By_Asteroid
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Idle_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Hardpoint_Destroyed
	Ref, Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Move_Into_Asteroid_Field
	Ref; *Description Here*

- SFXEvent_Move_Into_Nebula
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Stop
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Complete
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Started
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Ref; *Description Here*

- Shield_Armor_Type
	Ref; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- Slice_Cost_Credits
	Int; *Description Here*

- SpaceBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Full_Stop_Command
	Ref; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Spawned_Squadron_Delay_Seconds
	Int; *Description Here*

- Squadron_Capacity
	Int; *Description Here*

- Starting_Spawned_Units_Tech_0
	Ref, Int; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Target_Bones
	Ref, Ref; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Targeting_Stickiness_Time_Threshold
	Float; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Transport_Capacity
	Int; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- xxxSpace_Model_Name
	File; *Description Here*


|


|
|

SpaceUnitsSupers
----------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpaceUnit``                                                     ``Name``
================================================================= =================================================================

|

SpaceUnit
^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Behavior
	Ref; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Countdown_Text_ID
	Ref; *Description Here*

- Build_Countdown_Text_RGBA
	Int, Int, Int, Int; *Description Here*

- Build_Countdown_Timer
	Ref; *Description Here*

- Build_Limit_Current_Per_Player
	Int; *Description Here*

- Build_Limit_Lifetime_Per_Player
	Int; *Description Here*

- Build_Music_Completed
	Ref; *Description Here*

- Build_Speech_Completed
	Ref; *Description Here*

- Build_Speech_Countdowns
	Ref; *Description Here*

- Build_Speech_Stopped
	Ref; *Description Here*

- Build_Speech_Underway
	Ref; *Description Here*

- Build_Tab_Special_Structures
	Bool Y/N; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collision_Box_Modifier
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Formation_Priority
	Int; *Description Here*

- GUI_Row
	Ref; *Description Here*

- GalacticBehavior
	Ref; *Description Here*

- Galactic_Fleet_Override_Icon_Index
	Ref; *Description Here*

- Galactic_Fleet_Override_Model_Name
	Ref; *Description Here*

- Hyperspace
	Bool Y/N; *Description Here*

- Hyperspace_Speed
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- In_Background
	Bool Y/N; *Description Here*

- Is_Bomber
	Bool y/n; *Description Here*

- Is_Escort
	Bool y/n; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- Maintenance_Cost
	Float; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- Number_per_Squadron
	Int; *Description Here*

- Political_Faction
	Ref; *Description Here*

- Population_Value
	Int; *Description Here*

- Prevents_Story_Campaign_Autoresolve
	Bool y/n; *Description Here*

- Radar_Clip_To_Visible_Region
	Bool Y/N; *Description Here*

- Radar_Icon_Name
	File; *Description Here*

- Radar_Icon_Size
	Ref; *Description Here*

- Radar_Register_As_Foreground_Object
	Bool Y/N; *Description Here*

- Ranking_In_Category
	Ref; *Description Here*

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

- SFXEvent_Fire
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- SpaceBehavior
	Ref, Ref; *Description Here*

- Space_Escort_Unit_Types
	Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Space_Override_Population_Value
	Int; *Description Here*

- Squadron_Capacity
	Int; *Description Here*

- TSW_Attack_Anim_Duration_Seconds
	Float; *Description Here*

- TSW_Attack_Distance_From_Target
	Float; *Description Here*

- TSW_Explosion_Debris_Creation_Frame_Delay
	Ref; *Description Here*

- TSW_MusicEvent_Activation_Start
	Ref; *Description Here*

- TSW_Post_Destruction_Wait_Frames
	Ref; *Description Here*

- TSW_Post_Music_Wait_Frames
	Ref; *Description Here*

- TSW_Power_Up_Countdown_Seconds
	Float; *Description Here*

- TSW_SFXEvent_Activate_Voice
	Ref; *Description Here*

- TSW_SFXEvent_GUI_Bttton_Press
	Ref; *Description Here*

- TSW_SFXEvent_Weapon_Power_Up
	Ref; *Description Here*

- TSW_Start_Distance_From_Target
	Float; *Description Here*

- TSW_Start_Pos_Match_Targets_Z
	Ref; *Description Here*

- TSW_Z_Adjust_Relative_To_Target_Pos
	Float; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Transport_Capacity
	Int; *Description Here*

- Victory_Relevant
	Bool Y/N; *Description Here*

TransportUnits
--------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``TransportUnit``                                                 ``Name``
``UniqueUnit``                                                    ``Name``
================================================================= =================================================================

|

TransportUnit
^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Affiliation
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Asteroid_Damage_Hit_Particles
	Ref; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Behavior
	Ref; *Description Here*

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- Can_Participate_In_Space_Battle
	Ref; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Damage
	Int; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Exclude_From_Distance_Fade
	Bool t/f; *Description Here*

- Exit_Door_Angle_Degrees
	Float; *Description Here*

- Exit_Door_Distance
	Float; *Description Here*

- Fire_Category_Restrictions
	Ref, Ref, Ref, Ref, Ref; *Description Here*

- Fire_Cone_Height
	Float; *Description Here*

- Fire_Cone_Width
	Float; *Description Here*

- Fire_Inaccuracy_Distance
	Ref, Float; *Description Here*

- Formation_Priority
	Int; *Description Here*

- GUI_Bracket_Size
	Int; *Description Here*

- HardPoints
	Ref; *Description Here*

- Has_Space_Evaluator
	Bool T/F; *Description Here*

- Hover_Offset
	Float; *Description Here*

- Hyperspace
	Bool Y/N; *Description Here*

- Hyperspace_Speed
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Is_Escort
	Bool y/n; *Description Here*

- Is_Valid_Target
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref; *Description Here*

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

- Landing_Transport_Variant
	Ref; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- Min_Speed
	Int; *Description Here*

- Mouse_Collide_Override_Sphere_Radius
	Int; *Description Here*

- MovementClass
	Ref; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Obstacle_Height
	Float; *Description Here*

- Obstacle_Width
	Float; *Description Here*

- Obstacle_X_Offset
	Float; *Description Here*

- Obstacle_Y_Offset
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
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

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

- SFXEvent_Ambient_Loop
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Idle_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Ref; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- SpaceBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- TacticalBehavior
	Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- UnitCollisionClass
	Ref; *Description Here*

- Use_Special_Submit_Rules
	Ref; *Description Here*

- Use_Transported_Object_Bounds_For_Landing_Z
	Ref; *Description Here*

- User_Bound_Max
	Int, Int, Int; *Description Here*

- User_Bound_Min
	Ref, Ref, Int; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*


|

UniqueUnit
^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Bank_Turn_Angle
	Int; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations


|


|
|

UniqueUnits
-----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GroundVehicle``                                                 ``Name``
``UniqueUnit``                                                    ``Name``
================================================================= =================================================================

|

GroundVehicle
^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Affiliation
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Attack_Animation_Is_Overlay
	Bool y/n; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Base_Shield_Penetration_Particle
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
	Ref | Ref; *Description Here*

- Collidable_By_Projectile_Dead
	Bool Y/N; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Converted_To_Enemy_Die_Time_Seconds
	Int; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Deploys
	Bool Y/N; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- FormationGrouping
	Ref; *Description Here*

- FormationOrder
	Ref; *Description Here*

- FormationRaggedness
	Float; *Description Here*

- FormationSpacing
	Float; *Description Here*

- GUI_Bounds_Scale
	Float; *Description Here*

- GUI_Bracket_Size
	Int; *Description Here*

- Ground_Vehicle_Turret_Target
	Ref; *Description Here*

- Has_Land_Evaluator
	Bool Y/N; *Description Here*

- Has_Pre_Turn_Anim
	Ref; *Description Here*

- Icon_Name
	File; *Description Here*

- Influences_Capture_Point
	Ref; *Description Here*

- Is_Affected_By_Gravity_Control_Field
	Ref; *Description Here*

- Is_Squashable_By_Supercrusher
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Land_Damage_Alternates
	Int, Int, Int; *Description Here*

- Land_Damage_SFX
	Ref, Ref, Ref, Ref; *Description Here*

- Land_Damage_Thresholds
	Int, Float, Float; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Locomotor_Has_Animation_Priority
	Bool y/n; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- MaxJiggleDistance
	Ref; *Description Here*

- MaxSecondaryTurnROTCoefficient
	Float; *Description Here*

- Max_Rate_Of_Turn
	Int; *Description Here*

- Max_Speed
	Float; *Description Here*

- MinSecondaryTurnROTCoefficient
	Float; *Description Here*

- Min_Speed
	Float; *Description Here*

- Min_Speed_Fraction_For_Turn
	Float; *Description Here*

- MinimumPushReturnDistance
	Ref; *Description Here*

- MovementClass
	Ref; *Description Here*

- MovementPredictionInterval
	Ref; *Description Here*

- Movement_Animation_Speed
	Float; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Occlusion_Silhouette_Enabled
	Int; *Description Here*

- OccupationStyle
	Ref; *Description Here*

- Overall_Length
	Float; *Description Here*

- Overall_Width
	Float; *Description Here*

- OverrideAcceleration
	Float; *Description Here*

- OverrideDeceleration
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
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Rotation_Animation_Speed
	Float; *Description Here*

- SFXEvent_Assist_Attack
	Ref; *Description Here*

- SFXEvent_Assist_Move
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Engine_Idle_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- SecondaryTurnAngle
	Ref; *Description Here*

- SecondaryTurnInPlaceROTCoefficient
	Float; *Description Here*

- SecondaryTurnLookaheadDistance
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Sensor_Range
	Int; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Size_Value
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Stopped_Rate_Of_Turn
	Float; *Description Here*

- SurfaceFX_Name
	Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Targeting_Fire_Inaccuracy
	Ref, Float; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Turret_Elevate_Extent_Degrees
	Float; *Description Here*

- Turret_Rotate_Extent_Degrees
	Float; *Description Here*

- Type
	Ref; *Description Here*

- UnitCollisionClass
	Ref; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- UseSecondaryFacing
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Vehicle_Thief_Inside_Clone
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- Walk_Transition
	Bool Y/N; *Description Here*

- Weather_Category
	Ref; *Description Here*

- Wind_Disturbance_Radius
	Int; *Description Here*

- Wind_Disturbance_Sphere_Alpha
	Float; *Description Here*

- Wind_Disturbance_Strength
	Int; *Description Here*


|

UniqueUnit
^^^^^^^^^^
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

- Asteroid_Damage_Hit_Particles
	Ref; *Description Here*

- Attack_Animation_Is_Overlay
	Bool y/n; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Auto_Deploys
	Bool Y/N; *Description Here*

- Autonomous_Move_Extension_Vs_Attacker
	Float; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Bank_Turn_Angle
	Int; *Description Here*

- Base_Shield_Penetration_Particle
	Ref; *Description Here*

- Begin_Turn_Towards_Distance
	Float; *Description Here*

- Behavior
	Ref, Ref, Ref, Ref; *Description Here*

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Limit_Current_For_All_Allies
	Int; *Description Here*

- Build_Limit_Current_Per_Player
	Int; *Description Here*

- Build_Limit_Lifetime_For_All_Allies
	Ref; *Description Here*

- Build_Limit_Lifetime_Per_Player
	Ref; *Description Here*

- Build_Tab_Space_Units
	Bool Y/N; *Description Here*

- CategoryMask
	Ref | Ref | Ref; *Description Here*

- Collidable_By_Projectile_Dead
	Bool Y/N; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Collision_Box_Modifier
	Float; *Description Here*

- Converted_To_Enemy_Die_Time_Seconds
	Int; *Description Here*

- Create_Team
	Bool Y/N; *Description Here*

- Create_Team_Type
	Ref; *Description Here*

- Custom_Footprint_Radius
	Float; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_XExtent_Offset
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Damage_Type
	Ref; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Clone_Is_Obstacle
	Bool y/n; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_Explosions_End
	Ref; *Description Here*

- Death_Persistence_Duration
	Ref; *Description Here*

- Death_SFXEvent_End_Die
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Defend_Mode_Energy_Regen_Multiplier
	Float; *Description Here*

- Defend_Mode_Shield_Regen_Multiplier
	Float; *Description Here*

- Defend_Mode_Speed_Multiplier
	Float; *Description Here*

- Defend_Mode_Weapon_Delay_Multiplier
	Float; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Deploys
	Bool Y/N; *Description Here*

- Display_Contained_Hero_Grab_Bars
	Bool T/F; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Exclude_From_Distance_Fade
	Bool t/f; *Description Here*

- Fire_Category_Restrictions
	Ref, Ref, Ref, Ref, Ref; *Description Here*

- Fire_Inaccuracy_Distance
	Ref, Float; *Description Here*

- Fires_Forward
	Bool y/n; *Description Here*

- FormationGrouping
	Ref; *Description Here*

- FormationOrder
	Int; *Description Here*

- FormationPriority
	Int; *Description Here*

- Formation_Priority
	Int; *Description Here*

- GUI_Bracket_Height
	Int; *Description Here*

- GUI_Bracket_Size
	Int; *Description Here*

- GUI_Bracket_Width
	Int; *Description Here*

- GUI_Distance
	Int; *Description Here*

- GUI_Offset
	Ref; *Description Here*

- GUI_Row
	Ref; *Description Here*

- GUI_Velocity
	Int; *Description Here*

- Glory_Cinematics
	Ref; *Description Here*

- Guard_Chase_Range
	Float; *Description Here*

- HardPoints
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Has_Land_Evaluator
	Bool T/F; *Description Here*

- Has_Pre_Turn_Anim
	Ref; *Description Here*

- Has_Space_Evaluator
	Bool T/F; *Description Here*

- Hero_Ability
	None; *Description Here*

- Hover_Offset
	Float; *Description Here*

- Hyperspace
	Bool Y/N; *Description Here*

- Hyperspace_Speed
	Int; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Influences_Capture_Point
	Ref; *Description Here*

- IsDeathClone
	Ref; *Description Here*

- Is_Bomber
	Bool y/n; *Description Here*

- Is_Escort
	Bool y/n; *Description Here*

- Is_Named_Hero
	Bool Y/N; *Description Here*

- Is_Super_Weapon_Killer
	Bool Y/N; *Description Here*

- Is_Supercrusher
	Bool Y/N; *Description Here*

- Is_Valid_Target
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Landing_Transport_Variant
	Ref; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Locomotor_Has_Animation_Priority
	Bool y/n; *Description Here*

- Lua_Script
	Ref; *Description Here*

- Maintenance_Cost
	Float; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Lift
	Float; *Description Here*

- Max_Rate_Of_Roll
	Float; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Max_Thrust
	Float; *Description Here*

- Min_Speed
	Float; *Description Here*

- Min_Speed_Fraction_For_Turn
	Float; *Description Here*

- MinimumPushReturnDistance
	Ref; *Description Here*

- Minimum_Follow_Distance
	Float; *Description Here*

- MovementBoxExpansionFactor
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- MovementPredictionInterval
	Float; *Description Here*

- Movement_Animation_Speed
	Float; *Description Here*

- Multisample_FOW_Check
	Bool Y/N; *Description Here*

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Number_per_Squadron
	Int; *Description Here*

- Obstacle_Height
	Float; *Description Here*

- Obstacle_Width
	Float; *Description Here*

- Obstacle_X_Offset
	Float; *Description Here*

- Obstacle_Y_Offset
	Float; *Description Here*

- OccupationStyle
	Ref; *Description Here*

- Out_Of_Combat_Defense_Adjustment
	Float; *Description Here*

- Overall_Length
	Float; *Description Here*

- Overall_Width
	Float; *Description Here*

- OverrideAcceleration
	Float; *Description Here*

- OverrideDeceleration
	Float; *Description Here*

- Political_Control
	Int; *Description Here*

- Political_Faction
	Ref; *Description Here*

- Population_Value
	Int; *Description Here*

- Prevents_Story_Campaign_Autoresolve
	Bool y/n; *Description Here*

- Projectile_Appearance_Delay_Frames
	Int, Int; *Description Here*

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
	Ref; *Description Here*

- Radar_Icon_Name
	File; *Description Here*

- Radar_Icon_Scale_Land
	Float; *Description Here*

- Radar_Icon_Scale_Space
	Float; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Ranking_In_Category
	Int; *Description Here*

- Redirect_Damage_To_Teammates
	Bool Y/N; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Star_Base_Level
	Int; *Description Here*

- Respawn_Whole_Team_When_Killed
	Bool Y/N; *Description Here*

- Rotation_Animation_Speed
	Float; *Description Here*

- SFXEvent_Ambient_Loop
	Ref; *Description Here*

- SFXEvent_Ambient_Moving
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Max_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Ambient_Moving_Min_Delay_Seconds
	Ref; *Description Here*

- SFXEvent_Assist_Attack
	Ref; *Description Here*

- SFXEvent_Assist_Move
	Ref; *Description Here*

- SFXEvent_Attack
	Ref; *Description Here*

- SFXEvent_Attack_Hardpoint
	Ref, Ref; *Description Here*

- SFXEvent_Barrage
	Ref; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Deploy
	Ref; *Description Here*

- SFXEvent_Enemy_Damaged_Health_Critical_Warning
	Ref; *Description Here*

- SFXEvent_Enemy_Damaged_Health_Low_Warning
	Ref; *Description Here*

- SFXEvent_Enemy_Health_Critical_Warning
	Ref; *Description Here*

- SFXEvent_Enemy_Health_Low_Warning
	Ref; *Description Here*

- SFXEvent_Engine_Cinematic_Focus_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Idle_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Guard
	Ref; *Description Here*

- SFXEvent_Hardpoint_Destroyed
	Ref, Ref; *Description Here*

- SFXEvent_Health_Critical_Warning
	Ref; *Description Here*

- SFXEvent_Health_Low_Warning
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- SFXEvent_Move_Into_Asteroid_Field
	Ref; *Description Here*

- SFXEvent_Move_Into_Nebula
	Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Stop
	Ref; *Description Here*

- SFXEvent_Unit_Lost
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Ref; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- SpaceBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Full_Stop_Command
	Ref; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Specific_Death_Anim_Index
	Ref; *Description Here*

- Specific_Death_Anim_Type
	None; *Description Here*

- Spin_Away_On_Death
	Bool Y/N; *Description Here*

- Spin_Away_On_Death_Chance
	Float; *Description Here*

- Spin_Away_On_Death_Explosion
	Ref; *Description Here*

- Spin_Away_On_Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Spin_Away_On_Death_Time
	Floatf; *Description Here*

- Squadron_Capacity
	Int; *Description Here*

- Stopped_Rate_Of_Turn
	Int; *Description Here*

- Surface_Bombardment_Capable
	Bool y/n; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Target_Bones
	Ref, Ref, Ref; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

- Targeting_Stickiness_Time_Threshold
	Float; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Transport_Capacity
	Int; *Description Here*

- Turret_Bone_Name
	Ref; *Description Here*

- Turret_Elevate_Extent_Degrees
	Int; *Description Here*

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

- Type
	Ref; *Description Here*

- UnitCollisionClass
	Ref; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- User_Bound_Max
	Int, Int, Int; *Description Here*

- User_Bound_Min
	Ref, Ref, Int; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Vehicle_Thief_Inside_Clone
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- Visible_On_Radar_When_Fogged
	Bool t/f; *Description Here*

- Walk_Transition
	Bool Y/N; *Description Here*

- Weather_Category
	Ref; *Description Here*

- xxxSpace_Model_Name
	File; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
