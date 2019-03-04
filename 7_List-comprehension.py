'''
Accepts a list and prints a list that has only even numbers in it
'''

values = []

print('Please, enter values')

while True:
	val = input()
	if val == '':
		break
	else:
		val=int(val)
		values.append(val)

values2 = [ v for v in values if v%2 == 0 ]
print("Even values", values2)