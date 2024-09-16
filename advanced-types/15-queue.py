# LIFO
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # [1, 2, 3]
queue.pop(0)
print(queue)  # [2, 3]
print(queue[-1])  # 3
if not queue:
    print("empty")
