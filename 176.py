#Sum of all elements except largest and smallest
arr = list(map(int, input("Enter elements: ").split()))

if len(arr) <= 2:
    print("Not enough elements")
else:
    total = sum(arr)
    result = total - max(arr) - min(arr)
    print("Sum excluding largest and smallest:", result)