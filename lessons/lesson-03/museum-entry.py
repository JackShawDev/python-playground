print("Welcome to the Science Museum!")

print()

name = input("What is your name? ")
age = int(input("How old are you? "))

print()

print("Hello " + name + "!")

print()

if age < 5:
    print("Your entry is free!")
elif age <= 15:
    print("Child ticket: £5")
else:
    print("Adult ticket: £10")

