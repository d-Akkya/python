try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print('I am inside else')     # This is executed only if the try was successful 