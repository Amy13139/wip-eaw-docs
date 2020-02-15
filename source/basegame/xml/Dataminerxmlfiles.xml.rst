.. _xml_data_miner_xml_files:
.. Template to use for XML type documentation

*********************
Dataminerxmlfiles.xml
*********************


About
=====
This XML file is one of the 2 XML files loaded by filename, the other being ``megafiles.xml``. Unlike ``megafiles.xml``, this file is located in the Data/XML directory. This file contains the names of the other XML files for the program to load, and it contains their type.


Structure
=========
``GameXMLFiles``:

===============  ============================= =========
Node Name        Attributes                    Optional
===============  ============================= =========
``File``         ``filename, type, metafile``      No
===============  ============================= =========


``GameXMLFiles``
----------------


File
^^^^
The only node type within Dataminerxmlfiles.xml, it specifes a file and it's type of data.

- Attribute: filename
	File; The name of an XML file to load

- Attribute: type
	XmlType; Contains the type of the XML file, must be a value from the XML Reference Type section (other than the two unique files)

- Attribute: metafile
	Bool t/f; If true, the file will contain only references to other files to load. All files loaded inherit their type from this file's type. If false, the XML contains data.
