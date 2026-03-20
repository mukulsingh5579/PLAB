#Check if a number is a Strong Number


num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    
    # factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    
    sum_fact += fact
    temp //= 10

if sum_fact == num:
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")