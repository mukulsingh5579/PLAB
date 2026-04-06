#Count pairs with sum = k
arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter value of k: "))

count = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == k:
            count += 1

print("Number of pairs:", count)