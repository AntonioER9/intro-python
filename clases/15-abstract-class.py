from abc import ABC, abstractmethod


class Model(ABC):  # Abstract class
    @property
    @abstractmethod
    def tabla(self):
        pass

    def guardar(self):
        print("Guardar")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id}")


class Usuario(Model):
    tabla = "Usuario"

    def __init__(self):
        super().__init__()

    def guardar(self):
        super().guardar()
        print(f"Guardando en la tabla {self.tabla}")


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(1)

model = Model()  # Error
