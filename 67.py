#Sum of all even numbers up to n
n = int(input("Enter a number: "))

sum = 0
for i in range(2, n+1, 2):
    sum = sum + i

print("Sum of even numbers up to", n, "=", sum)