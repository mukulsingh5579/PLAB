#Remove extra spaces between words (normalize spacing)
sentence = input("Enter a sentence: ")

normalized = " ".join(sentence.split())

print("Normalized sentence:", normalized)