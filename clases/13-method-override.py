class Ave:
    def __init__(self):
        self.vodalor = True

    def vuela(self):
        print("Volando voy")


class Pato(Ave):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase padre
        self.nada = True

    def vuela(self):
        super().vuela()
        print("Vuelo como pato")
