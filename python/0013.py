import functools
from os import path
from lib.file_util import read_list

data_file = path.join(path.dirname(path.realpath(__file__)),"../data/0013.txt")
data = read_list(data_file)
data = [int(i) for i in data]

answer = sum(data)

print(str(answer)[0:10])