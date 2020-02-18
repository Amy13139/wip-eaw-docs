.. _xml_type_template:
.. Template to use for XML type documentation

*************
Space Objects
*************


About
=====
*Description*: This Type/Subtype does something!


Structure
=========
SpaceBuildables
---------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpaceBuildable``                                                ``Name``
================================================================= =================================================================

|

SpaceBuildable
^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

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

- Base_Level_Available
	Ref; *Description Here*

- Behavior
	Ref, Ref, Ref, Ref, Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Capture_Point_Radius
	Float; *Description Here*

- Capture_Point_Transition_Time_Seconds
	Int; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Custom_Soft_Footprint_Radius
	Ref; *Description Here*

- Damage
	Int; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Destroy_When_Child_Dies
	Bool T/F; *Description Here*

- Encyclopedia_Text
	Ref, Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Energy_Capacity
	Int; *Description Here*

- Energy_Refresh_Rate
	Int; *Description Here*

- Fire_Inaccuracy_Distance
	Ref, Float; *Description Here*

- GUI_Bounds_Scale
	Float; *Description Here*

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

- Has_Space_Evaluator
	Bool T/F; *Description Here*

- Hides_When_Built_On
	Bool T/F; *Description Here*

- Icon_Name
	File; *Description Here*

- Influences_Capture_Point
	Ref; *Description Here*

- Initial_State_Visible_Under_FOW
	Bool T/F; *Description Here*

- Is_Community_Property
	Bool Y/N; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- Land_Damage_Alternates
	Int, Int, Int; *Description Here*

- Land_Damage_SFX
	Ref, Ref, Ref; *Description Here*

- Land_Damage_Thresholds
	Int, Float, Float; *Description Here*

- Last_State_Visible_Under_FOW
	Ref; *Description Here*

- Loop_Idle_Anim_00
	Ref; *Description Here*

- MP_Encyclopedia_Text
	Ref, Ref; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Ownership_Sticks
	Bool Y/N; *Description Here*

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

- Radar_Icon_Name
	File; *Description Here*

- Radar_Icon_Size
	Ref; *Description Here*

- Radar_Show_Facing
	Bool Y/N; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Required_Ground_Base_Level
	Ref; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Fire
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
	Ref; *Description Here*

- Shield_Points
	Int; *Description Here*

- Shield_Refresh_Rate
	Int; *Description Here*

- Size_Value
	Int; *Description Here*

- SpaceBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_FOW_Reveal_Range
	Int; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Space_Obstacle_Offset
	Ref; *Description Here*

- Tactical_Build_Cost_Campaign
	Int; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Ref; *Description Here*

- Tactical_Build_Start_Lower_Z
	Float; *Description Here*

- Tactical_Build_Time_Seconds
	Ref; *Description Here*

- Tactical_Buildable_Constructed
	Ref; *Description Here*

- Tactical_Buildable_Objects_Campaign
	Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Tactical_Buildable_Objects_Multiplayer
	Ref, Ref, Ref, Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Tactical_Respawn_Time_In_Secs
	Int; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Targeting_Priority_Set
	Ref; *Description Here*

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

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- Visible_To_Enemies_When_Empty
	Bool T/F; *Description Here*


|


|
|

SpacePrimarySkydomes
--------------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpacePrimarySkydome``                                           ``Name``
================================================================= =================================================================

|

SpacePrimarySkydome
^^^^^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Behavior
	Ref; *Description Here*

- Exclude_From_Distance_Fade
	Bool t/f; *Description Here*

- Galactic_Model_Name
	None; *Description Here*

- In_Background
	Bool Y/N; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Is_Discardable
	Bool Y/N; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Sort_Order_Adjust
	None; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Text_ID
	None; The in-game name of this unit, references a .DAT file to allow from translations


|


|
|

SpaceProps
----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpaceProp``                                                     ``Name``
================================================================= =================================================================

|

SpaceProp
^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref, Ref; *Description Here*

- Behavior
	Ref, Ref; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Dead
	Bool Y/N; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Death_By_TSW_Replacements
	Ref, Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Debris_Attached_Particle
	Ref; *Description Here*

- Debris_Facing_Rotate_Vector
	Float, Float, Float; *Description Here*

- Debris_Max_Lifetime_Seconds
	Float; *Description Here*

- Debris_Min_Lifetime_Seconds
	Float; *Description Here*

- Debris_Movement_Vector
	Float, Float, Float; *Description Here*

- Exclude_From_Distance_Fade
	Bool t/f; *Description Here*

- Idle_Anim_00_Rate_Mod
	Float; *Description Here*

- In_Background
	Bool Y/N; *Description Here*

- Initial_State_Visible_Under_FOW
	Bool T/F; *Description Here*

- Is_Asteroid_Field
	Ref; *Description Here*

- Is_Decoration
	Ref; *Description Here*

- Is_Discardable
	Ref; *Description Here*

- Is_Impassable_Asteroid
	Ref; *Description Here*

- Is_Ion_Storm
	Bool Y/N; *Description Here*

- Is_Nebula
	Ref; *Description Here*

- Is_Valid_Target
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Ref; *Description Here*

- Layer_Z_Adjust
	Int; *Description Here*

- Loop_Idle_Anim_00
	Ref; *Description Here*

- Radar_Icon_Name
	Ref; *Description Here*

- Radar_Icon_Size
	Ref; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Scale
	Float; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Sort_Order_Adjust
	Ref; *Description Here*

- SpaceBehavior
	Ref; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Space_Obstacle_Offset
	Ref; *Description Here*

- Space_Obstacle_Radius
	Ref; *Description Here*

- Tactical_Health
	Ref; *Description Here*

- Text_ID
	None; The in-game name of this unit, references a .DAT file to allow from translations

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Visible_On_Radar_When_Fogged
	Bool T/F; *Description Here*


|


|
|

SpaceSecondarySkydomes
----------------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpaceSecondarySkydome``                                         ``Name``
================================================================= =================================================================

|

SpaceSecondarySkydome
^^^^^^^^^^^^^^^^^^^^^
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

- Is_Discardable
	Bool Y/N; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Sort_Order_Adjust
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Text_ID
	None; The in-game name of this unit, references a .DAT file to allow from translations

StarBases
---------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``StarBase``                                                      ``Name``
``Starbase``                                                      ``Name``
================================================================= =================================================================

|

StarBase
^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Abilities
	Ref; *Description Here*

- Additional_Population_Capacity
	Int; *Description Here*

- Affiliation
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Available_In_Skirmish
	Bool Y/N; *Description Here*

- Base_Level
	Int; *Description Here*

- Behavior
	Ref, Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Tab_Space_Station
	Bool Y/N; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Custom_Soft_Footprint_Radius
	Ref; *Description Here*

- Damage
	Int; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_Persistence_Duration
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

- GUI_Angles
	Ref; *Description Here*

- GUI_Bounds_Scale
	Float; *Description Here*

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

- GUI_X_Rot
	Int; *Description Here*

- Galactic_Model_Name
	File; *Description Here*

- HardPoints
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Has_Space_Evaluator
	Bool T/F; *Description Here*

- Icon_Name
	File; *Description Here*

- Initial_State_Visible_Under_FOW
	Bool T/F; *Description Here*

- Is_Community_Property
	Bool Y/N; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- Last_State_Visible_Under_FOW
	Ref; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Multisample_FOW_Check
	Bool Y/N; *Description Here*

- Next_Level_Base
	None; *Description Here*

- Prev_Level_Base
	Ref; *Description Here*

- Radar_Icon_Name
	File; *Description Here*

- Radar_Icon_Scale_Land
	Float; *Description Here*

- Radar_Icon_Scale_Space
	Float; *Description Here*

- Radar_Icon_Size
	Ref; *Description Here*

- Radar_Rotate_Icon
	Bool Y/N; *Description Here*

- Reinforcement_Prevention_Radius
	Ref; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Star_Base_Level
	Int; *Description Here*

- Reserve_Spawned_Units_Tech_0
	Ref, Ref; *Description Here*

- Retreat_Self_Destruct_Explosion
	Ref; *Description Here*

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

- SFXEvent_Fire
	Ref; *Description Here*

- SFXEvent_Hardpoint_All_Weapons_Destroyed
	Ref; *Description Here*

- SFXEvent_Hardpoint_Destroyed
	Ref, Ref; *Description Here*

- SFXEvent_Select
	Ref; *Description Here*

- SFXEvent_Unit_Under_Attack
	Ref; *Description Here*

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

- Should_Death_Clone_Play_Idle
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- Slice_Cost_Credits
	Int; *Description Here*

- SpaceBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Space_Obstacle_Offset
	Ref; *Description Here*

- Spawned_Squadron_Delay_Seconds
	Int; *Description Here*

- Starting_Spawned_Units_Tech_0
	Ref, Int; *Description Here*

- Tactical_Buildable_Objects_Campaign
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Tactical_Buildable_Objects_Multiplayer
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- Visible_On_Radar_When_Fogged
	Bool T/F; *Description Here*

- Visible_To_Enemies_When_Empty
	Bool T/F; *Description Here*


|

Starbase
^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Behavior
	Ref, Ref, Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
