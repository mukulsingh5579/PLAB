#Count vowels in each word of a sentence
def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()
    
    for word in words:
        count = 0
        for ch in word:
            if ch in vowels:
                count += 1
        print(word, "->", count)

# Example
count_vowels("hello world python")