#Remove Duplicates from List
# Remove duplicates
nums = list(map(int, input("Enter numbers: ").split()))

unique = []
for num in nums:
    if num not in unique:
        unique.append(num)

print("Unique list:", unique)