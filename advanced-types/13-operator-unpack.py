list = [1, 2, 3, 4, 5]
print(*list)  # 1 2 3 4 5

list2 = [5, 6]

combined = [*list, *list2]
print(combined)  # [1, 2, 3, 4, 5, 5, 6]


point1 = {"x": 1}
point2 = {"y": 2}
newPoint = {**point1, **point2, "z": 3}
print(newPoint)  # {'x': 1, 'y': 2, 'z': 3}
