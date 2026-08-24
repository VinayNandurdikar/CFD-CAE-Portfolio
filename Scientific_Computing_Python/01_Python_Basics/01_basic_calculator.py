# input() takes information from the user.
# input() gives the value as text, so float() converts it into a number.
# float() is used instead of int() because it also allows decimal numbers like 10.5.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# + is used for addition
addition = num1 + num2

# - is used for subtraction
subtraction = num1 - num2

# * is used for multiplication
multiplication = num1 * num2

# print() displays the result
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)

# Division by zero is not allowed.
# != means "not equal to".
# Therefore, divide only when num2 is not zero.

if num2 != 0:
    division = num1 / num2
    print("Division:", division)
else:
    print("Cannot divide by zero")
