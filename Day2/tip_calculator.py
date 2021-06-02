print("Welcome to the tip calculaotr. ")

total_bill = input("What was the total bill? ")
percent_tip = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")

total_bill_int = int(total_bill)
percent_tip_int = int(percent_tip)
people_int = int(people)

bill_pay = (total_bill_int/people_int) * (percent_tip_int/100)

print(f"Each person should pay {round(bill_pay,2)}")