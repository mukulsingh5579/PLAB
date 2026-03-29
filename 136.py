#Count positive, negative, and zero elements
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

pos = neg = zero = 0

for i in arr:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)