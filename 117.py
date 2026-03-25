#Increasing & Decreasing Numbers in Same Function

def inc_dec(n):
    if n == 0:
        return
    inc_dec(n - 1)
    print(n, end=" ")
    inc_dec(n - 1)

# Example
inc_dec(3)