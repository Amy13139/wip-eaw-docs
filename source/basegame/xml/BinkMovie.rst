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
``Movies``:

===============  ==============
Node Name        Attributes
===============  ==============
``Movie``        ``Name``
===============  ==============


``Movies``
------------------
Stores ``Movie`` nodes only.


``Movie``
^^^^^^^^^^
- Attribute: ``Name``:
	ID to use for references to the node

- ``Movie_File``:
	Filepath; The path to the .BIK file for the movie

- ``Cannot_Skip``:
	Bool t/f; If true, the movie cannot be skipped by pressing any buttons.

- ``Subnode 5``:
	Type | Type | Type; Description


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
