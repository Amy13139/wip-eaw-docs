# Classes to help manage the data of an EaW XML File
from typing import List, Union, Dict, Set
from os import path
from xml.etree import ElementTree as ET

# Constants
_TYPE_DICT: Dict[str, type] = {
	"None": type(None),
	"Bool": bool,
	"Dir": str,
	"File": str,
	"Filepath": str,
	"Float": float,
	"Floatf": float,
	"Int": int,
	"Ref": str,
}
# Valid extensions for files that can be referenced by an XML. Capitalization must be lowercase.
VALID_FILE_EXT: list = [
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
VALID_BOOL: dict = {
		"yes": "y/n",
		"no": "y/n",
		"true": "t/f",
		"false": "t/f",
}


# SubNode Class
class SubNode(object):
	"""
	Class to hold information related to a subnode, should be nested inside of a RootNode or Node
	Holds text data, but not XML attributes
	"""
	# Attributes
	_element: ET.Element
	name: str
	data_type: List[type]
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

		# Set data as list
		data: List[Union[bool, float, int, str, type(None)]]
		data = self.split_data(xml_subnode.text)

		# Set types in data_type list
		self.data_type = []
		for value in data:
			# Get type string, then add type in data_type list.
			self.data_type.append(
				_TYPE_DICT[self.get_type(value)]
			)

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
		self.name = self.get_true_type(self.name, subnode.name)
		# Add filenames
		if subnode.name == "File":
			self.filenames.update(subnode.filenames)

	def get_type(self, value: str) -> str:
		"""
		Gets the type of an EaW/FoC XML Value, see Docs for XML Data Type Reference
		Types: None, Bool, Dir, File, Float, Floatf, Int, Ref
		:param value: Value to determine type of
		:return: Type String, or multiple types if given a list.
		"""

		if value is None or not bool(value):
			return "None"

		# Get and return a single type
		ext: str = value[-4:].lower()

		# Check if value is File/Filepath
		if ext in VALID_FILE_EXT:
			if ext == ".xml":
				# Add to filenames list
				filename = path.basename(value.title())
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
			return "Bool"

		# Give up, assume reference
		return "Ref"

	@staticmethod
	def split_data(value: str) -> List[str]:
		"""
		Returns the string split into a list of values, if applicable
		:param value: String to split into a list
		:return: A list of string, created from the value
		"""
		split_data: List[str]
		separator: str
		if value is None:
			return []

		# Get separator, or return a single-element list
		if "," in value:
			separator = ","
		elif "|" in value:
			separator = "|"
		else:
			return [value.strip()]

		# Split, then strip whitespace
		split_data = value.split(separator)
		for i in range(len(split_data)):
			split_data[i] = split_data[i].strip()

		# Return
		return split_data

	@staticmethod
	def get_true_type(o_type, n_type) -> str:
		"""
		Compares two types, returns the correct type of the node
		:param o_type: Original type
		:param n_type: New type
		:return: A Type string
		"""
		# Return original if both are equal
		if o_type == n_type:
			return o_type

		# Return if None
		if o_type == "None":
			return n_type

		# Return if None
		if n_type == "None":
			return o_type

		# Override to Ref if it exists
		if n_type == "Ref" or o_type == "Ref":
			return "Ref"

		# Interchangeable Float/Int check, use float
		if "Int" in o_type or "Int" in n_type:
			if "Float" in o_type or "Float" in n_type:
				return o_type.replace("Int", "Float")

		# Skip if main type ends with ellipsis, assume different length lists
		if o_type.endswith("..."):
			return o_type

		# Skip if sub type ends with ellipsis, assume different length lists
		if n_type.endswith("..."):
			return n_type

		# Check if types are different length lists
		if o_type.startswith(n_type) or n_type.startswith(main_type):
			# If they are different lengths, add ellipse to type
			if "," in o_type or "," in n_type:
				actual_type = o_type.split(",")[0] + ", "
			if "|" in o_type or "|" in n_type:
				actual_type = o_type.split("|")[0] + " | "
			return str(actual_type * 2) + "..."

		# Return main type and warn about type mismatch if no conditions met
		print(
			"Warning: Mismatched types '{}' and '{}' for '{}' Node".format(
				main_type,
				n_type,
				node_key,
			)
		)
		return o_type


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
		self.nodes = []
		self.subnodes = []

	def add_node(self, node) -> None:
		"""
		Adds a Node, if not already present
		:param node: The node to be added to the RootNode
		"""
		# Iterate over Nodes
		name: str = node.name
		for node in self.nodes:
			# Exit if names match
			if node.name == name:
				return  # TODO: Update the node instead of returning
		# Add the Node
		self.nodes.append(node)

	def add_subnode(self, subnode: SubNode) -> None:
		"""
		Adds a SubNode, if not already present
		:param subnode: The subnode to be added to the RootNode
		"""
		# Run comparisons to ensure no conflicts occur
		for index in range(len(self.subnodes)):
			# Set current_subnode variable
			curr_subnode = self.subnodes[index]
			# Exit if comparison fails, subnode may have adjusted itself
			if not curr_subnode.compare(subnode):
				# Set subnode to ensure adjustment carries
				self.subnodes[index] = curr_subnode
				# Exit
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
		return names

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
		return names


# Node Class
class Node(_NodeSubNodeHolder):
	"""
	Class to hold information related to a node, should be nested inside of a RootNode or another Node
	Can hold nodes, subnodes, and XML attributes
	"""
	# Attributes
	_element: ET.Element
	name: str
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
	subfiles: Set[str]

	# Methods
	def __init__(self) -> None:
		"""
		Creates a new RootNode object
		:param xml_type: The RootNode's XML type.
		"""
		# Call super
		super(RootNode, self).__init__()
		self.subfiles: Set[str] = set()

	def from_file(self, xml_filepath: str) -> None:
		"""
		Sets the values of the RootNode from an XML file
		:param xml_filepath: The path to the XML file
		"""
		# Ensure file exists
		if not path.exists(xml_filepath):
			raise Exception("File '{}' does not exist\nAt: '{}'".format(
				path.basename(xml_filepath),
				xml_filepath,
			))

		# Set filename and get root element of the tree
		self.xml_filename = path.basename(xml_filepath)
		self.xml_dir = path.dirname(xml_filepath)
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

	def has_subfile(self) -> bool:
		"""
		Returns true if RootNode hold subfiles
		:return: Boolean, true if RootNode holds subfiles
		"""
		return bool(len(self.subfiles))

	def get_subfiles(self) -> Set[str]:
		"""
		Returns the subfiles of this node as a list of filepaths
		:return: Subfiles list
		"""
		# Iterate over Nodes
		for node in self.nodes:
			for file in node.get_subfiles():
				self.subfiles.add(path.join(self.xml_dir, file))
		# Iterate over SubNodes
		for subnode in self.subnodes:
			for file in subnode.filenames:
				self.subfiles.add(path.join(self.xml_dir, file))
		# Return
		return self.subfiles

	def get_filename(self) -> str:
		"""
		Returns the filename of the XML used to create this RootNode.
		:rtype: str
		:return: Filename
		"""
		return self.xml_filename


# XMLType Class
class XMLType(object):
	"""
	Class to hold information for the structures of an XML Data type
	Holds RootNodes and names. Operates in a single directory.
	"""
	# Attributes
	name: str
	root_nodes: List[RootNode]
	node_names: List[str]
	subnode_names: Dict[str, List[str]]

	# Methods
	def __init__(self, name: str) -> None:
		"""
		Creates a new XMLType
		:param name: The name of the XML Type
		"""
		# Set variables to blank values
		self.name = name
		self.root_nodes: List[RootNode] = []
		self.node_names: List[str] = []
		self.subnode_names: Dict[str, List[str]] = {}

	def add_rootnode(self, xml_filepath: str) -> None:
		"""
		Adds a rootnode to the type. Should only be called internally
		:param xml_filepath: The path of the file to add the rootnode from
		"""
		# Make the RootNode
		root: RootNode = RootNode()
		# Setup from file.
		root.from_file(xml_filepath)
		# Add the RootNode
		self.root_nodes.append(root)

	def parse_subfiles(self) -> None:
		"""
		Parses through all current subfiles that this RootNode has, given from current RootNodes.
		"""
		# Variables
		file: str
		subfiles: Set[str] = set()

		# Iterate over RootNode children
		for rootnode in self.root_nodes:
			for file in rootnode.get_subfiles():
				# Check if filename is already in use, skip if so.
				if self._valid_rootnode_filename(path.basename(file)):
					# Add to subfiles list if not already present
					if file not in subfiles:
						subfiles.add(file)

		# Add subfiles as RootNodes
		for subfile in subfiles:
			self.add_rootnode(subfile)
		# Update
		self.update()

	def update(self) -> None:
		"""
		Updates attributes from current RootNodes. Does not parse subfiles.
		"""
		# Clear attributes that will be updates
		self.node_names: List[str] = []
		self.subnode_names: Dict[str, List[str]] = {}
		# Iterate over RootNodes
		name: str
		s_name: str
		for rootnode in self.root_nodes:
			# Iterate over Nodes
			for node in rootnode.nodes:
				# Get and test name
				name = node.name
				if name not in self.node_names:
					# Add if not added
					self.node_names.append(name)
					self.subnode_names[name] = []

				# Iterate over SubNodes
				for subnode in node.subnodes:
					# Set and test name
					s_name = subnode.name
					if s_name not in self.subnode_names:
						# Add if not present
						self.subnode_names[name].append(s_name)

	def _valid_rootnode_filename(self, filename: str) -> bool:
		"""
		Check if a name is currently in use for rootnodes
		:param filename: The filename string to check
		:return: True if filename is valid, False if filename is in use
		"""
		# Iterate over RootNodes
		for rootnode in self.root_nodes:
			# Check is filenames are identical
			if filename == rootnode.xml_filename:
				# Return False if a match is found
				return False

		# Return True if no match found.
		return True
