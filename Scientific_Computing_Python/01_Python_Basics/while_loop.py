# Import the random module.
# We use random because the secret number should be chosen automatically
# and should be different each time the program runs.
import random

# randint(1, 100) generates a random whole number between 1 and 100.
secret_number = random.randint(1, 100)

print("Guess the secret number between 1 and 100.")

# while True creates a loop that keeps running
# until the correct number is guessed.
while True:

    # input() takes the user's guess.
    # int() converts the entered value from text into a whole number.
    guess = int(input("Enter your guess: "))

    # If the guess is smaller than the secret number,
    # tell the user that the guess is too low.
    if guess < secret_number:
        print("Too low! Try again.")

    # If the guess is greater than the secret number,
    # tell the user that the guess is too high.
    elif guess > secret_number:
        print("Too high! Try again.")

    # If the guess is neither lower nor higher,
    # it must be equal to the secret number.
    else:
        print("Correct! You guessed the secret number.")

        # break stops the while loop.
        # The program ends after the correct number is guessed.
        break
