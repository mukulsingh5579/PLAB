#Find the average of array elements

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

average = sum(arr) / n

print("Average of elements:", average)