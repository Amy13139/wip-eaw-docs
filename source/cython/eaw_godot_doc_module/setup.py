"""Basic setup.py file to allow module functionality for ReadTheDocs"""
from os import getcwd
from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Build import cythonize


print(getcwd())
# Base path for the module, relative to the current working directory
b_path: str = ""

extensions = [
	# XML Builder

	Extension(
		"eaw_godot_doc_module.build_xml.xml_constants",
		[b_path + "build_xml/xml_constants.py"],
	),
	Extension(
		"eaw_godot_doc_module.build_xml.xml_classes",
		[b_path + "build_xml/xml_classes.py"],
	),
	Extension(
		"eaw_godot_doc_module.build_xml.xml_builder",
		[b_path + "build_xml/xml_builder.py"],
	),

	# Main Builder
	Extension(
		"eaw_godot_doc_module.builder",
		[b_path + "build_xml/doc_builder.py"],
	),
]


setup(
	name='eaw_godot_doc_module',
	setup_requires=["cython"],
	author='luke13139',
	zip_safe=False,
	ext_modules=cythonize(
		extensions,
		compiler_directives={
			"language_level": 3
		},
	),
)
