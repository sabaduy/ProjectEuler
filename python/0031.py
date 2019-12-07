coins = [1,2,5,10,20,50,100,200]
target = 200

table = [0 for i in range(0,target + 1)]
table[0] = 1

for coin in coins:
	temp = coin
	while temp <= target:
		table[temp] += table[temp - coin]
		temp += 1

print(table[target])



