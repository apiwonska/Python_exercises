''' 
Takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
'''
from random import randint, sample

def num_in_list(a_list,n):
	if n in a_list:
		return True
	return False


nums = sample(range(0,25),randint(10,15))
nums.sort()
num = randint(0,25)

print(f"Checking if number = {num} is in the list = {nums}")

print(num_in_list(nums,num))