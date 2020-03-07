##########################################
SpecialStructure
##########################################


About
*****
Not yet documented, but you help document it through GitHub!


Structure
*********
``SpecialStructure``
--------------------
Not yet documented, but you help document it through GitHub!

.. csv-table::
	:header: "Nested Nodes", "Description"

	"``Abilities``", "Nested Node for units, contains either an activated ability or some form of special behavior for a unit. See `Unit Abilities on Petrolution <modtools.petrolution.net/docs/Unit_Abilities_EaW>`_ for a list of EaW active abilities. FoC is currently not included, but a page may be added to this documentation"


``Abilities``
^^^^^^^^^^^^^
Nested Node for units, contains either an activated ability or some form of special behavior for a unit. See `Unit Abilities on Petrolution <modtools.petrolution.net/docs/Unit_Abilities_EaW>`_ for a list of EaW active abilities. FoC is currently not included, but a page may be added to this documentation

.. csv-table::
	:header: "Nested Nodes", "Description"

	"``Force_Healing_Ability``", "Nested Node for Abilities on the ground; restores HP to units near the caster"


``Force_Healing_Ability``
^^^^^^^^^^^^^^^^^^^^^^^^^
Nested Node for Abilities on the ground; restores HP to units near the caster

``Force_Healing_Ability``'s SubNodes
""""""""""""""""""""""""""""""""""""
- Activation_Style
	Ref; Not yet documented, but you help document it through GitHub!


- Applicable_Unit_Categories
	Ref; Not yet documented, but you help document it through GitHub!


- Applicable_Unit_Types
	Ref; Not yet documented, but you help document it through GitHub!


- Heal_Amount
	Float; Not yet documented, but you help document it through GitHub!


- Heal_Interval_In_Secs
	Float; Not yet documented, but you help document it through GitHub!


- Heal_Percent
	Float; Not yet documented, but you help document it through GitHub!


- Heal_Range
	Float; Not yet documented, but you help document it through GitHub!


- Owner_Light_Effect_Color
	Float, Float, Float; Not yet documented, but you help document it through GitHub!


- Owner_Light_Effect_Color2
	Ref; Not yet documented, but you help document it through GitHub!


- Owner_Light_Effect_Duration
	Float; Not yet documented, but you help document it through GitHub!


- Owner_Light_Effect_Pulse_Count
	Int; Not yet documented, but you help document it through GitHub!


- Owner_Light_Effect_Type
	Ref; Not yet documented, but you help document it through GitHub!


- Owner_Particle_Bone_Name
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Target_Affected
	Ref; Not yet documented, but you help document it through GitHub!


- Single_Target_Heal
	Bool; Not yet documented, but you help document it through GitHub!





SubNodes
^^^^^^^^
- Affiliation
	Ref; Not yet documented, but you help document it through GitHub!


- Armor_Type
	Ref; Not yet documented, but you help document it through GitHub!


- Base_Position
	Ref; Not yet documented, but you help document it through GitHub!


- Behavior
	Ref; Not yet documented, but you help document it through GitHub!


- Build_Can_Be_Unlocked_By_Slicer
	Bool; Not yet documented, but you help document it through GitHub!


- Build_Cost_Credits
	Int; Not yet documented, but you help document it through GitHub!


- Build_Initially_Locked
	Bool; Not yet documented, but you help document it through GitHub!


- Build_Max_Instances_Per_Planet
	Int; Not yet documented, but you help document it through GitHub!


- Build_Tab_Special_Structures
	Bool; Not yet documented, but you help document it through GitHub!


- Build_Time_Seconds
	Int; Not yet documented, but you help document it through GitHub!


- CategoryMask
	Ref; Not yet documented, but you help document it through GitHub!


- Collidable_By_Projectile_Living
	Bool; Not yet documented, but you help document it through GitHub!


- Death_Clone_Is_Obstacle
	Bool; Not yet documented, but you help document it through GitHub!


- Death_Explosions
	Ref; Not yet documented, but you help document it through GitHub!


- Death_SFXEvent_Start_Die
	Ref; Not yet documented, but you help document it through GitHub!


- Destruction_Survivors
	Ref, Ref, Ref, Float; Not yet documented, but you help document it through GitHub!


- Encyclopedia_Text
	Ref; Not yet documented, but you help document it through GitHub!


- Encyclopedia_Unit_Class
	Ref; Not yet documented, but you help document it through GitHub!


- GUI_Bounds_Scale
	Float; Not yet documented, but you help document it through GitHub!


- GUI_Bracket_Size
	Int; Not yet documented, but you help document it through GitHub!


- GUI_Row
	Int; Not yet documented, but you help document it through GitHub!


- Has_Land_Evaluator
	Bool; Not yet documented, but you help document it through GitHub!


- Icon_Name
	File; The name of the icon displayed during gameplay, may reference a file stored in an :ref:`MTD File <basegame-filetype-mtd>`.


- Influences_Capture_Point
	Bool; Not yet documented, but you help document it through GitHub!


- Is_Community_Property
	Bool; Not yet documented, but you help document it through GitHub!


- Is_Dummy
	Bool; Not yet documented, but you help document it through GitHub!


- Is_Special_Weapon_In_Space
	Bool; Not yet documented, but you help document it through GitHub!


- Is_Visible_On_Radar
	Bool; Not yet documented, but you help document it through GitHub!


- Land_Damage_Alternates
	Int, Int, Int, Int; Not yet documented, but you help document it through GitHub!


- Land_Damage_SFX
	Ref, Ref, Ref, Ref; Not yet documented, but you help document it through GitHub!


- Land_Damage_Thresholds
	Float, Float, Float, Float; Not yet documented, but you help document it through GitHub!


- Land_FOW_Reveal_Range
	Float; Not yet documented, but you help document it through GitHub!


- Land_Model_Name
	File; Not yet documented, but you help document it through GitHub!


- Land_Victory_Relevant
	Bool; Not yet documented, but you help document it through GitHub!


- LandBehavior
	Ref, Ref, ...; Not yet documented, but you help document it through GitHub!


- Last_State_Visible_Under_FOW
	Bool; Not yet documented, but you help document it through GitHub!


- Multisample_FOW_Check
	Bool; Not yet documented, but you help document it through GitHub!


- No_Reflection_Below_Detail_Level
	Int; Not yet documented, but you help document it through GitHub!


- No_Refraction_Below_Detail_Level
	Int; Not yet documented, but you help document it through GitHub!


- Political_Control
	Int; Not yet documented, but you help document it through GitHub!


- Prevents_Blockade_Run_Attrition
	Bool; Not yet documented, but you help document it through GitHub!


- Projectile_Fire_Pulse_Count
	Int; Not yet documented, but you help document it through GitHub!


- Projectile_Fire_Pulse_Delay_Seconds
	Float; Not yet documented, but you help document it through GitHub!


- Projectile_Fire_Recharge_Seconds
	Float; Not yet documented, but you help document it through GitHub!


- Projectile_Types
	Ref; Not yet documented, but you help document it through GitHub!


- Radar_Icon_Size
	Float None Float; Not yet documented, but you help document it through GitHub!


- Required_Ground_Base_Level
	Int; Not yet documented, but you help document it through GitHub!


- Required_Planets
	Ref; Not yet documented, but you help document it through GitHub!


- Required_Special_Structures
	Ref; Not yet documented, but you help document it through GitHub!


- Required_Star_Base_Level
	Int; Not yet documented, but you help document it through GitHub!


- Required_Timeline
	Int; Not yet documented, but you help document it through GitHub!


- Reveal_During_Setup_Phase
	Bool; Not yet documented, but you help document it through GitHub!


- Scale_Factor
	Float; Not yet documented, but you help document it through GitHub!


- Score_Cost_Credits
	Int; Not yet documented, but you help document it through GitHub!


- SFXEvent_Build_Cancelled
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Build_Complete
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Build_Started
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Fire
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Select
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Special_Weapon_Ready
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Unit_Lost
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Unit_Under_Attack
	Ref; Not yet documented, but you help document it through GitHub!


- Size_Value
	Int; Not yet documented, but you help document it through GitHub!


- Slice_Cost_Credits
	Int; Not yet documented, but you help document it through GitHub!


- Space_Layer
	Ref; Not yet documented, but you help document it through GitHub!


- Space_Obstacle_Offset
	Int Int Int; Not yet documented, but you help document it through GitHub!


- Space_Victory_Relevant
	Bool; Not yet documented, but you help document it through GitHub!


- SpaceAutoResolveStunRate
	Int; Not yet documented, but you help document it through GitHub!


- SpaceBehavior
	Ref; Not yet documented, but you help document it through GitHub!


- Special_Weapon_Index
	Int; Not yet documented, but you help document it through GitHub!


- Special_Weapon_Target_Action_Index
	Int; Not yet documented, but you help document it through GitHub!


- Special_Weapon_Valid_Targets
	Ref | Ref | ...; Not yet documented, but you help document it through GitHub!


- Tactical_Additional_Structure_Type
	Ref; Not yet documented, but you help document it through GitHub!


- Tactical_Health
	Int; Not yet documented, but you help document it through GitHub!


- Tech_Level
	Int; Not yet documented, but you help document it through GitHub!


- Text_ID
	Ref; The ID of the text to insert for the name of this object in-game. Text is stored in a `DAT File <basegame-filetype-dat>`.


- Weapon_Quantity
	Int; Not yet documented, but you help document it through GitHub!


- Weapon_Type
	Ref; Not yet documented, but you help document it through GitHub!







EaW-Godot Port Connection
*************************
Not yet documented, but you help document it through GitHub!
