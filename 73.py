#Check Palindrome
num = int(input("Enter a number: "))
original = num
rev = 0

n = abs(num)

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if num < 0:
    rev = -rev

if original == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")