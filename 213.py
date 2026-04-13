#Find the second largest element in an array
arr = [10, 20, 4, 45, 99]

arr = list(set(arr))   # remove duplicates
arr.sort()

second_largest = arr[-2]

print("Second largest:", second_largest)