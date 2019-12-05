from lib.primes import sieve, sieve_until_count

primes_check = sieve_until_count(1000)

primes = sieve(1000)
primes_with_neg = [(-i) for i in primes[::-1]]
primes_with_neg.extend(primes)

# print(primes_with_neg)

best_a = None
best_b = None
best_n = 0
# best_series = []

for a in primes_with_neg:
	for b in primes_with_neg:
		answer = None
		n = 0
		series = []

		is_prime = True
		while is_prime:
			answer = abs(n ** 2 + a * n + b)
			if answer in primes_check:
				is_prime = True
				# series.append(answer)
				n += 1
			else:
				is_prime = False

		if n > best_n:
			best_a = a
			best_b = b
			best_n = n
			# best_series = series
			# print("Best a, b, n =", a, ",", b, ",", n)

print(best_a * best_b)


