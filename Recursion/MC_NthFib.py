#Return the nth fibonocci number

import profile

# I'm going to operate under the assumption that
# fib(1) = 1 and fib(0) = 0
# therefore:
# 0, 1, 1, 2, 3, 5, 8, 13
#    1, 2, 3, 4, 5, 6, 7

## Using looping - brute force
def fibB(n):
    a, b = 0, 1

    for x in range(n - 1):
        a, b = b, a + b
    return b
print fibB(5)

# using looping, print first n
def fibB_firstn(n):
    a, b = 0, 1
    for x in range(n):
        print b,
        a, b = b, a + b
fibB_firstn(7)

## Bad recursion
# def fibR(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0

#     def _nth_fib(curr, last, depth, n):
#         if depth == n:
#             return curr
#             print curr
#         else:
#             return _nth_fib(curr + last, curr, depth + 1, n)

#     return _nth_fib(1, 0, 2, n)

# Reucursion
def fibR(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibR(n-1) + fibR(n-2)


# Create a Fib class with an iterator

class Fib(object):

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def next(self):
        fib = self.b
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

#generator functions or just generators return generator objects
# These generators are functions that contain the yield key word.
# Rather than having to write every generators with the 
# __iter__ and next which is pretty cumbersome, python 
# provides the yield key word that provides an easy way for 
# defining generators. For example the Fibonacci iterator can 
# be recast as a generator using the yield key word as shown below:

# generator
def fibG():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

# calling generator to print the first n

def fib_gen_all(n):
    x = fibG()
    for i in range(n):
        print x.next()
        
# calling generator to get nth
def fib_gen(n):
    x = fibG()
    for i in range(n - 1):
        x.next()
    print x.next()

# using dynamic programing
def fib_mem(n):
    mem = {0: 0,
           1: 1}

    def _fib_mem(n):

        if n not in mem:
            mem[n] = _fib_mem(n-1) + _fib_mem(n-2)

        return mem[n]

    return _fib_mem(n)





profile.run('print nth_fib(50); print')
prfile.run('print nth_fib_brute(50); print')


