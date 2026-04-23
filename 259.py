#Handling Files with Context Managers
# Writing and then reading a file
content = "Hello! This is a test file."

with open("example.txt", "w") as file:
    file.write(content)

with open("example.txt", "r") as file:
    print(file.read())