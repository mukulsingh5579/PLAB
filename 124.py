#Remove All Spaces Recursively
def remove_spaces(s):
    if len(s) == 0:
        return ""
    if s[0] == " ":
        return remove_spaces(s[1:])
    else:
        return s[0] + remove_spaces(s[1:])

# Example
print(remove_spaces("hello world"))