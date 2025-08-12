# Catching Multiple Exceptions

# Ask the user for a number. Try converting it to integer and dividing 10 by it. Handle both ValueError and ZeroDivisionError in separate except blocks.

# try:
#     num = input("Enter a number: ")
#     num = int(num)
#     print(f'{num} is an integer.')
#     result = 10/num
#     print(f"10/{num} is {result:.3f}")
# except ValueError:
#     print("You must enter an integer.")
# except ZeroDivisionError:
#     print("You cannot divide by zero.")

# Simulate an operation where a file is opened and 100 is divided by the number from the file. Handle FileNotFoundError, ZeroDivisionError, and ValueError together in a single except.

# try:
#     with open("num_file.txt", "r") as f:
#         num = int(f.read())  
#         result = 100 / num
#         print(f"Result: {result:.3f}")

# except (FileNotFoundError, ZeroDivisionError, ValueError) as e:
#     print("Error: {e}")


# Ask the user for a number, divide it, and print different messages depending on which exception is caught.

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num    
#     print("Result:", result)

# except ValueError:
#     print("Please enter an integer.")

# except ZeroDivisionError:
#     print("You cannot divide by 0.")