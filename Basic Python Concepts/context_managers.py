# class LoggerContext:
#     def __enter__(self):
#         print(">> Entering the block")
#         return self  # optional
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("<< Exiting the block")

# with LoggerContext():
#     print("Inside the context manager")



# class SuppressZeroDivision:
#     def __enter__(self):
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is ZeroDivisionError:
#             print("ZeroDivisionError caught and suppressed.")
#             return True  # suppress only this
#         return False  # let other errors propagate

# with SuppressZeroDivision():
#     x = 1 / 0  # suppressed

# with SuppressZeroDivision():
#     x = int("abc")  # ValueError, NOT suppressed


import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"Elapsed time: {end - self.start:.4f} seconds")

with Timer():
    time.sleep(1)
