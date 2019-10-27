from os import path
from .file_util import read_list, write_list


data_file = path.join(path.dirname(path.realpath(__file__)),"./fib.dat")


def preload_from_file():
	data = [int(i) for i in read_list(data_file)]
	data_file_len = len(data)
	data_file_max = data[-1] if data_file_len > 0 else 0

	if data_file_len == 0:
		data = [0,1]

	return data

def write_to_file(data):
	data = [str(i) for i in data]

	write_list(data_file, data)

def fib(maximum):
	data = preload_from_file()

	current = data[0] + data[1]
	while True:
		if current <= maximum:
			data.append(current)
			current = data[-2] + data[-1]
		else:
			break

	write_to_file(data)

	return data


