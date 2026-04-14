#Replace every vowel with its position (a=1, e=2...)
def replace_vowels(s):
    vowel_pos = "aeiou"
    result = ""
    
    for ch in s:
        if ch.lower() in vowel_pos:
            pos = vowel_pos.index(ch.lower()) + 1
            result += str(pos)
        else:
            result += ch
    
    return result

# Example
print(replace_vowels("hello"))  # h2ll4