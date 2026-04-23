# Create a list of squares for even numbers only
numbers = range(10)
squares = [x**2 for x in numbers if x % 2 == 0]

print(squares)  # Output: [0, 4, 16, 36, 64]
