#Pairs with Given Sum
arr = [2, 4, 3, 5, 7, 8, 9]
target = 10

print("Pairs with sum =", target)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])