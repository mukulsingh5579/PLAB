#Count of perfect square elements
import math

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

count = 0

for i in arr:
    if i >= 0:
        root = int(math.sqrt(i))
        if root * root == i:
            count += 1

print("Count of perfect squares:", count)