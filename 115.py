#Reverse Triangle Pattern (Recursively)

def reverse_triangle(n):
    if n == 0:
        return
    print("*" * n)
    reverse_triangle(n - 1)

# Example
reverse_triangle(4)