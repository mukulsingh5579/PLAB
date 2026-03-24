#Print a triangle of stars (top-down) recursively

def print_triangle(n):
    if n == 0:
        return
    
    # print one row
    def print_line(x):
        if x == 0:
            return
        print("*", end="")
        print_line(x - 1)
    
    print_line(n)
    print()
    
    print_triangle(n - 1)