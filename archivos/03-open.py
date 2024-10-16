from io import open

# escritura
texto = "Una línea con texto\nOtra línea con texto"

archivo = open("archivos/hola.txt", "w")
archivo.write(texto)
archivo.close()

# lectura
archivo = open("archivos/hola.txt", "r")
texto = archivo.read()
archivo.close()

# with y seek
with open("archivos/hola.txt", "r") as archivo:
    print(archivo.readlines())
    archivo.seek(0)
    for linea in archivo:
        print(linea)

# lectura y escritura
with open("archivos/hola.txt", "r+") as archivo:
    lista = archivo.readlines()
    lista[1] = "Esta línea ha sido modificada en memoria\n"
    archivo.seek(0)
    archivo.writelines(lista)
