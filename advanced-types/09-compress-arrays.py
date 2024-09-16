users = [["John", 4], ["Jane", 2], ["Doe", 3], ["Alice", 1]]

names = []
for user in users:
    names.append(user[0])
print(names)  # ['John', 'Jane', 'Doe', 'Alice']

names2 = [user[0] for user in users]
print(names2)  # ['John', 'Jane', 'Doe', 'Alice']

names3 = [user[0] for user in users if user[1] > 2]
print(names3)  # ['John', 'Doe']

names4 = list(map(lambda user: user[0], users))
print(names4)  # ['John', 'Jane', 'Doe', 'Alice']

menosUsuarios = list(filter(lambda user: user[1] > 2, users))
print(menosUsuarios)  # [['John', 4], ['Doe', 3]]
