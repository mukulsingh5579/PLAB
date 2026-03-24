#Print a square of stars (n × n) recursively

def print_line(n):
    if n == 0:
        return
    print("*", end="")
    print_line(n - 1)

def print_square(n):
    if n == 0:
        return
    print_line(n)
    print()  # new line
    print_square(n - 1)

# Example
n = 4
print_square(n)