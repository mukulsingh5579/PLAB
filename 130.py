#Count vowels and consonants recursively

def count_vowels_consonants(s, index=0, v=0, c=0):
    vowels = "aeiouAEIOU"
    
    if index == len(s):
        return v, c
    
    if s[index].isalpha():
        if s[index] in vowels:
            v += 1
        else:
            c += 1
    
    return count_vowels_consonants(s, index + 1, v, c)
