#Print elements greater than given value k
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

k = int(input("Enter value of k: "))

print("Elements greater than", k, "are:")
for i in arr:
    if i > k:
        print(i, end=" ")