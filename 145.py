#Check if all elements are unique
arr = list(map(int, input("Enter elements: ").split()))

if len(arr) == len(set(arr)):
    print("All elements are unique")
else:
    print("Elements are not unique")