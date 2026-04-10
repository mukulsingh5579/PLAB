#Count consecutive occurrences in an array
arr = [1, 1, 2, 2, 2, 3, 1, 1]

count = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        count += 1
    else:
        print(f"{arr[i-1]} appears consecutively {count} times")
        count = 1

# last element
print(f"{arr[-1]} appears consecutively {count} times")