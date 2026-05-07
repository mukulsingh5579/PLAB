# Writing to a file
with open('note.txt', 'w') as f:
    f.write("Python is pretty sleek.")

# Reading from a file
with open('note.txt', 'r') as f:
    print(f.read())