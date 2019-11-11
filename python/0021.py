from lib.factors import get_proper_factors

amicable_numbers = set()
for a in range(1,10000):
	b = sum(get_proper_factors(a))
	if b == a:
		continue

	d_b = sum(get_proper_factors(b))
	if d_b == a:
		amicable_numbers.add(a)
		amicable_numbers.add(b)

print(sum(amicable_numbers))

