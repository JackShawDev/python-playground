def display_welcome():
    print("Welcome to the theme park!")

def greet_user(name):
    print("Hello " + name + "!")

def get_valid_age():
    age = -1 #sets the age variable to -1 so that the while loop will run at least once

    while age < 0 or age > 150: #this loop will continue to run until the user enters a valid age between 0 and 150
        age = int(input("How old are you? "))

        if age < 0:
            print("Please enter an age of 0 or higher.")
        elif age > 150:
            print("Please enter an age below 150.")

    return age

def get_guidebook_choice():
    guidebook = "" #sets the guidebook variable to an empty string so that the while loop will run at least once

    while guidebook != "Y" and guidebook != "N": #this loop will continue to run until the user enters either Y or N
        guidebook = input("Do you want a guidebook? (Y/N) ")

        if guidebook != "Y" and guidebook != "N":
            print("Please enter Y or N.")
    
    return guidebook


def calculate_ticket_price(age):
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

    return ticket_type, ticket_price    

def calculate_guidebook_price(guidebook):
    if guidebook == "Y":
        guidebook_price = 3
    else:
        guidebook_price = 0

    return guidebook_price

display_welcome()
print()

name = input("What is your name? ")
print()

greet_user(name)
print()

age = get_valid_age()
print()

guidebook = get_guidebook_choice()
print()

ticket_type, ticket_price = calculate_ticket_price(age)
guidebook_price = calculate_guidebook_price(guidebook)
total_price = ticket_price + guidebook_price

print("Ticket type: " + ticket_type)
print("Ticket price: £" + str(ticket_price))
print("Guidebook price: £" + str(guidebook_price))
print()

print("Total price: £" + str(total_price))

"""
Week 1 mini project - Visitor Ticket Calculator 
General layout and structure of the program is complete, but there are some issues with the input validation.

Week 2 Day 1 update - input validation has been added to the age and guidebook inputs, but there are still some issues with the input validation, for example if the user enters a non-integer value for age, the program will crash.

Week 3 Day 1 update - After learning the basics of functions I came back to refactor this project. Moved welcome message, user greeting, age and guidebook validation and pricing systems into functions, the core idea being each function should cover one task. 
This allowed me to remove the is_valid variable as it could no longer be false as the loops won't allow the program to move on unless the user inputs valid data.
This has improved readability, in a real world scenario now if a price change was to happen it's just in one place in it's own function rather than digging through the whole program.
No function for name as there is no validation or transformation with this content right now, this also applies to total_price.
It will also allow me to add new functions going forward such as discounts, special offers etc
Another improvement I want to make with the program is changing total price into a receipt, if you select N for the guidebook it shouldn't need to display Guidebook price: £0
"""