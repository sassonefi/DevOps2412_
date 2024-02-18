#HW for LS03
# 1 + 2
try:
    a = 1 / 0
except ZeroDivisionError:
    print("can't divide by zero")

# 3 - it's legal, the finally block will always be executed
try:
    x = 1
finally:
    print("finally")

#4 - any execption that inherits from the base Exception class can be caught

#5 - it's better to specify the type of exception.
#it's can be problematic: (FOUND IN CHATGPT)
# Lack of Specificity: The general except block catches all exceptions, including both built-in exceptions and user-defined exceptions. This lack of specificity makes it harder to identify and handle specific issues in your code.
#
# Difficulty in Debugging: Without knowing the specific type of exception that occurred, it becomes more challenging to debug and understand the root cause of the problem. Properly handling different types of exceptions allows you to respond appropriately to specific error conditions.
#
# Hidden Bugs: Using a generic except block may hide bugs in your code by catching and handling exceptions that you didn't anticipate. This can make it difficult to discover and fix issues.
#
# Readability and Maintenance: Code that catches all exceptions with a general except block can be less readable and maintainable. It's generally better to explicitly handle the exceptions you expect and allow others to propagate up the call stack if they are not anticipated.

#6 - exceptions related to Input/Output operations
# FileNotFoundError: Raised when a file or directory is requested, but it cannot be found.
#
# PermissionError: Raised when trying to open a file for writing without the necessary write permissions, or attempting to access a restricted system resource.
#
# IsADirectoryError: Raised when a directory is expected, but a file is encountered.
#
# NotADirectoryError: Raised when a directory is expected, but a non-directory object is encountered.
#
# FileExistsError: Raised when trying to create a file or directory that already exists.
#
# BlockingIOError: A subclass of OSError specifically related to blocking I/O operations.

#anf for  ZeroDivisionError  - catch exceptions specifically related to attempting to divide by zero

#7 and 8
with open('words.txt', 'w') as file:
    # Write name into the file
    file.write("My name is Efi")

# 9
with open('words.txt', 'r') as file:
    # read my name
    content = file.read()
print(content)

#10
with open('words.txt', 'w') as file:
    # Write name into the file
    file.write("סתם טקטס בעברית")
with open('words.txt', 'r') as file:
    # read my name
    content = file.read()
print(content)

from PIL import Image
width, height = 300, 200
background_color = (0, 255, 0)  # Green
image = Image.new("RGB", (width, height), background_color)

# Save as png
image.save("green_image.png")
