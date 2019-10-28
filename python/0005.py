import functools
from lib.factors import get_factors

maximum = 10
factors = []
discards = set()

for i in range(maximum,0,-1):
	print(i)

	# First pass
	if len(factors) == 0:
		temp = get_factors(i)
		temp.reverse()
		factors.append(i)
		discards.update(set(temp[1:]))

	else:
		temp = get_factors(i)

		


print(factors)
print(discards)
answer = functools.reduce(lambda a, b : a * b, factors)


print(answer)