buscar = 3

for number in range(5):  # 0, 1, 2, 3, 4
    print(number)
    if number == buscar:
        print("Número encontrado:", number)
        break
    else:
        print("Número no encontrado:", number)

for char in "Ultimate python":
    print(char)
