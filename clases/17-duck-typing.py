from abc import ABC, abstractmethod


class Usuario:
    def guardar(self):
        print("Guardando usuario")


class Sesion:
    def guardar(self):
        print("Guardando sesion")


def guardar(entidades):
    for entidad in [entidades]:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([usuario, sesion])  # Polimorfismo
guardar(sesion)  # Guardando sesion
