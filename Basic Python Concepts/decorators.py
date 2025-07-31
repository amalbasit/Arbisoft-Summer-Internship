

# def decorator_func(base_func):
#     def wrapper(*args, **kwargs):
#         print('this is the decorator func')
#         base_func(*args, **kwargs)
#     return wrapper


# def decorator2(base_func):
#     def wrapper(*args, **kwargs):
#         print('this is the decorator func2')
#         base_func(*args, **kwargs)
#     return wrapper

# @decorator_func
# @decorator2
# def base_func():
#     print('this is the base function')

# base_func()


# division w xero check pehle

# def checkDivZero(func):  # Decorator takes the function to wrap
#     def wrapper(a, b):   # Wrapper takes same args as base function
#         if b == 0:
#             print('Oops! Division by zero.')
#             return None
#         return func(a, b)  # Call the original function
#     return wrapper         # Return the wrapper

# @checkDivZero
# def divide(a, b):
#     return a / b

# print(divide(4, 2))   # ✅ 2.0
# print(divide(5, 0))   # ✅ Oops! Division by zero.




def checkDivZero(divide):

    def wrapper(a, b):
        if b == 0:
            print('Oops! You cannot divide by 0.')
            raise ZeroDivisionError
        return divide(a, b)
    return wrapper


@checkDivZero
def divide(a, b):
    return a/b


print(divide(4,9))
