# import time

# print(time.time())  # 1619780000.0

from datetime import datetime

fecha = datetime(2024, 1, 1)
print(fecha)  # 2024-01-01 00:00:00


fechaStr = datetime.strptime("2024-01-01", "%Y-%m-%d")
print(fechaStr)  # 2024-01-01 00:00:00
