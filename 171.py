#Check if array is sorted in ascending order
arr = [1, 2, 3, 4, 5]

is_ascending = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_ascending = False
        break

if is_ascending:
    print("Array is sorted in ascending order")
else:
    print("Array is NOT sorted in ascending order")