.. _basegame-filetype-dat:

*********
DAT Files
*********


About
=====
DAT Files are used to store strings to display for in-game text. They are stored in *key, value* pairs, where the keys
are referenced by `XML Files <basegame-filetype-xml>`, and the value is the string to display in-game. This system
allows for most localization to be done through changing the used DAT file, as long as they contain the same keys.


EaW DAT Structure
=================
All file format information can be found at `Petrolution Mod Tools <https://modtools.petrolution.net/docs/Formats>`_, developed
by Mike Lancamp. The website also contains several utilities for handling Alamo Engine files, including a utility to
edit the text in an EaW .DAT file.


EaW-Godot Port Connection
=========================
An importer for Godot has not yet been created. While these files are necessary, the other visuals will be done first.
DAT files will probably be changed into a GNU gettext (.po) format. See `godot:doc_localization_using_gettext`



