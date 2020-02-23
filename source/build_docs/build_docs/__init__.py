from . import build_xml
from os import path, getcwd

# Doc Generation Script
# Variables
# Basic Paths
SOURCE_DIR: str = getcwd()
EAW_DATA_DIR: str = path.join(SOURCE_DIR, "data")
FOC_DATA_DIR: str = path.join(EAW_DATA_DIR, "corruption")
BASEGAME_DIR: str = path.join(SOURCE_DIR, "basegame")
# XML Paths
EAW_XML_DIR: str = path.join(EAW_DATA_DIR, "XML")
FOC_XML_DIR: str = path.join(FOC_DATA_DIR, "XML")
BASEGAME_XML_DIR: str = path.join(BASEGAME_DIR, "xml")


# Build docs
def build() -> None:
	"""
	Build the documentation by running the build() functions of submodules
	:return: None
	"""
	do_xml()


def do_xml() -> None:
	"""
	Runs the build() function of the XML Builder. Prints for start and end
	:return:
	"""
	print("Building XML Structure...")

	build_xml.xml_builder.build(
			EAW_XML_DIR,
			FOC_XML_DIR,
			BASEGAME_XML_DIR,
	)

	print("Done Building XML Structure")
