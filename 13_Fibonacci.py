'''
Printing Fibonacci numbers
'''

def fibonacci(n):
	fib = []
	for i in range(0,n):
		if i==0 or i==1:
			fib.append(1)
		else:
			fib.append(fib[i-1]+fib[i-2])
	return fib

num = int(input("How many Fibonacci numbers to print:  "))

print(f"Here you have first {num} Fibonacci numbers: ", *fibonacci(num))
