'''
Returns a list that contains only the elements that are common between the lists.
'''
from random import randint

a = [ randint(0,30) for i in range(randint(10,15))]
b = [ randint(0,30) for i in range(randint(10,15))]
a.sort()
b.sort()

common = [ i for i in a if i in b]
common.sort()
common = [ common[i] for i in range(len(common)) if i==0 or (i!=0 and common[i]!=common[i-1]) ]

print('First list:  ', a)
print('Second list:  ', b)
print('Intersection:  ', common)

