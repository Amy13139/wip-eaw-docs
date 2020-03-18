.. _basegame-chunked:

*************
Chunked Files
*************


.. _basegame-chunked-about:

About
=====
Chunked files are files that use a binary "header" structure to organize and label their data. The knowledge that some
types of EaW/FoC files use this structure is useless for most people, but it allows much easier decoding and reverse
engineering of each of these files.


.. _basegame-chunked-struct:

Chunked File Structure
======================
.. note::
	All information on chunked files can be found at
	`Petrolution Mod Tools <https://modtools.petrolution.net/docs/ChunkFileFormat>`_, developed by Mike Lankamp.

.. warning::
	This section focuses on technical details for a binary format, and it assumes that the reader has at least a basic
	understanding of binary organization in computing.

.. glossary::

	Chunk
		A section of a Chunked File. A chunk is defined by an 8-byte :term:`Header` that directly precedes it in the
		file. Chunks can contain either other Chunks or :term:`Mini-Chunks`/Data, as determined by the :term:`Size`
		integer in the :term:`Header`.

	Header
		An 8-byte sections that directly precedes a chunk. Contains two sections, the :term:`ID` and :term:`Size`,
		both 4-byte (32 bit) unsigned integers.

	ID
		The first integer in the :term:`Header`, used to indicate the content of the chunk. The ID itself is only used
		to identify the type of chunk, and the ID is typically represented in hexadecimal format (since many IDs are
		multiples of 16). The ID is immediately followed by the :term:`Size` integer.

	Size
		The second 4-byte integer of the :term:`Header`, this number indicates the size, in bytes, of the chunk. The
		:term:`Header` is not included in the size. The size integer's 31st (most significant) bit is special: If it is
		set, the chunk contains other chunks. If it is not set, the chunk either contains :term:`Mini-Chunks` or data.
		Bit 31 should not be included when calculating the size of the chunk.

	Mini-Chunks
		Mini Chunks are smaller types of chunks, with the header being 2 bytes, and thus the ID and Size are a single
		byte each. Unlike normal :term:`Headers <Header>`, the most significant bit (Bit 7) in the :term:`Size` integer
		does **not** have any special meaning, and it should be included in the Mini-Chunk's size. There is no indicator
		for if a :term:`Chunk` contains Mini-Chunks or data.


.. graphviz::
	:name: basegame-chunked-struct-fig0
	:caption: A visual representation of Chunked Files' format; the dotted lines indicate conditional inclusion.


	digraph chunked_file {
		Chunk -> Header:main
		Chunk -> Contents:main

		Header [shape=record, label="<main> Header | {<id> ID | <size> Size}"]
		Contents [shape=record,
			label="<main> Contents | {<mini> Mini-Chunk(s) | <data> Raw Data} | <sub_chunk> Nested Chunk(s)"]

		Header:size -> Contents:sub_chunk [style=dotted]
		Header:size -> Contents:mini [style=dotted]

		Contents:sub_chunk:ne -> Chunk:e

		// Ranks
		R_Chunk [style=invis]; R_Header [style=invis]; R_Contents [style=invis];
		R_Chunk -> R_Header -> R_Contents [style=invis]
		{rank=same; R_Chunk; Chunk}
		{rank=same; R_Header; Header}
		{rank=same; R_Contents; Contents}
	}


Instances of Chunked Files
==========================
.. toctree::
	:titlesonly:
	:glob:
	:name: basegame-chunked-toc
	
	chunked_files/*


.. _basegame-chunked-import:

EaW-Godot Port Connection
=========================
A format of using a "match" statement in `GDScript <toc-learn-scripting-gdscript>`, with individual functions and/or
classes for handling each chunk, is used for all chunked-file imports currently supported. The import status of all file
types, including all chunked files, can be found on their documentation pages.
