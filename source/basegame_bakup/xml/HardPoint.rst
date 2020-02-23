.. _xml_hardpoint:
.. Template to use for XML type documentation

*********
HardPoint
*********


About
=====
Stores the individual parts of larger units. May or may not be targetable and destroyable. Most weapons in space are fired from hardpoints, with the notable exception of fighters and other small craft.


Structure
=========
HardPoints
----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``HardPoint``                                                     ``Name``
================================================================= =================================================================

|

HardPoint
^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Allow_Opportunity_Fire_When_Idle
	Bool T/F; *Description Here*

- Allow_Opportunity_Fire_When_Targeting
	Bool T/F; *Description Here*

- Allows_Special_Weapon_Use
	Ref; *Description Here*

- Attachment_Bone
	Ref; *Description Here*

- Collision_Mesh
	Ref; *Description Here*

- Damage_Decal
	Ref; *Description Here*

- Damage_Particles
	Ref; *Description Here*

- Damage_Type
	Ref; *Description Here*

- Death_Breakoff_Prop
	Ref; *Description Here*

- Death_Explosion_Particles
	Ref; *Description Here*

- Death_Explosion_SFXEvent
	Ref; *Description Here*

- Engine_Particles
	Ref; *Description Here*

- Fighter_Bay_Flyout_Distance
	Float; *Description Here*

- Fire_Bone_A
	Ref; *Description Here*

- Fire_Bone_B
	Ref; *Description Here*

- Fire_Bone_C
	Ref; *Description Here*

- Fire_Bone_D
	Ref; *Description Here*

- Fire_Category_Restrictions
	Ref, Ref; *Description Here*

- Fire_Cone_Height
	Float; *Description Here*

- Fire_Cone_Width
	Float; *Description Here*

- Fire_Inaccuracy_Distance
	Ref, Float; *Description Here*

- Fire_Max_Recharge_Seconds
	Float; *Description Here*

- Fire_Min_Recharge_Seconds
	Float; *Description Here*

- Fire_Projectile_Type
	Ref; *Description Here*

- Fire_Pulse_Count
	Int; *Description Here*

- Fire_Pulse_Delay_Seconds
	Float; *Description Here*

- Fire_Range_Distance
	Float; *Description Here*

- Fire_SFXEvent
	Ref; *Description Here*

- Fire_When_Deployed
	Bool Y/N; *Description Here*

- Fire_When_In_Normal_Attack_Mode
	Bool Y/N; *Description Here*

- Fire_When_In_Rocket_Attack_Mode
	Bool Y/N; *Description Here*

- Fire_When_Undeployed
	Bool Y/N; *Description Here*

- Health
	Float; *Description Here*

- Is_Destroyable
	Bool Y/N; *Description Here*

- Is_Targetable
	Bool Y/N; *Description Here*

- Model_To_Attach
	File; *Description Here*

- Projectile_Damage
	Int; *Description Here*

- Repair_Amount_Per_Frame
	Float; *Description Here*

- Repair_Cost_Per_Frame
	Float; *Description Here*

- Special_Ability_Name
	Ref; *Description Here*

- Tooltip_Text
	Ref; *Description Here*

- Type
	Ref; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing