class Employee:
    language = "Python"
    salary = 12    #This is a class attribute

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Welcome to Python Series") 
        #It is compulsory to add any parameter/arg while defining function in a class or else it will throw an error

akkya = Employee()
# akkya.language = "JavaScript" #This is an object/instance attribute

akkya.getInfo()   #Employee.getInfo(akkya)
akkya.greet()