.. _xml_radar_map:
.. Template to use for XML type documentation

********
RadarMap
********


About
=====
	*Why they needed an XML type for this is beyond mortal comprehension. -luke13139*


Structure
=========
RadarMap
--------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``RadarMapEvents``                                                None
``RadarMapSettings``                                              None
================================================================= =================================================================

|

RadarMapEvents
^^^^^^^^^^^^^^
- Radar_Map_Event
	Ref; *Description Here*


|

RadarMapSettings
^^^^^^^^^^^^^^^^
- Color
	Int, Int, Int, Int; *Description Here*

- Land_Backdrop_Texture_Name
	File; *Description Here*

- Land_FOW_Color
	Int, Int, Int, Int; *Description Here*

- Land_Is_Guide_Rectangle
	Bool Y/N; *Description Here*

- Passability_Color_Settings
	Ref; *Description Here*

- Space_Asteroid_Field_Border_Color
	Int, Int, Int, Int; *Description Here*

- Space_Asteroid_Field_Color
	Int, Int, Int, Int; *Description Here*

- Space_Backdrop_Texture_Name
	File; *Description Here*

- Space_FOW_Color
	Int, Int, Int, Int; *Description Here*

- Space_Is_Guide_Rectangle
	Bool Y/N; *Description Here*

- Use_Event_System
	Bool Y/N; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
