



def remove_duplicates(lst):
    return list(set(lst)).sort()

nums = [4, 2, 5, 2, 1, 5, 3]
print(remove_duplicates(nums))