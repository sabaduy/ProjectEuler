from lib.factors import get_proper_factors

upper_limit = 28123
abundant_numbers = []

for i in range(1, upper_limit + 1):
	proper_factors = get_proper_factors(i)
	if sum(proper_factors) > i:
		abundant_numbers.append(i)

# print("Count of abundant numbers:", len(abundant_numbers))

answers = set(range(1, upper_limit + 1))
for i, a in enumerate(abundant_numbers):
	for b in abundant_numbers[i:]:
		total = a + b
		if total > upper_limit:
			break
		answers.discard(total)

# print("Count of answers:", len(answers))
print(sum(answers))