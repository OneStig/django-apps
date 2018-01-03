import numpy as nu

def addInt(n1, n2):
    if type(n1) != type(1) and type(n2) != type(1):
        return 'N/A'
    else:
        return n1 + n2

print('test')

a = 'django'

print(a)

print(a[0]) # d
print(a[5]) # o
print(a[:4]) # djan
print(a[1:4]) # jan
print(a[4:]) # go

print(nu.pi)

print(addInt(1, 2))

print(addInt("hello", "world"))

evens = [2]
nums = [1]

for i in range(1, 100):
    nums.append(i);

evens = filter(lambda n:n%2 == 0, nums)
print(list(evens))

#if true:

#elif:

#else:

#def funcname(param='defaultval'):
