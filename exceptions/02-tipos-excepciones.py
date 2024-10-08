try:
    n1 = int(input("Número 1: "))
except ValueError as e:
    print(type(e))
except NameError as e:
    print(type(e))
