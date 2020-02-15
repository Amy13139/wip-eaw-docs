.. _xml_lightning_type_manager:
.. Template to use for XML type documentation

********************
LightningTypeManager
********************


About
=====
	*Palpatine may just go with plad lightning to mix up his style, ya'know? -luke13139*


Structure
=========
``Top level node``:

===============  ============== =========
Node Name        Attributes     Optional
===============  ============== =========
``UniqueUnit``   ``Name``       No
``Node Type 2``  ``Attributes`` Yes
``Node Type 3``  ``Attributes`` No
``Node Type 5``  ``Attributes`` Yes
===============  ============== =========

``Top level node variation 1``:

===============  ============== =========
Node Name        Attributes     Optional
===============  ============== =========
``Node Type 4``  ``Attributes`` No
===============  ============== =========


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
