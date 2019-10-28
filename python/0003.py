from lib.factors import factors

mylist = factors(600851475143)

answer = 1
for i in mylist:
	if len(factors(i)) == 2:
		answer = i

print(answer)