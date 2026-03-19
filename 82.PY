#Count numbers (1–500) divisible by 7 but not by 5

count = 0

for num in range(1, 501):
    if num % 7 == 0 and num % 5 != 0:
        count += 1

print("Count:", count)