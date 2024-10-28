class Animals:
    def bark(self):
        pass

class Pets(Animals):
    pass

class Dog(Pets):
    
    @staticmethod
    def bark():
        print('Bow Bow!')

d = Dog()
d.bark()