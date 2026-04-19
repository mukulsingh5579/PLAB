#Count how many words contain the letter ‘a’
sentence = input("Enter a sentence: ")

words = sentence.split()
count = 0

for word in words:
    if 'a' in word.lower():
        count += 1

print("Words containing 'a':", count)