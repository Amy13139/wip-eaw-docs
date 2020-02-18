.. _xml_type_template:
.. Template to use for XML type documentation

**********
Containers
**********


About
=====
*Description*: This Type/Subtype does something!


Structure
=========
Containers
----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Container``                                                     ``Name``
================================================================= =================================================================

|

Container
^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Autonomous_Move_Extension_Vs_Attacker
	Float; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Behavior
	Ref, Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Limit_Current_For_All_Allies
	Int; *Description Here*

- Build_Limit_Lifetime_Per_Player
	Int; *Description Here*

- CategoryMask
	Ref; *Description Here*

- ContainerArrangement
	Ref; *Description Here*

- Damage
	Int; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- FormationOrder
	Ref; *Description Here*

- FormationSpacing
	Ref; *Description Here*

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

- GUI_Velocity
	Int; *Description Here*

- Galactic_Model_Name
	File; *Description Here*

- Guard_Chase_Range
	Float; *Description Here*

- Hyperspace
	Bool y/n; *Description Here*

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

- Is_Named_Hero
	Bool Y/N; *Description Here*

- Is_Squashable
	Ref; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref, Ref, Ref; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Min_Speed
	Float; *Description Here*

- MovementClass
	Ref; *Description Here*

- MovementPredictionInterval
	Float; *Description Here*

- Name_Adjust
	Ref, Ref, Float; *Description Here*

- OccupationStyle
	Ref; *Description Here*

- Override_Acceleration
	Float; *Description Here*

- Override_Deceleration
	Float; *Description Here*

- Political_Faction
	Ref; *Description Here*

- Pre_Lit
	Bool Y/N; *Description Here*

- Radar_Icon_Scale_Land
	Int; *Description Here*

- Radar_Icon_Scale_Space
	Int; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Select_Box_Scale
	Int; *Description Here*

- Select_Box_Z_Adjust
	Floatf; *Description Here*

- Show_Name
	Bool Y/N; *Description Here*

- SpaceBehavior
	Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Squadron_Formation_Error_Tolerance
	Float; *Description Here*

- Squadron_Offsets
	Float, Float, Float; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Targeting_Max_Attack_Distance
	Float; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- UnitCollisionClass
	Ref; *Description Here*

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

EmpireGroundCompanies
---------------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GroundCompany``                                                 ``Name``
================================================================= =================================================================

|

GroundCompany
^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Affiliation
	Ref; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Behavior
	Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Tab_Land_Units
	Bool Y/N; *Description Here*

- Build_Time_Reduced_By_Multiple_Factories
	Ref; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- Company_Transport_Unit
	Ref; *Description Here*

- Company_Units
	Ref, Ref; *Description Here*

- Create_Team_Type
	Ref; *Description Here*

- Damage
	Int; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

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

- Icon_Name
	File; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Is_Escort
	Bool y/n; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Maintenance_Cost
	Float; *Description Here*

- Max_Squad_Size
	Ref; *Description Here*

- Population_Value
	Int; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Planets
	None; *Description Here*

- Required_Special_Structures
	Ref; *Description Here*

- Required_Star_Base_Level
	Int; *Description Here*

- Required_Timeline
	Int; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- Scale_Factor
	Int; *Description Here*

- Score_Cost_Credits
	Int; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

HeroCompanies
-------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``HeroCompany``                                                   ``Name``
================================================================= =================================================================

|

HeroCompany
^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Affiliation
	Ref; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Available_In_Skirmish
	Bool y/n; *Description Here*

- Behavior
	Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Limit_Current_Per_Player
	Int; *Description Here*

- Build_Limit_Lifetime_For_All_Allies
	Ref; *Description Here*

- Build_Tab_Heroes
	Bool Y/N; *Description Here*

- Build_Time_Reduced_By_Multiple_Factories
	Ref; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- Can_Be_Only_One
	Bool t/f; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Combat_Power_Value
	Int; *Description Here*

- Company_Transport_Unit
	Ref; *Description Here*

- Company_Units
	Ref; *Description Here*

- Create_Team_Type
	Ref; *Description Here*

- Damage
	Int; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Formation_Priority
	Int; *Description Here*

- GUI_Row
	Int; *Description Here*

- Guard_Chase_Range
	Float; *Description Here*

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Is_Force_Sensitive
	Bool Y/N; *Description Here*

- Is_Generic_Hero
	Bool Y/N; *Description Here*

- Is_Homogeneous
	Bool Y/N; *Description Here*

- Is_Named_Hero
	Bool Y/N; *Description Here*

- Is_Stealth_Company
	Bool Y/N; *Description Here*

- Lua_Script
	None; *Description Here*

- Max_Squad_Size
	Ref; *Description Here*

- Population_Value
	Int; *Description Here*

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

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- SFXEvent_Hero_Respawned
	Ref; *Description Here*

- SFXEvent_Move
	Ref; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

Indigenous_Companies
--------------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GroundCompany``                                                 ``Name``
================================================================= =================================================================

|

GroundCompany
^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Affiliation
	Ref; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Behavior
	Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Tab_Land_Units
	Bool Y/N; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- Company_Transport_Unit
	Ref; *Description Here*

- Company_Units
	Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Create_Team_Type
	Ref; *Description Here*

- Damage
	Int; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Formation_Priority
	Int; *Description Here*

- Icon_Name
	File; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Is_Escort
	Bool y/n; *Description Here*

- Max_Squad_Size
	Ref; *Description Here*

- Population_Value
	Int; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Planets
	None; *Description Here*

- SFXEvent_Tactical_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Complete
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Started
	Ref; *Description Here*

- Score_Cost_Credits
	Int; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Ref; *Description Here*

RebelGroundCompanies
--------------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GroundCompany``                                                 ``Name``
================================================================= =================================================================

|

GroundCompany
^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Affiliation
	Ref; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Behavior
	Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Tab_Land_Units
	Bool Y/N; *Description Here*

- Build_Time_Reduced_By_Multiple_Factories
	Ref; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- Company_Transport_Unit
	Ref; *Description Here*

- Company_Units
	Ref, Ref, Ref, Ref, Ref; *Description Here*

- Create_Team_Type
	Ref; *Description Here*

- Damage
	Int; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- Formation_Priority
	Int; *Description Here*

- Formation_Prority
	Int; *Description Here*

- GUI_Distance
	Int; *Description Here*

- GUI_Model
	File; *Description Here*

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

- Ignore_For_Reoptimization
	Ref; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Is_Escort
	Bool y/n; *Description Here*

- Is_Homogeneous
	Bool Y/N; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Maintenance_Cost
	Float; *Description Here*

- Max_Squad_Size
	Ref; *Description Here*

- Population_Value
	Int; *Description Here*

- Required_Ground_Base_Level
	Int; *Description Here*

- Required_Planets
	None; *Description Here*

- Required_Special_Structures
	Ref; *Description Here*

- Required_Star_Base_Level
	Int; *Description Here*

- Required_Timeline
	Int; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Fleet_Move
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Int; *Description Here*

- Ship_Class
	Ref; *Description Here*

- Slice_Cost_Credits
	Int; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*

Squadrons
---------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Squadron``                                                      ``Name``
================================================================= =================================================================

|

Squadron
^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Abilities
	Ref; *Description Here*

- Affiliation
	Ref; *Description Here*

- Attack_Move_Response_Range
	Float; *Description Here*

- Autonomous_Move_Extension_Vs_Attacker
	Float; *Description Here*

- Autoresolve_Health
	Int; *Description Here*

- Behavior
	Ref; *Description Here*

- Build_Can_Be_Unlocked_By_Slicer
	Bool Y/N; *Description Here*

- Build_Cost_Credits
	Int; *Description Here*

- Build_Initially_Locked
	Bool Y/N; *Description Here*

- Build_Limit_Current_For_All_Allies
	Int; *Description Here*

- Build_Limit_Lifetime_Per_Player
	Ref; *Description Here*

- Build_Tab_Space_Units
	Bool Y/N; *Description Here*

- Build_Time_Seconds
	Int; *Description Here*

- Create_Team_Type
	Ref; *Description Here*

- Damage
	Int; *Description Here*

- Encyclopedia_Good_Against
	Ref; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Encyclopedia_Vulnerable_To
	Ref; *Description Here*

- FormationOrder
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

- Icon_Name
	File; *Description Here*

- Idle_Chase_Range
	Float; *Description Here*

- Is_Bomber
	Bool y/n; *Description Here*

- Is_Dummy
	Bool Y/N; *Description Here*

- Is_Escort
	Bool Y/N; *Description Here*

- Is_Homogeneous
	Bool Y/N; *Description Here*

- Is_Named_Hero
	Bool Y/N; *Description Here*

- Max_Squad_Size
	Ref; *Description Here*

- Political_Control
	Int; *Description Here*

- Population_Value
	Int; *Description Here*

- Property_Flags
	Ref; *Description Here*

- Required_Special_Structures
	None; *Description Here*

- Required_Star_Base_Level
	Int; *Description Here*

- Required_Tech_Structure
	None; *Description Here*

- Required_Timeline
	None; *Description Here*

- SFXEvent_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Build_Complete
	Ref; *Description Here*

- SFXEvent_Build_Started
	Ref; *Description Here*

- SFXEvent_Hero_Respawned
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Cancelled
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Complete
	Ref; *Description Here*

- SFXEvent_Tactical_Build_Started
	Ref; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Slice_Cost_Credits
	Int; *Description Here*

- SpaceBehavior
	Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Squadron_Formation_Error_Tolerance
	Float; *Description Here*

- Squadron_Offsets
	Float, Float, Float; *Description Here*

- Squadron_Units
	Ref, Ref; *Description Here*

- Tactical_Build_Cost_Multiplayer
	Int; *Description Here*

- Tactical_Build_Prerequisites
	None; *Description Here*

- Tactical_Build_Time_Seconds
	Int; *Description Here*

- Tactical_Production_Queue
	Ref; *Description Here*

- Tech_Level
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Unit_Abilities_Data
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
