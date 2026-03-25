#Multiplication Table of n (Recursively)

def multiplication_table(n, i=1):
    if i > 10:
        return
    print(f"{n} x {i} = {n*i}")
    multiplication_table(n, i + 1)

# Example