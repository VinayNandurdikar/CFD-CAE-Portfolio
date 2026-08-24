# float() allows the user to enter whole numbers or decimal numbers.

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

# Display the values before swapping.

print("Before swapping:")
print("a =", a)
print("b =", b)

# Python allows us to swap two variables directly.
# The value of b goes into a and the value of a goes into b.
# No third/temporary variable is required.

a, b = b, a

# Display values after swapping.

print("After swapping:")
print("a =", a)
print("b =", b)
