print("Welcome to the theme park!")

print()

name = input("What is your name? ")

age = -1 #sets the age variable to -1 so that the while loop will run at least once

while age < 0 or age > 150: #this loop will continue to run until the user enters a valid age between 0 and 150
    age = int(input("How old are you? "))

    if age < 0:
        print("Please enter an age of 0 or higher.")
    elif age > 150:
        print("Please enter an age below 150.")

guidebook = "" #sets the guidebook variable to an empty string so that the while loop will run at least once

while guidebook != "Y" and guidebook != "N": #this loop will continue to run until the user enters either Y or N
    guidebook = input("Do you want a guidebook? (Y/N) ")

    if guidebook != "Y" and guidebook != "N":
        print("Please enter Y or N.")

is_valid = True

print()

print("Hello " + name + "!")

print()

if age < 5:
    ticket_type = "Free entry"
    ticket_price = 0
elif age <= 15:
    ticket_type = "Child ticket"
    ticket_price = 5
elif age <= 64:
    ticket_type = "Adult ticket"
    ticket_price = 10
else:
    ticket_type = "Senior ticket"
    ticket_price = 7

if guidebook == "Y":
    guidebook_price = 3
    print("You have opted for a guidebook.")
else:
    guidebook_price = 0
    print("You have not opted for a guidebook.")


if is_valid:
    total_price = ticket_price + guidebook_price

    print()

    print("Ticket type: " + ticket_type)
    print("Ticket price: £" + str(ticket_price))
    print("Guidebook price: £" + str(guidebook_price))

    print()

    print("Total price: £" + str(total_price))

"""
Week 1 mini project - Visitor Ticket Calculator 
General layout and structure of the program is complete, but there are some issues with the input validation.

Week 2 Day 1 update - input validation has been added to the age and guidebook inputs, but there are still some issues with the input validation, for example if the user enters a non-integer value for age, the program will crash.
"""