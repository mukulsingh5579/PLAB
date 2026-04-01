#Create a new array containing only even elements
arr = [3, -1, 4, 7, -5, 10]

evens = [x for x in arr if x % 2 == 0]

print("Even elements:", evens)