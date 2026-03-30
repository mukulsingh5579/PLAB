#Count how many times element appears
arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to count: "))

count = arr.count(x)
print("Count:", count)