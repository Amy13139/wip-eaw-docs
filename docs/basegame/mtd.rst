.. _basegame-mtd:

***********************************
Mega-Texture Directory (.MTD) Files
***********************************


.. _basegame-mtd-about:

About
=====
MTD Files (Mega-Texture Directory) are used to store multiple textures in a single texture file. MTD files must be
coupled with a texture file, which should share it's filename (other than the file extension). Unlike most other
textures in EaW, MTD files do not use a DDS file for their texture storage, instead using a TGA texture. MTD files
contain the texture name and box-boundary coordinates for it's pair image, with each name corresponding to the section
of the file within the box.


.. _basegame-mtd-struct:

MTD Structure
=============
All file format information can be found at `Petrolution Mod Tools <https://modtools.petrolution.net/docs/Formats>`_, developed
by Mike Lankamp. The website also contains several utilities for handling Alamo Engine files and a tool for extracting
and browsing MTD textures.


.. _basegame-mtd-import:

EaW-Godot Port Connection
=========================
An importer has been written to create a `class_LargeTexture` resource from an MTD and an identically named
texture. It needs more testing, and the names are currently not preserved in an easily accessible way. It will most
likely be converted to create multiple `class_AtlasTexture` resources instead of a single
`class_LargeTexture`.
