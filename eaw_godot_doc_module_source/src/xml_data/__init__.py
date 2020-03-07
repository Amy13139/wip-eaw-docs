"""
Gets absolute paths for XML Data directories and template files
"""
from typing import List
from os.path import join, dirname, realpath

# Path variables
_SELF_DIR = dirname(realpath(__file__))
_DATA_DIR = join(_SELF_DIR, "data")
EAW_XML_DIR = join(_DATA_DIR, "EAW")
FOC_XML_DIR = join(_DATA_DIR, "FOC")
# Template file paths
TEMPLATE_XML_DIR: str = join(_DATA_DIR, "xml_doc_templates")
TEMPLATE_TYPE: str = join(TEMPLATE_XML_DIR, "xml_type_auto.rst")
TEMPLATE_NODE: str = join(TEMPLATE_XML_DIR, "xml_node_auto.rst")


def get_type_template() -> List[str]:
	"""
	Gets the type template as a list of lines
	:return: The lines from the template
	"""
	with open(TEMPLATE_TYPE, 'rt') as template_file:
		return template_file.readlines()


def get_node_template() -> List[str]:
	"""
	Gets the root template as a list of lines
	:return: The lines from the template
	"""
	with open(TEMPLATE_NODE, 'rt') as template_file:
		return template_file.readlines()
