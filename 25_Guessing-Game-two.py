'''
The user picks a number between 0 and 100 and the program tries to guess it.
'''
from random import randint

print("\n >>>> GUESSING GAME 2 <<<<\n")

print("Pick a number between 0 and 100 and the program will try to guess it\n")
print("Press 'y' if the program choose your number.")
print("Press 'l' if your number is lower.")
print("Press 'h' if your number is heigher.")
print("To exit the program write 'q'\n")
input("Press 'Enter' when you are ready\n")

min_n = 0
max_n = 100
counter = 0

while True:	
	# Picking the number
	guess = randint(min_n,max_n)
	counter += 1

	# Checking possible solutions
	answers = ['y','l','h','q']
	if min_n==max_n:		# Only one solution
		print(f"\nThe number is {guess}! The program guessed the number in {counter} approach.\n")
		break
	elif guess==min_n:		# Possible only heigher or equal numbers
		answers.remove('l')
	elif guess==max_n:		# Possible only lower or equal numbers
		answers.remove('h')
	answers_str = '/'.join(answers)

	# Checking the guess with the user
	answer = ''
	while answer not in answers:
		answer = input(f"{counter} try: Is it {guess}? ({answers_str}) ").lower()
	
	# Taking the acction according to the answer. Updating min and max values
	if answer=='y': 
		print(f"\nThe number is {guess}! The program guessed the number in {counter} approach.\n")
		break
	elif answer=='q':	
		break
	elif answer=='l': 
		max_n=guess - 1
	elif answer=='h': 
		min_n=guess + 1





	


