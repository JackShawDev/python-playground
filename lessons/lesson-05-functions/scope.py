""" Experiment 1
def greet():
    name = "Jack"

    print("Inside before:", name)

    name = "Bob"

    print("Inside after:", name)

name = "Alice"

greet()

print("Outside:", name)
"""

""" Experiment 2
name = "Alice"

def greet():
    print(name)

greet()
"""

name = "Alice"

def greet():
    print("1.", name)

    name = "Jack"

    print("2.", name)

greet()

print("3.", name)