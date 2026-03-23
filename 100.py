#Sum of odd digits and even digits separately
num = int(input("Enter a number: "))

odd_sum = 0
even_sum = 0

for digit in str(num):
    d = int(digit)
    
    if d % 2 == 0:
        even_sum += d
    else:
        odd_sum += d

print("Sum of even digits:", even_sum)
print("Sum of odd digits:", odd_sum)