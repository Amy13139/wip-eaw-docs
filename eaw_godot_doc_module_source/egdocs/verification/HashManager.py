"""
File containing the classes for the 'verification' package
"""
from typing import Dict, Tuple, Union, Callable, ClassVar, List
from os import scandir
import os.path
import hashlib
from zlib import crc32
from ast import literal_eval

# Constants
_VALID_HASH = Union[str, int]
_HASHED_TYPE = Dict[str, Tuple[_VALID_HASH]]

_HASH_FILENAME = "hashes"
# Methods must be either a string compatible with hashlib.new() or a function that returns a hash from a byte input
_HASH_METHODS: Tuple[Union[str, Callable], ...] = ("sha256", crc32)


class HashManager:
	"""
	Manager for creating and checking hashes for files
	"""
	directory: str

	# Variables
	_curr_hashes: _HASHED_TYPE
	_old_hashes: _HASHED_TYPE

	def __init__(self, root: str):
		"""
		Creates a new HashManager that operates in the given directory

		:param root: The directory for the HashManager to operate in.
		"""
		assert os.path.exists(root), "Root directory '{}' does not exist".format(root)
		# Setup directory
		self.directory = root
		# Hash the current directory
		self.hash_dir()

	@staticmethod
	def hashlib_hash(hash_id: str, data: bytes) -> str:
		"""
		Hashes a file by creating a new hash object

		:param str hash_id: The name of the hash algorithm to use
		:param bytes data: The raw data to hash
		:return: A hexadecimal string hash
		"""
		# Ensure input is valid
		assert hash_id in hashlib.algorithms_available, "Hash algorithm '{}' not available".format(hash_id)

		# Create hash_obj with the input hash algorithm
		hash_obj: hashlib = hashlib.new(hash_id)
		hash_obj.update(data)
		return hash_obj.hexdigest()

	def hash_dir(self, path="") -> None:
		"""
		Updated stored hashes with the hashes of all files in the root directory of the HashManager

		:param str path: The path to iterate over, assumes root directory of HashManager if not given.
		"""
		if not len(path):
			path = self.directory

		assert os.path.exists(path), "Directory '{}' does not exist"

		item: os.DirEntry
		for item in scandir(path=self.directory):
			# Recursive function call on subdirectories
			if item.is_dir():
				self.hash_dir(path=item.path)
			# Get hash for each file
			elif item.is_file():
				# Don't hash the hash index file
				if os.path.basename(item.path) == _HASH_FILENAME:
					continue
				self._hash_file(item.path)

	def _hash_file(self, path: str) -> None:
		"""
		Stores the hashes of a given file.

		:param str path: The path to the file to hash
		"""
		# Set hashes variable
		hashes: List[_VALID_HASH] = []
		# Get relative path
		rel_path = os.path.relpath(path, self.directory)

		# Store file data as bytes
		with open(path, 'rb') as file:
			file_data = file.read()
			file.close()

		# Iterate over hash methods
		curr_hash: _VALID_HASH
		for hash_method in _HASH_METHODS:
			# Use hashlib if method is a string
			if hash_method is str:
				curr_hash = self.hashlib_hash(hash_method, file_data)

			# Assume method is callable if not a string
			else:
				curr_hash = hash_method(file_data)

			hashes.append(curr_hash)

		# Set an element of the _curr_hashes attribute
		self._curr_hashes[rel_path] = tuple(hashes)

	def _write_hashfile(self) -> None:
		"""Writes the current _curr_hashes attribute to the hashfile at directory root, overwriting the current file"""
		hashfile_path = os.path.join(self.directory, _HASH_FILENAME)
		with open(hashfile_path, "wt") as hashfile:
			hashfile.write(str(self._curr_hashes))
			hashfile.close()

	def _read_hashfile(self) -> None:
		"""Reads the hashfile in the root directory of the HashManager"""
		hashfile_path = os.path.join(self.directory, _HASH_FILENAME)

		# Create file if it does not exist
		if not os.path.exists(hashfile_path):
			self._write_hashfile()
			self._old_hashes = {}
		# Read dictionary literal if hashfile does exist
		else:
			with open(hashfile_path, "rt") as hashfile:
				read_data = literal_eval(hashfile.read())
				hashfile.close()
			# The data from the file should be a dictionary literal. If lengths are different, it is unusable
			if (read_data is not dict) or (len(read_data.values()[0]) != len(self._curr_hashes.values()[0])):
				print(("Warning: Hashfile '{}' has unreadable data or"
					"a different hash quantity, rehashing all files").format(hashfile_path))

				self._write_hashfile()
				self._old_hashes = {}
			else:
				# Set old hash dictionary to the read_data attribute
				self._old_hashes = read_data

	def check_file(self, file_path: str) -> bool:
		"""
		Checks if a file has been changed since the last hashfile update.

		:param str file_path: The path of the file to check the changed status on
		"""
		# Create relative path
		path = os.path.relpath(file_path, self.directory)
		# Verify that the relative path exists and is hashed
		assert os.path.exists(path) and path in self._curr_hashes,\
			"File '{}' does not exist or is has not been hashed".format(path)

		# Return True if file is not in the old hash list
		if path not in self._old_hashes:
			return True

		# Compare the tuples, return the result
		return self._curr_hashes[path] == self._old_hashes[path]


