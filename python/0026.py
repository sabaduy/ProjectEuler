# Sample Solution: https://blog.dreamshire.com/project-euler-26-solution/
# Reference:       http://mathworld.wolfram.com/FullReptendPrime.html

from lib.primes import sieve

primes = sieve(1000)

if primes[-1] < 8:
	print(3)
	exit(0)

for prime in primes[::-1]:
	period = 1
	while pow(10, period) % prime != 1:
		period += 1
	if (prime - 1) == period:
		print(prime)
		exit(0)
