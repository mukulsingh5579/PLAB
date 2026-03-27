#Remove all occurrences of a character recursively

def remove_char(s, ch):
    if s == "":
        return ""
    
    if s[0] == ch:
        return remove_char(s[1:], ch)
    else:
        return s[0] + remove_char(s[1:], ch)

# Example
print(remove_char("banana", "a")) 