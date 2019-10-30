import functools
from os import path
from lib.file_util import read_list

data_file = path.join(path.dirname(path.realpath(__file__)),"../data/0011.txt")
data = read_list(data_file)
data = [[int(j) for j in i.split(' ')] for i in data]

num_rows = len(data)
num_cols = len(data[0])


num_count = 4

best_method = 0 # 1 = Horizontal, 2 = Vertical, 3 = TL -> BR, 4 = TR -> BL
best_row    = 0
best_col    = 0
answer      = 0



# Horizontal check
for row in range(0,num_rows):
	for col in range(0,num_cols-num_count):
		temp = [data[row][col+i] for i in range(0,num_count)]
		temp_answer = functools.reduce(lambda a, b: a * b, temp)
		if temp_answer > answer:
			best_method = 1
			best_row    = row
			best_col    = col
			answer      = temp_answer

# Vertical check
for row in range(0,num_rows-num_count):
	for col in range(0,num_cols):
		temp = [data[row+i][col] for i in range(0,num_count)]
		temp_answer = functools.reduce(lambda a, b: a * b, temp)
		if temp_answer > answer:
			best_method = 2
			best_row    = row
			best_col    = col
			answer      = temp_answer

# TL - >BR check
for row in range(0,num_rows-num_count):
	for col in range(0,num_cols-num_count):
		temp = [data[row+i][col+i] for i in range(0,num_count)]
		temp_answer = functools.reduce(lambda a, b: a * b, temp)
		if temp_answer > answer:
			best_method = 3
			best_row    = row
			best_col    = col
			answer      = temp_answer

# TR - >BL check
for row in range(0,num_rows-num_count):
	for col in range(0,num_cols-num_count):
		temp = [data[row+i][col+num_count-1-i] for i in range(0,num_count)]
		temp_answer = functools.reduce(lambda a, b: a * b, temp)
		if temp_answer > answer:
			best_method = 4
			best_row    = row
			best_col    = col
			answer      = temp_answer

# print(best_method, best_row, best_col, answer)
print(answer)