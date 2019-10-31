def process_one_digit(number_str):
	if number_str == "1":
		return "one"
	elif number_str == "2":
		return "two"
	elif number_str == "3":
		return "three"
	elif number_str == "4":
		return "four"
	elif number_str == "5":
		return "five"
	elif number_str == "6":
		return "six"
	elif number_str == "7":
		return "seven"
	elif number_str == "8":
		return "eight"
	elif number_str == "9":
		return "nine"
	else:
		return None

def process_two_digits(number_str):
	length = len(number_str.lstrip("0"))
	if length == 0:
		return ""
	elif length == 1:
		return process_one_digit(number_str.lstrip("0"))

	result = ""

	digit_one = number_str[0]
	digit_two = number_str[1]

	
	if digit_one == "1":
		if digit_two == "0":
			return "ten"
		elif digit_two == "1":
			return "eleven"
		elif digit_two == "2":
			return "twelve"
		elif digit_two == "3":
			return "thirteen"
		elif digit_two == "4":
			return "fourteen"
		elif digit_two == "5":
			return "fifteen"
		elif digit_two == "6":
			return "sixteen"
		elif digit_two == "7":
			return "seventeen"
		elif digit_two == "8":
			return "eighteen"
		elif digit_two == "9":
			return "nineteen"
	elif digit_one == "2":
		result = "twenty"
	elif digit_one == "3":
		result = "thirty"
	elif digit_one == "4":
		result = "forty"
	elif digit_one == "5":
		result = "fifty"
	elif digit_one == "6":
		result = "sixty"
	elif digit_one == "7":
		result = "seventy"
	elif digit_one == "8":
		result = "eighty"
	elif digit_one == "9":
		result = "ninety"


	digit_two_processed = process_one_digit(digit_two)

	if digit_two_processed != None:
		result = result + "-" + digit_two_processed

	return result


def process_three_digits(number_str):
	length = len(number_str.lstrip("0"))
	if length == 0:
		return ""
	elif length < 3:
		return process_two_digits(number_str.lstrip("0"))

	result = process_one_digit(number_str[0]) + " hundred"

	if number_str[1:] != "00":
		result += " and " + process_two_digits(number_str[1:])

	return result


def int_to_text(number):
	was_int = False
	if isinstance(number, int):
		was_int = True
		number = str(number)

	# print(number)

	if len(number) > 1 and not was_int:
		# print("stripping lead zero")
		number = number.lstrip("0")
		if number == "":
			number = "0"

	# print(number)

	if number == "0":
		return "zero"

	return process_three_digits(number)


answer = 0
for i in range(1,1000):
	text = int_to_text(i)
	text = text.replace(' ', '').replace('-','')
	answer += len(text)

answer += len("one thousand".replace(' ', '').replace('-',''))
print(answer)
