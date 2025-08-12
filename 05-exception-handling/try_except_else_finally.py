# Try, Except, Else, Finally


# Ask the user for a filename and try to open it. If it succeeds, read and print the content in else, and print "Done" in finally.

# try:
#     file = open('txt_file.txt')
# except FileNotFoundError:
#     print('The file does not exist.')
# else:
#     print(file.read())
# finally:
#     print('Done.')

# Ask the user to enter two numbers and divide them. Print "Success" only if no error occurs (in else) and "Execution complete" in finally.

# try:
#     num = float(input('Enter the numerator: '))
#     denom = float(input('Enter the denominator: '))
#     result = num/denom
#     print(f"Result: {result:.2f}")
# except ZeroDivisionError:
#     print("You cannot divide by 0.")
# except ValueError:
#     print('You must enter a number.')
# else:
#     print('Success!')
# finally:
#     print('Execution complete!')