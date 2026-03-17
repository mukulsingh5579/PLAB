#Count the number of digits

num = int(input("Enter a number: "))
count = 0

n = abs(num)  # handle negative numbers

if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count += 1

print("Number of digits:", count)