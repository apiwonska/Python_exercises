'''
Guessing game 1
'''

from random import randint
print("\n >>>  GUESSING GAME  <<< \n")

num = randint(1,9)
guess = int(input("I choose a number between 1 and 9 (inclusive). Try to guess the number: "))
count = 1

while guess != num:
	if guess > num:
		guess = int(input("Too height! Try again:  "))
	else:
		guess = int(input("Too low! Try again:  "))
	count += 1

print(f" !!! BINGO !!!\n You guessed in {count} tries. The number is {num}")