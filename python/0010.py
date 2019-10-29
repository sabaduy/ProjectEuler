from lib.primes import sieve

primes = sieve(2000000 - 1)
print(sum(primes))