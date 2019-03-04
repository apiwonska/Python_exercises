'''
Calculates quadratic function roots or value.
'''

class QuadraticFunction():
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c

	def __str__(self):
		return f"Funkcja kwadratowa postaci: f(x) = {self.a}x^2 + {self.b}x + {self.c}"

	def calculate_value(self):
		x = int(input("Podaj argument funkcji:  "))
		y = self.a*x**2 + self.b*x + self.c
		print(f"Wartość funkcji dla argumentu {x}: {y}") 

	def calculate_zeros(self):
		delta = self.b**2 - 4*self.a*self.c
		if delta  == 0:
			x = -self.b/(2*self.a)
			print(f"Funkcja ma jedno miejsce zerowe {x}")
		elif delta > 0 :
			x1 = (-self.b + (delta)**0.5)/(2*self.a)
			x2 = (-self.b - (delta)**0.5)/(2*self.a)
			print(f"Funkcja ma dwa miejsca zerowe {round(x1, 2)}, {round(x2, 2)}")
		else:
			print("Funkcja nie ma miejsc zerowych")

def get_factors_for_quadratic_function():
	a,b,c = None, None, None
	while a == 0 or type(a) != float or type(b) != float or type(c) != float:
		print("\nPodaj współczynniki funkcji kwadratowej a,b,c:  ")
		try: 
			a = float(input("a:  "))
			b = float(input("b:  "))
			c = float(input("c:  "))
		except:
			print("'a', 'b', 'c' muszą być liczbami rzeczywistymi")
		if a == 0:
			print("'a' nie może być równe 0")
	return [a,b,c]


if __name__ == "__main__":

	print("\nTen program sprawdza miejsca zerowe funkcji kwadratowej lub liczy wartość funcji")

	factors = get_factors_for_quadratic_function()
	function = QuadraticFunction(factors[0],factors[1],factors[2])
	print(function)

	while True:		
		action = input("Co chcesz zrobić? \n(1) Sprawdź miejsca zerowe \n(2) Policz wartość funkcji \n(z) Zakończ\n")
		print("\n")
		if action == 'z':
			break
		elif action == '1':
			function.calculate_zeros()
			print("\n")
		elif action == '2':
			function.calculate_value()
			print("\n")




	
	

