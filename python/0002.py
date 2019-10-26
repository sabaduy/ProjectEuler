from lib.fib import fib

mylist = fib(4000000)
mylist = [i for i in mylist if i % 2 == 0]
print(sum(mylist))