.. _xml_type_template:
.. Template to use for XML type documentation

*******
Planets
*******


About
=====
*Description*: This Type/Subtype does something!


Structure
=========
Planets
-------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Planet``                                                        ``Name``
================================================================= =================================================================

|

Planet
^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Abilities
	Ref; *Description Here*

- Additional_Population_Capacity
	Int; *Description Here*

- Always_Instantiate_Galactic
	Bool y/n; *Description Here*

- Behavior
	Ref, Ref, Ref; *Description Here*

- Camera_Aligned
	Bool y/n; *Description Here*

- Describe_Advantage
	Ref; *Description Here*

- Describe_History
	Ref; *Description Here*

- Describe_Population
	Ref; *Description Here*

- Describe_Tactical
	Ref; *Description Here*

- Describe_Terrain
	Ref; *Description Here*

- Describe_Weather
	Ref; *Description Here*

- Describe_Wildlife
	Ref; *Description Here*

- Destroyed_Galactic_Model_Name
	File; *Description Here*

- Destroyed_Space_Tactical_Map
	None; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Weather_Icon
	File; *Description Here*

- Encyclopedia_Weather_Info
	Ref; *Description Here*

- Encyclopedia_Weather_Name
	Ref; *Description Here*

- Facing_Adjust
	Float, Float, Float; *Description Here*

- Force_Strength
	Float; *Description Here*

- GUI_Model_Name
	File; *Description Here*

- Galactic_Influence_Range
	Float; *Description Here*

- Galactic_Model_Name
	File; *Description Here*

- Galactic_Position
	Float, Float, Float; *Description Here*

- Hyperspace_Fleet_Reveal_Range
	Float; *Description Here*

- In_Background
	Bool y/n; *Description Here*

- Land_Tactical_Map
	Ref; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Ground_Base
	Int; *Description Here*

- Max_Space_Base
	Int; *Description Here*

- Mouse_Collide_Override_Sphere_Radius
	Float; *Description Here*

- Name_Adjust
	Ref, Ref, Float; *Description Here*

- Native_Icon_Name
	File; *Description Here*

- Planet_Ability_Description
	Ref; *Description Here*

- Planet_Ability_Icon
	File; *Description Here*

- Planet_Ability_Name
	Ref; *Description Here*

- Planet_Black_Market_Influences
	Bool Y/N; *Description Here*

- Planet_Capture_Bonus_Reward
	Ref; *Description Here*

- Planet_Credit_Value
	Int; *Description Here*

- Planet_Destroyed_Credit_Value
	Int; *Description Here*

- Planet_Groundbase_Stealth
	Bool Y/N; *Description Here*

- Planet_Is_Destroyable_By_TSW
	Ref; *Description Here*

- Planet_Is_Mining_Colony
	Bool Y/N; *Description Here*

- Planet_Restricted_Unit_Categories
	None; *Description Here*

- Planet_Restricted_Unit_Types
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Planet_Retains_Residual_Influence
	Ref; *Description Here*

- Planet_Slice_Affinity_Types
	None; *Description Here*

- Planet_Slice_Difficulty_Rating
	Int; *Description Here*

- Planet_Surface_Accessible
	Ref; *Description Here*

- Planet_Tech_Availability_Rating
	Int; *Description Here*

- Planet_Vigilance
	Bool Y/N; *Description Here*

- Political_Control
	Int; *Description Here*

- Potential_Indigenous_Power
	Ref, Int; *Description Here*

- Pre_Lit
	Bool y/n; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Show_Name
	Bool Y/N; *Description Here*

- Space_Tactical_Map
	Ref; *Description Here*

- Special_Structures
	Int; *Description Here*

- Special_Structures_Land
	Int; *Description Here*

- Special_Structures_Space
	Int; *Description Here*

- Terrain
	Ref; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- The_Force
	Ref; *Description Here*

- Zoomed_Terrain_Index
	Int; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
