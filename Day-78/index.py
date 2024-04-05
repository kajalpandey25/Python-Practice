class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")        
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()


# Quick: Implement a Cat class by using the animal class. Add some methods specific to cat.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass  # Each specific animal class will implement its own sound.

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):
        return "Meow"

    def purr(self):
        return f"{self.name} is purring"

    def scratch(self):
        return f"{self.name} is scratching"

# Example usage:
my_cat = Cat("Whiskers", "Persian")
print(my_cat.make_sound())  # Output: Meow
print(my_cat.purr())        # Output: Whiskers is purring
print(my_cat.scratch())     # Output: Whiskers is scratching

