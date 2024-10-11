from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")

texto = archivo.read_text("uft-8")
print(texto)
archivo.write_text("Hola, mundo!")
