import random
import string

print(random.random())  # 0.0 <= x < 1.0

print(random.randint(1, 10))  # 1 <= x <= 10

print(random.choice(["a", "b", "c"]))  # a, b, c

print(random.choices(["a", "b", "c"], k=2))  # ['a', 'c']

print(random.sample(["a", "b", "c"], k=2))  # ['b', 'a']

print(random.shuffle(["a", "b", "c"]))  # None

chars = string.ascii_letters + string.digits
