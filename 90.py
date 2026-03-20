#Print first n terms of a Geometric Progression (GP)


a = int(input("Enter first term (a): "))
r = int(input("Enter common ratio (r): "))
n = int(input("Enter number of terms: "))

print("GP series:")
term = a
for i in range(n):
    print(term, end=" ")
    term *= r