def largo(texto):
    resultado = 0
    for char in texto:
        resultado += 1
    return resultado


l = largo("Hola Mundo")
print(l)
