.. _data-structures:
.. Data structure documentation

***************
Data Structures
***************

About
=====
The data structures of the EaW-Godot Port were designed with a few major design goals:

- Store the data from Empire at War in a usable format
- Maintain a logical, hierarchical organization structure
- Have the end result be easily human-readable
- Have the data be optimized for gameplay

To this end, all data structures are sub-classes off Godot's ``Resource`` class. This allows easy edits with the engine through use of the ``export`` keyword, which puts a variable into the inspector GUI for the resource. It also keeps all data contained to Godot, allowing edits to any aspect of the game and removing the potential issues of supporting an editor alongside the port.


``export``'s Limitations
------------------------
.. note::
	This section was written during development of Godot 4.0, they may have improved the export system by the release of the 4.0 update.

Currently, the ``export`` keyword has limited functionality in specifying custom resource sub-classes and adding tooltips. This means that it lacks support for a hierarchical structure and documentation on all values cannot be easily viewed in-editor. This is a requested feature, so it may be completed by the release of the Eaw-Godot Port.


Data Hierarchy Information
--------------------------


EaW's Flaws
^^^^^^^^^^^
The hierarchical data structures used were implemented to solve the many problems with EaW's XML files. Each individual unit is bloated with massive amounts of data that should have been implemented as an override to a default, or moved to a separate file altogether. Even with the variant system EaW has in place, huge chunks of XML files need to be copy-pasted over to the variants.

The best example of copy-paste bloat is Chewbacca. Chewbacca has no issues on his own, but his ability to capture enemy vehicles created several. The solution was to create a clone of every single unit Chewbacca could capture, and change the unit when it was captured. This lead to every single imperial vehicle having a Chewbacca clone, which would need to have edits copy-pasted over to it from the original vehicle.

.. Todo, move some of this to UnitData when done

EaW-Godot's Solution
^^^^^^^^^^^^^^^^^^^^
The data structure of the EaW-Godot Port had to both copy the features from EaW and improve on their organization, so a philosophy of independent functionality was adopted. This has forced the complete re-organization of EaW XML data, but it makes the data much more accessible and completely self-contained. For example, the faction affiliation, build cost, and bribery cost are stored in each EaW unit individually. In the EaW-Godot Port, the faction affiliation is dynamic, the build cost is stored in gamemode data, and the bribery cost of the unit is stored in the Consortium's faction files by class, with overrides for specific units. This makes any individual unit have the same tactical capabilities, regardless of the context the unit is used in. It also moves data not related to tactical combat over to the location required for preserving this independent functionality. For tactical changes, a unit variation can be used or a combat modifier can be added.

To prevent the need to copy-paste massive amounts of information that is still located on any resources, a hierarchy of sub-resources are used. Since they are all Godot resources, they can be saved to a file if needed by more than 1 parent resource, allowing edits to transfer to all parents. If they are not used by more than 1 parent, they can be build-in to their parent class, significantly reducing file bloat.


Technical Design
================


The "Compile" Process
---------------------
The data for each structure is unoptimized by itself, due to it's accessibility. This is offset by each resource's ``compile`` function, which outputs all data of the resource into a ``Dictionary``. This function is how the game loads all of it's custom resources initially. Each resource calls the function on all of it's sub-resources as well, concatenating the entire hierarchy into a single dictionary, which can be cheaply stored by the game. This does mean that all external file dependencies (short of other custom resource types) are stored as file paths, allowing the game to load them on demand.