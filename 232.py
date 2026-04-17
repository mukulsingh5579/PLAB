#Find Missing Number in Array (1 to n)
arr = [1, 2, 4, 5, 6]  # Missing 3
n = 6

total = n * (n + 1) // 2
sum_arr = sum(arr)

print("Missing Number:", total - sum_arr)