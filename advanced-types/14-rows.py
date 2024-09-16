# rows FIFO
from collections import deque

row = deque([1, 2])
row.append(3)
row.append(4)
row.append(5)

print(row)  # deque([1, 2, 3, 4, 5])
row.popleft()
print(row)  # deque([2, 3, 4, 5])
if not row:
    print("empty")
