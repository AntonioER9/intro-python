# from pathlib import Path

# Path("/usr/bin")
path = Path("hola-mundo/mi-archivo.py")
path.is_file()  # True
path.name  # 'mi-archivo.py'
path.stem  # 'mi-archivo'
path.absolute()  # PosixPath('/home/runner/hola-mundo/mi-archivo.py')


p = path.with_name("test.py")
print(p)  # hola-mundo/test.py
