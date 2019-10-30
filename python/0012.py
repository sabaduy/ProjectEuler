from lib.factors import get_factors

def triangle_seq_gen():
	current = 1
	total   = 0
	while True:
		total   += current
		current += 1
		yield total

min_divisors = 500
triangle_num = triangle_seq_gen()

answer = 0
while True:
	answer = next(triangle_num)
	if len(get_factors(answer)) > min_divisors:
		break

print(answer)