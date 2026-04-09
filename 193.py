#File Reader (Read Any Text File)
filename = input("Enter file name: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("\nFile Content:\n", content)
except FileNotFoundError:
    print("File not found!")