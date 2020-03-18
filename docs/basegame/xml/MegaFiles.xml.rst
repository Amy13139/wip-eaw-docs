.. _basegame-xml-megafiles:

*************
MegaFiles.xml
*************


.. _basegame-xml-megafiles-about:

About
=====
Contains names of all `MEG File <basegame-meg>` archives for the game to load. One of 2 XML files loaded
by filename.

.. note::
	This file is located in the base Data directory (alongside the .MEG archives), **NOT** in the Data/XML
	folder.


.. _basegame-xml-megafiles-struct:

SubNode
=======
- File
	Filepath; A .MEG archive file, each archive's filenames are cached, allowing the game to load/reference assets by
	their location before they were archived.


.. _basegame-xml-megafiles-import:

EaW-Godot Port Connection
=========================
This will be loaded first, alongside :doc:`DataMinerXmlFiles.xml`. All file listed will be pushed through the import
process described in the `MEG File Documentation Page <basegame-meg>`
