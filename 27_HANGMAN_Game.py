'''
Hangman game
  _
 | |
 |
/|\

'''
from random import choice

def get_letter():
	'''
	asks for user input
	returns: letter
	rtype: str
	'''
	letter= ''
	while not letter.isalpha() or len(letter)!=1 :
		letter = input("Guess your letter:  ").upper()	
		if letter == 'EXIT':
			break	
	return letter

def place_letter(letter):
	'''
	checks if the letter is in the word
	'''
	global counter, word, guessed
	if letter in word:
		for i in range(0,len(word)):
			if word[i]==letter:
				guessed[i]=letter
		print('\n',' '.join(guessed),'\n')
	else:
		counter-=1
		print(f"This letter is not in the word. Try again! You have {counter} more chances")


if __name__ == '__main__':

	print(" >>>> Welcome to HANGMAN GAME! <<<< \n")
	print("(Type 'exit' if you want to quit)")

	# Program picks the word from dictionary in external file
	words = [w.rstrip() for w in open('27_sowpods.txt','r').readlines()]
	word = choice(words)

	guessed = ['_' for w in word]
	print(' '.join(guessed),'\n')

	counter = 7		# number of mistakes that the user can make

	# ask user for letter and show if the letter is in the word
	while '_' in guessed and counter!=0 :
		letter = get_letter()
		if letter == 'EXIT':
			break
		elif letter in guessed:
				print("You already have this letter. Choose different letter!")
		else:
			place_letter(letter)

	# Result of the game
	if word==guessed:
	 print(f"Congratulations! You guessed in {counter} attempts\n")
	else:
		print('\n',word)
		print("\n>>>> END <<<<")
		if counter==0:
			print("     _\n    | |\n    |\n   /|\\\n")


	






