answer = set()

for a in range(2,101):
	for b in range(2,101):
		answer.add(a**b)

print(len(answer))