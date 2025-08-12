class CountUpTo:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

# counter = CountUpTo(3)
# for num in counter:
#     print(num)  # 1, 2, 3


# Write your own class that mimics range() behavior using __iter__ and __next__.

class rangeItr:

    def __init__(self, start, stop, step=1):
        self.itr = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self


    def __next__(self):    
        if self.itr > self.stop:
            raise StopIteration
        
        

class rangeItr:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start   # Track the current value

    def __iter__(self):
        return self            # Return self as the iterator object

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


x = rangeItr(1,12,2)
for i in x:
    print(i)
# x = rangeItr(1,10)