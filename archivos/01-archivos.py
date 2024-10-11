from pathlib import Path

archivo = path("archivos/01-archivos.txt")
archivo.exists()  # True

print(archivo.stat())  # Información del archivo
print(archivo.stat().st_size)  # Tamaño del archivo
