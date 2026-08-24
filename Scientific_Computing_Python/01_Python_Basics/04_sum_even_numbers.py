# Ask the user to enter several numbers separated by spaces.

numbers = input("Enter numbers separated by spaces: ")

# split() separates the entered text wherever there is a space.
#
# Example:
# "10 15 20"
#
# becomes:
# ["10", "15", "20"]

numbers = numbers.split()

# Start the total from zero.
# We will keep adding even numbers to this variable.

total = 0

# for loop is used because we want to examine every number in the list.

for number in numbers:

    # Values from input() are strings.
    # int() converts each value into an integer.

    number = int(number)

    # % is called the modulo operator.
    # It gives the remainder after division.
    #
    # Example:
    # 10 % 2 = 0
    # 11 % 2 = 1
    #
    # Therefore, if remainder is 0, the number is even.

    if number % 2 == 0:

        # += means add the number to the existing total.
        # total += number
        # is the same as:
        # total = total + number

        total += number

# Display the final answer.

print("Sum of even numbers:", total)
