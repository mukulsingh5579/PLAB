#Convert Number to Binary (Recursively)
def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)

# Example
num = int(input("Enter number: "))
result = to_binary(num)
print("Binary:", result if result else "0")