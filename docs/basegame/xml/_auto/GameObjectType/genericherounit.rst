##########################################
GenericHeroUnit
##########################################


About
*****
A Hero unit that is not specific to any faction.


Structure
*********
``GenericHeroUnit``
-------------------
A Hero unit that is not specific to any faction.

.. csv-table::
	:header: "Nested Nodes", "Description"

	"``Abilities``", "Nested Node for units, contains either an activated ability or some form of special behavior for a unit. See `Unit Abilities on Petrolution <modtools.petrolution.net/docs/Unit_Abilities_EaW>`_ for a list of EaW active abilities. FoC is currently not included, but a page may be added to this documentation"


``Abilities``
^^^^^^^^^^^^^
Nested Node for units, contains either an activated ability or some form of special behavior for a unit. See `Unit Abilities on Petrolution <modtools.petrolution.net/docs/Unit_Abilities_EaW>`_ for a list of EaW active abilities. FoC is currently not included, but a page may be added to this documentation

.. csv-table::
	:header: "Nested Nodes", "Description"

	"``Galactic_Stealth_Ability``", "Nested Node for Abilities in GC; allows a unit to move into enemy-occupied space without starting combat, also dictates how much information the unit reveals with it's presence."
	"``System_Spy_Ability``", "Not yet documented, but you help document it through GitHub!"


``Galactic_Stealth_Ability``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Nested Node for Abilities in GC; allows a unit to move into enemy-occupied space without starting combat, also dictates how much information the unit reveals with it's presence.

``Galactic_Stealth_Ability``'s SubNodes
"""""""""""""""""""""""""""""""""""""""
- Evade_Detection_Chance
	Float; Not yet documented, but you help document it through GitHub!




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


- See_Base_Levels
	Bool; Not yet documented, but you help document it through GitHub!


- See_Credit_Income
	Bool; Not yet documented, but you help document it through GitHub!


- See_Credit_Income_Breakdown
	Bool; Not yet documented, but you help document it through GitHub!


- See_Current_Production
	Bool; Not yet documented, but you help document it through GitHub!


- See_Fleet_Contents
	Bool; Not yet documented, but you help document it through GitHub!


- See_Ground_Company_Contents
	Bool; Not yet documented, but you help document it through GitHub!


- See_Major_Stealth_Heroes
	Bool; Not yet documented, but you help document it through GitHub!


- See_Minor_Stealth_Heroes
	Bool; Not yet documented, but you help document it through GitHub!


- See_Num_Fleets
	Bool; Not yet documented, but you help document it through GitHub!


- See_Num_Ground_Companies
	Bool; Not yet documented, but you help document it through GitHub!


- See_Political_Control
	Bool; Not yet documented, but you help document it through GitHub!


- See_Political_Control_Breakdown
	Bool; Not yet documented, but you help document it through GitHub!


- See_Special_Structures
	Bool; Not yet documented, but you help document it through GitHub!





SubNodes
^^^^^^^^
- Affiliation
	Ref; Not yet documented, but you help document it through GitHub!


- Always_Spawn_In_Orbit
	Bool; Not yet documented, but you help document it through GitHub!


- Attach_To_Flagship_During_Space_Battle
	Bool; Not yet documented, but you help document it through GitHub!


- Autoresolve_Health
	Int; Not yet documented, but you help document it through GitHub!


- Can_Be_Neutralized_By_Major_Heroes
	Bool; Not yet documented, but you help document it through GitHub!


- Can_Be_Neutralized_By_Minor_Heroes
	Bool; Not yet documented, but you help document it through GitHub!


- Can_Hyperspace_Without_Activating_Ability
	Bool; Not yet documented, but you help document it through GitHub!


- CategoryMask
	Ref; Not yet documented, but you help document it through GitHub!


- Encyclopedia_Text
	Ref; Not yet documented, but you help document it through GitHub!


- Encyclopedia_Unit_Class
	Ref; Not yet documented, but you help document it through GitHub!


- GUI_Row
	Int; Not yet documented, but you help document it through GitHub!


- Icon_Name
	File; The name of the icon displayed during gameplay, may reference a file stored in an :ref:`MTD File <basegame-filetype-mtd>`.


- Is_Generic_Hero
	Bool; Not yet documented, but you help document it through GitHub!


- Is_Sprite
	Bool; Not yet documented, but you help document it through GitHub!


- Mass
	Float; Not yet documented, but you help document it through GitHub!


- Neutralization_Cost
	Float; Not yet documented, but you help document it through GitHub!


- Political_Control
	Int; Not yet documented, but you help document it through GitHub!


- Ranking_In_Category
	Int; Not yet documented, but you help document it through GitHub!


- Scale_Factor
	Float; Not yet documented, but you help document it through GitHub!


- SFXEvent_Fleet_Move
	Ref; Not yet documented, but you help document it through GitHub!


- SFXEvent_Move
	Ref; Not yet documented, but you help document it through GitHub!


- Size_Value
	Int; Not yet documented, but you help document it through GitHub!


- Stay_In_Transport_During_Ground_Battle
	Bool; Not yet documented, but you help document it through GitHub!


- Text_ID
	Ref; The ID of the text to insert for the name of this object in-game. Text is stored in a `DAT File <basegame-filetype-dat>`.


- Type
	Ref; Not yet documented, but you help document it through GitHub!







EaW-Godot Port Connection
*************************
Not yet documented, but you help document it through GitHub!

