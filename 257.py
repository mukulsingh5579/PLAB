#Dictionary Comprehension (Frequency Counter)
text = "apple banana apple cherry banana apple"
word_count = {word: text.split().count(word) for word in set(text.split())}

print(word_count) 
# Output: {'cherry': 1, 'apple': 3, 'banana': 2}