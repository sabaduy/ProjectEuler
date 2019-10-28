from .file_util import read_list, write_list

def factors(number):
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

		current = current + 1


	# Prepare to recreate factors after inflection point
	reversed_factors = reversed(factors)

	# Add the inflection point after the reversed factors if
	# the inflection point is current^2
	if current ** 2 == number:
		factors.append(current)

	# Recreate largewr factors
	for i in reversed_factors:
		factors.append(number // i)

	return factors