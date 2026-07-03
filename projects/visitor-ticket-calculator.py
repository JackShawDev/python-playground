print("Welcome to the theme park!")

print()

name = input("What is your name? ")
age = int(input("How old are you? "))
guidebook = input("Do you want a guidebook? (Y/N) ")

is_valid = True

print()

print("Hello " + name + "!")

print()

if age < 0:
    print("Please enter an age above 0.")
    is_valid = False
elif age > 150:
    print("Please enter an age below 150.")
    is_valid = False
else:
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
elif guidebook == "N":
    guidebook_price = 0
    print("You have not opted for a guidebook.")
else:
    print("Invalid input. Please enter Y or N.")
    is_valid = False

if is_valid:
    total_price = ticket_price + guidebook_price

print()

print("Ticket type: " + ticket_type)
print("Ticket price: £" + str(ticket_price))
print("Guidebook price: £" + str(guidebook_price))

print()

print("Total price: £" + str(total_price))