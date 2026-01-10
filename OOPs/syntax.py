class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} says woof!")
        
my_dog = Dog("Buddy", "Lebra")
my_dog.bark()   