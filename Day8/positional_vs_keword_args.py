# Function with more than 1 input

def greet_with(name, location):
    print(f"Hello {name} ")
    print(f"What is it like in {location}")

greet_with("Fazal", "Dubai")

# postonal argument
greet_with("Dubai", "Fazal")

# Keyword Argument
greet_with(name="Fazal", location="Dubia")