#Word Guessing Game (Like Mini Hangman)
import random

words = ["python", "hacker", "coding", "matrix"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6

while tries > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    guess = input("Guess a letter: ")
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)

if "_" not in guessed:
    print("You win! Word was:", word)
else:
    print("You lose! Word was:", word)