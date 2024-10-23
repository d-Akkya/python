class Employee:
    language = "Python"
    salary = 12    #This is a class attribute

akkya = Employee()
akkya.language = "JavaScript" #This is an object/instance attribute
print(akkya.salary, akkya.language)