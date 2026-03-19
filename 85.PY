#Find smallest and largest digit in a number

num = int(input("Enter a number: "))

digits = [int(d) for d in str(num)]

print("Smallest digit:", min(digits))
print("Largest digit:", max(digits))