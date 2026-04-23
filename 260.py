#Lambda Functions & Sorting
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort the list by 'age' instead of name
users.sort(key=lambda user: user["age"])

print(users)
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, ...]