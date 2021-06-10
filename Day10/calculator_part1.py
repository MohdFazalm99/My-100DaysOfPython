#Calculator

# ADDITION
def add(n1, n2):
  return n1 + n2

# SUBSTRACTION
def subtract(n1, n2):
  return n1 - n2

# MULTIPLICATION
def multiply(n1, n2):
  return n1 * n2

# DIVISION
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
  print(symbol)


operation_symbol = input("Pick an operation: ") 
num2 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

#Here we select "*" which overides the "+" we selected on line 26.
operation_symbol = input("Pick an operation: ") 
num3 = int(input("What's the next number?: "))

#Here the calculation_function selected will be the multiply() function
calculation_function = operations[operation_symbol] 
second_answer = calculation_function(calculation_function(num1, num2), num3)
second_answer = calculation_function(first_answer, num3)


print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
