#Sum of First n Odd Numbers
def sum_odd(n):
    if n == 0:
        return 0
    return (2*n - 1) + sum_odd(n-1)

# Example
n = int(input("Enter n: "))
print("Sum of first", n, "odd numbers:", sum_odd(n))