import numpy as nu
import re

def addInt(n1, n2):
    if type(n1) != type(1) and type(n2) != type(1):
        return 'N/A'
    else:
        return n1 + n2


def funcA():
    def funcB():
        print("funcB called")

    print("funcA called")
    funcB()


funcA()

print(nu.pi)

print(addInt(1, 2))

print(addInt("hello", "world"))

evens = [2]
nums = [1]

for i in range(1, 100):
    nums.append(i);

evens = filter(lambda n:n%2 == 0, nums)
print(list(evens))

patterns = ['term1', 'term2']

text = 'asdfsafkdsjfkdsterm1fsajfdksjfdksf'

for p in patterns:
    print(p)

    if re.search(p, text):
        print('found')
    else:
        print('not found')


#if true:

#elif:

#else:

#def funcname(param='defaultval'):
