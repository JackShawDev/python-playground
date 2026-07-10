print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Your task is to guess the number in as few attempts as possible.")

print()

secret_number = 42  # The number to guess
guess = None
attempts = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))


    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
    else:
        attempts = attempts + 1
        
        if guess == secret_number:
            print("Congratulations! You've guessed the correct number.")
            print("It took you " + str(attempts) + " attempts.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

"""
Uses most of the foundational concepts learned in week 2, future iterations could use random number generation, difficulty levels, prevent crashing from invalid input or replay/exit options.
"""