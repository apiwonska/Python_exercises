'''
Determine whether the number is prime or not.
'''

def is_prime(num):	
	if (num > 1) and (len([i for i in range(2,num//2+1) if num%i == 0]) == 0):
		return f"{num} is a prime number"
	return f"{num} is not a prime number"

number = int(input("Please enter a number:  "))
print(is_prime(number))