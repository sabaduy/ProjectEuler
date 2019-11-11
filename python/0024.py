from math import factorial

numbers = list(range(0,10))
answer  = []

combinations_left = 1000000-1

while len(numbers) > 0 and combinations_left > 0:
	fact_result = factorial(len(numbers) - 1)
	possible_index = combinations_left // fact_result

	# print(combinations_left)
	# print(numbers)
	# print(fact_result)
	# print(possible_index)

	if possible_index >= len(numbers):
		exit(1)

	answer.append(numbers[possible_index])
	numbers.pop(possible_index)
	combinations_left = combinations_left % fact_result

# Leftover numbers to use
if len(numbers) > 0:
	for i in numbers:
		answer.append(i)

print(''.join([str(i) for i in answer]))