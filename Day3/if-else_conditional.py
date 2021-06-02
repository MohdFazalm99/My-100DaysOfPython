# IF-ELSE statement
# SYNTAX
# if condition:
#   do this
# else:
#  do this

# Comparison Operators used in IF-ELSE

# > - Greater than
# > - less than
# >= - Greater than or equal to
# <= - less than or equal to
# == - equal to
# != - NOT equal to

# Expample 1
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry! you have grow-up taller to ride the rollercoaster\n")

# Example 2
number = int(input("Which number do you want to check? "))

if number % 2 ==0:
  print(f"{number} is an even")
else:
  print(f"{number} is an odd")
