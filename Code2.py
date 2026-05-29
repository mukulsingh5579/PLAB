import random

def guessing_game():
    # The computer selects a random number between 1 and 20
    secret_number = random.randint(1, 20)
    attempts = 0
    
    print("👋 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20. Can you guess it?")
    
    while True:
        # Get the player's guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! 📉 Try again.")
            elif guess > secret_number:
                print("Too high! 📈 Try again.")
            else:
                print(f"🎉 Correct! You found the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guessing_game()