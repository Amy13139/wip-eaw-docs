.. _xml_type_template:
.. Template to use for XML type documentation

*********
Particles
*********


About
=====
*Description*: This Type/Subtype does something!


Structure
=========
Particles
---------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Particle``                                                      ``Name``
================================================================= =================================================================

|

Particle
^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Allow_Particle_Model_Culling
	Bool y/n; *Description Here*

- Behavior
	Ref; *Description Here*

- Exclude_From_Distance_Fade
	Ref; *Description Here*

- Explosion_Jitter_Factor
	Int; *Description Here*

- Explosion_Scorch_Mark
	Ref; *Description Here*

- Galactic_Model_Name
	File; *Description Here*

- In_Background
	Ref; *Description Here*

- Is_Decoration
	Ref; *Description Here*

- Is_Editor_Placed
	Bool t/f; *Description Here*

- Land_Model_Name
	Ref; *Description Here*

- Model_Visible_To_Enemy
	Bool Y/N; *Description Here*

- No_Particle_Below_Detail_Level
	Float; *Description Here*

- Particle_Attach_To_Collision
	Int; *Description Here*

- Particle_Lifetime_Frames
	Ref; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Space_Model_Name
	File; *Description Here*

SpecialEffects
--------------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``SpecialEffect``                                                 ``Name``
================================================================= =================================================================

|

SpecialEffect
^^^^^^^^^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Behavior
	Ref; *Description Here*

- Is_Decoration
	Bool Y/N; *Description Here*

- Is_Discardable
	Bool Y/N; *Description Here*

- Land_Model_Name
	File; *Description Here*

- Scale_Factor
	Float; *Description Here*

- Space_Model_Name
	File; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
