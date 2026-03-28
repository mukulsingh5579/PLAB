#Find the maximum element in an array

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

maximum = max(arr)

print("Maximum element:", maximum)