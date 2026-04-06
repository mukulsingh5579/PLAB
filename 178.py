#Count elements greater than average
arr = list(map(int, input("Enter elements: ").split()))

avg = sum(arr) / len(arr)

count = 0
for num in arr:
    if num > avg:
        count += 1

print("Elements greater than average:", count)