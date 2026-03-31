#Count numbers divisible by both 3 and 5
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

count = 0

for i in arr:
    if i % 3 == 0 and i % 5 == 0:
        count += 1

print("Count of numbers divisible by 3 and 5:", count)