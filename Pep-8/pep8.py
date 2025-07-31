def func_is_really_long(arg1, arg2, 
                        arg3, arg4):
    so_long_ew = True
    more_longer_uhh_yeah = False

    if (so_long_ew or 
            more_longer_uhh_yeah):
        print("true")
         

func_is_really_long(1,2,3,4)


liste = [
    1,2,3,
    4,5,6
    ]
                                                      #HHH
# below here

# Two blank lines before top-level function or class
import math


def calculate_area(radius):
    # One blank line separates logical sections within function
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    area = math.pi * radius ** 2

    return area


def calculate_perimeter(radius):
    return 2 * math.pi * radius


# Two blank lines before class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # One blank line between methods
    def area(self):
        return calculate_area(self.radius)

    def perimeter(self):
        return calculate_perimeter(self.radius)


# Related short one-liner functions with no blank lines between
def dummy1(): pass
def dummy2(): pass
def dummy3(): pass


# Sparing use of blank lines within function to indicate logic separation
def analyze_circle(radius):
    if radius <= 0:
        print("Invalid radius")
        return

    # Area calculation
    area = calculate_area(radius)

    # Perimeter calculation
    perimeter = calculate_perimeter(radius)

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")



# word_list = []

# # BAD: Inefficient and implementation-dependent
# s = ""
# for word in word_list:
#     s += word  # Relies on CPython refcounting optimization


# # GOOD: Efficient and safe across all implementations
# s = "".join(word_list)


def hello(x, y):
    print(x, y)

hello(y='amla', x='jed')
