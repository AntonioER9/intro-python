class Dog:
    def __init__(self, name, age):  # Método mágico
        self.name = name  # Atributo privado
        self.age = age

    def __del__(self):  # Método destructor
        print(f"{self.name} has been deleted")

    def __str__(self):
        return f"Dog: {self.name}, {self.age} years old"

    def bark(self):
        return "Woof!"


dog = Dog("Rex", 3)
print(dog)
