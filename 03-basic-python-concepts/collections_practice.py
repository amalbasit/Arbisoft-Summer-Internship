from collections import defaultdict

students = [
    ("Ali", "A"),
    ("Sara", "B"),
    ("Ahmed", "A"),
    ("Zara", "B"),
    ("Hassan", "C")
]

sections = defaultdict(list)

for name, section in students:
    sections[section].append(name)

print(dict(sections))



from collections import deque

data_stream = [10, 20, 30, 40, 50]
window = deque(maxlen=3)

for number in data_stream:
    window.append(number)
    print("Current window:", list(window))






print('\n')

from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = Counter(words)
print(word_counts)

most_common_word = word_counts.most_common(1)[0][0]
print("Most common word:", most_common_word)

# Finding all feature pairs in a dataset
from itertools import combinations

features = ['age', 'income', 'spend', 'score']
for pair in combinations(features, 2):
    print(pair)
print('\n')

# Python code to demonstrate namedtuple()
from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)



Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p.x, p.y)