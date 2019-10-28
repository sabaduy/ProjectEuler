from os import path
from .file_util import read_list, write_list


data_file = path.join(path.dirname(path.realpath(__file__)),"./fib.txt")

def preload_from_file():
	data = [int(i) for i in read_list(data_file)]
	data_file_len = len(data)
	data_file_max = data[-1] if data_file_len > 0 else 0

	# Initialize
	if data_file_len == 0:
		data = [0,1]

	return data

def write_to_file(data):
	data = [str(i) for i in data]

	write_list(data_file, data)



def fib(maximum):
	"""Get the Fibonacci sequence up to the maximum"""
	sequence = preload_from_file()

	current = sequence[0] + sequence[1]
	while True:
		if current <= maximum:
			sequence.append(current)
			current = sequence[-2] + sequence[-1]
		else:
			break

	write_to_file(sequence)

	return sequence


