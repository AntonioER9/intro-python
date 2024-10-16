from pathlib import Path
from zipfile import ZipFile

# escribir archivos comprimidos
with ZipFile("archivos/productos.zip", "w") as zip:
    zip.write("archivos/productos.json")
    for path in Path.rglob("*.*"):
        print(path)
        if str(path) != "archivos/productos.zip":
            zip.write(path)

# leer archivos comprimidos
with ZipFile("archivos/productos.zip", "r") as zip:
    zip.extractall("archivos/extraidos")
    for path in Path("archivos/extraidos").rglob("*.*"):
        print(path)
        print(path.read_text())
        path.unlink()
