
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a = 1
b = 23
c = 2

print(greatest(a, b, c))