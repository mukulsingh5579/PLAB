#Word Count in Sentence
text = input("Enter a sentence: ")

words = text.split()
print("Total words:", len(words))

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequency:")
for k, v in freq.items():
    print(k, ":", v)