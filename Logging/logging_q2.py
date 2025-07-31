
import logging

# 2. Exception Logging
# Ask the user to enter a number. Divide 100 by that number. Use try/except to catch:

# ValueError

# ZeroDivisionError

# Log each error using logging.error().

logging.basicConfig(
    filename = 'q2.log', 
    filemode = 'w', 
    level = 'ERROR',
    format = '%(asctime)s - %(name)s - %(filename)s - %(levelname)s - Line: %(lineno)d - %(message)s')


try:
    num = int(input('Enter a number: '))
    result = 100/num
    print(f"Result: {result:.3f}")
except ValueError as v:
    logging.error("ValueError. Enter an integer.")
    print("Enter an integer.")
except ZeroDivisionError as z:
    logging.error("ZeroDivisionError. You cannot divide by 0.")
    print("You cannot divide by 0.")