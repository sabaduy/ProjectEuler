import functools
from os import path
from lib.file_util import read_list, write_list

data_file = path.join(path.dirname(path.realpath(__file__)),"./0008.txt")
data = ''.join(read_list(data_file))

count = 13
answer = 0
for i in range(0, len(data) - count):
	temp = [int(j) for j in data[i:i+count]]
	product = functools.reduce(lambda a, b: a * b, temp)
	if product > answer:
		answer = product

print(answer)
