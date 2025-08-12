# Using 'as' Keyword


# Try to convert user input to an integer and catch the ValueError. Print the error message using as e.

# try:
#     num = int(input("Enter a number: "))
# except ValueError as e:
#     print(f"Error: {e}")

# Divide two numbers entered by the user and catch ZeroDivisionError as e. Print: "An error occurred: division by zero", using the error message.

# try:
#     num = int(input("Enter the numerator: "))
#     denom = int(input("Enter the denominator: "))
#     result = num/denom
#     print(f"Result: {result:.3f}")
# except ZeroDivisionError as e:
#     print(f"An error occurred: {e}")

# Open a file, and in case of failure, print the full error details using the exception object.

# try:
#     file = open('txt_file.txt')
#     print("File was opened.")
# except Exception as e:
#     print(f"Error: {e}")