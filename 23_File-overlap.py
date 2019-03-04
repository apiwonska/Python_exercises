'''
Given two files with numbers in it find the numbers that are overlaping
'''

def get_nums(file):
	with open(file,'r') as file:
		return file.read().rstrip().split('\n')

def get_overlap(file1, file2):	
	return sorted([int(i) for i in get_nums(file1) if i in get_nums(file2)])

print(get_overlap('23_Numbers_1.txt', '23_Numbers_2.txt'))

