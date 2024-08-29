n1 = input("Enter a first number: ")
n2 = input("Enter a second number: ")

n1 = int(n1)
n2 = int(n2)

sum = n1 + n2
substraction = n1 - n2
multiplication = n1 * n2
division = n1 / n2

message = f"""
For the numbers {n1} and {n1}:,
the sum is {sum},
the substraction is {substraction},
the multiplication is {multiplication},
the division is {division}
"""

print(message)
