import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")



# Get the total number of items in list
num_items = len(names)

# Generate random numbers between 0 and the last index
random_choice =random.randint(0,num_items -1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay+ " is going to buy the meal today!")


# We can also use random.choice() function
"""The choice() method returns a randomly selected element from the specified sequence.

The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

Example

import random

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))"""