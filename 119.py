#Character Pattern (A, AB, ABC, ...)
def char_pattern(n, current=1):
    if current > n:
        return
    
    for i in range(current):
        print(chr(65 + i), end="")
    print()
    
    char_pattern(n, current + 1)

# Example
char_pattern(4)