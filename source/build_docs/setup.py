"""Basic setup.py file to allow module functionality for ReadTheDocs"""
from setuptools import setup

setup(
   name='build_docs',
   version='0.1',
   description='Generates EaW/FoC Documentation Files',
   author='luke13139',
   packages=['build_docs', 'build_docs.build_xml'],
)
