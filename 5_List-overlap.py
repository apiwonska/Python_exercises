'''
Returns a list that contains only the elements that are common between the lists.
'''
from random import randint

a = [ randint(0,30) for i in range(randint(10,15))]
b = [ randint(0,30) for i in range(randint(10,15))]
a.sort()
b.sort()

common = list(set(a)&set(b))
common.sort()

print('First list:  ', a)
print('Second list:  ', b)
print('Intersection:  ', common)

