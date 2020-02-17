.. _xml:
.. Introduction/Readme for XML file section of the documentation

************************
XML Files - EaW/FoC Data
************************


About
=====
XML files store large amounts of data for EaW. They contain most attributes of the game that are easily modded, such as unit information. The structure of XML is standardized, so please refer to the XML 1.0 Documentation for details about the format.


EaW XML Structure
=================


Special Files
-------------
EaW uses XMLs to store large amounts of their data, but not all XMLs are loaded. The 2 XML files that are always loaded are ``megafiles.xml``, which specifies the .MEG files that the game should load, and ``Dataminerxmlfiles.xml``, which indicates all other XML files to load and the type of data the file contains. These files are both crucial for separating used and unused assets for the game. Both of these files and the different types of XML files that ``Dataminerxmlfiles.xml`` can indicate are listed below under the XML Type Reference.


Generic XML Files
-----------------
The type of an XML file determines what nodes it can contain and how it's content is used. The type is specified by ``Dataminerxmlfiles.xml``. Each XML file has a top-level node, which may indicate a subset of the type. The top-level node can contain any number of nodes beneath it, which can each have any number of subnodes (up to the maximum amount of subnodes definable for a node). Each subnode will have a data type specified, as they cannot contain any form of node, and will usually only take a single line. Each node will have a ``name`` attribute. ::

    Example: ``SpaceUnitsCapital`` is a top-level node for a ``GameObjectType``, indicating the file contains capital ship space units.

Unless otherwise stated, XML files for EaW use PascalCase for their name. Each node will have all possible attributes and sub-nodes listed. The type of content for each node is listed, and the Type Reference is located below. Each type can contain a suffix, which indicates a specific condition that the data must meet. Suffixes can be separated by space, in some instances. Sometimes, items are given unique suffixes. Check the description if the suffix for a data type is not listed in the reference.

Attributes to nodes are always strings, so an attribute of type ``Bool t/f`` would be either ``"true"`` or ``"false"``


Data Type Reference
-------------------
Some subnodes contain multiple items for their data. If this is the case, it will be represented with either comma separation or | separation, identical to the data in the subnode. Type specifications are concluded by a semi-colon. All suffixes are separated by a space unless otherwise noted.

=============== =================================================================================
Data Type Name  Description
=============== =================================================================================
Int             A 32-bit integer
String          Characters, cushioned by quotation marks
Bool            A boolean value.
Ref \*          A Reference to a node, by name. No quotation marks
Float           A floating point number. Must have a decimal and tenths digit
Floatf          Same as a float, but the number has an "``f``" attached to the end of it.
=============== =================================================================================

.. note::
	# indicates a number; \* indicates any value, but a condition may be provided in the description or as a suffix.

====================== ======================== ================================================================================================
Suffix                 Applicable To            Description
====================== ======================== ================================================================================================
[#,#]                  Int, Float, Floatf       Numerical value must within the range of the two numbers. Inclusive.
<#, >#, <=#, >=#,      Int, Float, Floatf       Numerical value must satisfy the conditional operator.
File                   String                   String is a filename
Filepath               String                   String is a path to a file. Should starts with Data\\.
Dirpath                String                   String is a path to a directory. Should starts with Data\\.
t/f                    Bool                     Boolean is ``true`` or ``false``. Capitalization may vary, and it carries from the suffix.
Y/N                    Bool                     Boolean is ``Yes`` or ``No``. Capitalization may vary, and it carries from the suffix.
\*                     Ref                      Name of a node type. Shows the type of node that the subnode can reference
====================== ======================== ================================================================================================


XML Type Reference
==================
.. toctree::
	:titlesonly:
	:glob:

	All XML File Structures <xml/xml_structure>
	xml/megafiles.xml
	xml/Dataminerxmlfiles.xml
	xml/*
