#Print numbers (1–100) whose digit sum is multiple of 3

for num in range(1, 101):
    digit_sum = sum(int(d) for d in str(num))
    
    if digit_sum % 3 == 0:
        print(num, end=" ")