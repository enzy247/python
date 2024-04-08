
import random
arr = []
n = int(input())
for i in range(n):
    element = random.randint(1, 999)
    arr.append(element)
print("Двухзначтыне элементы массива:")
for element in arr:
    if len(str(element)) == 2:
        print(element)

print("\nТрехзначтные элементы массива:")
for element in arr:
    if len(str(element)) == 3:
        print(element)

