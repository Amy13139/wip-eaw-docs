.. _xml_bink_movie:
.. BIK movie storage docs

*********
BinkMovie
*********


About
=====
References .BIK Movie files, giving them a name attribute which can be referenced


Structure
=========
Movies
------
================================================================= =================================================================
Node Name                                                         Attributes
================================================================= =================================================================
``Movie``                                                         ``Name``
================================================================= =================================================================

|

Movie
^^^^^
- Attribute - Name
	String; The name of the node, can be referenced by other nodes

- Alpha
	Bool t/f; *Description Here*

- Cannot_Skip
	Bool t/f; *Description Here*

- Caption_Duration
	Ref, Int; *Description Here*

- Caption_Frame
	Ref, Int; *Description Here*

- Commandbar_Offset
	Ref; *Description Here*

- Halt_Game_Music
	Ref; *Description Here*

- Has_Credits
	Bool t/f; *Description Here*

- Movie_File
	Filepath; *Description Here*

- Movie_Start_Frame
	Int; *Description Here*

- Overlay
	Bool t/f; *Description Here*

- Pause_Game_While_Playing
	Bool t/f; *Description Here*

- SFXEvent_Frame
	Ref, Int; *Description Here*

- SpeechEvent_Frame
	Ref, Int; *Description Here*

- Text_Crawl_Name
	Ref; *Description Here*

- Text_Crawl_Start_Frame
	Int; *Description Here*


EaW-Godot Port Connection
=========================
This file is imported into a thing
