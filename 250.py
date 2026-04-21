#Find Second Largest Number
numbers = list(map(int, input("Enter numbers: ").split()))

largest = second = -999999

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest number:", second)