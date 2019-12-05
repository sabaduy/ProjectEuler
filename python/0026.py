def long_division_str(numerator, divisor, decimal_precision=1000):
	"""Perform long division. No rounding is done"""


	numerator_str = str(numerator)
	answer = ""

	decimal_found = False
	decimal_count = 0


	# print("Start Part 1")

	# Handle all numerator numbers
	current_index = 0
	remainder     = int(numerator_str[current_index])
	while current_index < len(numerator_str):
		# print("current_index:", current_index)
		# print("remainder:    ", remainder)
		# print("answer:       ", answer)

		if remainder >= divisor:
			if decimal_found:
				decimal_count += 1
			answer += str(remainder // divisor)

		current_index += 1
		if current_index < len(numerator_str):
			if numerator_str[current_index] == ".":
				decimal_found = True
				answer += "."
				current_index += 1

			remainder = ((remainder % divisor) * 10) + int(numerator_str[current_index])

		# Prepare for numbers after numerator (aka next section)
		else:
			remainder = (remainder % divisor) * 10

	# print("\nEnd Part 1")
	# print("current_index:", current_index)
	# print("remainder:    ", remainder)
	# print("answer:       ", answer)
	

	# Handle small typing issues
	if answer == "":
		answer = "0."
	elif remainder > 0:
		answer += "."

	# print("\nStart Part 2")
	# print("remainder:    ", remainder)
	# print("answer:       ", answer)

	# Handle decimals after numerator is done
	while remainder > 0 and decimal_count <= decimal_precision:
		# print("remainder:    ", remainder)
		# print("answer:       ", answer)
		if remainder >= divisor:
			decimal_count += 1
			answer += str(remainder // divisor)
			remainder = (remainder % divisor) * 10
		else:
			# print("Moving Over...")
			answer += "0"
			remainder = remainder * 10


	# Remove decimal point if not needed
	if answer[-1] == ".":
		answer = answer[:-1]


	return answer




print(long_division_str(1,97))