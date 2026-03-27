#Convert string to uppercase recursively

def to_upper(s):
    if s == "":
        return ""
    
    return s[0].upper() + to_upper(s[1:])

# Example
print(to_upper("hello world")) 