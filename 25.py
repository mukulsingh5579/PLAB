# Create a list of squares for even numbers from 0 to 10
squares = [x**2 for x in range(11) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64, 100]