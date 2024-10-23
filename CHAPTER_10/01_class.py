class Employee:
    salary = 12    #This is a class attribute
    language = "Py"

akkya = Employee()
akkya.name = "d-Akkya" #This is an object/instance attribute
print(akkya.name, akkya.salary, akkya.language)

rohan = Employee()
rohan.name = "Rohan Champu"
print(rohan.language, rohan.salary, rohan.name)

# Here name is instance attribute where as salary & language are class attributes as they directly belong to the class 