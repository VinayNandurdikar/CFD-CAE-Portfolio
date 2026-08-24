# Ask the user to enter a number.
# float() is used so the program can accept both whole numbers and decimals.
number = float(input("Enter a number: "))

# Check whether the number is greater than zero.
if number > 0:
    print("The number is positive.")

# If the first condition is false, check whether the number is less than zero.
elif number < 0:
    print("The number is negative.")

# If the number is neither greater than zero nor less than zero,
# then it must be zero.
else:
    print("The number is zero.")
