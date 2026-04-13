#Find the sum of all elements at odd indices
arr = [10, 20, 30, 40, 50, 60]

sum_odd = 0
for i in range(len(arr)):
    if i % 2 != 0:
        sum_odd += arr[i]

print("Sum of elements at odd indices:", sum_odd)