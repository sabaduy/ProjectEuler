from math import sqrt

a = 1
b = 2
c = 3

found = False
while not found and b < 1000:
	for i in range(1, b):
		c = sqrt(i ** 2 + b ** 2)

		if (i + b + c == 1000):
			a = i
			found = True
			break

	if not found:
		b += 1

print(int(a*b*c))