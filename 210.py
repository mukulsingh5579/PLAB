#Count Consecutive Occurrences
arr = [1, 1, 2, 2, 2, 3, 1, 1]

count = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        count += 1
    else:
        print(arr[i - 1], "appears", count, "times consecutively")
        count = 1

# last element
print(arr[-1], "appears", count, "times consecutively")