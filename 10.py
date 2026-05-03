#The "Swiss Army Knife" Dictionary (Using defaultdict)
from collections import defaultdict

# Groups words by their starting letter
words = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
grouped_words = defaultdict(list)

for word in words:
    grouped_words[word[0]].append(word)

print(dict(grouped_words)) 
# Output: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}