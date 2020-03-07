##########################################
HeroUnit
##########################################


About
*****
Not yet documented, but you help document it through GitHub!


Structure
*********
``HeroUnit``
------------
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

	"``Galactic_Stealth_Ability``", "Nested Node for Abilities in GC; allows a unit to move into enemy-occupied space without starting combat, also dictates how much information the unit reveals with it's presence."
	"``Neutralize_Hero_Ability``", "Not yet documented, but you help document it through GitHub!"
	"``Personal_Flame_Thrower_Ability``", "Not yet documented, but you help document it through GitHub!"
	"``System_Spy_Ability``", "Not yet documented, but you help document it through GitHub!"


``Galactic_Stealth_Ability``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Nested Node for Abilities in GC; allows a unit to move into enemy-occupied space without starting combat, also dictates how much information the unit reveals with it's presence.

``Galactic_Stealth_Ability``'s SubNodes
"""""""""""""""""""""""""""""""""""""""
- Evade_Detection_Chance
	Float; Not yet documented, but you help document it through GitHub!




``Neutralize_Hero_Ability``
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Not yet documented, but you help document it through GitHub!

``Neutralize_Hero_Ability``'s SubNodes
""""""""""""""""""""""""""""""""""""""
- Can_Neutralize_Major_Heroes
	Bool; Not yet documented, but you help document it through GitHub!


- Can_Neutralize_Minor_Heroes
	Bool; Not yet documented, but you help document it through GitHub!


- Cost_Mod_By_Base_Level
	Float, Float, Float, Float; Not yet documented, but you help document it through GitHub!


- Cost_Mod_By_Previous_Neutralizations
	Float, Float, Float, Float; Not yet documented, but you help document it through GitHub!


- General_Major_Hero_Cost_Mod
	Float; Not yet documented, but you help document it through GitHub!


- General_Minor_Hero_Cost_Mod
	Float; Not yet documented, but you help document it through GitHub!


- Owner_Respawn_Time_In_Secs
	Float, Float; Not yet documented, but you help document it through GitHub!


- Target_Respawn_Time_In_Secs
	Float, Float; Not yet documented, but you help document it through GitHub!




``Personal_Flame_Thrower_Ability``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Not yet documented, but you help document it through GitHub!

``Personal_Flame_Thrower_Ability``'s SubNodes
"""""""""""""""""""""""""""""""""""""""""""""
- Activation_Max_Range
	Float; Not yet documented, but you help document it through GitHub!


- Activation_Min_Range
	Float; Not yet documented, but you help document it through GitHub!


- Activation_Style
	Ref; Not yet documented, but you help document it through GitHub!


- Applicable_Unit_Categories
	Ref; Not yet documented, but you help document it through GitHub!


- Applicable_Unit_Types
	Ref; Not yet documented, but you help document it through GitHub!


- Damage_Amount
	Float; The quantity of damage to deal. Does not include multipliers and resistances.


- Damage_Arc_In_Degrees
	Float; Not yet documented, but you help document it through GitHub!


- Damage_Delay_In_Secs
	Float; Not yet documented, but you help document it through GitHub!


- Fire_Time_In_Secs
	Float; Not yet documented, but you help document it through GitHub!


- Flame_Emitter_Model_Name
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Activate
	Ref; Not yet documented, but you help document it through GitHub!




``System_Spy_Ability``
^^^^^^^^^^^^^^^^^^^^^^
Not yet documented, but you help document it through GitHub!

``System_Spy_Ability``'s SubNodes
"""""""""""""""""""""""""""""""""
- Activation_Style
	Ref; Not yet documented, but you help document it through GitHub!


- Causes_Despawn
	Bool; Not yet documented, but you help document it through GitHub!


- Duration_In_Secs
	Float; Not yet documented, but you help document it through GitHub!


- Initially_Enabled
	Bool; Not yet documented, but you help document it through GitHub!


- See_Major_Stealth_Heroes
	Bool; Not yet documented, but you help document it through GitHub!


- See_Minor_Stealth_Heroes
	Bool; Not yet documented, but you help document it through GitHub!


- See_Num_Fleets
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
- GUI_Activated_Ability_Name
	Ref; Not yet documented, but you help document it through GitHub!


- Recharge_Seconds
	Float; Not yet documented, but you help document it through GitHub!


- Type
	Ref; Not yet documented, but you help document it through GitHub!





SubNodes
^^^^^^^^
- Affiliation
	Ref; Not yet documented, but you help document it through GitHub!


- AI_Combat_Power
	Int; Not yet documented, but you help document it through GitHub!


- Alternate_Max_Rate_Of_Turn
	Float; Not yet documented, but you help document it through GitHub!


- Alternate_Max_Speed
	Float; Not yet documented, but you help document it through GitHub!


- Always_Spawn_In_Orbit
	Bool; Not yet documented, but you help document it through GitHub!


- Armor_Type
	Ref; Not yet documented, but you help document it through GitHub!


- Attach_To_Flagship_During_Space_Battle
	Bool; Not yet documented, but you help document it through GitHub!


- Attack_Move_Response_Range
	Float; Not yet documented, but you help document it through GitHub!


- Autonomous_Move_Extension_Vs_Attacker
	Float; Not yet documented, but you help document it through GitHub!


- Autoresolve_Health
	Int; Not yet documented, but you help document it through GitHub!


- Blob_Shadow_Below_Detail_Level
	Int; Not yet documented, but you help document it through GitHub!


- Blob_Shadow_Bone_Name
	Ref; Not yet documented, but you help document it through GitHub!


- Blob_Shadow_Material_Name
	Ref; Not yet documented, but you help document it through GitHub!


- Blob_Shadow_Scale
	Float, Float; Not yet documented, but you help document it through GitHub!


- Can_Be_Neutralized_By_Major_Heroes
	Bool; Not yet documented, but you help document it through GitHub!


- Can_Be_Neutralized_By_Minor_Heroes
	Bool; Not yet documented, but you help document it through GitHub!


- CanCellStack
	Bool; Not yet documented, but you help document it through GitHub!


- CategoryMask
	Ref | Ref; Not yet documented, but you help document it through GitHub!


- Collidable_By_Projectile_Living
	Bool; Not yet documented, but you help document it through GitHub!


- Custom_Hard_XExtent
	Float; Not yet documented, but you help document it through GitHub!


- Custom_Hard_YExtent
	Float; Not yet documented, but you help document it through GitHub!


- Custom_Soft_Footprint_Radius
	Float; Not yet documented, but you help document it through GitHub!


- Damage
	Int; Not yet documented, but you help document it through GitHub!


- Death_Fade_Time
	Float; Not yet documented, but you help document it through GitHub!


- Death_Persistence_Duration
	Float; Not yet documented, but you help document it through GitHub!


- Dense_FOW_Reveal_Range_Multiplier
	Float; Not yet documented, but you help document it through GitHub!


- Deploys
	Bool; Not yet documented, but you help document it through GitHub!


- Encyclopedia_Text
	Ref Ref; Not yet documented, but you help document it through GitHub!


- Encyclopedia_Unit_Class
	Ref; Not yet documented, but you help document it through GitHub!


- FormationSpacing
	Float; Not yet documented, but you help document it through GitHub!


- GalacticBehavior
	Ref; Not yet documented, but you help document it through GitHub!


- Ground_Infantry_Turret_Target
	Bool; Not yet documented, but you help document it through GitHub!


- Guard_Chase_Range
	Float; Not yet documented, but you help document it through GitHub!


- GUI_Bracket_Height
	Int; Not yet documented, but you help document it through GitHub!


- GUI_Bracket_Size
	Int; Not yet documented, but you help document it through GitHub!


- GUI_Bracket_Width
	Int; Not yet documented, but you help document it through GitHub!


- Has_Land_Evaluator
	Bool; Not yet documented, but you help document it through GitHub!


- Highlight_Blob_Material_Name
	Ref; Not yet documented, but you help document it through GitHub!


- Hover_Offset
	Float; Not yet documented, but you help document it through GitHub!


- Icon_Name
	File; The name of the icon displayed during gameplay, may reference a file stored in an :ref:`MTD File <basegame-filetype-mtd>`.


- Idle_Chase_Range
	Float; Not yet documented, but you help document it through GitHub!


- Is_Named_Hero
	Bool; Not yet documented, but you help document it through GitHub!


- Is_Visible_On_Radar
	Bool; Not yet documented, but you help document it through GitHub!


- Land_FOW_Reveal_Range
	Float; Not yet documented, but you help document it through GitHub!


- Land_Model_Name
	File; Not yet documented, but you help document it through GitHub!


- LandBehavior
	Ref, Ref, ...; Not yet documented, but you help document it through GitHub!


- Loop_Idle_Anim_00
	Bool; Not yet documented, but you help document it through GitHub!


- Lua_Script
	Ref; Not yet documented, but you help document it through GitHub!


- Mass
	Float; Not yet documented, but you help document it through GitHub!


- Max_Lift
	Float; Not yet documented, but you help document it through GitHub!


- Max_Rate_Of_Turn
	Float; Not yet documented, but you help document it through GitHub!


- Max_Speed
	Int; Not yet documented, but you help document it through GitHub!


- Min_Speed
	Float; Not yet documented, but you help document it through GitHub!


- MinimumPushReturnDistance
	Int; Not yet documented, but you help document it through GitHub!


- Mouse_Collide_Override_Sphere_Radius
	Float; Not yet documented, but you help document it through GitHub!


- Movement_Animation_Speed
	Float; Not yet documented, but you help document it through GitHub!


- MovementClass
	Ref; Not yet documented, but you help document it through GitHub!


- Neutralization_Cost
	Float; Not yet documented, but you help document it through GitHub!


- Occlusion_Silhouette_Enabled
	Int; Not yet documented, but you help document it through GitHub!


- OccupationStyle
	Ref; Not yet documented, but you help document it through GitHub!


- OverrideAcceleration
	Float; Not yet documented, but you help document it through GitHub!


- OverrideDeceleration
	Float; Not yet documented, but you help document it through GitHub!


- Play_SFXEvent_On_Sighting
	Bool; Not yet documented, but you help document it through GitHub!


- Primary_Locomotor_Name
	Ref; Not yet documented, but you help document it through GitHub!


- Projectile_Damage
	Float; Not yet documented, but you help document it through GitHub!


- Projectile_Fire_Recharge_Seconds
	Float; Not yet documented, but you help document it through GitHub!


- Projectile_Types
	Ref; Not yet documented, but you help document it through GitHub!


- Ranged_Target_Z_Adjust
	Float; Not yet documented, but you help document it through GitHub!


- Ranking_In_Category
	Int; Not yet documented, but you help document it through GitHub!


- Scale_Factor
	Float; Not yet documented, but you help document it through GitHub!


- Score_Cost_Credits
	Int; Not yet documented, but you help document it through GitHub!


- Secondary_Locomotor_Name
	Ref; Not yet documented, but you help document it through GitHub!


- Select_Box_Scale
	Int; Not yet documented, but you help document it through GitHub!


- Select_Box_Z_Adjust
	Floatf; Not yet documented, but you help document it through GitHub!


- Selection_Blob_Material_Name
	Ref; Not yet documented, but you help document it through GitHub!


- Sensor_Range
	Int; Not yet documented, but you help document it through GitHub!


- SFXEvent_Attack
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Deploy
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Engine_Moving_Loop
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Fire
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Fleet_Move
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Group_Attack
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Group_Move
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Guard
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Health_Critical_Warning
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Health_Low_Warning
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Move
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Select
	Ref; Not yet documented, but you help document it through GitHub!


- Shield_Points
	Int; Not yet documented, but you help document it through GitHub!


- Size_Value
	Int; Not yet documented, but you help document it through GitHub!


- Space_Layer
	Ref; Not yet documented, but you help document it through GitHub!


- Stay_In_Transport_During_Ground_Battle
	Bool; Not yet documented, but you help document it through GitHub!


- Stealth_Capable
	Bool; Not yet documented, but you help document it through GitHub!


- SurfaceFX_Name
	Ref, Ref; Not yet documented, but you help document it through GitHub!


- Tactical_Health
	Int; Not yet documented, but you help document it through GitHub!


- Targeting_Max_Attack_Distance
	Float; Not yet documented, but you help document it through GitHub!


- Targeting_Priority_Set
	Ref; Not yet documented, but you help document it through GitHub!


- Targeting_Stickiness_Time_Threshold
	Float; Not yet documented, but you help document it through GitHub!


- Text_ID
	Ref; The ID of the text to insert for the name of this object in-game. Text is stored in a `DAT File <basegame-filetype-dat>`.


- Type
	Ref; Not yet documented, but you help document it through GitHub!


- UnitCollisionClass
	Ref; Not yet documented, but you help document it through GitHub!


- Uses_Multiple_Locomotors
	Bool; Not yet documented, but you help document it through GitHub!


- Victory_Relevant
	Bool; Not yet documented, but you help document it through GitHub!







EaW-Godot Port Connection
*************************
Not yet documented, but you help document it through GitHub!
