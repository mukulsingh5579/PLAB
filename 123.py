#Count Vowels in a String Recursively
def count_vowels(s):
    vowels = "aeiouAEIOU"
    if len(s) == 0:
        return 0
    if s[0] in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

# Example
print(count_vowels("hello world"))