 .. _basegame-filetype-xml:

************************
XML Files - EaW/FoC Data
************************


.. _basegame-filetype-xml-about:

About
=====
XML files store large amounts of data for EaW. They contain most attributes of the game that are easily modded, such as unit information. The structure of XML is standardized, so please refer to the XML 1.0 Documentation for details about the format.


.. _basegame-filetype-xml-struct:

EaW XML Structure
=================


Special Files
-------------
EaW and FoC use XMLs to store large amounts of their data, but not all XMLs are loaded. The 2 XML files that are always loaded are ``megafiles.xml``, which specifies the .MEG files that the game should load, and ``Dataminerxmlfiles.xml``, which indicates all other XML files to load and the type of data the file contains. These files are both crucial for separating used and unused assets for the game. Both of these files and the different types of XML files that ``Dataminerxmlfiles.xml`` can indicate are listed below under the XML Type Reference.


Generic XML Files
-----------------
All EaW/FoC XML Files have all of their data contained within subnodes, which can be contained within nodes. Each
node has a type and a name; the name is used for internal reference and may be contained in "Ref" subnodes. Each subnode
holds a certain data type, which are listed in the next section.


Data Type Reference
-------------------
Some subnodes contain multiple items for their data. If this is the case, it will be represented with either comma separation or | separation, identical to the data in the subnode. Type specifications are concluded by a semi-colon. All suffixes are separated by a space unless otherwise noted.

.. csv-table::
	:header:Data Type Name, Description

	"Int", "A 32-bit integer. Limits and functional values of said integer should be in the description, if they exist."
	"File", "A filename, may have an incorrect extension due to how EaW was compiled."
	"Filepath", "A path to a file. Same as filename, but with a full path before it. Root of ``Data/``."
	"Dir", "A path to a directory. Root of ``Data/``."
	"String", "Only for attributes, indicates no special type for the attribute."
	"Bool", "A boolean value. Can be yes/no or true/false, t/f or y/n suffixes indicate which is used. Capitalization
	varies for the first letter of the boolean, and the suffix has the corresponding capitalization."
	"Ref", "A Reference to another node by its name. Description should indicate type of node this can reference"
	"Float", "A floating point number. Must have a decimal and tenths digit. Can be occasionally be substituted by an
	``Int``"
	"Floatf", "Same as a float, but the number has an ``f`` attached to the end of it."


.. _basegame-filetype-xml-toc:

XML Type Reference
==================
.. toctree::
	:titlesonly:
	:glob:

	xml/*
	xml/_auto/*
