
'''
Asks the user for a number and checks if it's odd or even
'''

num = int(input("Please enrer a number: "))

if num%4==0:
	print(num, 'is even and a multiple of 4')
elif num%2==0:		
	print(num, 'is even')
else:
	print(num, 'is odd')