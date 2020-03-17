"""
Gets absolute paths for XML Data directories and template files
"""
from typing import List, Dict
from os.path import join, dirname, realpath
from xml.etree import ElementTree
import tarfile


# Path variables
_SELF_DIR = dirname(realpath(__file__))
_DATA_UNPACKAGED_PATH = join(_SELF_DIR, "data")
_DATA_TAR_PATH = join(_SELF_DIR, "data.tar.gz")
EAW_XML_DIR = "EAW/"
FOC_XML_DIR = "FOC/"
# Template file paths
TEMPLATE_XML_DIR: str = "xml_doc_templates/"
_TEMPLATE_TYPE_PATH: str = TEMPLATE_XML_DIR + "xml_type_auto.rst"
_TEMPLATE_TYPE_NO_NODE_PATH: str = TEMPLATE_XML_DIR + "xml_type_auto_no_node.rst"
_TEMPLATE_NODE_PATH: str = TEMPLATE_XML_DIR + "xml_node_auto.rst"

DATA_TARFILE = tarfile.open(
	name=_DATA_TAR_PATH,
	mode="r:gz",
)


def get_file(str_file: str) -> List[str]:
	"""
	Gets a file as text from the data.tar.gz file
	:param str_file: The name of the file to get
	:return: A list of strings, each string being a line of the file
	"""
	data = DATA_TARFILE.extractfile(str_file).read().decode().split("\n")
	for i in range(len(data)):
		data[i] += "\n"
	return data


# Templates
TEMPLATES: Dict[str, List[str]] = {
	"type": get_file(_TEMPLATE_TYPE_PATH),
	"type_no_node": get_file(_TEMPLATE_TYPE_NO_NODE_PATH),
	"node": get_file(_TEMPLATE_NODE_PATH),
}


def get_xml_file(xml_file: str) -> ElementTree.Element:
	"""
	Gets an XML File from the data.tar.gz file
	:param xml_file: The name of the XML File to parse
	:return: The Element Tree of the XML File
	"""
	return ElementTree.fromstringlist(get_file(xml_file))
