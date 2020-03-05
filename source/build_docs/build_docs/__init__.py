from . import build_xml
from os import path, getcwd, listdir, remove
from shutil import rmtree

# Doc Generation Script
# Variables
# Basic Paths
SOURCE_DIR: str = getcwd()
EAW_DATA_DIR: str = path.join(SOURCE_DIR, "basegame_data")
FOC_DATA_DIR: str = path.join(EAW_DATA_DIR, "corruption")
BASEGAME_DIR: str = path.join(SOURCE_DIR, "basegame")
# XML Paths
EAW_XML_DIR: str = path.join(EAW_DATA_DIR, "XML")
FOC_XML_DIR: str = path.join(FOC_DATA_DIR, "XML")
BASEGAME_XML_DIR: str = path.join(BASEGAME_DIR, "xml")
BASEGAME_AUTO_XML_DIR: str = path.join(BASEGAME_XML_DIR, "auto")


# Build docs
def build() -> None:
	"""
	Build the documentation by running the build functions of submodules
	:return: None
	"""
	do_xml()


# Build XML Function
def do_xml() -> None:
	"""
	Runs the build() function of the XML Builder. Also clears old build files.
	"""
	print("Clearing Old XML Docs...")

	clear_dir(BASEGAME_AUTO_XML_DIR)
	rmtree(BASEGAME_AUTO_XML_DIR)

	print("Done Clearing Old XML Docs\n")

	print("Building XML Structure...")

	build_xml.xml_builder.build(
			EAW_XML_DIR,
			FOC_XML_DIR,
			BASEGAME_AUTO_XML_DIR,
	)

	print("Done Building XML Structure\n")


# Utility Functions
def clear_dir(dirpath: str) -> None:
	for item in listdir(dirpath):
		full_path: str = path.join(dirpath, item)
		if path.isfile(full_path):
			remove(full_path)
		elif path.isdir(full_path):
			clear_dir(full_path)
