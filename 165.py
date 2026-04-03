#Find elements in one array but not in the other
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

only_in_arr1 = list(set(arr1) - set(arr2))
only_in_arr2 = list(set(arr2) - set(arr1))

print("Only in arr1:", only_in_arr1)
print("Only in arr2:", only_in_arr2)