# Nested IF_ELSE statement

# SYNTAX
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

# Expample 1
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age? "))
  if age <=18:
      print("Please pay $7.")
  else:
        print("Please pay $12.")
else:
  print("Sorry! you have grow-up taller to ride the rollercoaster\n")

# Elif 

# SYNTAX

# if condition1:
#   do A 
# elif conditio2:
#   do B 
# else:
#   do this

# Expample 2
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age? "))
  if age <12:
      print("Please pay $5.")
  elif age <=18:
    print("Please pay $7")
  else:
        print("Please pay $12.")
else:
  print("Sorry! you have grow-up taller to ride the rollercoaster\n")
