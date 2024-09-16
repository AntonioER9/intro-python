users = [[4, "John"], [2, "Jane"], [3, "Doe"], [1, "Alice"]]

users.sort(key=lambda el: el[1])

print(users)  # [[1, 'Alice'], [3, 'Doe'], [2, 'Jane'], [4, 'John']]
