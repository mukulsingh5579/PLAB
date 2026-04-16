#Second Largest Element
# Find second largest number
nums = list(map(int, input("Enter numbers: ").split()))

nums = list(set(nums))  # remove duplicates
nums.sort()

print("Second largest:", nums[-2])