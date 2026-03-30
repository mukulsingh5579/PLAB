#Find last occurrence of element
arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element: "))

if x in arr:
    last_index = len(arr) - 1 - arr[::-1].index(x)
    print("Last occurrence index:", last_index)
else:
    print("Element not found")