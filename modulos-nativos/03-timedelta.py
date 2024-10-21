from datetime import datetime, timedelta

fecha1 = datetime(2024, 1, 1)
fecha2 = datetime(2024, 2, 1)

delta = fecha2 - fecha1
print(delta)  # 31 days, 0:00:00
print(delta.days)  # 31

timedelta(days=31)  # 31 days, 0:00:00
