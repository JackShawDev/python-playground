print("Welcome!")

print()

name = input("What is your name? ")
age = int(input("How old are you? "))
current_year = int(input("What year is it? "))
birth_year = current_year - age

print()

print("Hello " + name + "!")

print()

print("You are " + str(age) + " years old in " + str(current_year) + ".")

print()

print("You were probably born in " + str(birth_year) + " or " + str(birth_year - 1) + ".")

"""
Opted to use current year instead of hardcoding 2026 to make the program more flexible and accurate for future use, this however makes it a bit less user friendly.
In the future I would expect to be able to get the date from the system but I don't have that knowledge yet.
Another improvement would be asking for date of birth (most accurate but invasive) or asking for the month of birth (less accurate but less invasive).
A cruder version I could implement would be to ask if the user has had their birthday yet this year, and then calculate the birth year based on that, but would require more user input and booleans which I haven't learned yet.
"""