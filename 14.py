import random
arr = []
n = int(input())
for i in range(n):
    element = random.randint(-100, 100)
    arr.append(element)
print("Четные элементы массива:")
for element in arr:
    if element%2 == 0:
        print(element)

print("\nЭлементы массива, оканчивающиеся на нуль:")
for element in arr:
    if element%10==0:
        print(element)

