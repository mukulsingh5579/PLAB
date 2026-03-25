#Sum of Series with Steps (1 + 2 + ... + n)
def sum_series(n):
    if n == 1:
        print("1 = 1")
        return 1
    
    result = sum_series(n - 1) + n
    print(f"{n} added → total = {result}")
    return result

# Example
total = sum_series(5)
print("Final Sum =", total)