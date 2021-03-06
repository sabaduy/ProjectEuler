from os import path
from .file_util import read_list, write_list


data_file = path.join(path.dirname(path.realpath(__file__)),"./primes.txt")

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
	"""Use the sieve method to get primes up to and including the maximum"""
	primes = preload_from_file()

	current = primes[-1] + 1

	while current <= maximum:
		divisor = 2
		is_prime = True
		for i in primes:
			if current % i == 0:
				is_prime = False
				break
			elif current / divisor < i:
				break
			else:
				divisor = i

		if is_prime:
			primes.append(current)

		current += 1

	if current > maximum:
		primes = [i for i in primes if i <= maximum]

	write_to_file(primes)

	return primes

def sieve_until_count(max_count):
	"""Use the sieve method to get primes up to the specified number of primes"""
	primes = preload_from_file()

	current = primes[-1] + 1

	while len(primes) <= max_count:
		divisor = 2
		is_prime = True
		for i in primes:
			if current % i == 0:
				is_prime = False
				break
			elif current / divisor < i:
				break
			else:
				divisor = i

		if is_prime:
			primes.append(current)

		current += 1

	if len(primes) > max_count:
		primes = primes[:max_count]

	write_to_file(primes)

	return primes


def get_primes__factorization(maximum):
	"""Use factorization to get the primes up to and including maximum"""
	from .factors import get_factors
	primes = preload_from_file()

	current = primes[-1] + 1

	while current <= maximum:
		if len(get_factors(current)) == 2:
			primes.append(current)

		current += 1

	if current > maximum:
		primes = [i for i in primes if i <= maximum]

	write_to_file(primes)

	return primes