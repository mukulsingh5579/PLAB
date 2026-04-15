#Capitalize the first letter of each word
sentence = input("Enter a sentence: ")
words = sentence.split()

result = []
for word in words:
    result.append(word.capitalize())

print("Result:", " ".join(result))