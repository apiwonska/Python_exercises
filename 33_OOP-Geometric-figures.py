'''
Create hierarhy of classes represanting geometrical figures. 
Each figure class should be able to calculate perimeter and area. 
Each should have a method returning figure description.
Figures: circle, rectangle, square, triangle
'''

from abc import ABC, abstractmethod
from math import pi, sqrt

class GeometricFigure(ABC):

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f"{self.name}"

	@abstractmethod
	def perimeter(self):
		pass

	@abstractmethod
	def area(self):
		pass

	@property
	def description(self):
		return f"Geometric figure: {self.name}, perimeter: {self.perimeter}, area: {self.area}"

class Circle(GeometricFigure):
	def __init__(self,radius):
		super().__init__(name = "Circle")
		self.radius = radius

	@property
	def perimeter(self):
		return round(pi*self.radius,2)
	
	@property
	def area(self):
		return round(pi*self.radius**2,2)
	

class Rectangle(GeometricFigure):
	def __init__(self,a,b):
		super().__init__(name = "Rectangle")
		self.a = a
		self.b = b

	@property
	def perimeter(self):
		return round(2*(self.a + self.b),2)
	
	@property
	def area(self):
		return round(self.a*self.b,2)

class Triangle(GeometricFigure):
	def __init__(self,a, b, c):
		super().__init__(name = "Triangle")
		self.a = a
		self.b = b
		self.c = c

	@property
	def perimeter(self):
		return round(self.a + self.b + self.c,2)
	
	@property
	def area(self):
		p = 0.5*(self.a+self.b+self.c)
		ar = sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
		return round(ar,2)

class Square(Rectangle, GeometricFigure):
	def __init__(self, a):
		super().__init__(a, b = a)
		GeometricFigure.__init__(self, name = "Kwadrat")

def main():
	c = Circle(3)
	print(c.description)

	r = Rectangle(2,3)
	print(r.description)

	s = Square(3)
	print(s.description)

	t = Triangle(3,3,3)
	print(t.description)


if __name__ == "__main__":
	main()
	
