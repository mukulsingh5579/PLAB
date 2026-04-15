#Print all words that start and end with the same letter
sentence = input("Enter a sentence: ")
words = sentence.split()

for word in words:
    if len(word) > 0 and word[0].lower() == word[-1].lower():
        print(word)