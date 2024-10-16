import csv

# escribir
with open("ejemplo.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Nombre", "Apellido", "Departamento"])
    writer.writerow(["Juan", "Pérez", "Ventas"])
    writer.writerow(["Laura", "Gómez", "Sistemas"])

# leer
with open("ejemplo.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
