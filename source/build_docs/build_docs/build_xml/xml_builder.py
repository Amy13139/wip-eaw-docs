# This script gets all of the elements from the EaW and FoC XML files and organizes them for documentation
from .xml_classes import *


def build_docs(xml_dir_out: str, xml_types: List[XMLType]) -> None:
	"""
	Takes a list of XMLTypes and uses them to build the XML Documentation
	:param xml_dir_out: The output directory, should also be the XML Docs directory
	:param xml_types: The list of XML Types to use for building the documentation
	"""
	
	# Get Functions - Generic Sphinx Utilities
	def get_line_padding(line_num: int) -> str:
		"""
		Gets line_num blank lines
		:param line_num: The number of blank lines to get
		"""
		line: str = ""
		for i in range(line_num):
			line += "\n"
		return line

	def get_table_line(items: Iterable[str]) -> str:
		"""
		Gets a string as part of a Sphinx rst table.
		:param items: The items to add to the table line
		"""
		line: str = TAB
		for item in items:
			# If not last item, add ", "
			if item != items[-1]:
				line += '"{}", '.format(item)
			else:
				# Ignore ", " if last item
				line += '"{}"'.format(item)
		line += get_line_padding(1)
		return line

	def get_table_start(headers: Iterable[str]) -> str:
		"""
		Starts a table in Sphinx rst format.
		:param headers: The headers of the table
		"""
		# Get table start
		line = ".. csv-table::"
		line += get_line_padding(1)
		# Get headers
		line += TAB + ":header: "
		for header in headers:
			# If not last header, add ", "
			if header != headers[-1]:
				line += '"{}", '.format(header)
			# Ignore ", " if last item
			else:
				line += '"{}"'.format(header)
		# Newlines after header
		line += get_line_padding(2)
		return line

	def get_table_end(line_num: int) -> str:
		"""
		Alias for get_line_padding with line_num += 1. May change if table format is changed.
		:param line_num: The number of blank lines to get, must be >=1
		"""
		return get_line_padding(line_num + 1)

	def get_header(header: str, sep: str) -> str:
		"""
		Gets a header in Sphinx rst format.
		:param header: The text of the header
		:param sep: The separator to use for creating the header
		"""
		line = header + "\n"
		line += str(sep * len(header)) + "\n"
		return line

	# Get Functions - xml_classes Input
	def get_subnode(list_subnode: SubNode) -> str:
		"""
		Gets a subnode in the format for the xml_structure.rst file
		:param list_subnode: The subnode to get information from to the list
		"""
		# Get Subnode info
		line = "- {}{}".format(list_subnode.name, TAB_INDICATOR)
		line += "{}{}; {}\n".format(TAB, list_subnode.get_typestring(), get_subnode_description(list_subnode.name))
		line += get_line_padding(2)
		return line

	def get_node(curr_node: Node, is_nested=False) -> str:
		"""
		Gets a node's information in the format for the xml_structure.rst file
		:param curr_node: The node to use for the writing.
		:param is_nested: If True, will treat the file as a nested file, and have a different header.
		"""
		# Get header
		if is_nested:
			line: str = get_header(curr_node.name, '^')
		else:
			line: str = get_header(curr_node.name, "-")
		line += get_node_description(curr_node.name)
		line += get_line_padding(2)
		# Handle nested nodes
		if curr_node.has_nodes():
			# Get table
			line += get_table_start(("Nested Nodes", "Description"))
			for nested_node_name in curr_node.get_node_names():
				line += get_table_line((nested_node_name, get_node_description(nested_node_name)))
			line += get_table_end(1)
			# Recurse for nested nodes
			for nested_node in curr_node.get_nodes():
				line += get_node(nested_node, True)
		# Handle SubNodes, should be present
		if curr_node.has_subnodes():
			# Get header
			if is_nested:
				line += get_header("Nested SubNodes", '"')
			else:
				line += get_header("SubNodes", '^')
			# Iterate over subnodes
			for curr_subnode in curr_node.get_subnodes():
				line += get_subnode(curr_subnode)
			line += get_line_padding(1)
		line += get_line_padding(1)
		# Return
		return line

	def get_rootnode(rootnode: RootNode) -> str:
		"""
		Gets the information of a rootnode to a file
		:param rootnode: The RootNode to get the information from
		:return:
		"""
		# Get RootNode name as header
		line: str = get_header(rootnode.name, "=")
		line += get_root_description(rootnode.name)
		line += get_line_padding(2)

		# Get Nodes table for RootNode's Nodes
		if rootnode.has_nodes():
			line += get_table_start(("Node Children", "Description"))
			# Iterate over nodes
			for node_name in rootnode.get_node_names():
				line += get_table_line((node_name, get_node_description(node_name)))
			# Close the table
			line += get_table_end(2)
			for node in rootnode.get_nodes():
				line += get_node(node)

		# Get SubNodes list for RootNode's Direct Subnodes
		if rootnode.has_subnodes():
			line += get_header("SubNode Children", "-")
			# Iterate over direct subnodes
			subnode: SubNode
			for subnode in rootnode.get_subnodes():
				line += get_subnode(subnode)
			# Close the table
			line += get_line_padding(1)
		# Return
		return line

	def get_xml_type(xml_type: XMLType) -> str:
		"""
		Gets the information of an XML Type to a file

		:param xml_type: The XMLType to get information from
		"""
		# Get XMLType name as header
		line: str = get_header(xml_type.name, "*")
		# Get table for RootNodes in XML Type in a table
		line += get_table_start(("Root Node", "Description"))
		# Iterate over names, ensure alphabetical sorting
		for rootnode_name in sorted(xml_type.root_names):
			line += get_table_line((rootnode_name, get_root_description(rootnode_name)))
		line += get_table_end(1)

		# Iterate over RootNodes
		for rootnode in xml_type.get_rootnodes():
			line += get_rootnode(rootnode)
		# Return
		return line

	# Write Functions - Generic Sphinx Utilities
	def write_line_padding(out_file: TextIO, line_num: int) -> None:
		"""
		Writes line_num blank lines
		:param out_file: The file to write to
		:param line_num: The number of blank lines to write
		"""
		out_file.write(get_line_padding(line_num))

	def write_table_line(out_file: TextIO, items: Iterable[str]) -> None:
		"""
		Writes a string as part of a Sphinx rst table.
		:param out_file: The file to write to
		:param items: The items to add to the table line
		"""
		out_file.write(get_table_line(items))

	def write_table_start(out_file: TextIO, headers: Iterable[str]) -> None:
		"""
		Starts a table in Sphinx rst format.
		:param out_file: The file to write to
		:param headers: The headers of the table
		"""
		# Write table start
		out_file.write(get_table_start(headers))

	def write_table_end(out_file: TextIO, line_num: int) -> None:
		"""
		Alias for write_line_padding with line_num += 1. May change if table format is changed.
		:param out_file: The file to write to
		:param line_num: The number of blank lines to write, must be >=1
		"""
		out_file.write(get_table_end(line_num))

	def write_header(out_file: TextIO, header: str, sep: str) -> None:
		"""
		Writes a header in Sphinx rst format.
		:param out_file: The file to write to
		:param header: The text of the header
		:param sep: The separator to use for creating the header
		"""
		out_file.write(get_header(header, sep))
	
	# Write Functions - xml_classes Input
	def write_subnode(out_file: TextIO, list_subnode: SubNode) -> None:
		"""
		Writes a subnode in the format for the xml_structure.rst file
		:param out_file: The file to write to
		:param list_subnode: The subnode to get information from to the list
		"""
		out_file.write(get_subnode(list_subnode))

	def write_node(out_file: TextIO, curr_node: Node, is_nested=False) -> None:
		"""
		Writes a node's information in the format for the xml_structure.rst file
		:param out_file: The file to write to
		:param curr_node: The node to use for the writing.
		:param is_nested: If True, will treat the file as a nested file, and have a different header.
		"""
		out_file.write(get_node(curr_node))
		
	def write_rootnode(out_file: TextIO, rootnode: RootNode) -> None:
		"""
		Writes the information of a rootnode to a file
		:param out_file: The file to write to
		:param rootnode: The RootNode to get the information from
		"""
		out_file.write(get_rootnode(rootnode))
		
	def write_xml_type(out_file: TextIO, xml_type: XMLType) -> None:
		"""
		Writes the information of an XML Type to a file
		:param out_file: The file to write to
		:param xml_type: The XMLType to get information from
		"""
		out_file.write(get_xml_type(xml_type))
	
	# Build Functions
	def build_structure_xml() -> None:
		"""
		Build the XML structure file
		"""
		# Create File
		xml_structure_path = join(xml_dir_out, XML_STRUCTURE_FILENAME)

		# Build Structure XML
		with open(xml_structure_path, "wt", newline="\n") as structure_file:
			# Write title
			write_header(structure_file, "All XML Structures - Autogenerated File", "#")

			# Iterate over XMLTypes
			for xml_type in sorted(xml_types, key=lambda x: x.name):
				write_xml_type(structure_file, xml_type)

	def build_xml_docs() -> None:
		"""
		Build the main XML doc files.
		"""
		def write_rootnode_file(rootnode: RootNode) -> None:
			"""
			Write a doc file for a RootNode
			:param rootnode: The RootNode to get information from
			"""
			# Get rootnode file name
			rootnode_path = join(dir_path, "{}.rst".format(rootnode.name))
			
			# Copy template. To Insert: Name, About, Structure, Context
			root_file_lines: List[str] = template_root.copy()
			# Create inserts list
			root_inserts: List[str] = [
				# 1. Name
				rootnode.name,
				# 2. About
				get_root_description(rootnode.name),
				# 3. Structure, to be filled in later
				get_rootnode(rootnode),
				# 4. Context
				get_root_context(rootnode.name),
			]

			# Get iterator from inserts
			root_insert_iter: Iterator[str] = iter(root_inserts)

			# Iterate over lines
			for index in range(len(root_file_lines)):
				if "{}" in root_file_lines[index]:
					root_file_lines[index] = root_file_lines[index].format(next(root_insert_iter))
			# Write to file
			with open(rootnode_path, "wt") as root_file:
				root_file.writelines(root_file_lines)
				root_file.close()
			del root_file

		# Get templates
		template_type = get_type_template()
		template_root = get_root_template()

		# Iterate over types
		for xml_type in xml_types:
			# Get path to main file
			filepath = join(xml_dir_out, "{}.rst".format(xml_type.name))
			dir_path = join(xml_dir_out, xml_type.name)

			# Create Subdirectory
			if not exists(dir_path):
				mkdir(dir_path)

			# Copy template. To Insert: Name, Description, SubDirectory, Context, Node Names, SubNode Names
			type_file_lines: List[str] = template_type.copy()
			# Create inserts list
			inserts: List[str] = [
				# 1. Name
				xml_type.name,
				# 2. Description
				get_root_description(xml_type.name),
				# 3. Subdirectory
				xml_type.name,
				# 4. Context
				get_root_context(xml_type.name),
			]
			# Continue inserts setup

			# 5. Node Names
			node_names_str = ""
			for node_name in xml_type.node_names:
				node_names_str += "- {}\n".format(
					node_name,
				)
			inserts.append(node_names_str)
			del node_names_str

			# 6. SubNode Names
			subnode_names_set: Set[str] = set()
			subnode_names_str = ""
			for subnode_set in xml_type.subnode_names.values():
				subnode_names_set.update(subnode_set)
			for subnode_name in sorted(subnode_names_set, key=attrib_key):
				subnode_names_str += "- {}\n".format(
					subnode_name,
				)
			inserts.append(subnode_names_str)
			del subnode_names_set, subnode_names_str

			# Get iterator from inserts
			insert_iter: Iterator[str] = iter(inserts)
			# Iterate over lines
			for i in range(len(type_file_lines)):
				if "{}" in type_file_lines[i]:
					type_file_lines[i] = type_file_lines[i].format(next(insert_iter))
			with open(filepath, "wt") as main_file:
				main_file.writelines(type_file_lines)
				main_file.close()
			del main_file

			# Iterate over RootNodes
			for curr_rootnode in xml_type.get_rootnodes():
				write_rootnode_file(curr_rootnode)

	# Build file structure
	build_structure_xml()

	# Build main docs
	build_xml_docs()


def build(xml_dir_eaw: str, xml_dir_foc: str, xml_dir_out: str) -> None:
	"""
	Function to iterate over EaW and FoC XML Files, given both of their XML directories.

	:param xml_dir_eaw: The absolute path to the EaW XML Directory.
	:param xml_dir_foc: The absolute path to the FoC XML Directory.
	:param xml_dir_out: The absolute path to the Documentation directory for XML Files.

	:returns: None, writes to an output file.
	"""

	# Setup type list
	xml_type_list: List[XMLType] = []

	# Dataminerxmlfiles.Xml Path
	eaw_data_xml_path: str = join(xml_dir_eaw, "Dataminerxmlfiles.Xml")
	# Ensure Dataminerxmlfiles.Xml file exists
	if not exists(eaw_data_xml_path):
		raise Exception("'{}' does not exist".format(eaw_data_xml_path))

	foc_data_xml_path: str = join(xml_dir_foc, "Dataminerxmlfiles.Xml")
	# Ensure Dataminerxmlfiles.Xml file exists
	if not exists(foc_data_xml_path):
		raise Exception("'{}' does not exist".format(eaw_data_xml_path))

	# Parse data files
	eaw_data_xml: xml.etree.ElementTree.Element = ET.parse(eaw_data_xml_path).getroot()
	foc_data_xml: xml.etree.ElementTree.Element = ET.parse(foc_data_xml_path).getroot()
	item: xml.etree.ElementTree.Element

	# Iterate over the data files
	for data_file in (eaw_data_xml, foc_data_xml):
		for item in data_file:
			if item.tag == "File":
				# Get filename
				if data_file == eaw_data_xml:
					file: str = join(xml_dir_eaw, item.get("filename").strip().title())
				else:
					file: str = join(xml_dir_foc, item.get("filename").strip().title())

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
		# print("\n{}# {} SubNodes".format(TAB, xtype.name))
		# # Make subnode list
		# subnode_set: Set[str] = set()
		# for single_set in xtype.subnode_names.values():
		# 	subnode_set.update(single_set)
		# subnode_set -= set(DESCRIPTION_SUBNODE)
		# for name in sorted(subnode_set, key=attrib_key):
		# 	print(TAB + '"{}": "",'.format(name))
		# print()
	# Build XML Docs
	build_docs(xml_dir_out, xml_type_list)
