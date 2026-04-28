# Writing to a file
with open("note.txt", "w") as file:
    file.write("Python was here!\nThis is a new line.")

# Reading from a file
with open("note.txt", "r") as file:
    content = file.read()
    print(content)