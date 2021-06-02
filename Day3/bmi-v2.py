
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi_value = weight/(height **2)

bmi = round(bmi_value, 2)


#  Under 18.5 they are underweight
if bmi < 18.5:
  print(f"Your BMI value is {bmi}, you are underweight")

# - Over 18.5 but below 25 they have a normal weight
elif bmi >18.5 or bmi < 25:
  print(f"Your BMI value is {bmi}, you are normal weight")

# - Over 25 but below 30 they are slightly overweight
elif bmi > 25 or bmi < 30:
  print(f"Your BMI value is {bmi}, you are overweight")

# - Over 30 but below 35 they are obese
elif bmi >30 or bmi < 35:
  print(f"Your BMI value is {bmi}, you are obese")

# - Above 35 they are clinically obese.
else:
  print(f"Your BMI value is {bmi}, you are clinically obese")