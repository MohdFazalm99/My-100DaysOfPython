# List 

""" Lists are used to store multiple items in a single variable .
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

"""

states_of_america = ["Dalaware", "Pennsylvania","New Jersey", "New York", "Texas", "Arizona", "Washington"]

print(states_of_america[3])
print(states_of_america[-1])

# Altering the items in list
states_of_america[1] = "Uttar Pardesh"
print(states_of_america[1])

# Adding new item in the list or "append"
states_of_america.append("Fazalistan")
print(states_of_america[-1])

