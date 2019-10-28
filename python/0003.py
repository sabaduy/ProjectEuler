from lib.factors import get_factors

mylist = get_factors(600851475143)

answer = 1
for i in mylist:
	if len(get_factors(i)) == 2:
		answer = i

print(answer)