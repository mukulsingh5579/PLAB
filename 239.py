#Find Missing Number in a List (1 to N)
nums = [1, 2, 4, 5, 6]   # Missing 3
n = 6

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

print("Missing number is:", expected_sum - actual_sum)