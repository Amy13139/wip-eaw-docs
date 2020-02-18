.. _xml_type_template:
.. Template to use for XML type documentation

*****
Props
*****


About
=====
*Description*: This Type/Subtype does something!


Structure
=========
Prop_Forest
-----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Prop_Forest``                                                   ``Name``
================================================================= =================================================================

|

Prop_Forest
^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_XExtent_Offset
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Hard_YExtent_Offset
	Float; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Model_Name
	File; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Tactical_Model_Name
	File; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- UnitCollisionClass
	Ref; *Description Here*


|


|
|

Props_Desert
------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Prop_Desert``                                                   ``Name``
================================================================= =================================================================

|

Prop_Desert
^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_XExtent_Offset
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Hard_YExtent_Offset
	Float; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Is_Discardable
	Bool Y/N; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Max_Distance_From_Spawner
	Int; *Description Here*

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

- Scale_Factor
	Float; *Description Here*

- Space_Layer
	Ref | Ref | Ref; *Description Here*

- Space_Obstacle_Offset
	Ref; *Description Here*

- Space_Obstacle_Radius
	Ref; *Description Here*

- Spawn_Indigenous_Units_Chance
	Floatf; *Description Here*

- Spawn_Indigenous_Units_In_Packs
	Bool Y/N; *Description Here*

- Spawn_Indigenous_Units_Radius
	Floatf; *Description Here*

- Spawned_Indigenous_Units_Delay_Seconds
	Float; *Description Here*

- Spawned_Indigenous_Units_Quantity
	Int; *Description Here*

- Spawned_Indigenous_Units_Type
	Ref; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- UnitCollisionClass
	Ref; *Description Here*


|


|
|

Props_Generic
-------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Props_Generic``                                                 ``Name``
``SpaceProp``                                                     ``Name``
================================================================= =================================================================

|

Props_Generic
^^^^^^^^^^^^^
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

- Avoidance_Disabled
	Ref; *Description Here*

- Behavior
	Ref; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Dead
	Bool Y/N; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Damage
	Int; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Deploys
	Bool Y/N; *Description Here*

- Encyclopedia_Text
	Ref; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- FormationGrouping
	Ref; *Description Here*

- FormationOrder
	Ref; *Description Here*

- FormationSpacing
	Float; *Description Here*

- Ground_Vehicle_Turret_Target
	Ref; *Description Here*

- Has_Land_Evaluator
	Bool Y/N; *Description Here*

- Icon_Name
	File; *Description Here*

- Influences_Capture_Point
	Ref; *Description Here*

- Is_Affected_By_Gravity_Control_Field
	Ref; *Description Here*

- Is_Branched_Map_Discardable
	Bool Y/N; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Is_Discardable
	Bool Y/N; *Description Here*

- Is_Valid_Target
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref, Ref, Ref, Ref, Ref, Ref; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- MinimumPushReturnDistance
	Ref; *Description Here*

- MovementClass
	Ref; *Description Here*

- Movement_Animation_Speed
	Float; *Description Here*

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

- Political_Control
	Int; *Description Here*

- SFXEvent_Engine_Idle_Loop
	Ref; *Description Here*

- SFXEvent_Engine_Moving_Loop
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Score_Cost_Credits
	Ref; *Description Here*

- Size_Value
	Int; *Description Here*

- Snap_Movement_Orders_To_Center
	Ref; *Description Here*

- Space_Layer
	Ref; *Description Here*

- SurfaceFX_Name
	Ref, Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- UnitCollisionClass
	Ref; *Description Here*

- Victory_Relevant
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

SpaceProp
^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Is_Decoration
	Ref; *Description Here*

- Is_Discardable
	Ref; *Description Here*

- Land_Model_Name
	Ref; *Description Here*

- Scale_Factor
	Ref; *Description Here*

- Sort_Order_Adjust
	Ref; *Description Here*

- Text_ID
	None; The in-game name of this unit, references a .DAT file to allow from translations


|


|
|

Props_Snow
----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Props_Snow``                                                    ``Name``
================================================================= =================================================================

|

Props_Snow
^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_XExtent_Offset
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Hard_YExtent_Offset
	Float; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Model_Name
	File; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- UnitCollisionClass
	Ref; *Description Here*


|


|
|

Props_Story
-----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``GroundBuildable``                                               ``Name``
``Props_Story``                                                   ``Name``
``SpaceStructure``                                                ``Name``
================================================================= =================================================================

|

GroundBuildable
^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Variant_Of_Existing_Type
	Ref; *Description Here*


|

Props_Story
^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Affiliation
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Base_Level_Available
	Int; *Description Here*

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
	Bool Y/N; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_SFXEvent_Start_Die
	Ref; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

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

- Radar_Icon_Scale_Land
	Float; *Description Here*

- Radar_Icon_Scale_Space
	Float; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*


|

SpaceStructure
^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Affiliation
	Ref; *Description Here*

- Armor_Type
	Ref; *Description Here*

- Base_Level_Available
	Int; *Description Here*

- Behavior
	None; *Description Here*

- CategoryMask
	Ref; *Description Here*

- Collidable_By_Projectile_Living
	Bool Y/N; *Description Here*

- Death_Clone
	Ref, Ref; *Description Here*

- Death_Explosions
	Ref; *Description Here*

- Death_Projectiles
	Ref; *Description Here*

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

- Facing_Adjust
	Float, Float, Float; *Description Here*

- GUI_Bounds_Scale
	Float; *Description Here*

- GUI_Bracket_Size
	Int; *Description Here*

- Has_Space_Evaluator
	Bool T/F; *Description Here*

- Icon_Name
	File; *Description Here*

- Initial_State_Visible_Under_FOW
	Bool T/F; *Description Here*

- Is_Visible_On_Radar
	Bool Y/N; *Description Here*

- LandBehavior
	Ref, Ref; *Description Here*

- Land_Damage_Alternates
	Int, Int, Int, Int; *Description Here*

- Land_Damage_SFX
	Ref, Ref, Ref, Ref; *Description Here*

- Land_Damage_Thresholds
	Int, Float, Float, Int; *Description Here*

- Layer_Z_Adjust
	Float; *Description Here*

- Mass
	Float; Always 0.99... 5, with an arbitrary number of 9s. Probably unused.

- No_Colorization_Color
	Int, Int, Int, Int; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Property_Flags
	Ref; *Description Here*

- Radar_Icon_Size
	Ref; *Description Here*

- Ranged_Target_Z_Adjust
	Float; *Description Here*

- Remove_Upon_Death
	Bool t/f; *Description Here*

- Reveal_During_Setup_Phase
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

- SpaceBehavior
	Ref, Ref; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Space_Obstacle_Offset
	Ref; *Description Here*

- Space_Obstacle_Radius
	Ref; *Description Here*

- Tactical_Health
	Int; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Variant_Of_Existing_Type
	Ref; *Description Here*

- Victory_Relevant
	Bool y/n; *Description Here*

- Visible_On_Radar_When_Fogged
	Bool T/F; *Description Here*


|


|
|

Props_Swamp
-----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Props_Swamp``                                                   ``Name``
================================================================= =================================================================

|

Props_Swamp
^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_XExtent_Offset
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Hard_YExtent_Offset
	Float; *Description Here*

- Encyclopedia_Unit_Class
	Ref; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Is_Editor_Placed
	Bool t/f; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Model_Name
	File; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- UnitCollisionClass
	Ref; *Description Here*


|


|
|

Props_Temperate
---------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Props_Temperate``                                               ``Name``
================================================================= =================================================================

|

Props_Temperate
^^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Blob_Shadow_Below_Detail_Level
	Int; *Description Here*

- Blob_Shadow_Material_Name
	Ref; *Description Here*

- Blob_Shadow_Scale
	Float, Float; *Description Here*

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_XExtent_Offset
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Hard_YExtent_Offset
	Float; *Description Here*

- Exclude_From_Distance_Fade
	Bool t/f; *Description Here*

- Idle_Anim_00_Rate_Mod
	Float; *Description Here*

- In_Background
	Ref; *Description Here*

- Is_Decoration
	Ref; *Description Here*

- Is_Discardable
	Ref; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Loop_Idle_Anim_00
	Ref; *Description Here*

- Max_Distance_From_Spawner
	Int; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Sort_Order_Adjust
	Ref; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Spawn_Indigenous_Units_Chance
	Floatf; *Description Here*

- Spawn_Indigenous_Units_In_Packs
	Bool Y/N; *Description Here*

- Spawn_Indigenous_Units_Radius
	Floatf; *Description Here*

- Spawned_Indigenous_Units_Delay_Seconds
	Float; *Description Here*

- Spawned_Indigenous_Units_Quantity
	Int; *Description Here*

- Spawned_Indigenous_Units_Type
	Ref, Ref; *Description Here*

- Tactical_Model_Name
	File; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- UnitCollisionClass
	Ref; *Description Here*

- Variant_Of_Existing_Type
	Ref; *Description Here*


|


|
|

Props_Urban
-----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Props_Urban``                                                   ``Name``
================================================================= =================================================================

|

Props_Urban
^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Behavior
	Ref; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Is_Discardable
	Bool Y/N; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- No_Reflection_Below_Detail_Level
	Int; *Description Here*

- No_Refraction_Below_Detail_Level
	Int; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations


|


|
|

Props_Volcanic
--------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Props_Volcanic``                                                ``Name``
================================================================= =================================================================

|

Props_Volcanic
^^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Custom_Hard_XExtent
	Float; *Description Here*

- Custom_Hard_XExtent_Offset
	Float; *Description Here*

- Custom_Hard_YExtent
	Float; *Description Here*

- Custom_Hard_YExtent_Offset
	Float; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Is_Editor_Placed
	Bool t/f; *Description Here*

- LandBehavior
	Ref; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Space_Layer
	Ref; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- UnitCollisionClass
	Ref; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
