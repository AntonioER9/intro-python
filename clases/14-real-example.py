class Model:
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("No se ha definido la tabla")

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
