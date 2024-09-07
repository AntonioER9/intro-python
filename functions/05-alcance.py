saludo = "Hola"  # saludo es una variable global


def saludar():
    global saludo
    saludo = "Hola desde función"


def saludaPerro():
    saludo = "Guau"  # saludo es una variable local
