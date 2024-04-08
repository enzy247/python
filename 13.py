import random
arr = []
n = int(input())
for i in range(n):
    element = random.randint(-100, 100)
    arr.append(element)
print("Неотрицательные элементы массива:")
for element in arr:
    if element >= 0:
        print(element)

print("\nЭлементы массива, не превышающие 100:")
for element in arr:
    if element <= 100:
        print(element)

