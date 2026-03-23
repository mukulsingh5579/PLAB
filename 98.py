#Take 5 numbers, skip 0 using continue, sum non-zero numbers
total = 0

for i in range(5):
    num = int(input("Enter number: "))
    
    if num == 0:
        continue
    
    total += num

print("Sum of non-zero numbers:", total)