from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("Guardando usuario")


class Sesion(Model):
    def guardar(self):
        print("Guardando sesion")


def guardar(entidades):
    for entidad in [entidades]:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([usuario, sesion])  # Polimorfismo
guardar(sesion)  # Guardando sesion
