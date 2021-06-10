
# calculator

# ADD
def add(n1, n2):
    return n1 + n2

# SUBTRACT
def subtract(n1, n2):
    return n1 - n2

# MULTIPLY
def multiply(n1, n2):
    return n1 * n2

# DIVIDE
def divide(n1, n2):
    return n1 / n2


# OPERATIONS IN DICT
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}


num1 =int(input("What is the first number?: "))
for symbols in operations:
    print(symbols)
operation_symbol = input("Pick an operation from the line above: ")
num2 =int(input("What is the second number?: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")