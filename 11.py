#List Flattening with "Double Comprehension"
nested_list = [[1, 2], [3, 4], [5, 6]]

# Read as: "give me x for each sublist in nested_list, and for each x in that sublist"
flattened = [item for sublist in nested_list for item in sublist]

print(flattened) 
# Output: [1, 2, 3, 4, 5, 6]