#Sum of odd elements only
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

odd_sum = 0

for i in arr:
    if i % 2 != 0:
        odd_sum += i

print("Sum of odd elements:", odd_sum)