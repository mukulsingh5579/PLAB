#Find index of maximum element
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

max_index = 0

for i in range(1, n):
    if arr[i] > arr[max_index]:
        max_index = i

print("Index of maximum element:", max_index)