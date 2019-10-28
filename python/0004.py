def is_palindrome(number):
	as_str = str(number)
	rev = ''.join(reversed(list(as_str)))
	return as_str == rev



num_chars = 3
small_number = int('1' + ''.join(['0' for i in range(0, num_chars - 1)]))
large_number = int(''.join(['9' for i in range(0, num_chars)]))


# Rather simple, unoptimized solution...
answer = 0
for i in range(small_number,large_number + 1):
	for j in range(small_number, large_number + 1):
		number = i * j
		if is_palindrome(number) and number > answer:
			answer = number

print(answer)