
def simple_gen():
    yield "a"
    yield "b"
    yield "c"

f = simple_gen()
print(next(f))  # "a"
print(next(f))


# Python code to illustrate generator, yield() and next(). 
def generator(): 
    t = 1
    print ('First result is ',t) 
    yield t 

    t += 1
    print ('Second result is ',t) 
    yield t 

    t += 1
    print('Third result is ',t) 
    yield t 

call = generator() 
next(call) 
next(call) 
next(call)


# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i)


    

# def read_large_file(file_path):
#     with open(file_path) as f:
#         for line in f:
#             yield line.strip()

# # Processing one line at a time
# for line in read_large_file('bigfile.txt'):
#     process(line)



# Create a generator expression for cubes of numbers from 1 to 10.

import math

def gen():
    for i in range(1,11):
        yield i*2



for j in gen():
    print(j)

print('\n')
ed = (x**2 for x in range(1,11))

for i in ed:
    print(i)