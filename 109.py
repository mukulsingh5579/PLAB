#Sum of First n Even Numbers
def sum_even(n):
    if n == 0:
        return 0
    return 2*n + sum_even(n-1)

# Example
n = int(input("Enter n: "))
print("Sum of first", n, "even numbers:", sum_even(n))