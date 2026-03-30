#Find first occurrence of element
arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element: "))

if x in arr:
    print("First occurrence index:", arr.index(x))
else:
    print("Element not found")