'''
Ask the user for a string and print out whether this string is a palindrome or not. 
'''

text = (input("Palindrome check. Please enter text:  ")).lower()
if text == text[::-1]:
	print("The text is a palindrome")
else:
	print("The text is not a palindrome")