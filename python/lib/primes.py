from os import path
from .file_util import read_list, write_list


data_file = path.join(path.dirname(path.realpath(__file__)),"./primes.dat")

def preload_from_file():
	data = [int(i) for i in read_list(data_file)]
	data_file_len = len(data)
	data_file_max = data[-1] if data_file_len > 0 else 0

	# Initialize
	if data_file_len == 0:
		data = [2]

	return data

def write_to_file(data):
	data = [str(i) for i in data]

	write_list(data_file, data)



def sieve(maximum):
	primes = preload_from_file()

	current = primes[-1] + 1

	while current <= maximum:
		is_prime = True
		for i in primes:
			if current % i == 0:
				is_prime = False
				break

		if is_prime:
			primes.append(current)

		current = current + 1

	write_to_file(primes)

	return primes