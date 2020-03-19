.. _basegame-meg:

***********************
Mega-Files (.MEG) Files
***********************


.. _basegame-meg-about:

About
=====
MEG files (Mega-Files) are a uncompressed file archives. They store files by name. Most assets of the basegame are stored
in MEG files. The game loads MEG files based off of the `megafiles.xml <basegame-xml-megafiles>` file, which is located
in the game's data folder at it's root, **not** in the game's XML directory.


.. _basegame-meg-stuct:

MEG Structure
=============
All file format information can be found at `Petrolution Mod Tools <https://modtools.petrolution.net/docs/Formats>`_, developed
by Mike Lankamp. The website also contains several utilities for handling Alamo Engine files and a tool for extracting
MEG archives.


.. _basegame-meg-import:

EaW-Godot Port Connection
=========================
While these files do not currently have an extraction script written in GDScript, a Python script has been written to
extract MEG files. Due to the uncompressed storage, extraction is simple, only needing to write a chunk of data to a
file of a given name.
