##########################################
GroundVehicle
##########################################


About
*****
Not yet documented, but you help document it through GitHub!


Structure
*********
``GroundVehicle``
-----------------
Not yet documented, but you help document it through GitHub!

.. csv-table::
	:header: "Nested Nodes", "Description"

	"``Abilities``", "Nested Node for units, contains either an activated ability or some form of special behavior for a unit. See `Unit Abilities on Petrolution <modtools.petrolution.net/docs/Unit_Abilities_EaW>`_ for a list of EaW active abilities. FoC is currently not included, but a page may be added to this documentation"
	"``Unit_Abilities_Data``", "Not yet documented, but you help document it through GitHub!"


``Abilities``
^^^^^^^^^^^^^
Nested Node for units, contains either an activated ability or some form of special behavior for a unit. See `Unit Abilities on Petrolution <modtools.petrolution.net/docs/Unit_Abilities_EaW>`_ for a list of EaW active abilities. FoC is currently not included, but a page may be added to this documentation

.. csv-table::
	:header: "Nested Nodes", "Description"

	"``Redirect_Blaster_Ability``", "Not yet documented, but you help document it through GitHub!"


``Redirect_Blaster_Ability``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Not yet documented, but you help document it through GitHub!

``Redirect_Blaster_Ability``'s SubNodes
"""""""""""""""""""""""""""""""""""""""
- Activation_Style
	Ref; Not yet documented, but you help document it through GitHub!


- Applicable_Unit_Categories
	Ref | Ref | ...; Not yet documented, but you help document it through GitHub!


- Applicable_Unit_Types
	Ref; Not yet documented, but you help document it through GitHub!


- Block_Chance
	Float; Not yet documented, but you help document it through GitHub!


- Initially_Enabled
	Bool; Not yet documented, but you help document it through GitHub!


- Max_Projectile_Redirection_Angle_In_Degrees
	Float; Not yet documented, but you help document it through GitHub!


- Reaction_Arc_In_Degrees
	Float; Not yet documented, but you help document it through GitHub!


- Redirect_Chance
	Float; Not yet documented, but you help document it through GitHub!


- SFXEvent_Activate
	Ref; Not yet documented, but you help document it through GitHub!


- Turn_To_Face_Unblockable_Shots
	Bool; Not yet documented, but you help document it through GitHub!





``Unit_Abilities_Data``
^^^^^^^^^^^^^^^^^^^^^^^
Not yet documented, but you help document it through GitHub!

.. csv-table::
	:header: "Nested Nodes", "Description"

	"``Unit_Ability``", "Not yet documented, but you help document it through GitHub!"


``Unit_Ability``
^^^^^^^^^^^^^^^^
Not yet documented, but you help document it through GitHub!

``Unit_Ability``'s SubNodes
"""""""""""""""""""""""""""
- Max_Num_Spawned_Objects
	Int; Not yet documented, but you help document it through GitHub!


- Owner_Attachment_Bone
	Ref, Ref, Ref; Not yet documented, but you help document it through GitHub!


- Recharge_Seconds
	Int; Not yet documented, but you help document it through GitHub!


- SFXEvent_GUI_Unit_Ability_Activated
	Ref; Not yet documented, but you help document it through GitHub!


- Spawned_Object_Type
	Ref; Not yet documented, but you help document it through GitHub!


- Type
	Ref; Not yet documented, but you help document it through GitHub!





SubNodes
^^^^^^^^
- Affiliation
	Ref; Not yet documented, but you help document it through GitHub!


- AI_Combat_Power
	Int; Not yet documented, but you help document it through GitHub!


- Air_Vehicle_Turret_Target
	Bool; Not yet documented, but you help document it through GitHub!


- Apply_Y_Turret_Rotate_To_Axis
	Int; Not yet documented, but you help document it through GitHub!


- Apply_Z_Turret_Rotate_To_Axis
	Int; Not yet documented, but you help document it through GitHub!


- Armor_Type
	Ref; Not yet documented, but you help document it through GitHub!


- Attack_Animation_Is_Overlay
	Bool; Not yet documented, but you help document it through GitHub!


- Attack_Move_Response_Range
	Float; Not yet documented, but you help document it through GitHub!


- Auto_Deploys
	Bool; Not yet documented, but you help document it through GitHub!


- Autonomous_Move_Extension_Vs_Attacker
	Float; Not yet documented, but you help document it through GitHub!


- Autoresolve_Health
	Int; Not yet documented, but you help document it through GitHub!


- Base_Shield_Penetration_Particle
	Ref; Not yet documented, but you help document it through GitHub!


- Behavior
	Ref; Not yet documented, but you help document it through GitHub!


- Blob_Shadow_Below_Detail_Level
	Int; Not yet documented, but you help document it through GitHub!


- Blob_Shadow_Material_Name
	Ref; Not yet documented, but you help document it through GitHub!


- Blob_Shadow_Scale
	Float, Float; Not yet documented, but you help document it through GitHub!


- Cache_Crusher_Boxes
	Bool; Not yet documented, but you help document it through GitHub!


- CategoryMask
	Ref | Ref | ...; Not yet documented, but you help document it through GitHub!


- Collidable_By_Projectile_Dead
	Bool; Not yet documented, but you help document it through GitHub!


- Collidable_By_Projectile_Living
	Bool; Not yet documented, but you help document it through GitHub!


- Converted_To_Enemy_Die_Time_Seconds
	Int; Not yet documented, but you help document it through GitHub!


- Custom_Hard_XExtent
	Float; Not yet documented, but you help document it through GitHub!


- Custom_Hard_YExtent
	Float; Not yet documented, but you help document it through GitHub!


- Damage
	Int; Not yet documented, but you help document it through GitHub!


- Death_Clone
	Ref, Ref; Not yet documented, but you help document it through GitHub!


- Death_SFXEvent_Start_Die
	Ref; Not yet documented, but you help document it through GitHub!


- Deploys
	Bool; Not yet documented, but you help document it through GitHub!


- Encyclopedia_Good_Against
	Ref Ref Ref; Not yet documented, but you help document it through GitHub!


- Encyclopedia_Text
	Ref; Not yet documented, but you help document it through GitHub!


- Encyclopedia_Unit_Class
	Ref; Not yet documented, but you help document it through GitHub!


- Encyclopedia_Vulnerable_To
	Ref Ref; Not yet documented, but you help document it through GitHub!


- Energy_Capacity
	Int; Not yet documented, but you help document it through GitHub!


- Energy_Refresh_Rate
	Int; Not yet documented, but you help document it through GitHub!


- FormationGrouping
	Ref; Not yet documented, but you help document it through GitHub!


- Ground_Vehicle_Turret_Target
	Bool; Not yet documented, but you help document it through GitHub!


- Guard_Chase_Range
	Float; Not yet documented, but you help document it through GitHub!


- GUI_Bounds_Scale
	Float; Not yet documented, but you help document it through GitHub!


- GUI_Bracket_Size
	Int; Not yet documented, but you help document it through GitHub!


- Has_Land_Evaluator
	Bool; Not yet documented, but you help document it through GitHub!


- Has_Pre_Turn_Anim
	Bool; Not yet documented, but you help document it through GitHub!


- Icon_Name
	File; The name of the icon displayed during gameplay, may reference a file stored in an :ref:`MTD File <basegame-filetype-mtd>`.


- Idle_Chase_Range
	Float; Not yet documented, but you help document it through GitHub!


- Influences_Capture_Point
	Bool; Not yet documented, but you help document it through GitHub!


- Is_Supercrusher
	Bool; Not yet documented, but you help document it through GitHub!


- Is_Visible_On_Radar
	Bool; Not yet documented, but you help document it through GitHub!


- Land_Damage_Alternates
	Int, Int, Int; Not yet documented, but you help document it through GitHub!


- Land_Damage_SFX
	Ref, Ref, Ref; Not yet documented, but you help document it through GitHub!


- Land_Damage_Thresholds
	Float, Float, Float; Not yet documented, but you help document it through GitHub!


- Land_FOW_Reveal_Range
	Float; Not yet documented, but you help document it through GitHub!


- Land_Model_Name
	File; Not yet documented, but you help document it through GitHub!


- LandBehavior
	Ref, Ref, ...; Not yet documented, but you help document it through GitHub!


- Locomotor_Has_Animation_Priority
	Bool; Not yet documented, but you help document it through GitHub!


- Mass
	Float; Not yet documented, but you help document it through GitHub!


- Max_Rate_Of_Turn
	Int; Not yet documented, but you help document it through GitHub!


- Max_Speed
	Float; Not yet documented, but you help document it through GitHub!


- Min_Speed_Fraction_For_Turn
	Float; Not yet documented, but you help document it through GitHub!


- MinimumPushReturnDistance
	Int; Not yet documented, but you help document it through GitHub!


- Movement_Animation_Speed
	Float; Not yet documented, but you help document it through GitHub!


- MovementBoxExpansionFactor
	Float; Not yet documented, but you help document it through GitHub!


- MovementClass
	Ref; Not yet documented, but you help document it through GitHub!


- MovementPredictionInterval
	Float; Not yet documented, but you help document it through GitHub!


- No_Reflection_Below_Detail_Level
	Int; Not yet documented, but you help document it through GitHub!


- No_Refraction_Below_Detail_Level
	Int; Not yet documented, but you help document it through GitHub!


- OccupationStyle
	Ref; Not yet documented, but you help document it through GitHub!


- Overall_Length
	Float; Not yet documented, but you help document it through GitHub!


- Overall_Width
	Float; Not yet documented, but you help document it through GitHub!


- Political_Control
	Int; Not yet documented, but you help document it through GitHub!


- Projectile_Appearance_Delay_Frames
	Int, Int; Not yet documented, but you help document it through GitHub!


- Projectile_Fire_Pulse_Count
	Int; Not yet documented, but you help document it through GitHub!


- Projectile_Fire_Pulse_Delay_Seconds
	Float; Not yet documented, but you help document it through GitHub!


- Projectile_Fire_Recharge_Seconds
	Float; Not yet documented, but you help document it through GitHub!


- Projectile_Types
	Ref; Not yet documented, but you help document it through GitHub!


- Property_Flags
	Ref; Not yet documented, but you help document it through GitHub!


- Ranged_Target_Z_Adjust
	Float; Not yet documented, but you help document it through GitHub!


- Ranking_In_Category
	Int; Not yet documented, but you help document it through GitHub!


- Rotation_Animation_Speed
	Float; Not yet documented, but you help document it through GitHub!


- Scale_Factor
	Float; Not yet documented, but you help document it through GitHub!


- Score_Cost_Credits
	Int; Not yet documented, but you help document it through GitHub!


- Select_Box_Scale
	Int; Not yet documented, but you help document it through GitHub!


- Select_Box_Z_Adjust
	Floatf; Not yet documented, but you help document it through GitHub!


- SFXEvent_Assist_Attack
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Assist_Move
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Attack
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Fire
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Fleet_Move
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Guard
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Move
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Select
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Tactical_Build_Cancelled
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Tactical_Build_Complete
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Tactical_Build_Started
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Unit_Lost
	Ref; Not yet documented, but you help document it through GitHub!


- Size_Value
	Int; Not yet documented, but you help document it through GitHub!


- Space_Layer
	Ref; Not yet documented, but you help document it through GitHub!


- Stopped_Rate_Of_Turn
	Int; Not yet documented, but you help document it through GitHub!


- Tactical_Health
	Int; Not yet documented, but you help document it through GitHub!


- Target_Bones
	Ref, Ref, Ref; Not yet documented, but you help document it through GitHub!


- Targeting_Fire_Inaccuracy
	Ref, Float; Not yet documented, but you help document it through GitHub!


- Targeting_Max_Attack_Distance
	Float; Not yet documented, but you help document it through GitHub!


- Targeting_Min_Attack_Distance
	Float; Not yet documented, but you help document it through GitHub!


- Targeting_Priority_Set
	Ref; Not yet documented, but you help document it through GitHub!


- Targeting_Stickiness_Time_Threshold
	Float; Not yet documented, but you help document it through GitHub!


- Text_ID
	Ref; The ID of the text to insert for the name of this object in-game. Text is stored in a `DAT File <basegame-filetype-dat>`.


- Turret_Bone_Name
	Ref; Not yet documented, but you help document it through GitHub!


- Turret_Elevate_Extent_Degrees
	Int; Not yet documented, but you help document it through GitHub!


- Turret_Rotate_Extent_Degrees
	Int; Not yet documented, but you help document it through GitHub!


- Turret_Rotate_Speed
	Float; Not yet documented, but you help document it through GitHub!


- Turret_Targets_Air_Vehicles
	Int; Not yet documented, but you help document it through GitHub!


- Turret_Targets_Anything_Else
	Int; Not yet documented, but you help document it through GitHub!


- Turret_Targets_Ground_Infantry
	Int; Not yet documented, but you help document it through GitHub!


- Turret_Targets_Ground_Vehicles
	Int; Not yet documented, but you help document it through GitHub!


- Type
	Ref; Not yet documented, but you help document it through GitHub!


- UnitCollisionClass
	Ref Ref; Not yet documented, but you help document it through GitHub!


- Vehicle_Thief_Inside_Clone
	Ref; Not yet documented, but you help document it through GitHub!


- Victory_Relevant
	Bool; Not yet documented, but you help document it through GitHub!


- Walk_Transition
	Bool; Not yet documented, but you help document it through GitHub!


- Weather_Category
	Ref; Not yet documented, but you help document it through GitHub!







EaW-Godot Port Connection
*************************
Not yet documented, but you help document it through GitHub!

