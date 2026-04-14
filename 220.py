#Print characters that appear more than once (without map/dictionary)
def repeated_chars(s):
    visited = ""
    
    for i in range(len(s)):
        if s[i] in visited:
            continue
        
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
        
        if count > 1:
            print(s[i], end=" ")
        
        visited += s[i]

# Example
repeated_chars("programming")  # r g m