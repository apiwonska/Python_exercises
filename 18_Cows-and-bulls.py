'''
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
'''

from random import randint
from string import digits

def get_guess():
	'''
	Accepts a 4 digit number and converts it to a list
	rtype: list
	'''
	guess_str = ''
	while (len(guess_str) != 4) or any(i not in digits for i in guess_str):
		guess_str= input("Enter 4 digit number:  ")
	return [int(guess_str[i]) for i in range(4)]

def cowbullcount(num,guess):
	'''
	Counts cows and bulls	
	rtype: boolean
	''' 
	c, b = 0, 0
	n = number.copy()
	g = guess.copy()
	global count
	for i in reversed(range(4)):
		if guess[i]==number[i]:
			c += 1
			g.pop(i)
			n.pop(i)
	for i in range(len(g)):
		if g[i] in n:
			b += 1
			n.remove(g[i])
	count += 1
	print(f"{c} cows, {b} bulls")
	if c==4:
		return True
	return False

print("\n >>>> Welcome to the COWS AND BULLS GAME! <<<< \n")

number = [randint(0,9) for i in range(4)]
count = 0
success = False

while not success:
	guess = get_guess()	
	success = cowbullcount(number, guess)

print(f"\n >>>> SUCCESS <<<< \nYou won in {count} round(s)\n")