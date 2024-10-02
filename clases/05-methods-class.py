class Dog:
    patas = 4

    # Propiedad de la clase
    def __init__(self, name, age):  # Método constructor
        self.name = name
        self.age = age

    @classmethod
    def bark(cls):
        return "Woof!"

    @classmethod
    def factory(cls):
        return cls("Rex", 3)


my_dog = Dog("Rex", 3)
print(type(my_dog))
my_dog.bark()  # 'Woof!'

Dog.bark()  # 'Woof!'
rex = Dog.factory()
