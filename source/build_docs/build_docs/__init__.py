from . import xml_build
from os import path, getcwd
# Doc Generation Script
# Variables
eaw_data_dir = path.join(getcwd(), "data")
foc_data_dir = path.join(eaw_data_dir, "corruption")
basegame_data_dir = path.join(getcwd(), "basegame")
xml_data_dir = path.join(basegame_data_dir, "xml")


# Build docs
def build():
	build_xml_structure()


def build_xml_structure():
	print("Building XML Structure...")
	xml_build.build_xml_structure(
		path.join(eaw_data_dir, "XML"),
		path.join(foc_data_dir, "XML"),
		path.join(xml_data_dir, "xml_structure.rst")
	)
	print("Done Building XML Structure")
