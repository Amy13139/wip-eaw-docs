.. _xml_file:
.. Introduction/Readme for XML file section of the documentation

XML Files - EaW/FoC Data
========================


About
-----


XML files store large amounts of data for EaW. They contain most attributes of the game that are easily modded, such as unit information. The structure of XML is standardized, so please refer to the XML 1.0 Documentation for details about the format.


EaW XML Structure
-----------------


Special Files
^^^^^^^^^^^^^


EaW uses XMLs to store large amounts of their data, but not all XMLs are loaded. The 2 XML files that are always loaded are **megafiles.xml**, which specifies the .MEG files that the game should load, and **Dataminerxmlfiles.xml**, which indicates all other XML files to load and the type of data the file contains. These files are both crucial for separating used and unused assets for the game. Both of these files and the different types of XML files that **Dataminerxmlfiles.xml** can indicate are listed below under the XML Type Reference.


Generic XML Files
^^^^^^^^^^^^^^^^^


The type of an XML file determines what nodes it can contain and how it's content is used. The type is specified by **Dataminerxmlfiles.xml**. Each XML file has a top-level node, which may indicate a subset of the type. The top-level node can contain any number of nodes beneath it, which can each have any number of subnodes (up to the maximum amount of subnodes definable for a node). Each subnode will have a data type specified, as they cannot contain any form of node, and will usually only take a single line.

    Ex: *SpaceUnitsCapital* is a top-level node for a *GameObjectType*, indicating the file contains capital ship space units.

Unless otherwise stated, XML files for EaW use PascalCase for their name. Each node will have all possible attributes and sub-nodes listed. The type of content for each node is listed, and the Type Reference is located below. Each type can contain a suffix, which indicates a specific condition that the data must meet. Suffixes can be separated by space, in some instances.

Attributes to nodes are always strings, so an attribute of type "Bool t/f" would be wither "true" or "false"


Type Reference
^^^^^^^^^^^^^^


- Int; A 32-bit integer

  - [0,#]; Range that the integer can legally be in, inclusive
  - >#, <#, <=#, etc; Conditions that the integer must meet

- String; A string of characters, cushioned by quotation marks
- Bool \*/\*; A boolean value, the first asterisk is the indicator for true, the second asterisk is the indicator for false. Common combinations listed below.

  - t/f; true or false
  - T/F; True or False
  - y/n; yes or no
  - Y/N; Yes or No


XML Type Reference
^^^^^^^^^^^^^^^^^^


- megafiles.xml
- Dataminerxmlfiles.xml
- GameObjectType
- HeroClashType
- SFXEvent
- TerrainDecalFX
- LightningTypeManager
- DynamicTrackFX
- MusicEvent
- SpeechEvent
- GameConstants
- CommandBarComponent
- TradeRoute
- TradeRouteLines
- RadarMap
- Draw3DTextCrawl
- WeatherPattern
- HardPoint
- Campaign
- Faction
- TacticalCameraConstants
- LightSource
- BinkMovie
- TargetingPrioritySet
- DifficultyAdjustment
- WeatherAudioManager
