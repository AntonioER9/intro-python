from pathlib import Path

path = Path("hola-mundo/mi-archivo.py")
path.exists()  # True
path.mkdir()  # Crea el directorio hola-mundo
path.rmdir()  # Elimina el directorio hola-mundo
path.rename("hola-mundo/test.py")  # Renombra el archivo mi-archivo.py a test.py

for p in path.iterdir():
    print(p)  # hola-mundo/test.py
