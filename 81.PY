#Print numbers (1–100) whose sum of digits is even

for num in range(1, 101):
    digit_sum = sum(int(d) for d in str(num))
    
    if digit_sum % 2 == 0:
        print(num, end=" ")