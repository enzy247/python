
import random
arr = []
n = int(input())
for i in range(n):
    element=int(input())
    arr.append(element)
print ("i%2")
for i in n+1:
    if (i-1)%2==0:
        print (arr[i])
print ("i%3")
for i in n+1:
    if (i-1)%3==0:
        print (arr[i])    

    

