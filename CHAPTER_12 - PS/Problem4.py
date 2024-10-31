try:
    a = int(input('Enter a number: '))
    b = int(input('Enter second number: '))
    print(a/b)
except ZeroDivisionError as e:
    print("Infinite")