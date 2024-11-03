from functools import reduce

a = [11, 23, 434, 56, 67, 78 ,454]

def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, a))