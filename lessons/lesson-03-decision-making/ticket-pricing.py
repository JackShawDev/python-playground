print("Welcome to the Leisure Centre!")

print()

name = input("What is your name? ")
age = int(input("How old are you? "))
is_adult = age >= 16

print()

print("Hello " + name + "!")

print()

if is_adult:
    print("Your ticket price is £10")
else:
    print("Your ticket price is £5")

"""
In the future I would likely add more variables to this program to add more realism such as membership status, if they have a booking, any discounts (student, senior etc.) 
I would also be interested in adding a birthday check rather than just using age to determine if they are an adult or not for accuracy, but also a system to maybe validate it rather than taking the users word (seems very far off my current knowledge)
"""