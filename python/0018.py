def main(relative_path):
	from os import path
	from lib.file_util import read_list

	data_file = path.join(path.dirname(path.realpath(__file__)), relative_path)
	data = read_list(data_file)
	data = [[int(j) for j in i.split(" ")] for i in data]

	answer = data[-1]
	for i in reversed(list(range(0, len(data) - 1))):
		previous = answer
		answer = data[i]
		for j in range(0, len(answer)):
			answer[j] = answer[j] + max(previous[j], previous[j+1])

	print(answer[0])

if __name__ == "__main__":
	main("../data/0018.txt")