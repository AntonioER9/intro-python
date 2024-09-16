point = {"x": 1, "y": 2}
print(point)  # {'x': 1, 'y': 2}
print(point["x"])  # 1
point["z"] = 3
print(point)  # {'x': 1, 'y': 2, 'z': 3}
if "z" in point:
    print(point["z"])  # 3

print(point.get("a", 0))  # 0

del point["x"]
print(point)  # {'y': 2, 'z': 3}

for key in point:
    print(key, point[key])  # y 2, z 3

for key, value in point.items():
    print(key, value)  # y 2, z 3

users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "Joe"},
]

for user in users:
    print(user["name"])  # John, Jane, Joe
