class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self == other or self < other


print(Coords(1, 2) == Coords(1, 2))  # True
print(Coords(1, 2) != Coords(1, 2))  # False
print(Coords(1, 2) < Coords(1, 2))  # False
print(Coords(1, 2) <= Coords(1, 2))  # True
