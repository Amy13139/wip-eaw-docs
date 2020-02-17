# This file gets all of the elements from the EaW and FoC XML files and organizes them for documentation
import xml.etree.ElementTree as ET
from os import listdir, path, getcwd

# Valid extensions for files that can be referenced by an XML. Capitalization must be lowercase.
VALID_FILE_EXT = [
	".alo",  # Model/Particle
	".ala",  # Animation
	".meg",  # Archive, only megafiles.xml
	".tga",  # Texture, May refer to DDS
	".dds",  # Texture, Modded
	".xml",  # Data
	".bik",  # Movie
	".wav",  # Audio
	".mp3",  # Audio
]

# Keys are values that are considered booleans, values are suffixes for the type. Capitalization must be lowercase.
VALID_BOOL = {
	"yes": "y/n",
	"no": "y/n",
	"true": "t/f",
	"false": "t/f",
}

# Descriptions for subnodes/attributes. Attribute prefix is "attribute - ". Capitalization must be lowercase for keys.
DESCRIPTORS = {
	"attribute - name": "The name of the node, can be referenced by other nodes",
	"attribute - description": "An optional description for the node, only used to help anyone reading the XML.",
	"text_id": "The in-game name of this unit, references a .DAT file to allow from translations",
	"mass": "Always 0.99... 5, with an arbitrary number of 9s. Probably unused.",
	"file": "A file to load, has the same type as this file",
}

# Default EaW and FoC XML Directories, used when the program is run
DEFAULT_XML_DIR_EAW = path.join(getcwd(), "build_docs", "XML")
DEFAULT_XML_DIR_FOC = path.join(getcwd(), "build_docs", "corruption", "XML")
DEFAULT_OUTPUT_FILE = path.join(getcwd(), "basegame", "xml" "xml_structure.rst")

# Tab character
TAB = "\t"
# Used at the end of the line to indicate it has tabbed children, must have a newline at the end to function properly
TAB_INDICATOR = "\n"
# Number of "=" signs used for the rows on the Sphinx table.
NUM_TABLE_INDICATORS = 65


def build_xml_structure(xml_dir_eaw=DEFAULT_XML_DIR_EAW, xml_dir_foc=DEFAULT_XML_DIR_FOC, output_file=DEFAULT_OUTPUT_FILE, table_output=True):
	"""Function to iterate over EaW and FoC XML Files, given both of their XML directories.

	:param xml_dir_eaw: The absolute path to the EaW XML Directory.
	:param xml_dir_foc: The absolute path to the FoC XML Directory.
	:param output_file: File to write the structure to. Will truncate file if it exists.
	:param table_output: Creates Sphinx tables for nodes if true, creates tabbed list if false

	:returns: None, writes to an output file instead.
	"""

	# Start with EaW XML Iteration
	xml_tree = parse_xml_dir(xml_dir_eaw, True)

	# Then FoC XML Iteration
	xml_tree = add_tree_dict(xml_tree, parse_xml_dir(xml_dir_foc, True))

	# Create File
	if not path.exists(output_file):
		open(output_file, "x")
	# Build output as either table or tabbed list
	if table_output:
		build_table_output(output_file, xml_tree)
	else:
		build_tabbed_output(output_file, xml_tree)


def parse_xml_dir(xml_dir, use_dataminerxml=False):
	"""Iterates over a single directory of XML Files, fails if directory contains a file that is not an XML or TXT.

	:param xml_dir: The absolute path to the directory to parse.
	:param use_dataminerxml: If True, only parses files from Dataminerxmlfiles.Xml

	:returns: {top_level_node: {node: {subnode: type, ...}, ...}, ...}
	"""

	# Set XML tree to empty Dictionary
	xml_tree = {}

	# Begin Iterations, if not using Dataminerxmlfiles.xml
	if not use_dataminerxml:
		for item in listdir(xml_dir):
			# Get absolute path
			item_path = path.join(xml_dir, item)

			# Recursively parse sub-directories
			if path.isdir(item_path):
				# Get tree from the subdirectory and add it to current tree
				xml_tree = add_tree_dict(xml_tree, parse_xml_dir(item_path))
			else:
				# Get file extension, lowercase
				ext = item.split(".")[-1].lower()

				# Parse XML File
				if ext == "xml":
					# Create another XML tree from file, then add it to the main tree
					xml_tree = add_tree_dict(xml_tree, parse_xml(item_path))

				# Pass on TXT, ignore
				elif ext == "txt":
					pass

				# Raise Error on file that is not XML or TXT
				else:
					raise Exception("Encountered a file with extension '{}'".format(item))

	# Parse Dataminerxmlfiles, then other XMLs
	else:
		# Setup Variables
		xml_files = []
		# Ensure file exists
		data_xml_path = path.join(xml_dir, "Dataminerxmlfiles.Xml")
		if not path.exists(data_xml_path):
			raise Exception("'{}' does not exist".format(data_xml_path))

		# Load and begin iterating over main XML
		data_xml = ET.parse(data_xml_path).getroot()
		for item in data_xml:
			if item.tag == "File":
				file = path.join(xml_dir, item.get("filename").strip())
				xml_files.append(file)
		# Parse XML files
		for xml_path in xml_files:
			xml_tree = add_tree_dict(xml_tree, parse_xml(xml_path))

	# Return tree
	return xml_tree


def parse_xml(xml_path):
	"""Gives the nodes in the top-level node, and the sub-nodes for each node

	:param xml_path: The absolute path to the XML file to parse.

	:returns: Dictionary of {top_level_node: {node: {subnode: type, ...}, ...}}
	"""

	# Setup XML tree, get root element
	xml_tree = {}

	# Protect against invalid XML files, as even the base game has invalid files
	try:
		root = ET.parse(xml_path).getroot()
	except ET.ParseError:
		print("Error: '{}' could not be parsed, may be an invalid file".format(xml_path))
		return {}
	# Get top_level_node
	top_level_node = root.tag

	# Iterate over nodes
	for node in root:
		# Check if this is actually a node, or if the file only has subnodes
		if len(node):
			# Add node to XML tree, if not already added
			if node.tag not in xml_tree:
				xml_tree[node.tag] = {}

			# Add attributes as subnodes, keeps organization easy
			for key in node.keys():
				attrib_name = "AAA_Attribute - " + key
				if attrib_name not in xml_tree[node.tag]:
					# Set Attribute type as value
					attrib_type = get_type(node.attrib[key])
					# If type cannot be determine, use "String" Instead
					if attrib_type != "Ref" and attrib_type != "None":
						xml_tree[node.tag][attrib_name] = attrib_type
					else:
						xml_tree[node.tag][attrib_name] = "String"

			# Iterate over subnodes
			for subnode in node:
				# Get subnode type
				subnode_type = get_type(subnode.text)

				# Skip setting type if type is null and already present
				if subnode.tag in xml_tree and subnode_type is None:
					continue

				# Add type to tree
				xml_tree[node.tag][subnode.tag] = subnode_type
		else:
			# Get subnode type
			node_type = get_type(node.text)

			# Skip setting type if type is null and already present
			if node.tag in xml_tree and node_type is None:
				continue

			# Add type to tree
			xml_tree[node.tag] = node_type

	# Return tree, add top_level_node as main key
	return {top_level_node: xml_tree}


def add_tree_dict(main_xml_tree, sub_xml_tree):
	""" Adds two xml_tree dictionaries intelligently.

	:param main_xml_tree: Dictionary, The XML tree to add to
	:param sub_xml_tree: Dictionary, The XML tree to be added. Must be complete.

	:return: Dictionary, The result of the addition
	"""

	def get_true_type(main_type_check, sub_type_check):
		# Set main_type if None, Skip
		if main_type_check is None:
			return sub_type_check
		# Skip if sub_type is None
		if sub_type_check is None:
			return main_type_check
		# Override to Ref if it exists
		if sub_type_check == "Ref" or main_type_check == "Ref":
			return "Ref"
		if "Int" in main_type_check or "Int" in sub_type_check:
			if "Float" in main_type_check or "Float" in sub_type_check:
				return main_type_check.replace("Int", "Float")
		# Skip if main type ends with ellipsis, see below
		if main_type_check.endswith("..."):
			return main_type_check
		# Check if types are different length lists
		if main_type_check.startswith(sub_type_check) or sub_type_check.startswith(main_type):
			# If they are different lengths, add ellipse to type
			if "," in main_type_check or "," in sub_type_check:
				actual_type = main_type_check.split(",")[0] + ", "
			if "|" in main_type_check or "|" in sub_type_check:
				actual_type = main_type_check.split("|")[0] + " | "
			return str(actual_type * 2) + "..."

		# Return main type and warn about type mismatch if no conditions met
		print("Warning: Mismatched types '{}' and '{}' for '{}' Node".format(main_type, sub_type_check, node_key))
		return main_type_check

	# Setup variables
	dict_sum = main_xml_tree

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
								dict_sum[top_node_key][node_key][subnode_key] = get_true_type(main_type, sub_type)

						# Add if not present
						else:
							dict_sum[top_node_key][node_key][subnode_key] = sub_xml_tree[top_node_key][node_key][subnode_key]

				# Add if not present
				else:
					dict_sum[top_node_key][node_key] = sub_xml_tree[top_node_key][node_key]

		# Add if not present
		else:
			dict_sum[top_node_key] = sub_xml_tree[top_node_key]

	# Return
	return dict_sum


def get_type(value):
	"""Gets the type of an EaW/FoC XML Value, see Docs for XML Data Type Reference

	:param value: Value to determine type of
	:return: Type String, or multiple types if given a list.
	"""

	if value is None:
		return "None"

	# Set separator if value is a list, None otherwise
	sep = None
	if "," in value:
		sep = ","
		print_sep = ", "
	elif "|" in value:
		sep = "|"
		print_sep = " | "

	# Return list of types if value had a separator
	if sep is not None:
		return_string = ""
		# Split value by separator, and get each item's type
		value_list = value.split(sep)
		for item in value_list:
			# Add type of value with separator to return string
			return_string += get_type(item.strip()) + print_sep
		# Return type as list
		return return_string.rstrip(print_sep)

	# Get and return a single type
	else:
		# Check if value is File/Filepath
		if value.lower()[-4:] in VALID_FILE_EXT:
			if "\\" in value or "/" in value:
				return "Filepath"
			return "File"

		# Check if value is Dir
		if "\\" in value or "/" in value:
			return "Dir"

		# Check if value is Floatf
		if value.endswith("f"):
			try:
				# This will raise a ValueError if it cannot convert to float
				float(value[0:-1])
				return "Floatf"
			except ValueError:
				pass

		# Check if value is Int
		elif value.isnumeric():
			return "Int"

		# Check if value is Float
		elif "." in value:
			try:
				# This will raise a ValueError if it cannot convert to float
				float(value)
				return "Float"
			except ValueError:
				pass

		# Check if value is Bool
		elif value.lower() in VALID_BOOL:
			# Check if True/False or Yes/No instead of true/false or yes/no
			if value[0].isupper():
				return "Bool " + VALID_BOOL[value.lower()].upper()
			return "Bool " + VALID_BOOL[value.lower()]

		# Give up, assume reference
		return "Ref"


def build_tabbed_output(output_file, xml_tree):
	# Build List Output XML
	with open(output_file, "wt", newline="\n") as file:
		# Write top level nodes in alphabetical order
		start = True
		for top_level_node in sorted(xml_tree):
			# Write newline if it is not the file start
			if start:
				start = False
			else:
				file.write("\n")

			# Write Root Node
			file.write(top_level_node + TAB_INDICATOR)

			# Write nodes under the top level node in alphabetical order
			for node in sorted(xml_tree[top_level_node]):
				# Check if node is actually node
				if type(xml_tree[top_level_node][node]) is dict:
					# Write Node
					file.write(TAB + node + TAB_INDICATOR)

					# Write subnodes under their node in alphabetical order
					for subnode in sorted(xml_tree[top_level_node][node]):
						# Write Subnode and Type, Attributes placed first with AAA_ Prefix
						file.write((TAB * 2) + "{} - {}".format(subnode.replace("AAA_", ""),
							xml_tree[top_level_node][node][subnode]) + "\n")

				# If node is actually a subnode, write as such
				else:
					# Write node and type
					file.write(TAB + "{} - {}".format(node, xml_tree[top_level_node][node]) + "\n")


def build_table_output(output_file, xml_tree):
	def get_table_str(node_name, attributes):
		table_string = node_name.ljust(NUM_TABLE_INDICATORS)
		table_string += " " + attributes.ljust(NUM_TABLE_INDICATORS)
		return table_string + "\n"

	def codify(string):
		return "``{}``".format(string)

	def start_table(out_file, root_name):
		out_file.write(table_sep_str)
		out_file.write(get_table_str("Node Name", "Attributes"))
		out_file.write(table_sep_str)

	def write_header(out_file, header, sep):
		out_file.write(header + "\n")
		out_file.write(str(sep * len(header)) + "\n")

	def write_list_subnode(out_file, list_subnode, list_type):
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

	table_sep_str = ("=" * NUM_TABLE_INDICATORS) + " " + ("=" * NUM_TABLE_INDICATORS) + "\n"
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
				start_table(file, top_level_node)

				# Write Nodes and attributes in alphabetical order
				for node in sorted(xml_tree[top_level_node]):
					attrib_string = ""
					# Get Attributes
					for subnode in sorted(xml_tree[top_level_node][node]):
						# Attributes placed first with AAA_ Prefix
						if subnode.startswith("AAA_"):
							attrib_string += codify(subnode.replace("AAA_Attribute - ", "")) + ", "
					# Write string to table, codify values
					if attrib_string == "":
						attrib_string = "None"
					file.write(get_table_str(codify(node), attrib_string.strip(", ")))

				file.write(table_sep_str)
				file.write("\n")
				file.write("\n")

				# Write top node sections
				# Iterate over nodes
				for node in sorted(xml_tree[top_level_node]):
					write_header(file, node, "^")
					# Begin subnodes
					for subnode in sorted(xml_tree[top_level_node][node]):
						write_list_subnode(file, subnode, xml_tree[top_level_node][node][subnode])
					file.write("\n")
					file.write("\n")

			# Write top node sections immediately if subnode only
			else:
				file.write("\n")
				file.write("\n")
				# Iterate over subnodes
				for subnode in sorted(xml_tree[top_level_node]):
					write_list_subnode(file, subnode, xml_tree[top_level_node][subnode])
					file.write("\n")
					file.write("\n")


if __name__ == "__main__":
	build_xml_structure()
