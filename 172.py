#Check if array is sorted in descending order
arr = [5, 4, 3, 2, 1]

is_descending = True

for i in range(len(arr) - 1):
    if arr[i] < arr[i + 1]:
        is_descending = False
        break

if is_descending:
    print("Array is sorted in descending order")
else:
    print("Array is NOT sorted in descending order")