# Classes to help manage the data of an EaW XML File
from .constants import *


# SubNode Class
class SubNode(object):
	"""
	Class to hold information related to a subnode, should be nested inside of a RootNode or Node
	Holds text data, but not XML attributes
	"""
	# Attributes
	_element: ET.Element
	name: str
	_data: List[Union[bool, float, int, str, type(None)]]
	sep_char: str
	sep_str: str
	_data_types: List[str]
	typestring: str
	filenames: Set[str]

	# Methods
	def __init__(self, xml_subnode: ET.Element) -> None:
		"""
		Creates a new SubNode object
		:param xml_subnode: The xml.etree.ElementTree.Element object to create the SubNode from
		"""
		# Set attributes
		self.filenames: Set[str] = set()
		self._element: ET.Element = xml_subnode
		self.name: str = xml_subnode.tag
		self._data_types = []
		self.typestring = ""
		self.sep_char = ""
		self.sep_str = ""

		# Set data as list
		self._get_data(xml_subnode.text)

		# Set types in data_type list
		for value in self._data:
			# Get type string, then add type in data_type list.
			self._data_types.append(self._get_type(value))

		# Verify
		self._verify_data_types()

	def get_typestring(self, force_regen=False) -> str:
		"""
		Gets the type of this subnode as a string
		:return: A type string
		"""
		# Create if it does not exist
		if force_regen or not self.typestring:
			self.typestring = ""
			data_length = len(self._data_types)
			last_index = data_length - 1
			# Iterate over data types
			for index in range(data_length):
				# Add string name of the current type
				self.typestring += self._data_types[index]
				# Add separator if not the last item
				if index != last_index:
					self.typestring += self.sep_str

		# Return the typestring
		return self.typestring

	def compare(self, subnode) -> bool:
		"""
		Checks if another subnode should be added, may modify itself to resolve conflicts with another subnode
		:param subnode: The subnode to check for conflicts with.
		:return: Boolean, True if this no conflicts found
		"""
		# OK the node if it has a different name.
		if subnode.name != self.name:
			return True
		# Alter self if incorrect type
		self._get_true_type(subnode.get_typestring())
		# Add filenames
		if subnode.name == "File":
			self.filenames.update(subnode.filenames)

	def _get_data(self, raw_data: str) -> None:
		"""
		Sets data from the raw_data string
		:param raw_data: String to split into a list
		"""
		data: List[str]
		# Set data to a single-element list of ["None"]
		if raw_data is None:
			self._data = ["None"]
			return

		# Get separator, or set data to a single-element list before exiting
		if "," in raw_data:
			# Set separator values
			self.sep_char = ","
			self.sep_str = ", "
		elif "|" in raw_data:
			# Set separator values
			self.sep_char = "|"
			self.sep_str = " | "
		else:
			# If not a list, set to a single-element list, then exit.
			self._data = [raw_data.strip()]
			return

		# Split, then strip whitespace
		data = raw_data.split(self.sep_char)
		for i in range(len(data)):
			data[i] = data[i].strip()

		# Return
		self._data = data

	def _get_true_type(self, n_type: str) -> None:
		"""
		Compares two types, returns the correct type of the node
		:param n_type: New type string
		:return: A Type string
		"""
		def _substitution_check(sub_type: str, replace_filter="") -> str:
			"""
			Substitution check, return either an empty or string with substitution completed
			:param sub_type: The type to substitute
			:param replace_filter: If set, only returns a string if the substitution type has the filter in it.
			:return:
			"""
			def _finalize() -> str:
				"""
				Internal finalization, returns substitution or empty string
				:return: String, either empty or with a substitution done
				"""
				# Get the sub's replacement
				start_pos = sub_element_holder.find(sub_type)
				end_pos = other_element_holder.find(",", start_pos)
				if end_pos == -1:
					end_pos = len(other_element_holder)
				replacement_element_type: str = other_element_holder[
					start_pos:end_pos
				]
				# Ensure filter matches
				if replace_filter in replacement_element_type:
					# Check if replacement creates an equality
					if sub_element_holder.replace(sub_type, replacement_element_type) == other_element_holder:
						# Return a replacement with both types listed
						return sub_element_holder.replace(sub_type, "[{}, {}]".format(
							sub_type,
							replacement_element_type,
						))
				return ""

			# Check if sub_type exists in either sequence
			if sub_type in self.typestring or sub_type in n_type:
				sub_element_holder: str
				other_element_holder: str
				# If substitution element is in the current typestring
				if sub_type in self.typestring:
					sub_element_holder = self.typestring
					other_element_holder = n_type
					final = _finalize()
					if final:
						return final

				# Flip usages if none is in the new string.
				if sub_type in n_type:
					sub_element_holder = n_type
					other_element_holder = self.typestring
					final = _finalize()
					if final:
						return final

			# Return blank string on fail
			return ""
		
		# Ensure typestring is created
		self.get_typestring()

		# Return original if both are equal
		if self.typestring == n_type:
			return

		# Return if None
		if self.typestring == "None":
			self.typestring = n_type
			return

		# Return if None
		if n_type == "None":
			return

		# Override to Ref if it exists
		if n_type == "Ref" or self.typestring == "Ref":
			self.typestring = "Ref"
			return
		
		# Interchangeable Float/Int check, use float
		if "Int" in self.typestring or "Int" in n_type:
			if "Float" in self.typestring or "Float" in n_type:
				self.typestring = self.typestring.replace("Int", "Float")
				n_type = n_type.replace("Int", "Float")
				if self.typestring == n_type:
					return

		# Check if substitutions already completed
		if "[" in n_type:
			self.typestring = n_type
			return
		if "[" in self.typestring:
			return

		# Check for "None" Substitution with anything
		sub = _substitution_check("None")
		if sub:
			self.typestring = sub
			return

		# Check for "Float" Substitution with "Floatf"
		sub = _substitution_check("Float", "Floatf")
		if sub:
			self.typestring = sub
			return
		del sub

		# Be more generous with list checking, then force-regen the typestring
		self._verify_data_types(2)
		if self.get_typestring(True).endswith("..."):
			return

		# Return main type and warn about type mismatch if no conditions met
		if self.typestring != n_type:
			print("Warning: Mismatched types '{}' and '{}' in {}".format(self.typestring, n_type, self.name))

	def _get_type(self, value: str) -> str:
		"""
		Gets the type of an EaW/FoC XML Value, see Docs for XML Data Type Reference
		Types: None, Bool, Dir, File, Float, Floatf, Int, Ref
		:param value: Value to determine type of
		:return: Type String, or multiple types if given a list.
		"""

		if value is None or not value:
			return "None"

		# Get and return a single type
		ext: str = value[-4:].lower()

		# Check if value is File/Filepath
		if ext in VALID_FILE_EXT:
			if ext == ".xml":
				# Add to filenames list
				filename = basename(value.title())
				self.filenames.add(filename)
			# Check if file is directory
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
		try:
			# This will raise a ValueError if it cannot convert to int
			int(value)
			return "Int"
		except ValueError:
			pass

		# Check if value is Float
		if "." in value:
			try:
				# This will raise a ValueError if it cannot convert to float
				float(value)
				return "Float"
			except ValueError:
				pass

		# Check if value is Bool
		elif value.lower() in VALID_BOOL:
			# Check if True/False or Yes/No instead of true/false or yes/no
			return "Bool"

		# Give up, assume reference
		return "Ref"

	def _verify_data_types(self, min_elements=5) -> None:
		"""
		Runs special checks on the data types, alters if needed.
		:param min_elements: The minimum number of elements in the list to check if it is a sequence.
		"""
		# Cancel if typestring ends with ellipsis, already run
		if self._data_types[-1] == "...":
			return

		# Check special cases for the _data_types list
		data_len = len(self._data_types)
		# Check if both floats and ints present
		if "Int" in self._data_types and "Float" in self._data_types:
			# Replace all "Int" types with "Float"
			for index in range(data_len):
				if self._data_types[index] == "Int":
					self._data_types[index] = "Float"

		# Check if list at least min_elements and repeats, shorten with ellipsis if so.
		if data_len >= min_elements:
			# Check if sequence repeats, up to 2 elemtents for repeat check.
			repeat_num = len(set(self._data_types))
			# Get the sequence to check for repeat checks
			if (data_len / 2) >= repeat_num and not data_len % repeat_num:
				repeat_item = self._data_types[:repeat_num]
				repeat_list = []
				# Repeat the character sequence to match the length of the current list
				for i in range(int(data_len / repeat_num)):
					repeat_list.extend(repeat_item)
				# Check equivilance
				if self._data_types == repeat_list:
					# Set to two iterations of the item, then stop
					self._data_types = self._data_types[:(repeat_num * 2)]
					# Add an ellipsis to the end
					self._data_types.append("...")


# Private base class with a few shared functions
class _NodeSubNodeHolder(object):
	"""
	Base class to hold methods and attributes for Node and SubNode storage
	"""
	# Attributes
	nodes: list
	subnodes: List[SubNode]

	# Methods
	def __init__(self) -> None:
		self.nodes: List[_NodeSubNodeHolder] = []
		self.subnodes = []

	def add_node(self, node) -> None:
		"""
		Adds a Node, if not already present
		:param node: The node to be added to the RootNode
		"""
		# Check for conflicts with current nodes; iterate over nodes
		for index in range(len(self.nodes)):
			# Exit if comparison fails. Node can update itself from the compare() method
			if not self.nodes[index].compare(node):
				return

		# Add the Node if no conflicts
		self.nodes.append(node)

	def add_subnode(self, subnode: SubNode) -> None:
		"""
		Adds a SubNode, if not already present
		:param subnode: The subnode to be added to the RootNode
		"""
		# Run comparisons to ensure no conflicts occur
		for index in range(len(self.subnodes)):
			# Exit if comparison fails, subnode may have adjusted itself
			if not self.subnodes[index].compare(subnode):
				return

		# Add SubNode, condition above must be met
		self.subnodes.append(subnode)

	def get_node_names(self) -> List[str]:
		"""
		Gets and returns a list of all Node names
		:return: List of Node names
		"""
		# Variables
		names: List[str] = []

		# Iterate over nodes
		for node in self.nodes:
			names.append(node.name)
		# Return Names
		return sorted(names)

	def get_subnode_names(self) -> List[str]:
		"""
		Gets and returns a list of all SubNode names
		:return: List of SubNode names
		"""
		# Variables
		names: List[str] = []

		# Iterate over nodes
		for subnode in self.subnodes:
			names.append(subnode.name)
		# Return Names
		return sorted(names)

	def get_nodes(self) -> list:
		"""
		Returns the Nodes held by the parent
		:rtype: List[Node]
		:return: A List of Nodes
		"""
		return sorted(self.nodes, key=lambda x: x.name)

	def get_subnodes(self) -> List[SubNode]:
		"""
		Returns the SubNodes held by the parent
		:return: A List of SunNodes
		"""
		return sorted(self.subnodes, key=lambda x: attrib_key(x.name))

	def has_nodes(self) -> bool:
		"""
		Checks for Nodes
		:return: True if any Node is found, False otherwise
		"""
		return bool(self.nodes)

	def has_subnodes(self) -> bool:
		"""
		Checks for SubNodes
		:return: True if any SubNode is found, False otherwise
		"""
		return bool(self.subnodes)


# Node Class
class Node(_NodeSubNodeHolder):
	"""
	Class to hold information related to a node, should be nested inside of a RootNode or another Node
	Can hold nodes, subnodes, and XML attributes
	"""
	# Attributes
	_element: ET.Element
	name: str
	nodes: list
	attributes: List[str]
	subfiles: Set[str]

	# Methods
	def __init__(self, xml_node: ET.Element) -> None:
		"""
		Creates a new Node object
		:param xml_node: The xml.etree.ElementTree.Element object to create the Node from
		"""
		# Call super
		super(Node, self).__init__()
		# Set blank variables
		self.nodes: List[Node] = []
		self.attributes = []
		self.subfiles = set()
		# Set _element
		self._element = xml_node
		# Call _setup() to setup node, uses _element
		self._setup()

	def _setup(self) -> None:
		"""
		Sets the attributes of the node from it's XML Element.
		Should only be called on creation through __init__()
		"""
		# Set name from tag
		self.name = self._element.tag

		# Get attributes and add them to the attributes list
		for attribute in self._element.attrib:
			self.attributes.append(attribute)

		# Get Children, add them to their respective lists
		child: ET.Element
		for child in self._element:
			# Determine if child is a SubNode or a Node
			# If child has children or attributes it is a Node
			if len(child) or len(child.attrib):
				# Add Node
				self.add_node(Node(child))
			else:
				self.add_subnode(SubNode(child))

	def compare(self, node: _NodeSubNodeHolder) -> bool:
		"""
		Compares two nodes, alters this Node is needed
		:param node: The node to compare.
		:return: A boolean, True if no conflicts
		"""
		node_names = self.get_node_names()
		subnode_names = self.get_subnode_names()

		if node.name == self.name:
			# Compare Nodes
			for new_node_i in range(len(node.nodes)):
				if node.nodes[new_node_i].name in node_names:
					for node_i in range(len(self.nodes)):
						self.nodes[node_i].compare(node.nodes[new_node_i])

			# Compare SubNodes
			for new_subnode_i in range(len(node.subnodes)):
				if node.subnodes[new_subnode_i] in subnode_names:
					for subnode_i in range(len(self.subnodes)):
						self.subnodes[subnode_i].compare(node.subnodes[new_subnode_i])

			# Return False
			return False

		# No conflicts, Return True
		return True

	def get_subfiles(self) -> Set[str]:
		"""
		Gets the subfiles of this node
		:return: A list of filenames
		"""
		self.subfiles.clear()
		# Iterate over Nodes
		for node in self.nodes:
			self.subfiles.update(node.get_subfiles())
		# Iterate over SubNodes
		for subnode in self.subnodes:
			self.subfiles.update(subnode.filenames)
		# Return
		return self.subfiles


# RootNode Class
class RootNode(_NodeSubNodeHolder):
	"""
	Class to hold information related to a top-level node, including nodes and/or subnodes
	Holds Nodes or SubNodes
	"""
	# Attributes
	name: str
	xml_filename: str
	xml_dir: str
	nodes: List[Node]
	subfiles: Set[str]

	# Methods
	def __init__(self) -> None:
		"""
		Creates a new RootNode object
		:param xml_type: The RootNode's XML type.
		"""
		# Call super
		super(RootNode, self).__init__()
		self.nodes: List[Node] = []
		self.subfiles: Set[str] = set()

	def from_file(self, xml_filepath: str) -> None:
		"""
		Sets the attributes of the RootNode from an XML file
		:param xml_filepath: The path to the XML file
		"""
		# Ensure file exists
		if not exists(xml_filepath):
			raise Exception("File '{}' does not exist\nAt: '{}'".format(
				basename(xml_filepath),
				xml_filepath,
			))

		# Set filename and get root element of the tree
		self.xml_filename = basename(xml_filepath)
		self.xml_dir = dirname(xml_filepath)
		root: ET.Element = ET.parse(xml_filepath).getroot()
		# Set name
		self.name = root.tag

		# Iterate over and add child nodes
		child: ET.Element
		for child in root:
			# Determine if child is a SubNode or a Node
			# If child has children or attributes it is a Node
			if len(child) or len(child.attrib):
				# Add Node
				self.add_node(Node(child))
			else:
				self.add_subnode(SubNode(child))

	def add_file(self, xml_filepath: str) -> None:
		"""
		Adds to the attributes of the RootNode from an XML file
		:param xml_filepath: The path to an XML file with an identical rootnode name
		"""
		# Ensure file exists
		if not exists(xml_filepath):
			raise Exception("File '{}' does not exist\nAt: '{}'".format(
				basename(xml_filepath),
				xml_filepath,
			))

		# Set filename and get root element of the tree
		root: ET.Element = ET.parse(xml_filepath).getroot()
		# Check name
		if self.name != root.tag:
			raise Exception("Tag '{}' is not equal to current name '{}'".format(root.tag, self.name))

		# Iterate over and add child nodes
		child: ET.Element
		for child in root:
			# Determine if child is a SubNode or a Node
			# If child has children or attributes it is a Node
			if len(child) or len(child.attrib):
				# Add Node
				self.add_node(Node(child))
			else:
				self.add_subnode(SubNode(child))

	def has_subfile(self) -> bool:
		"""
		Returns true if RootNode hold subfiles
		:return: Boolean, true if RootNode holds subfiles
		"""
		self._update_subfiles()
		return bool(len(self.subfiles))

	def get_subfiles(self) -> Set[str]:
		"""
		Returns the subfiles of this node as a list of filepaths
		:return: Subfiles list
		"""

		# Return
		self._update_subfiles()
		return self.subfiles

	def get_filename(self) -> str:
		"""
		Returns the filename of the XML used to create this RootNode.
		:rtype: str
		:return: Filename
		"""
		return self.xml_filename

	def _update_subfiles(self) -> None:
		"""
		Updates the subfiles attribute, automatically called from get_subfiles and has_subfiles functions.
		"""
		# Clear list of subfiles
		self.subfiles.clear()
		# Iterate over Nodes
		for node in self.nodes:
			for file in node.get_subfiles():
				self.subfiles.add(join(self.xml_dir, file))
		# Iterate over SubNodes
		for subnode in self.subnodes:
			for file in subnode.filenames:
				self.subfiles.add(join(self.xml_dir, file))


# XMLType Class
class XMLType(object):
	"""
	Class to hold information for the structures of an XML Data type
	Holds RootNodes and names. Operates in a single directory.
	"""
	# Attributes
	name: str
	root_nodes: List[RootNode]
	root_names: Set[str]
	node_names: Set[str]
	subnode_names: Dict[str, Set[str]]
	has_subfile: bool

	# Methods
	def __init__(self, name: str) -> None:
		"""
		Creates a new XMLType
		:param name: The name of the XML Type
		"""
		# Set variables to blank values
		self.name = name
		self.has_subfile = False
		self.root_nodes: List[RootNode] = []
		self.root_names: Set[str] = set()
		self.node_names: Set[str] = set()
		self.subnode_names: Dict[str, Set[str]] = {}

	def add_rootnode(self, xml_filepath: str) -> None:
		"""
		Adds a rootnode to the type. Should only be called internally
		:param xml_filepath: The path of the file to add the rootnode from
		"""
		if self._valid_rootnode_file(xml_filepath):
			# Make the RootNode
			root: RootNode = RootNode()
			# Setup from file.
			root.from_file(xml_filepath)
			# Add name to list, update subfiles if not already done
			self.root_names.add(root.name)
			if (not self.has_subfile) and root.has_subfile():
				self.has_subfile = True
			# Add the RootNod
			self.root_nodes.append(root)
		# Update
		self.update()

	def parse_subfiles(self) -> None:
		"""
		Parses through all current subfiles that this RootNode has, given from current RootNodes.
		"""
		# Exit if type has no subfiles

		if not self.has_subfile:
			return
		# Variables
		file: str
		subfiles: Set[str] = set()

		# Set has_subfile to false, allows parsing subfiles only as needed
		self.has_subfile = False

		# Iterate over RootNode children
		for rootnode in self.root_nodes:
			for file in rootnode.get_subfiles():
				# Check if rootnode already exists, skip if so.
				if self._valid_rootnode_file(file):
					# Add to subfiles list if not already present
					if file not in subfiles:
						subfiles.add(file)

		# Add subfiles as RootNodes
		for subfile in subfiles:
			self.add_rootnode(subfile)
		# Update
		self.update()

		# Rerun if new subfiles were added
		if self.has_subfile:
			self.parse_subfiles()

	def get_rootnodes(self) -> List[RootNode]:
		"""
		Gets the list of child RootNodes
		:return: A list of all RootNodes present in this type
		"""
		return sorted(self.root_nodes, key=lambda x: x.name)

	def get_nodes(self) -> List[Node]:
		"""
		Gathers a set of all nodes present this XML Type, merges nodes with identical names
		:return: A set of all nodes present in this type.
		"""
		# Setup a node holder
		node_holder: _NodeSubNodeHolder = _NodeSubNodeHolder()

		# Iterate over RootNodes
		for rootnode in self.root_nodes:
			# Iterate over node in each RootNode
			for node in rootnode.get_nodes():
				# Add the Nodes to the node_holder
				node_holder.add_node(node)

		# Return the list of nodes from node_holder
		return node_holder.get_nodes()

	def update(self) -> None:
		"""
		Updates attributes from current RootNodes. Does not parse subfiles.
		"""
		# Clear attributes that will be updates
		self.node_names: List[str] = []
		self.subnode_names: Dict[str, Set[str]] = {}
		# Iterate over RootNodes
		name: str
		s_name: str
		for rootnode in self.root_nodes:
			# Iterate over Nodes
			for node in rootnode.nodes:
				self._node_update_process(node)
			if len(rootnode.subnodes):
				# Create Set in subnode_names for the RootNode's Subnodes
				self.subnode_names[rootnode.name] = set()
				# Iterate over SubNodes
				for subnode in rootnode.subnodes:
					self.subnode_names[rootnode.name].add(subnode.name)

	def _valid_rootnode_file(self, xml_filepath: str) -> bool:
		"""
		Check if a file is currently in use for rootnodes. Adds to existing rootnode if present.
		:param xml_filepath: The path of the file to check validity for
		:return: True if file is valid, False if filename is in use.
		"""
		root_name: str = ET.parse(xml_filepath).getroot().tag
		# Iterate over RootNodes
		for rootnode in self.root_nodes:
			# Check is filenames are identical
			if root_name == rootnode.name:
				rootnode.subfiles.add(xml_filepath)
				# Return False, match is found
				return False

		# Return True if no match found.
		return True

	def _node_update_process(self, node: Node) -> None:
		"""
		Runs update process with a node, this can call itself to parse nested nodes
		:param node: The node to updates from
		:return:
		"""
		# Get and test name
		name = node.name
		if name not in self.node_names:
			# Add if not added
			self.node_names.append(name)
			# Modify attributes to say "Attribute - " in the front
			attrs: List[str] = []
			for attr in node.attributes:
				attrs.append("Attribute - " + attr.title())
			# Create set, use Node attributes as base
			self.subnode_names[name] = set(attrs)

		# Iterate over SubNodes
		for subnode in node.subnodes:
			# Set and test name
			s_name = subnode.name
			self.subnode_names[name].add(s_name)

		# Iterate over nodes
		for nested_node in node.nodes:
			self._node_update_process(nested_node)
