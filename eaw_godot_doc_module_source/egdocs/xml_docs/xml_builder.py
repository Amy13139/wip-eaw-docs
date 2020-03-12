"""
Contains functions to parse all elements from the EaW and FoC XML files and organize them for documentation
"""
from typing import Dict, List
import os
import os.path
from .rst_utils import *
from .xml_data import *
from .xml_inserts import *
from .xml_classes import XMLType, Node


def build_docs(xml_dir_out: str, xml_types: List[XMLType]) -> None:
	"""
	Takes a list of XMLTypes and uses them to build the XML Documentation
	:param xml_dir_out: The output directory, should also be the XML Docs directory
	:param xml_types: The list of XML Types to use for building the documentation
	"""

	# Write Functions
	def write_node_file(node: Node) -> None:
		"""
		Write a doc file for a Node
		:param node: The Node to get information from
		"""
		# Get node file name
		node_path = os.path.join(dir_path, "{}.rst".format(node.name.lower()))

		# Copy template
		node_file_lines: List[str] = TEMPLATES["node"].copy()
		# Create inserts dict
		node_file_inserts: Dict[str, str] = {
			# Name
			"name": node.name,
			# Typename
			"typename": xml_type.name,
			# About/Description
			"about": node.get_description(),
			# Structure, to be filled in later
			"struct": repr(node),
			# Context
			"import": node.get_context(),
		}

		# Add insert variants
		node_file_inserts.update(get_insert_variants(node_file_inserts))

		# Iterate over template, format with created inserts dictionary
		for index in range(len(node_file_lines)):
			if "{" in node_file_lines[index] and "}" in node_file_lines[index]:
				node_file_lines[index] = node_file_lines[index].format(**node_file_inserts)

		# Write to file
		with open(node_path, "wt") as node_file:
			node_file.writelines(node_file_lines)
			node_file.close()

	def get_insert_variants(insert_dict: Dict[str, str]) -> Dict[str, str]:
		"""
		Creates variants from the given string dictionary, each stored in an <base_key>_<suffix_name> key
		Currently supported suffixes are _lower, _upper, _title, _capital
		:param insert_dict: The dictionary to create variants from
		:return: A dictionary of variants, should be added to the original input dictionary
		"""
		variant_dict: Dict[str, str] = {}
		# Add variants for each key
		for key in insert_dict.keys():
			# lowercase
			variant_dict[key + "_lower"] = insert_dict[key].lower()
			# UPPERCASE
			variant_dict[key + "_upper"] = insert_dict[key].upper()
			# Title
			variant_dict[key + "_title"] = insert_dict[key].title()
			# Capital
			variant_dict[key + "_capital"] = insert_dict[key].capitalize()

		# Return
		return variant_dict
	
	# Build XML Docs
	# Iterate over XML Types; Writing XML Files and Node Files
	for xml_type in xml_types:
		# Get path to main file
		file_path = os.path.join(xml_dir_out, "{}.rst".format(xml_type.name.lower()))
		dir_path = os.path.join(xml_dir_out, xml_type.name)

		# Create inserts dict
		inserts: Dict[str, str] = {
			# Name
			"name": xml_type.name,
			# Description/About
			"about": get_type_description(xml_type.name),
			# Context/Import Info
			"import": get_type_context(xml_type.name),
		}

		# Check if type has nodes
		if len(xml_type.node_names):
			# Create Subdirectory
			if not os.path.exists(dir_path):
				os.makedirs(dir_path)

			# Copy template
			type_file_lines: List[str] = TEMPLATES["type"].copy()

			# Node Names
			node_names_str: str = ""
			for node_name in xml_type.node_names:
				# Add the name to the name strings
				node_names_str += "- {}\n".format(node_name)
			inserts["node_list"] = node_names_str

		# No nodes are present
		else:
			type_file_lines: List[str] = TEMPLATES["type_no_node"].copy()

		# SubNodes
		subnode_line: str = ""
		for subnode in xml_type.get_subnodes():
			subnode_line += repr(subnode)
		if subnode_line == "":
			subnode_line = "No Direct SubNodes in this XML type"
		inserts["subnode_list"] = subnode_line

		# Add insert variants
		inserts.update(get_insert_variants(inserts))

		# Iterate over lines, format as needed
		for i in range(len(type_file_lines)):
			if "{" in type_file_lines[i] and "}" in type_file_lines[i]:
				type_file_lines[i] = type_file_lines[i].format(**inserts)
		# Write the formatted template to file
		with open(file_path, "wt") as main_file:
			main_file.writelines(type_file_lines)
			main_file.close()

		# Iterate over Nodes in the XMLType, write a file for each
		for curr_node in xml_type.get_nodes():
			write_node_file(curr_node)


def build(build_dir: str) -> None:
	"""
	Function to build XML Documentation by iterating over both EaW and FoC XML Files.
	:param build_dir: The path to build the documentation in.
	"""

	# Setup type list
	xml_type_list: List[XMLType] = []

	# Parse data files
	eaw_data_xml: xml.etree.ElementTree.Element = get_xml_file(EAW_XML_DIR + "Dataminerxmlfiles.Xml")
	foc_data_xml: xml.etree.ElementTree.Element = get_xml_file(FOC_XML_DIR + "Dataminerxmlfiles.Xml")
	item: xml.etree.ElementTree.Element

	# Iterate over the data files
	for data_file in (eaw_data_xml, foc_data_xml):
		for item in data_file:
			if item.tag == "File":
				filename: str = item.get("filename").strip().title()
				# Get filename
				if data_file == eaw_data_xml:
					file = EAW_XML_DIR + filename
				else:
					file = FOC_XML_DIR + filename

				# Get type
				xml_type_str: str = item.get("type").strip()

				# Setup iteration
				prev_type: XMLType
				new: bool = True

				# Iterate over current types
				for prev_type in xml_type_list:
					# Check if names match
					if xml_type_str == prev_type.name:
						# If names match, add to existing
						new = False
						prev_type.add_rootnode(file)
						break
				# If not added earlier, add as new XMLType
				if new:
					# Add to type list
					current_type = XMLType(xml_type_str)
					current_type.add_rootnode(file)
					xml_type_list.append(current_type)
	# Cleanup, delete some variables
	del data_file, current_type, file

	# Parse files
	for xtype in xml_type_list:
		xtype.parse_subfiles()

	# Build XML Docs
	build_docs(build_dir, xml_type_list)
