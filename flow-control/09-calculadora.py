print("Bienvenido a la calculadora")
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

resultado = ""
while True:
    if not resultado:
        resultado = input("Introduce el número de la operación que deseas realizar: ")
        if resultado.lower() == "exit":
            break
        resultado = int(resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "exit":
        break

    n2 = input("Ingresa el segundo número: ")
    if n2.lower() == "exit":
        break
    n2 = int(n2)
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicación":
        resultado *= n2
    elif op.lower() == "división":
        resultado /= n2
    else:
        print("Operación no válida")
        break
    print("Resultado:", resultado)
