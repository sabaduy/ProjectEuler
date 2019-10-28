from .file_util import read_list, write_list
from .primes import sieve

def get_factors(number):
	"""Get the factors of a number"""
	factors = [1]

	current = 2
	divisor = 2

	# Only need to check up to number / divisor
	while current <= number / divisor:
		if number % current == 0:
			# Inflection point
			if factors[-1] * current == number or current ** 2 == number:
				break
			else:
				factors.append(current)
		
		# Update divisor
		elif len(factors) == 1:
			divisor = divisor + 1

		current += 1


	# Prepare to recreate factors after inflection point
	reversed_factors = reversed(factors)

	# Add the inflection point after the reversed factors if
	# the inflection point is current^2
	if current ** 2 == number:
		factors.append(current)

	# Recreate larger factors
	for i in reversed_factors:
		factors.append(number // i)

	return factors


def get_prime_factors(number):
	"""Get the prime factors of a number as a list"""
	primes = sieve(number)
	
	factors = []
	
	while number > 1:
		for i in primes:
			while number % i == 0:
				factors.append(i)
				number = number // i

	return factors


def get_prime_factors_dict(number):
	"""Get the prime factors of a number as a dictionary"""
	prime_factors = get_prime_factors(number)
	as_dict = {}
	for i in prime_factors:
		if i not in as_dict.keys():
			as_dict[i] = 1
		else:
			as_dict[i] = as_dict[i] + 1

	return as_dict

