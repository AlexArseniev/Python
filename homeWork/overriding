#overriding

class Animal:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def introduce_yourself(self):
        print(f"The animal is {self.age} years old. It's name is {self.name}")
            


class Cat(Animal):
    
    def __init__(self,name,age, breed):
        Animal.__init__(self, name, age)
        self.breed = breed
        
        
    
    def introduce_yourself(self):
        print(f"The animal is {self.age} years old. It is {self.breed} and it is called {self.name}")
    
an_animal = Animal("Bobi", 5)
a_cat = Cat("Kush",10,"debel persiec")


an_animal.introduce_yourself()
a_cat.introduce_yourself()
