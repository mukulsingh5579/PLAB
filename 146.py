#Sum of even elements only
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

even_sum = 0

for i in arr:
    if i % 2 == 0:
        even_sum += i

print("Sum of even elements:", even_sum)