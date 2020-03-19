.. _readme:

EaW-FoC Documentation
====================================


.. _readme-about:

About
-----


Abbreviations
^^^^^^^^^^^^^
This documentation and other EaW-Godot Port Project materials use abbreviations for common terms. They meaning of these
abbreviations are listed below.

- EaW : *Star Wars® Empire at War™*
- FoC : *Star Wars® Empire at War™: Forces of Corruption™*


Background
^^^^^^^^^^
The EaW-FoC Documentation is an attempt to document the data formats of the game *Star Wars® Empire at War™*, as well
as its expansion *Star Wars® Empire at War™: Forces of Corruption™*. Both the game and its expansion were developed by
`Petroglyph Games <http://www.petroglyphgames.com/>`_. EaW and FoC were developed with the Alamo Game Engine, and both
the game and the expansion were released in 2006. Since its release, FoC has become the standard for the game, with most
online retailers not distributing EaW and FoC separately. The game has received few updates, but it did receive a few
surprise updates in 2018 that fixed some game-breaking bugs.

`Star Wars®: Empire at War™ Gold Pack on Steam <https://store.steampowered.com/app/32470>`_

Throughout the years since the game's release, it has become the center of a dedicated and active modding community,
with many modding teams providing consistent support and development for their mod(s). Despite the impressive modding
scene, there does not seem to be any comprehensive documentation for the data formats of the game, with several
documentation/tutorial attempts being abandoned before completion.


EaW-FoC Documentation
^^^^^^^^^^^^^^^^^^^^^

The EaW-FoC Section of this documentation is built to collect all known information about the custom data structures and
file types used by the game. This can greatly help development of projects that need to convert data to or from an EaW
format.

This documentation includes information about how this data is treated by the
`EaW-Godot Port <https://github.com/luke13139/eaw-godot-importer>`_, an attempt to create a method to convert the data
types in this documentation into a format usable by the `Godot Engine <https://godotengine.org/>`_, which is the
effective equivalent of porting the game to modern hardware without needing to create an entirely new game, which would
force modders to re-create their work, would not be able to properly replicate the old game, and would violate the
rights of both the developers and the owner of *Star Wars®* by redistributing an imitation of their game.


.. _readme-basegame:

EaW/FoC File Types
------------------
This section contains links to all created documentation on every file type used by EaW for data/asset storage.
The documentation for these files are unofficial, and they are separated by file type. Please report any errors or
proposed additions to the `Documentation's GitHub <https://github.com/luke13139/wip-eaw-docs>`_.

.. note::
	Information on ALA, ALO, DAT, LUA, MEG, MTD, and Chunked Files was obtained from
	`Petrolution Mod Tools`_, a website developed by Mike Lankamp. The website contains several utilities for working
	with EaW/FoC file types, and it contains documentation on the binary format of each file. The source code for the
	utility programs was release on `GitHub <https://github.com>`_ in 2017.

	`GlyphXTools On GitHub <https://github.com/GlyphXTools>`_

- `ALA <basegame-chunked-ala>`
	Animations for ALO Models. Instance of `Chunked Files`_.

	`ALA Docs <basegame-chunked-ala>`

- `ALO <basegame-chunked-alo>`
	Models and Particles. Instance of `Chunked Files`_.

	`ALO Docs <basegame-chunked-alo>`

- `BIK <basegame-bik>`
	Bink Movie: Compressed Audio/Video

	`BIK Docs <basegame-bik>`

- `DAT <basegame-dat>`
	In-Game Text, allows for internationalization

	`DAT Docs <basegame-dat>`

- DDS
	Texture

	`Microsoft DDS Documentation <https://docs.microsoft.com/windows/win32/direct3ddds/dx-graphics-dds>`_

- FXO
	Compiled Direct3D 9 Shader. Petroglyph released the source code for the FoC shaders in 2017.

	`Microsoft ASM Reference <https://docs.microsoft.com/windows/win32/direct3dhlsl/dx9-graphics-reference-asm>`_

	`FOC Shader Source Code <http://www.petroglyphgames.com/eawmodtool/>`_

- H
	C++ Header

	`Microsoft C++ Header Documentation <https://docs.microsoft.com/cpp/cpp/header-files-cpp>`_

- LUA
	Petroglyph-Lua Object File: Full documentation of differences from base Lua 5.0 Object File is located at
	`Petrolution Mod Tools`_, but it will be added to this documentation later.

	`Lua Documentation <https://www.lua.org/docs.html>`_

- `MEG <basegame-meg>`
	Mega-File: Uncompressed File Archive.

	`MEG Docs <basegame-meg>`

- MP3
	Audio

	`MP3 on Wikipedia <https://wikipedia.org/wiki/MP3>`_

- `MTD <basegame-mtd>`
	Mega-Texture Directory: Packed Texture Index for a TGA.

	`MTD Docs <basegame-mtd>`

- RC
	C++ Resource Script

	`Microsoft Resource File Reference <https://docs.microsoft.com/cpp/windows/resource-files-visual-studio>`_

- TEC
	In-Game Cinematic: Unknown format. They appear to be instances of `Chunked Files`_.

- TED
	Game Map: Unknown format. They appear to be instances of `Chunked Files`_.

- TEE
	Environment Set: Unknown format. They appear to be instances of `Chunked Files`_.

- TEM
	Material Set: Unknown format. They appear to be instances of `Chunked Files`_.

- TGA
	Uncompressed Texture

	`TGA Verison 2.0 Specification <https://www.dca.fee.unicamp.br/~martino/disciplinas/ea978/tgaffs.pdf>`_

- TXT
	Text List and Dialogue Event Chains. Text Lists are newline separated.

- WAV
	Audio

	`Microsoft Waveform Audio Reference <https://docs.microsoft.com/windows/win32/multimedia/waveform-audio-reference>`_

- `XML <basegame-xml>`
	Generic Data Storage, including unit data, game settings, and creation of references for other files

.. _Chunked Files: `<basegame-chunked>`

.. _Petrolution Mod Tools: `<https://modtools.petrolution.net>`

.. Sidebar Tables of Contents

.. toctree::
	:titlesonly:
	:caption: About
	:name: about-toc
	:hidden:

	self

.. toctree::
	:titlesonly:
	:caption: EaW-Godot Port Documentation
	:name: port-toc
	:hidden:
	:glob:

	port/*


.. toctree::
	:titlesonly:
	:caption: EaW/FoC Filetype Documentation
	:name: basegame-toc
	:hidden:
	:glob:

	basegame/*


