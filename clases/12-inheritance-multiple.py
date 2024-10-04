class Animal:
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Dog:
    def walk(self):
        print("Walking")


class Cat(Animal, Dog):
    def run(self):
        print("Running")


Dog = Dog()
