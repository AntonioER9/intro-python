for j in range(3):
    for k in range(3):
        print(j, k)
        if j == 1 and k == 1:
            print("Número encontrado:", j, k)
            break
        else:
            print("Número no encontrado:", j, k)
