.. _xml_type_template:
.. Template to use for XML type documentation

***********
Projectiles
***********


About
=====
*Description*: This Type/Subtype does something!


Structure
=========
Projectiles
-----------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Projectile``                                                    ``Description``, ``Name``
================================================================= =================================================================

|

Projectile
^^^^^^^^^^
- Attribute - Description
	String; An optional description for the node, only used to help anyone reading the XML.

- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- AI_Combat_Power
	Int; *Description Here*

- Behavior
	Ref, Ref; *Description Here*

- Damage_Type
	Ref; *Description Here*

- Death_Explosions
	None; *Description Here*

- Death_SFXEvent_Start_Die
	None; *Description Here*

- Dense_FOW_Reveal_Range_Multiplier
	Float; *Description Here*

- Explode_When_Reached_Target_Radius
	Ref; *Description Here*

- Internal_Damage_Type
	Ref; *Description Here*

- Land_FOW_Reveal_Range
	Float; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Loop_Idle_Anim_00
	Bool Y/N; *Description Here*

- Max_Rate_Of_Turn
	Float; *Description Here*

- Max_Speed
	Float; *Description Here*

- Model_Visible_To_Enemy
	Bool Y/N; *Description Here*

- Projectile_Absorbed_By_Shields_Particle
	Ref; *Description Here*

- Projectile_Acceleration_Per_Frame
	Float; *Description Here*

- Projectile_Blast_Area_Damage
	Float; *Description Here*

- Projectile_Blast_Area_Dropoff
	Bool T/F; *Description Here*

- Projectile_Blast_Area_Dropoff_Tiers
	Int; *Description Here*

- Projectile_Blast_Area_Immune_Faction
	Ref; *Description Here*

- Projectile_Blast_Area_Range
	Float; *Description Here*

- Projectile_Block_Chance_Modifier
	Float; *Description Here*

- Projectile_Bomb_Fall_Accel_Rate
	Float; *Description Here*

- Projectile_Category
	Ref; *Description Here*

- Projectile_Cause_Invulnerability_Duration_Frames
	Ref; *Description Here*

- Projectile_Cause_Invulnerability_Max_Targets
	Ref; *Description Here*

- Projectile_Cause_Invulnerability_On_Detonation
	Ref; *Description Here*

- Projectile_Cause_Invulnerability_Radius
	Float; *Description Here*

- Projectile_Cause_Invulnerability_Spawn_Effect
	Ref; *Description Here*

- Projectile_Cause_Invulnerability_Targets_Category_Mask
	Ref | Ref | Ref | Ref; *Description Here*

- Projectile_Convert_Enemy_On_Detonation
	Ref; *Description Here*

- Projectile_Convert_Enemy_Radius
	Ref; *Description Here*

- Projectile_Convert_Enemy_Spawn_Effect
	Ref; *Description Here*

- Projectile_Convert_Enemy_Targets_Category_Mask
	Ref; *Description Here*

- Projectile_Custom_Render
	Int; *Description Here*

- Projectile_Damage
	Float; *Description Here*

- Projectile_Damage_Delay_Secs
	Float; *Description Here*

- Projectile_Damages_Random_Hard_Points
	Bool y/n; *Description Here*

- Projectile_Disable_Engines_Duration
	Float; *Description Here*

- Projectile_Disables_Engines_When_Power_Drained
	Bool Y/N; *Description Here*

- Projectile_Does_Energy_Damage
	Bool Y/N; *Description Here*

- Projectile_Does_Hitpoint_Damage
	Bool Y/N; *Description Here*

- Projectile_Does_Shield_Damage
	Bool Y/N; *Description Here*

- Projectile_Energy_Per_Shot
	Int; *Description Here*

- Projectile_Grenade_Can_Lob_Slower
	Bool y/n; *Description Here*

- Projectile_Grenade_Gravity
	Float; *Description Here*

- Projectile_Grenade_Gravity_Lob_Mod
	Float; *Description Here*

- Projectile_Grenade_Sticks_On_Collision
	Bool y/n; *Description Here*

- Projectile_Ground_Detonation_Particle
	None; *Description Here*

- Projectile_Ground_Detonation_SurfaceFX
	None; *Description Here*

- Projectile_Instant_Heal_Duration_Frames
	Ref; *Description Here*

- Projectile_Instant_Heal_Health_Increase
	Ref; *Description Here*

- Projectile_Instant_Heal_On_Detonation
	Ref; *Description Here*

- Projectile_Instant_Heal_Radius
	Ref; *Description Here*

- Projectile_Instant_Heal_Spawn_Effect
	Ref; *Description Here*

- Projectile_Instant_Heal_Targets_Category_Mask
	Ref | Ref; *Description Here*

- Projectile_Ion_Stun_Duration
	Float; *Description Here*

- Projectile_Ion_Stun_On_Detonation
	Bool t/f; *Description Here*

- Projectile_Ion_Stun_Shot_Rate_Reduction_Percent
	Float; *Description Here*

- Projectile_Ion_Stun_Speed_Reduction_Percent
	Floatf; *Description Here*

- Projectile_Ion_Stun_Stack_Duration
	Bool Y/N; *Description Here*

- Projectile_Laser_Color
	Int, Int, Int, Int; *Description Here*

- Projectile_Length
	Float; *Description Here*

- Projectile_Lifetime_Detonation_Particle
	Ref; *Description Here*

- Projectile_Max_Flight_Distance
	Float; *Description Here*

- Projectile_Max_Lifetime
	Float; *Description Here*

- Projectile_Max_Scan_Range
	Float; *Description Here*

- Projectile_Object_Armor_Reduced_Detonation_Particle
	Ref; *Description Here*

- Projectile_Object_Detonation_Particle
	Ref; *Description Here*

- Projectile_Redirect_Chance_Modifier
	Float; *Description Here*

- Projectile_Rocket_Curve_Distance
	Int; *Description Here*

- Projectile_Rocket_Curve_Offset
	Int; *Description Here*

- Projectile_Rocket_Straight_Distance
	Int; *Description Here*

- Projectile_SFXEvent_Detonate
	Ref; *Description Here*

- Projectile_SFXEvent_Detonate_Reduced_By_Armor
	Ref; *Description Here*

- Projectile_Stun_Duration_Frames
	Int; *Description Here*

- Projectile_Stun_On_Detonation
	Bool Y/N; *Description Here*

- Projectile_Stun_Radius
	Int; *Description Here*

- Projectile_Stun_Spawn_Effect
	Ref; *Description Here*

- Projectile_Stun_Victims_Category_Mask
	Ref | Ref; *Description Here*

- Projectile_Stun_Victims_Unit_Types
	Ref; *Description Here*

- Projectile_Target_Point_On_Terrain
	Ref; *Description Here*

- Projectile_Texture_Slot
	Int, Int; *Description Here*

- Projectile_Weaken_Enemy_Cause_Damage_Reduction_Percent
	Float; *Description Here*

- Projectile_Weaken_Enemy_Duration_Seconds
	Float; *Description Here*

- Projectile_Weaken_Enemy_On_Detonation
	Bool Y/N; *Description Here*

- Projectile_Weaken_Enemy_Radius
	Int; *Description Here*

- Projectile_Weaken_Enemy_Spawn_Effect
	Ref; *Description Here*

- Projectile_Weaken_Enemy_Take_Damage_Increase_Percent
	Int; *Description Here*

- Projectile_Weaken_Enemy_Targets_Category_Mask
	Ref; *Description Here*

- Projectile_Width
	Float; *Description Here*

- SFXEvent_Fire
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Space_FOW_Reveal_Range
	Float; *Description Here*

- Space_Model_Name
	File; *Description Here*

- Text_ID
	Ref; The in-game name of this unit, references a .DAT file to allow from translations

- Variant_Of_Existing_Type
	Ref; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
