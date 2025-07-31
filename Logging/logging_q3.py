
import logging

# 3. Full Traceback Logging
# Modify Question 2 to use logging.exception() so that the full traceback is logged when an error occurs.


logging.basicConfig(
    filename = 'q3.log', 
    filemode = 'w', 
    level = 'ERROR',
    format = '%(asctime)s - %(name)s - %(filename)s - %(levelname)s - Line: %(lineno)d - %(message)s')


try:
    num = int(input('Enter a number: '))
    result = 100/num
    print(f"Result: {result:.3f}")
except ValueError as v:
    logging.exception("Enter an integer.")
    print("Enter an integer.")
except ZeroDivisionError as z:
    logging.exception("You cannot divide by 0.")
    print("You cannot divide by 0.")