#Count how many elements are even at an even index
arr = [2, 3, 4, 5, 6, 7, 8]

count = 0
for i in range(len(arr)):
    if i % 2 == 0 and arr[i] % 2 == 0:
        count += 1

print("Count:", count)