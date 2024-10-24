class Demo:
    a = 4

obj = Demo()
print(obj.a)  # Prints the class attribute because instance attribute is not present
obj.a = 23  # Instance attribute is set
print(obj.a)  # Prints the instance attribute because instance attribute is present
print(Demo.a) # Prints the class attribute