print("Welcome to the Science Museum!")

print()

name = input("What is your name? ")
age = int(input("How old are you? "))

print()

print("Hello " + name + "!")

print()

if age < 0:
    print("Please enter an age above 0.")
elif age > 120:
    print("Please enter an age below 120.")
elif age < 5:
    print("Your entry is free!")
elif age <= 15:
    print("Child ticket: £5")
else:
    print("Adult ticket: £10")

"""
Currently I have no experience with loops but want to add some rudimentary verification to the age input.
"""