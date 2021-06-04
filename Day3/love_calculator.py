
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


# Here we are combining the names for counting
combined_string = name1 + name2

# Here we are converting the string into lowercase
lower_case_string = combined_string.lower()

# Logic of love calculator
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e


l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

# here we are again concatinating the strings, and agin in order to concatinate these numbers we have to convert it itno integer 
love_score = int(str(true) + str(love))

print(love_score)

if (love_score < 10) or (love_score > 90):
  print(f"your love score is {love_score}, you go together like coke and mentos")

elif (love_score >=40) and (love_score <= 50):
   print(f"your love score is {love_score}, you are alright together")

else:
  print(f"your love score is {love_score}")
