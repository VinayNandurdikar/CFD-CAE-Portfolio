# input() is used because we want the user to enter some text.
# A sequence of characters is called a string in Python.

text = input("Enter a string: ")

# [::-1] is Python slicing.
# -1 means move through the string backwards.
# Therefore it reverses the string.

reversed_text = text[::-1]

# print() displays the reversed string.

print("Reversed string:", reversed_text)
