#Check if Array is Sorted
arr = [1, 2, 3, 4, 5]

ascending = True
descending = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        ascending = False
    if arr[i] < arr[i + 1]:
        descending = False

if ascending:
    print("Array is sorted in ascending order")
elif descending:
    print("Array is sorted in descending order")
else:
    print("Array is not sorted")