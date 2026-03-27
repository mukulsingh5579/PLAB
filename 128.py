#Print string in reverse recursively (no loop)
def reverse_string(s):
    if s == "":
        return ""
    
    return reverse_string(s[1:]) + s[0]

# Example
print(reverse_string("hello"))  