'''
Asks for a number and returns a list of divisors
'''

number = int(input("Please enter a number:  "))

divisors = [ n for n in range(1,number//2+1) if number%n == 0]
divisors.append(number)

print("List of divisors of a given number:  ", divisors)