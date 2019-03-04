'''
Makes calculations on fractions
'''
from math import gcd

class Fraction():

	def __init__(self, numerator, denominator):
		self.num = numerator
		self.den = denominator 

	def __str__(self):
		return f"{self.num}/{self.den}"

	# Skracanie ułamków
	def cancelling_down(self):
		greatest_common_divisor = gcd(self.num, self.den)
		self.num //= greatest_common_divisor
		self.den //= greatest_common_divisor
		# return self

	@staticmethod
	def add(f1, f2):
		num = f1.num*f2.den + f2.num*f1.den
		den = f1.den*f2.den
		result = Fraction(num,den).cancelling_down()
		return result

	@staticmethod
	def substract(f1, f2):
		num = f1.num*f2.den - f2.num*f1.den
		den = f1.den*f2.den
		result = Fraction(num,den).cancelling_down()
		return result

	@staticmethod
	def multiply(f1, f2):
		num = f1.num*f2.num
		den = f1.den*f2.den
		result = Fraction(num,den).cancelling_down()
		return result

	@staticmethod
	def divide(f1, f2):
		num = f1.num*f2.den
		den = f1.den*f2.num
		result = Fraction(num,den).cancelling_down()
		return result
		
def get_two_fractions():
	print("Podaj dwa ułamki zwykłe")
	fractions = [None, None]
	for i in range(2):
		print(f"\nUłamek {i+1}:\n")
		numerator,denominator = 'a','a'
		while True:
			numerator = input("Podaj licznik:  ")
			denominator = input("Podaj mianownik (różny od 0):  ")
			if (
				numerator.isdigit() and	
				denominator.isdigit() and 
				denominator != '0' 
				):
				break
			else:
				print("Licznik i mianownik muszą być liczbami całkowitymi.\nMianownik musi być różny od zera.")

		fractions[i] = Fraction(int(numerator), int(denominator))
	print("\nUłamek 1: ",fractions[0],", Ułamek 2: ",fractions[1])
	return fractions

def main():

	print("\nProgram wykonuje operacje na ułamkach zwykłych.\n")

	action= input("Co chcesz zrobić?\n(1) Dodać\n(2) Odjąć\n(3) Pomnożyć\n(4) Podzielić\n")

	fractions = get_two_fractions()
	if action == '1':
		add_fractions = Fraction.add(fractions[0], fractions[1])
		print(f"{fractions[0]} + {fractions[1]} = {add_fractions}")
	elif action == '2':
		substract_fractions = Fraction.substract(fractions[0], fractions[1])
		print(f"{fractions[0]} - {fractions[1]} = {substract_fractions}")
	elif action == '3':
		multiply_fractions = Fraction.multiply(fractions[0], fractions[1])
		print(f"{fractions[0]} * {fractions[1]} = {multiply_fractions}")
	elif action == '4':
		divide_fractions = Fraction.divide(fractions[0], fractions[1])
		print(f"{fractions[0]} / {fractions[1]} = {divide_fractions}")

if __name__ == '__main__':

	main()


