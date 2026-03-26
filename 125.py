#Replace all 'a' with 'x' Recursively
def replace_char(s):
    if len(s) == 0:
        return ""
    if s[0] == 'a':
        return 'x' + replace_char(s[1:])
    else:
        return s[0] + replace_char(s[1:])

# Example
print(replace_char("banana"))