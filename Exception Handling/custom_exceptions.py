# Custom Exceptions


# Define NegativeNumberError exception. Write a function that raises it if the user enters a negative number.

# class NegativeNumberError(Exception):
#     pass

# def func():
#     try:
#         num = int(input("Enter a positive number: "))
#         if num < 0:
#             raise NegativeNumberError
#         print(f"Num: {num}")

#     except NegativeNumberError: 
#         print("You entered a negative number.")

# func()

# Create a PasswordTooShortError. Raise it if password length is less than 8 characters.

# class PasswordTooShortError(Exception):
#     pass

# try:
#     password = input("Create your password (must be at least 8 characters): ")
#     if len(password) < 8:
#         raise PasswordTooShortError
#     print("Password created successfully!")
# except PasswordTooShortError:
#     print("Your password was too short.")

# Simulate a bank withdrawal system with InsufficientFundsError if user tries to withdraw more than balance.

# class InsufficientFundsError(Exception):
#     def __init__(self, *args):
#         super().__init__(*args, f"Your transaction was declined due to insufficient funds.")

# class BankWithdrawlSystem:

#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         try: 
#             if amount > self.balance:
#                 raise InsufficientFundsError
#             self.balance -= amount
#             print(f"${amount} withdrawn successfully!")
#         except InsufficientFundsError as e:
#             print(e)

#     def deposit(self, amount):
#         self.balance += amount


# obj = BankWithdrawlSystem(200)
# obj.deposit(250)
# obj.withdraw(500)