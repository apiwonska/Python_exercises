'''
Given a .txt file that has a list of a bunch of names, counts how many of each name there are in the file.
Prints out the results to the screen. 
'''

with open('22_Names.txt','r') as file:
	all_names = file.read().rstrip().split('\n')
	names = { n: all_names.count(n) for n in set(all_names)}

	print(names)
