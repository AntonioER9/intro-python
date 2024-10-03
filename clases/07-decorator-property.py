class Dog:
    def __init__(self, name, age):  # Método constructor
        self.name = name  # Atributo privado

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip():
            self.__name = name
        return


dog = Dog("Rex")
print(dog.name)  # 'Rex'
