from os import path
from lib.file_util import read_list

data_file = path.join(path.dirname(path.realpath(__file__)),"../data/0018.txt")
data = read_list(data_file)
data = [[int(j) for j in i.split(" ")] for i in data]

answer = data[-1]
for i in reversed(list(range(0, len(data) - 1))):
	previous = answer
	answer = data[i]
	for j in range(0, len(answer)):
		answer[j] = answer[j] + max(previous[j], previous[j+1])

print(answer[0])