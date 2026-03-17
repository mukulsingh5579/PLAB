#Reverse of a number
num = int(input("Enter a number: "))
rev = 0

n = abs(num)

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

# Handle negative number
if num < 0:
    rev = -rev

print("Reversed number:", rev)