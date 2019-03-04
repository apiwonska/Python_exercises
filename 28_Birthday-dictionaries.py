'''
A program that stores information about birthday dates in separate file.
- you can check who's birthday is in
- you can check birthday date of a specific person
- you can add entry
'''
'''
Stores information about birthday dates in external file
You can check, add or delete informations.
'''
import os
import json


def read_bday():
    '''
    Printout all the names from external file.
    return: None
    '''
    with open(file_name, 'r') as file:
        names = dict(json.load(file))
    if any(names):
        print("\nWe know the birthday of: ")
        for n in names.keys():
            print(n)
    else:
        print("Bday dictionary is empty")


def check_bday():
    '''
    Asks user for a name and checks bday date in external file
    return: None
    '''
    with open(file_name, 'r') as file:
        names = dict(json.load(file))

    while True:
        # asks for a name
        name = input("\nWho's birthday do you want to look up?:  ")
        # checks for the birthday date in the dictionary
        if name in names.keys():
            print(f"\n{name}'s' birthday is {names[name]}")
        else:
            print("\nThere is no such name in the dictionary")
        # Check if the user want to continue
        repeat = input("\nPress 'c' if you want to check another one:  ")
        if repeat != 'c':
            break


def add_bday():
    '''
    Ask the user for name and bday date.
    Add these data into the file.
    Return: None
    '''
    name = input("\nName:  ")
    bday = input("Birthday (dd/mm/yyyy format):  ")

    with open(file_name, 'r') as file:
        names = dict(json.load(file))
    names[name] = bday

    with open(file_name, 'w') as file:
        json.dump(names, file, sort_keys=True, ensure_ascii=False)


def remove_bday():
    '''
    Ask the user for name and removes the record from external file.
    Return: None
    '''
    name = input("\nName:  ")

    with open(file_name, 'r') as file:
        names = dict(json.load(file))
    names.pop(name)

    with open(file_name, 'w') as file:
        json.dump(names, file, sort_keys=True, ensure_ascii=False)
    print(f"{name} was removed from bday dictionary")


if __name__ == '__main__':

    print("\n>>>> Welcome to the birthday dictionary. <<<<\n")

    file_name = "28_Birthday-dictioneries.json"
    # Checks if the external file exist and if not it creates it
    if not os.path.exists(file_name):
        names = ''
        with open(file_name, 'w') as file:
            json.dump(names, file, sort_keys=True, ensure_ascii=False)

    while True:
        action = []
        while action not in ['1', '2', '3', '4']:
            action = input(
                "What do you wand to do? \n(1) See all content of bday dictionary\n(2) Check birthday\n(3) Add record \n(4) Remove record \nPress (1,2,3 or 4):  ")
        # See current content od bday dictionary
        if action == '1':
            read_bday()
        # Checks birthday
        elif action == '2':
            check_bday()
        # Add record to bday dictionary
        elif action == '3':
            add_bday()
        # Add record to bday dictionary
        elif action == '4':
            remove_bday()
        # Check if user want to continue
        repeat = input("\nPress 'c' if you want to continue:  ")
        if repeat != 'c':
            break
