
age = input("What is your current age? ")

age_int = int(age)

years_remaining = 90 - age_int
days_remaining = years_remaining *365
week_remainings = years_remaining *52
months_remaining = years_remaining *12

print(f"you have {days_remaining} days, {week_remainings}weeks, and {months_remaining} months left")
