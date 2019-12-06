# Reference for Upper Bound: https://www.mathblog.dk/project-euler-30-sum-numbers-that-can-be-written-as-the-sum-fifth-powers-digits/
#
# Basically, we need to find x for x(9^5) where x is the number of digits from 9^5
# Do this until x is no longer increased
# Step 1 ==> 9^5 = 59049 ==> x = 5
# Step 2 ==> 5(9^5) = 295246 ==> x = 6
# Step 3 ==> 6(9^5) = 354294 ==> x = 6 ==> Done!
# 354294 is a good upper bound

mylist = []

for number in range(2,354295):
	temp = [int(i)**5 for i in str(number)]
	if sum(temp) == number:
		# print(number)
		mylist.append(number)

print(sum(mylist))