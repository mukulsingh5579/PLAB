#Check if two strings are anagrams (without using collections)
def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
    
    s1 = sorted(s1)
    s2 = sorted(s2)
    
    return s1 == s2

# Example
print(are_anagrams("listen", "silent"))  # True