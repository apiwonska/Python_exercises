'''
Generates password
'''

from random import choice
from string import ascii_letters, digits

def password_personal(str):
	password = [ word[0] for word in str.split(' ')]
	for i in range(len(password)):
		if password[i].lower() =='a':	
			password[i]='@'
		elif password[i].lower()=='o':	
			password[i]='0'
	return ''.join(password)

def password_random(num):
	characters = ascii_letters + digits + '!#$%&()+-/:;@[\\]^_|~'
	return ''.join( choice(characters) for n in range(num) )
 
strength = ''
while (strength != 'p') and (strength != 'r'):
	strength = input("Do you want a personal password easy to remember or a random password? p/r  ").lower()

if strength == 'p':
	sentence = ''
	while len(sentence.split(' ')) < 8 :
		sentence = input("Please enter a string of at least 8 words:\n")
	print('Password:',password_personal(sentence))

elif strength == 'r':
	num = 0
	while num < 8:
		num = int(input("Please enter the length of the password (minimum 8):  "))
	print('Password:',password_random(num))
