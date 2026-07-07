age = -1

while age < 0:
    age = int(input("How old are you? "))

print("Age accepted.")

"""
Very basic loop concept, but is an example of using a loop to validate user input. 
This loop could be broken by removing the age = int(input("How old are you? ")) line, meaning it would never ask the user for input and would continue to loop indefinitely.
"""