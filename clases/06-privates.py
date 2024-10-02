class Dog:
    def __init__(self, name, age):  # Método constructor
        self.__name = name  # Atributo privado
        self.age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def bark(self):
        return "Woof!"

    @classmethod
    def factory(cls):
        return cls("Rex", 3)


perro1 = Dog.factory()
print(perro1.bark())  # 'Woof!'
print(perro1.get_name())  # 'Rex'
