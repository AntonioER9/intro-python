def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print("Resultado:", resultado)


suma(1, 2, 3)
suma(1, 2)
suma(1, 5, 7, 8, 9, 10)
