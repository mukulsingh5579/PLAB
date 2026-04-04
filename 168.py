#Element-wise product of two arrays
def elementwise_product(arr1, arr2):
    return [a * b for a, b in zip(arr1, arr2)]

# Example
A = [1, 2, 3]
B = [4, 5, 6]
print("Element-wise product:", elementwise_product(A, B))