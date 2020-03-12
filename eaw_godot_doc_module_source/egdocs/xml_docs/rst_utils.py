"""
Contains utilities for writing/generating RST files
"""
from typing import Final, Iterable


__all__ = [
	"TAB",
	"get_line_padding",
	"get_table_line",
	"get_table_start",
	"get_table_end",
	"get_header",
	"codify",
]


# Tab character, can be replaced with spaces if needed
TAB: Final[str] = "\t"


def get_line_padding(line_num: int) -> str:
	"""
	Gets line_num blank lines.

	:param line_num: The number of blank lines to get
	"""
	line: str = ""
	for i in range(line_num):
		line += "\n"
	return line


def get_table_line(items: Iterable[str]) -> str:
	"""
	Gets a string as part of a Sphinx rst table.

	:param items: The items to add to the table line
	"""
	line: str = TAB
	for item in items:
		# If not last item, add ", "
		if item != items[-1]:
			line += '"{}", '.format(item)
		else:
			# Ignore ", " if last item
			line += '"{}"'.format(item)
	line += get_line_padding(1)
	return line


def get_table_start(headers: Iterable[str]) -> str:
	"""
	Starts a table in Sphinx rst format.

	:param headers: The headers of the table
	"""
	# Get table start
	line = ".. csv-table::"
	line += get_line_padding(1)
	# Get headers
	line += TAB + ":header: "
	for header in headers:
		# If not last header, add ", "
		if header != headers[-1]:
			line += '"{}", '.format(header)
		# Ignore ", " if last item
		else:
			line += '"{}"'.format(header)
	# Newlines after header
	line += get_line_padding(2)
	return line


def get_table_end(line_num: int) -> str:
	"""
	Alias for get_line_padding with line_num += 1. May change if table format is changed.

	:param line_num: The number of blank lines to get, must be >=1
	"""
	return get_line_padding(line_num + 1)


def get_header(header: str, sep: str) -> str:
	"""
	Gets a header in Sphinx rst format.

	:param header: The text of the header
	:param sep: The separator to use for creating the header
	"""
	line = header + "\n"
	line += str(sep * len(header)) + "\n"
	return line


def codify(in_str: str) -> str:
	"""
	Cushions a string with four "`" character, used to indicated code in a Sphinx rst file.
	:param in_str: The string to cushion
	:return: The cushioned string
	"""
	return "``{}``".format(in_str)
