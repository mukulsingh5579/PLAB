#Check Perfect Square (Without Using sqrt())
num = int(input("Enter a number: "))

i = 1
is_square = False

while i * i <= num:
    if i * i == num:
        is_square = True
        break
    i += 1

if is_square:
    print("Number is a Perfect Square")
else:
    print("Number is NOT a Perfect Square")