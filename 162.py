#Check if two arrays contain same elements (ignore order)
arr1 = [1, 2, 3, 4]
arr2 = [4, 3, 2, 1]

if sorted(arr1) == sorted(arr2):
    print("Arrays have same elements")
else:
    print("Arrays do not have same elements")