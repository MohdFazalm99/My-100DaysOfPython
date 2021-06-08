# Dictionary

"""Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:
"""
# Crearting List
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }

# Retrieving items from dictionary
print(programming_dictionary["Function"])

# Adding new items to dictioany.
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary) 

#Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dict
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in s dicionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through dict
for key in programming_dictionary:
    print(programming_dictionary[key])
    print(key)
