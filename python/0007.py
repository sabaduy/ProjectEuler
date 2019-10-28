from lib.primes import sieve_until_count
from lib.factors import get_factors

mylist = sieve_until_count(10001)
print(mylist[-1])