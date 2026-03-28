#Find the minimum element in an array

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

minimum = min(arr)

print("Minimum element:", minimum)