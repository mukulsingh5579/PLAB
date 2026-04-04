#Count common elements between two arrays
def count_common(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    common = set1 & set2
    return len(common)

# Example
A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
print("Common elements count:", count_common(A, B))