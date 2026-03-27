#Print all characters one by one recursively

def print_chars(s, index=0):
    if index == len(s):
        return
    
    print(s[index])
    print_chars(s, index + 1)

# Example
print_chars("hello")