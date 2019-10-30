maximum = 1000000

longest = []
for i in range(1,maximum):
	chain = [i]
	current = i
	while current != 1:
		if current % 2 == 0:
			current = current // 2
			chain.append(current)
		else:
			current = (current * 3) + 1
			chain.append(current)

	if len(chain) > len(longest):
		longest = chain

print(longest[0])