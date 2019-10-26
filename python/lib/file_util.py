def read_list(file: str) -> list:
	"""Reads the data from a file and returns a list"""
	from os import path

	data = []

	if path.exists(file):
		with open(file, "r") as file:
			for line in file:
				data.append(line.strip())

	return data

def write_list(file: str, data: list):
	"""Writes one line per item in data list"""
	with open(file, "w") as file:
		for i in data:
			file.write(i + '\n')