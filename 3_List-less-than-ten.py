'''
Shows a new list with numbers smaller than a number given by the user
'''

values = input("Enter a list of numbers (e.g.: '1, 1, 2'):  \n")
values = [ int(n.strip()) for n in values.split(",")]

max_num = int(input("Please enter a maximum number. The list will be filtered for the numbers smaller than maximum number "))

values_filtered = [ n for n in values if n < max_num ]

print("Filtered list:", values_filtered)


