# Basic Try-Except


# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    x = 5/0
    print(f"Result: {x}")
except ZeroDivisionError:
    print("You cannot divide a number by 0.")

# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# try:
#     num = int(input("Enter a number: "))
#     print(f"Number: {num}")
# except ValueError:
#     print("You did not enter an integer.")

# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

# try:
#     with open('text_file.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("The file was not found.")

# Try accessing an element at index 5 in a list of 3 elements. Handle IndexError.

# list1 = [1,2,4,7,23]

# try:
#     print(list1[5])
# except IndexError:
#     print("There is no value at that index.")
# except TypeError:
#     print('You must enter an integer for the index.')