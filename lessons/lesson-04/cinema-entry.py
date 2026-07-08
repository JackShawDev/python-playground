print("Welcome to the cinema!")

print()

name = input("What is your name? ")

print()

print("Hello " + name + "!")

print()

age = -1 

while age < 0 or age > 120: 
    age = int(input("How old are you? "))

    if age < 0:
        print("Please enter an age of 0 or higher.")
    elif age > 120:
        print("Please enter an age below 120.")

film_rating = ""

while film_rating != "Y" and film_rating != "N": 
    film_rating = input("Is the film rated 18+? (Y/N) ")

    if film_rating != "Y" and film_rating != "N":
        print("Please enter Y or N.")
    else:
        if film_rating == "Y" and age < 18:
            print("Sorry, you cannot watch this film as it is rated 18+.")
        else:
            is_member = "" 

            while is_member != "Y" and is_member != "N": 
                is_member = input("Are you a member? (Y/N) ")

                if is_member != "Y" and is_member != "N":
                    print("Please enter Y or N.")

                    if is_member == "Y":
                        ticket_price = 8
                        print("Thank you for your membership.")
                    else:
                        ticket_price = 12
                        print("Standard ticket selected.")

                    print()

                    print("Ticket price: £" + str(ticket_price))

"""
is_member = "" 

while is_member != "Y" and is_member != "N": 
    is_member = input("Are you a member? (Y/N) ")

    if is_member != "Y" and is_member != "N":
        print("Please enter Y or N.")

if is_member == "Y":
    ticket_price = 8
    print("You are a member, so your ticket price is £8.")
else:
    ticket_price = 12
    print("You are not a member, so your ticket price is £12.")

print()

print("Ticket price: £" + str(ticket_price))
"""

"""
Made using code mainly recycled from projects/visitor-ticket-calculator.py
Initially I had the above code but I realised that I could simplify it by removing the membership question if the user is under 18 and the film is rated 18+
So I moved it into the if statement as I realised I don't know how to close the program yet before it's natural end
"""