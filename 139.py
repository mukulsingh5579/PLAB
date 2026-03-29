#Find index of minimum element
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

min_index = 0

for i in range(1, n):
    if arr[i] < arr[min_index]:
        min_index = i

print("Index of minimum element:", min_index)