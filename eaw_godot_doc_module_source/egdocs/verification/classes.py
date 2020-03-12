"""
File containing the classes for the 'verification' package
"""
from typing import Dict, Tuple
from os import walk
from ast import literal_eval


class HashManager:
	"""
	Manager for creating and checking hashes for files
	"""
	# Constants
	_HASH_TUPLE_TYPE = Tuple[str, str]
	_HASHED_TYPE = Dict[str, HASH_TUPLE_TYPE]

	_HASH_FILENAME = "hash.txt"
	_HASH_TUPLE_METHODS = ("sha256", "md5")

	# Variables
	_read_hashes: _HASHED_TYPE
	_hashed: _HASHED_TYPE

	def __init__(self, root: str):
		"""
		Creates a new HashManager that operates in the given directory
		:param root: The directory for the HashManager to operate in.
		"""


	def hash_dir(self, path: str) -> _HASHED_TYPE:
		pass

	def hash_file(self, path: str) -> HASH_TUPLE_TYPE:
		pass

