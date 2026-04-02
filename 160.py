#Copy one array to another manually
arr1 = [1, 2, 3, 4, 5]
arr2 = []

for i in range(len(arr1)):
    arr2.append(arr1[i])

print("Original array:", arr1)
print("Copied array:", arr2)