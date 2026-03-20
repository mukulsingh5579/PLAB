#Print first n terms of an Arithmetic Progression (AP)

a = int(input("Enter first term (a): "))
d = int(input("Enter common difference (d): "))
n = int(input("Enter number of terms: "))

print("AP series:")
for i in range(n):
    print(a + i * d, end=" ")