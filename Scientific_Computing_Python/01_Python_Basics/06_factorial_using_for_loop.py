# Ask the user to enter a number.
# int() is used because factorial is normally calculated for whole numbers.
number = int(input("Enter a number: "))

# Factorial calculation starts from 1.
# We use 1 because multiplying by 1 does not change the value.
factorial = 1

# Factorial is defined only for non-negative integers.
if number < 0:
    print("Factorial does not exist for negative numbers.")

else:
    # range(1, number + 1) generates numbers from 1 up to the entered number.
    # We use number + 1 because the last value in range() is not included.
    for i in range(1, number + 1):

        # *= means:
        # factorial = factorial * i
        factorial *= i

    # Display the final factorial value.
    print("Factorial of", number, "is", factorial)
