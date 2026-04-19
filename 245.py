#Remove extra spaces between words (normalize spacing)
sentence = input("Enter a sentence: ")

words = sentence.split()   # removes extra spaces automatically
normalized = " ".join(words)

print(normalized)