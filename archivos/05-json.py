import json
from pathlib import Path

# escribir json
productos = [
    {"nombre": "laptop", "precio": 1200},
    {"nombre": "mouse", "precio": 20},
    {"nombre": "teclado", "precio": 50},
]

data = json.dumps(productos)

Path("archivos/productos.json").write_text(data)

# leer json
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)

# modificar json
productos.append({"nombre": "monitor", "precio": 250})
