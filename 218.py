#Reverse words in a string if their length is even
def reverse_even_words(sentence):
    words = sentence.split()
    result = []
    
    for word in words:
        if len(word) % 2 == 0:
            result.append(word[::-1])
        else:
            result.append(word)
    
    return " ".join(result)

# Example
print(reverse_even_words("this is a test code"))