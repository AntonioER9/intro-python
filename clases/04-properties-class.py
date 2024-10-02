class Dog:
    patas = 4

    # Propiedad de la clase
    def __init__(self, name, age):  # Método constructor
        self.name = name
        self.age = age

    def bark(self):  # Método de la clase
        return "Woof!"


my_dog = Dog("Rex", 3)
print(type(my_dog))
my_dog.bark()  # 'Woof!'
