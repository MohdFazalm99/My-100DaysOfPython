total = 0

for num in range(2,101,2):
    total += num
print("Sum of all even number between 2 & 100 is =" ,total)

total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        total2 += number
print(total2)