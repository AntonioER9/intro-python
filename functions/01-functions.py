def hola(nombre, apellido="Feliz"):  # nombre es un parámetro
    print("Hola, mundo!")
    print(f"Hola, {nombre} {apellido}!")


hola("Antonio", "Espinoza")  # Antonio es un argumento
hola("Chanchito")
hola(apellido="González", nombre="Chanchito")
