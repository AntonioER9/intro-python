numbers = [2, 4, 4, 5, 1]
numbers2 = sorted(numbers, reverse=True)
numbers.sort()
print(numbers)  # [1, 2, 4, 4, 5]
print(numbers2)  # [5, 4, 4, 2, 1]

users = [[4, "John"], [2, "Jane"], [3, "Doe"], [1, "Alice"]]
users.sort()
print(users)  # [[1, 'Alice'], [2, 'Jane'], [3, 'Doe'], [4, 'John']]


def order(element):
    return element[1]


users.sort(key=order, reverse=True)
print(users)  # [[4, 'John'], [2, 'Jane'], [3, 'Doe'], [1, 'Alice']]
