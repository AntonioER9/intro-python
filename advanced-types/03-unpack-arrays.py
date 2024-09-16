numbers = [1, 2, 3, 4, 5]

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

first, *others = numbers
print(first)  # 1
print(others)  # [2, 3, 4, 5]
