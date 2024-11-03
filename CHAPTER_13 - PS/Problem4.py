def divisible5(n):
    if (n%5 == 0):
        return True
    return False

a = [3438, 323, 454, 65, 55, 45, 43, 988, 34543, 654654, 75]

f = list(filter(divisible5, a))
print(f)