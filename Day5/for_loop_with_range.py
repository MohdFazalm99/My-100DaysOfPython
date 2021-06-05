"""
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

Syntax

range(start, stop, step)
Parameter Values
Parameter	Description
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1

"""

# Ex 1 simple
for num in range(1,11):
    print(num)

# Ex 2 WIth increment
for num in range(1,11, 2):
    print(num)

# Ex 3 
total = 0
for number in range(1,101):
    total += number
print(total)