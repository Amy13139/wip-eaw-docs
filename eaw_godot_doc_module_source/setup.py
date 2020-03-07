"""Basic setup.py file to allow module functionality for ReadTheDocs"""
from setuptools import setup, Extension
from Cython.Build import cythonize

root_path = "src/"
xml_doc_path = root_path + "build_xml_docs/"


compiler_directives = {
	"language_level": 3,
}

extensions = [
	# XML Builder
	Extension(
		"eaw_godot_doc_module.build_xml_docs.xml_constants",
		[xml_doc_path + "xml_constants.py"],
	),
	Extension(
		"eaw_godot_doc_module.build_xml_docs.xml_classes",
		[xml_doc_path + "xml_classes.py"],
	),
	Extension(
		"eaw_godot_doc_module.build_xml_docs.xml_builder",
		[xml_doc_path + "xml_builder.py"],
	),

	# Main Builder
	Extension(
		"eaw_godot_doc_module.builder",
		[root_path + "main.py"],
	),
]


setup(
	ext_modules=cythonize(extensions, compiler_directives=compiler_directives),
)
