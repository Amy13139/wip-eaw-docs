.. _xml_hardpoint:
.. Template to use for XML type documentation

HardPoint
===================================================


About
-----
Stores the individual parts of larger units. May or may not be targetable/destroyable. Most weapons in space are fired from hardpoints, with the notable exception of fighters and other small craft.


Structure
---------
- ``Top level node``

  - ``Node Type 1``; ``Attributes``
  - ``Node Type 2``; ``Attributes``; Optional
  - ``Node Type 3``; ``Attributes``
  - ``Node Type 5``; ``Attributes``; Optional

- ``Top level node variation 1``

  - ``Node Type 4``; ``Attributes``; Optional


``Top level node``
------------------
*Optional Description*: Having this top level node means that it is a top level node. No reason to add this if there are no variant top-level node types


``Node 1``
^^^^^^^^^^
- ``Subnode``:
	Type; Description

- ``Subnode 2``:
	Type; Description

- ``Subnode 3``:
	Type, Type, Type; Description

- ``Subnode 5``:
	Type | Type | Type; Description


``Node 2``
^^^^^^^^^^
- ``Subnode 6``:
	Type; Description


``Top level node variation 1``
------------------------------
*Description*: Having this top level node means that it is a different level node


``Node 1``
^^^^^^^^^^
- ``Subnode 4``:
	Type; Description


EaW-Godot Port Connection
=========================
This file is imported into a thing
