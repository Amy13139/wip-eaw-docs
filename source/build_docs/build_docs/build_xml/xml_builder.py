# This script gets all of the elements from the EaW and FoC XML files and organizes them for documentation
from xml.etree import ElementTree as ET
from os import listdir, path, getcwd
from .xml_classes import *

# Keys are values that are considered booleans, values are suffixes for the type. Capitalization must be lowercase.
VALID_BOOL: dict = {
		"yes": "y/n",
		"no": "y/n",
		"true": "t/f",
		"false": "t/f",
}

# Descriptions for subnodes/attributes. Attribute prefix is "attribute - ". Capitalization must be lowercase for keys.
DESCRIPTORS: dict = {
		"attribute - name": "The name of the node, can be referenced by other nodes",
		"attribute - description": "An optional description for the node, only used to help anyone reading the XML.",
		"text_id": "The in-game name of this unit, references a .DAT file to allow from translations",
		"mass": "Varies between 0 and 1, usually very close to 1. Probably unused.",
		"file": "A file to load, context of loading is based on the root node.",
}

# Default EaW and FoC XML Directories, used when the program is run
DEFAULT_XML_DIR_EAW: str = path.join(getcwd(), "data", "XML")
DEFAULT_XML_DIR_FOC: str = path.join(getcwd(), "data", "corruption", "XML")
DEFAULT_OUTPUT_FILE: str = path.join(getcwd(), "basegame", "xml", "xml_structure.rst")

# Tab character
TAB: str = "\t"
# Used at the end of the line to indicate it has tabbed children, must have a newline at the end to function properly
TAB_INDICATOR: str = "\n"
# Number of "=" signs used for the rows on the Sphinx table.
NUM_TABLE_INDICATORS: int = 65


def build_xml_files() -> None:
	pass


def build(
		xml_dir_eaw: str = DEFAULT_XML_DIR_EAW,
		xml_dir_foc: str = DEFAULT_XML_DIR_FOC,
		xml_dir_out: str = DEFAULT_OUTPUT_FILE,
) -> None:
	"""
	Function to iterate over EaW and FoC XML Files, given both of their XML directories.

	:param xml_dir_eaw: The absolute path to the EaW XML Directory.
	:param xml_dir_foc: The absolute path to the FoC XML Directory.
	:param xml_dir_out: The absolute path to the Documentation directory for XML Files.

	:returns: None, writes to an output file.
	"""

	def get_xml_tree() -> dict:
		"""
		Gets a tree of EaW XML Data structure.

		:rtype: dict
		:return: XML Tree Dictionary
		"""

		def parse_xml_dir(xml_dir: str) -> dict:
			"""
			Iterates over a single directory of XML Files, fails if directory contains a file that is not an XML or TXT.

			:param xml_dir: The absolute path to the directory to parse.

			:returns: {top_level_node: {node: {subnode: type, ...}, ...}, ...}
			"""

			def parse_xml(xml_filepath: str) -> dict:
				"""Gives the nodes in the top-level node, and the sub-nodes for each node

				:param xml_filepath: The absolute path to the XML file to parse.

				:returns: Dictionary of {top_level_node: {node: {subnode: type, ...}, ...}}
				"""

				# Setup XML tree, get root element
				xml_file_tree: dict = {}
				sub_files: list = []

				# Protect against invalid XML files, as even the base game has invalid files
				try:
					root: xml.etree.ElementTree.Element = ET.parse(xml_filepath).getroot()
				except ET.ParseError:
					print("Error: '{}' could not be parsed, may be an invalid file".format(xml_filepath))
					return {}
				# Get top_level_node
				top_level_node: xml.etree.ElementTree.Element = root.tag

				# Iterate over nodes
				node: xml.etree.ElementTree.Element
				for node in root:
					# Check if this is actually a node, or if the file only has subnodes
					if len(node):
						# Add node to XML tree, if not already added
						if node.tag not in xml_file_tree:
							xml_file_tree[node.tag] = {}

						# Add attributes as subnodes, keeps organization easy
						for key in node.keys():
							attrib_name = "AAA_Attribute - " + key
							if attrib_name not in xml_file_tree[node.tag]:
								# Set Attribute type as value
								attrib_type = get_type(node.attrib[key])
								# If type cannot be determine, use "String" Instead
								if attrib_type != "Ref" and attrib_type != "None":
									xml_file_tree[node.tag][attrib_name] = attrib_type
								else:
									xml_file_tree[node.tag][attrib_name] = "String"

						# Iterate over subnodes
						subnode: xml.etree.ElementTree.Element
						for subnode in node:
							# Get subnode type
							subnode_type = get_type(subnode.text)

							# Skip setting type if type is null and already present
							if subnode.tag in xml_file_tree and subnode_type is None:
								continue

							# Add type to tree
							xml_file_tree[node.tag][subnode.tag] = subnode_type

					else:
						# Get subnode type
						node_type = get_type(node.text)

						# Skip setting type if type is null and already present
						if node.tag in xml_file_tree and node_type is None:
							continue

						# Add type to tree
						xml_file_tree[node.tag] = node_type

						# Load file if subnode is "File"
						if node.tag == "File" and node_type == "File":
							# Add full path to file to sub_files list
							sub_files.append(path.join(path.dirname(xml_filepath), node.text.strip().title()))

				# Set top_level_node as main key
				xml_file_tree = {top_level_node: xml_file_tree}
				# Load sub files
				for sub_file in sub_files:
					xml_file_tree = add_tree_dict(xml_file_tree, parse_xml(sub_file))
				# Return
				return xml_file_tree

			def add_tree_dict(main_xml_tree: dict, sub_xml_tree: dict) -> dict:
				""" Adds two xml_dir_tree dictionaries intelligently.

				:param main_xml_tree: Dictionary, The XML tree to add to
				:param sub_xml_tree: Dictionary, The XML tree to be added. Must be complete.

				:return: Dictionary, The result of the addition
				"""

				# Setup variables
				dict_sum: dict = main_xml_tree

				# Addition start, top_level_nodes
				for top_node_key in sub_xml_tree.keys():
					# Checking top_level_nodes
					if top_node_key in dict_sum:
						# Iterating over nodes
						for node_key in sub_xml_tree[top_node_key].keys():
							# Checking nodes
							if node_key in dict_sum[top_node_key]:
								# Check if tree has only subnodes
								if type(sub_xml_tree[top_node_key][node_key]) is not dict:
									if type(dict_sum[top_node_key][node_key]) is not dict:
										sub_type = sub_xml_tree[top_node_key][node_key]
										main_type = dict_sum[top_node_key][node_key]
										if sub_xml_tree[top_node_key][node_key] != dict_sum[top_node_key][node_key]:
											# Apply type logic
											dict_sum[top_node_key][node_key] = get_true_type(main_type, sub_type)
										# Continue to prevent sub-node iterations
										continue

									# Except on Node/Subnode mismatch
									else:
										raise Exception("Node {} found as both a subnode and node".format(node_key))

								# Iterating over subnodes
								for subnode_key in sub_xml_tree[top_node_key][node_key].keys():
									# Check subnodes
									if subnode_key in dict_sum[top_node_key][node_key]:
										# Check if types match
										sub_type = sub_xml_tree[top_node_key][node_key][subnode_key]
										main_type = dict_sum[top_node_key][node_key][subnode_key]
										# Handle types that do not match
										if not sub_type == main_type:
											# Apply type logic
											dict_sum[top_node_key][node_key][subnode_key] = (
												get_true_type(main_type, sub_type)
											)

									# Add if not present
									else:
										dict_sum[top_node_key][node_key][subnode_key] = (
											sub_xml_tree[top_node_key][node_key][subnode_key]
										)

							# Add if not present
							else:
								dict_sum[top_node_key][node_key] = sub_xml_tree[top_node_key][node_key]

					# Add if not present
					else:
						dict_sum[top_node_key] = sub_xml_tree[top_node_key]

				# Return
				return dict_sum

			# Set XML tree to empty Dictionary
			xml_dir_tree: dict = {}
			# Dataminerxmlfiles.Xml Path
			data_xml_path: str = path.join(xml_dir, "Dataminerxmlfiles.Xml")  # TODO: String is .title()d, fix filenames
			# Setup File list, add megafiles.xml and Dataminerxmlfiles.Xml
			xml_files: List[str] = [path.join(xml_dir, "megafiles.xml")]

			# Parse Dataminerxmlfiles, then other XMLs

			# Ensure Dataminerxmlfiles.Xml file exists
			if not path.exists(data_xml_path):
				raise Exception("'{}' does not exist".format(data_xml_path))

			# Load and begin iterating over main XML
			data_xml: xml.etree.ElementTree.Element = ET.parse(data_xml_path).getroot()
			item: xml.etree.ElementTree.Element
			for item in data_xml:
				if item.tag == "File":
					# TODO: Remove .title() and replace XMLs
					file: str = path.join(xml_dir, item.get("filename").strip().title())
					xml_files.append(file)
			# Parse XML files
			for xml_path in xml_files:
				xml_dir_tree = add_tree_dict(xml_dir_tree, parse_xml(xml_path))

			# Return tree
			return xml_dir_tree

		# Start with EaW XML Iteration
		new_xml_tree: dict = parse_xml_dir(xml_dir_eaw)

		# Then FoC XML Iteration
		new_xml_tree = add_tree_dict(new_xml_tree, parse_xml_dir(xml_dir_foc))
		# Return
		return new_xml_tree

	def build_table_output() -> None:
		def get_table_str(node_name, attributes) -> str:
			table_string = node_name.ljust(NUM_TABLE_INDICATORS)
			table_string += " " + attributes.ljust(NUM_TABLE_INDICATORS)
			return table_string + "\n"

		def codify(string) -> str:
			return "``{}``".format(string)

		def start_table(out_file) -> None:
			out_file.write(table_sep_str)
			out_file.write(get_table_str("Node Name", "Attributes"))
			out_file.write(table_sep_str)

		def write_header(out_file, header, sep) -> None:
			out_file.write(header + "\n")
			out_file.write(str(sep * len(header)) + "\n")

		def write_footer(out_file, lines) -> None:
			out_file.write("\n")
			for line in range(lines):
				out_file.write("| \n")
			out_file.write("\n")

		def write_list_subnode(out_file, list_subnode, list_type) -> None:
			# Copy subnode
			print_subnode = list_subnode

			# Setup Operations
			description = "*Description Here*"
			if print_subnode.startswith("AAA_"):
				print_subnode = print_subnode.replace("AAA_", "")
			if print_subnode.lower() in DESCRIPTORS:
				description = DESCRIPTORS[print_subnode.lower()]

			# Write
			out_file.write("- {}{}".format(print_subnode, TAB_INDICATOR))
			out_file.write(TAB + list_type + "; {}\n".format(description))
			out_file.write("\n")

		# Create string to use for tables
		table_sep_str = ("=" * NUM_TABLE_INDICATORS) + " " + ("=" * NUM_TABLE_INDICATORS) + "\n"

		# Create File
		if not path.exists(output_file):
			open(output_file, "x")

		# Build Table Output XML
		with open(output_file, "wt", newline="\n") as file:
			# Write title
			write_header(file, "All XML Structures - Autogenerated File", "=")

			# Write top-level node table
			for top_level_node in sorted(xml_tree):
				subnode_only = False
				# Write top level node as header
				write_header(file, top_level_node, "-")
				# Check if only subnodes
				for node in xml_tree[top_level_node]:
					if type(xml_tree[top_level_node][node]) is not dict:
						if not subnode_only:
							subnode_only = True

				# Write attribute table if not subnode only, as subnodes cannot have attributes
				if not subnode_only:
					# Start Table
					start_table(file)

					# Write Nodes and attributes in alphabetical order
					for node in sorted(xml_tree[top_level_node]):
						attrib_string = ""
						# Get Attributes
						subnode: str
						for subnode in sorted(xml_tree[top_level_node][node]):
							# Attributes placed first with AAA_ Prefix
							if subnode.startswith("AAA_"):
								attrib_string += codify(subnode.replace("AAA_Attribute - ", "")) + ", "

						# Write string to table, codify values
						if attrib_string == "":
							attrib_string = "None"
						file.write(get_table_str(codify(node), attrib_string.strip(", ")))

					# End table, write blank line(s)
					file.write(table_sep_str)
					write_footer(file, 1)

					# Write top node sections
					# Iterate over nodes
					for node in sorted(xml_tree[top_level_node]):
						write_header(file, node, "^")
						# Begin subnodes
						for subnode in sorted(xml_tree[top_level_node][node]):
							write_list_subnode(file, subnode, xml_tree[top_level_node][node][subnode])
						write_footer(file, 1)

				# Write top node sections immediately if subnode only
				else:
					# Iterate over subnodes
					for subnode in sorted(xml_tree[top_level_node]):
						write_list_subnode(file, subnode, xml_tree[top_level_node][subnode])
				write_footer(file, 2)

	# Setup output file
	output_file: str = path.join(xml_dir_out, "xml_structure.rst")
	xml_type_list: List[XMLType] = []

	# Dataminerxmlfiles.Xml Path
	data_xml_path: str = path.join(xml_dir_eaw, "Dataminerxmlfiles.Xml")  # TODO: String is .title()d, fix filenames

	# Ensure Dataminerxmlfiles.Xml file exists
	if not path.exists(data_xml_path):
		raise Exception("'{}' does not exist".format(data_xml_path))

	# Load and begin iterating over main XML
	data_xml: xml.etree.ElementTree.Element = ET.parse(data_xml_path).getroot()
	item: xml.etree.ElementTree.Element
	for item in data_xml:
		if item.tag == "File":
			# Get filename
			file: str = path.join(xml_dir_eaw, item.get("filename").strip().title())

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
	del current_type, file
	# Parse, then print names
	for xtype in xml_type_list:
		xtype.parse_subfiles()
		xtype.parse_subfiles()
		print(xtype.name + ": " + str(xtype.node_names))

	# Build output as table
	# build_table_output()


if __name__ == "__main__":
	build()
