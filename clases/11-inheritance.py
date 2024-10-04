class Animal:
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Dog(Animal):
    def walk(self):
        print("Walking")


class Cat(Animal):
    def run(self):
        print("Running")


Dog = Dog()
Dog.eat()
Cat = Cat()
Cat.eat()
