#Find second smallest element
arr = [10, 20, 4, 45, 99]

smallest = second_smallest = float('inf')

for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second smallest element:", second_smallest)