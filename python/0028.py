dimensions = 1001

mylist = [1]
layer = 0
counter = 0

while mylist[-1] <= dimensions**2:
	if counter % 4 == 0:
		layer += 1

	mylist.append(2*layer + mylist[-1])
	counter += 1

mylist.pop()

print(sum(mylist))
