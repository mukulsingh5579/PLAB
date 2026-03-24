#Print a line of n stars recursively

def print_line(n):
    if n == 0:
        return
    print("*", end="")
    print_line(n - 1)

# Example
n = 5
print_line(n)