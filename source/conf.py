# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from os import path, getcwd
import build_docs


# -- Project information -----------------------------------------------------

project = 'eaw-godot-docs'
copyright = '2020, luke13139'
author = 'luke13139'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Use contents instead of index
master_doc = 'contents'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Doc Generation
# Variables
eaw_data_dir = path.join(getcwd(), "data\\")
foc_data_dir = path.join(eaw_data_dir, "corruption\\")
basegame_data_dir = path.join(getcwd(), "basegame\\")
xml_data_dir = path.join(basegame_data_dir, "xml")

# Build docs
print("Building XML Structure...")
build_docs.xml.build_xml_structure(
	path.join(eaw_data_dir, "XML"),
	path.join(foc_data_dir, "XML"),
	path.join(xml_data_dir, "xml_structure.rst")
)
print("Done Building XML Structure")
