
# List Unpacking

lst = [1, 2, 3, 4, 5]

a, b, *rest = lst

print(a)
print(b)
print(rest, "\n")


# Nested List Unpacking

nest_lst = [1, [2, 3], 4, [5]]

i, j, l, (m,) = nest_lst

j = j + [l]

print(i)
print(j)
print(m)


# Dictionary Unpacking

dct = {'name': 'Amal', 'age': 21, 'country': 'Pakistan'}

name, age, country = dct.values()

print(name)
print(age)
print(country, "\n")


# Dictionary Unpacking with **

info1 = {'name': 'Amal', 'age': 21}
info2 = {'country': 'Pakistan', 'city': 'Lahore'}

merged = {**info1, **info2}

print(merged, "\n")



# Packing values into a tuple using *args
def pack_tuple(*args):
    print(args)

pack_tuple(1, 2, 3)


# Regular positional args and *args
def func(a, b, *args):
    print("a:", a)
    print("b:", b)
    print("args:", args)

func(1, 2, 3, 4, 5)



# Packing key-value pairs into a dictionary
def func(**kwargs):
    print(kwargs) 

func(name="Amal", age=25)


# Unpacking a dict

def func(name, age):
    print(name, age)

data = {"name": "Amal", "age": 21}
func(**data)


# Unpacking list values into function parameters
def add(a, b, c):
    return a + b + c

nums = [1, 3, 4]
print(add(*nums))