#Check if element x exists in array
arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to search: "))

if x in arr:
    print("Element exists in array")
else:
    print("Element does not exist")