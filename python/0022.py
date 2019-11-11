from os import path
from lib.file_util import read_list

data_file = path.join(path.dirname(path.realpath(__file__)), "../data/0022.txt")
data = read_list(data_file)
data = [i.replace('"', '') for i in data[0].split(",")]

data.sort()
mylist = []
for index, value in enumerate(data):
	string_list = list(value)
	value = sum([(ord(i) - ord('A') + 1) for i in string_list])
	mylist.append(value * (index + 1))

print(sum(mylist))