from lib.primes import sieve
from lib.factors import get_prime_factors_dict

maximum = 20
prime_factors = {}

for i in range(2, maximum + 1):
	# print(i)

	temp = get_prime_factors_dict(i)
	# print(temp)

	for key, value in temp.items():
		if key not in prime_factors.keys() or prime_factors[key] < value:
			prime_factors[key] = value

# print(prime_factors)

answer = 1
for key, value in prime_factors.items():
	answer *= key ** value

print(answer)