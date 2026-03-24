#Print Digits in Words (Recursively)
words = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]

def number_to_words(n):
    if n == 0:
        return
    number_to_words(n // 10)
    print(words[n % 10], end=" ")

# Example
num = int(input("Enter number: "))
if num == 0:
    print("zero")
else:
    number_to_words(num)