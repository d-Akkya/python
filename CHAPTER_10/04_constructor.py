class Employee:
    language = "Python"
    salary = 12    #This is a class attribute

    def __init__(self, name, salary, language):   #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Welcome to Python Series") 
        #It is compulsory to add any parameter/arg while defining function in a class or else it will throw an error

akkya = Employee("Akkya", 2000000, "JavaScript")
# akkya.name = "Akkya"
print(akkya.name, akkya.salary, akkya.language)