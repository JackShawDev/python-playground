print("Welcome to the multiplication table generator!")

print()

table = int(input("Enter the number for which you want to generate the multiplication table: "))

print()

for multiplier in range(1, 11):
    result = table * multiplier
    print(str(table) + " x " + str(multiplier) + " = " + str(result))

"""
limited user validation for the input number, they could enter a string and crash the program
could expand by asking the user how high they want the multiplication table to go, and then use that number in the range function, not implemented here as they could enter such large numbers that the output would be too long to read
"""