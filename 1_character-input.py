
'''
A program that asks the user for name, age and a number (n) and then prints the message n times.
'''

name = input("Please enter your name:  ")
age = int(input("Please enter your age:  "))
print_num = int(input("How many times to print the message?  "))

for num in range(print_num):
	print(f"Dear {name}, in 100 years you will be {age+100} yeas old")

