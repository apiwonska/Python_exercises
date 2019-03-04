'''
Asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order.
'''

def reverse_str(str):
	return ' '.join(str.split(' ')[::-1])

text = input("Write a string containing multiple words:  ")
print("Here is the reversed string:  ",reverse_str(text))