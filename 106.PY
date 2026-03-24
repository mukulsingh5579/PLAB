#GCD (HCF) using Euclid’s Algorithm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Example
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", gcd(a, b))