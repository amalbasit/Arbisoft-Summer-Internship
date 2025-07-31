
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
