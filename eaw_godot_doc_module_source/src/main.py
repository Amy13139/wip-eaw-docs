"""
Main script for build_docs module; contains high-level functions to build EaW/FoC Documentation
This should be compiled with Cython.
"""
from .build_xml_docs.xml_builder import build as xml_build
from xml_data import *
from os import path, getcwd, listdir, remove, rmdir
from time import thread_time as t_time

# Doc Generation Script
# Variables
# Basic Paths
SOURCE_DIR: str = getcwd()
BASEGAME_DIR: str = path.join(SOURCE_DIR, "basegame")
# XML Paths
BASEGAME_XML_DIR: str = path.join(BASEGAME_DIR, "xml")
BASEGAME_AUTO_XML_DIR: str = path.join(BASEGAME_XML_DIR, "_auto")


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

	if path.exists(BASEGAME_AUTO_XML_DIR):
		print("Clearing Old XML Docs...")
		clear_dir(BASEGAME_AUTO_XML_DIR)
		print("Done Clearing Old XML Docs\n")
	else:
		print("No Old XML Docs Found")

	# Log the time before building docs
	start_time = t_time()
	print("Building XML Docs...")

	xml_build(
		EAW_XML_DIR,
		FOC_XML_DIR,
		BASEGAME_AUTO_XML_DIR,
		get_type_template(),
		get_node_template(),
	)

	# Get the time elapsed
	end_time = t_time() - start_time
	print("Done Building XML Docs")
	print("Time Elapsed: {} Seconds\n".format(str(end_time)))


# Utility Functions
def clear_dir(dirpath: str) -> None:
	for item in listdir(dirpath):
		full_path: str = path.join(dirpath, item)
		if path.isfile(full_path):
			remove(full_path)
		elif path.isdir(full_path):
			clear_dir(full_path)
	rmdir(dirpath)
