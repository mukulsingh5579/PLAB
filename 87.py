#Find the sum of all factors of a number

num = int(input("Enter a number: "))
sum_factors = 0

for i in range(1, num + 1):
    if num % i == 0:
        sum_factors += i

print("Sum of factors:", sum_factors)