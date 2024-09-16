mascotas = ["perro", "gato", "loro", "pez", "conejo"]
mascotas.append("hamster")
print(mascotas)  # ['perro', 'gato', 'loro', 'pez', 'conejo', 'hamster']
mascotas.insert(1, "tortuga")
print(mascotas)  # ['perro', 'tortuga', 'gato', 'loro', 'pez', 'conejo', 'hamster']
mascotas.remove("pez")
print(mascotas)  # ['perro', 'tortuga', 'gato', 'loro', 'conejo', 'hamster']
mascotas.pop()
print(mascotas)  # ['perro', 'tortuga', 'gato', 'loro', 'conejo']
del mascotas[1]
print(mascotas)  # ['perro', 'gato', 'loro', 'conejo']
mascotas.clear()
print(mascotas)  # []
