.. _basegame-chunked-alo:

*********
ALO Files
*********


.. _basegame-chunked-alo-about:

About
=====
ALO Files (May stand for Alamo Object) are files that contain either a model or a particle object. These files are
mostly self-contained, with textures being the only external component needed for particles, and models requiring both
external textures and particles. However, many models will be split into multiple files, such as the Imperial Star
Destroyer, to allow for sections to be removed dynamically.


.. _basegame-chunked-alo-struct:

ALO Structures
==============
All file format information can be found at `Petrolution Mod Tools <https://modtools.petrolution.net/docs/Formats>`_, developed
by Mike Lancamp. The website also contains several utilities for handling Alamo Engine files, including some to both
view and edit ALO files.

.. warning::
	ALO Particle Files and ALO Model Files are under separate pages in Petrolution Mod Tools, but they both share the
	.ALO file extension. When processing ALO files, the type of object the ALO contains should not be assumed.

`Gaulker's Alamo Tools for Blender`_ is a utility to export ALO models and ALA files to and from Blender.


.. _basegame-chunked-alo-import:

EaW-Godot Port Connection
=========================


Models
------
A model importer has been written for the Godot Engine (based off of `Gaulker's Alamo Tools for Blender`_). It is
currently able to import all features from ALO models (more testing needed), except collision, which is created from
the mesh triangles instead of the collision-specific section of each mesh.

The importer saves a `PackedScene <godot:class_PackedScene>` (.scn) file. It has a `class_Skeleton` RootNode, with
`MeshInstances <class_MeshInstance>` as child nodes.


Particles
---------
Currently, a particle importer has been theorized, but many features needed are not supported in Godot 3. It is under
development, so it may be improved with the Godot 4 update, but a custom particle implementation may be necessary.


.. _Gaulker's Alamo Tools for Blender: https://focumentation.fandom.com/wiki/Alamo_Tools_for_Blender
