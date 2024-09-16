# Set significa grupo, conjunto, colección.
# Es una colección desordenada de elementos únicos.
# Los sets son mutables, pero los elementos deben ser inmutables.
# Los sets no soportan indexación.
# Los sets no soportan slicing.
# Los sets no soportan concatenación.
# Los sets no soportan repetición.
# Los sets no soportan comprensión.

primer = {1, 2, 3, 4, 5}
print(primer)  # {1, 2, 3, 4, 5}
segundo = [1, 2, 3, 4, 5, 5, 5]
segundo = set(segundo)
print(segundo)  # {1, 2, 3, 4, 5}
print(primer | segundo)  # {1, 2, 3, 4, 5} # Union
print(primer & segundo)  # {1, 2, 3, 4, 5} # Intersection
print(primer - segundo)  # set() # Difference
print(primer ^ segundo)  # set() # Symmetric Difference
