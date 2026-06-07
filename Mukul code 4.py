def greet_user(name):
    """A simple function to greet a user."""
    return f"Hello, {name}! Welcome to the world of Python."


def main():
    # 1. Ask the user for their name
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
    
    print("\nLet's count to 3:")
    # 2. A simple for loop
    for i in range(1, 4):
        print(f"Number: {i}")
        
    # 3. Working with a list
    programming_languages = ["Python", "JavaScript", "C++"]
    print("\nHere are a few awesome languages:")
    for lang in programming_languages:
        print(f"- {lang}")

# This ensures the code only runs if you execute this script directly
if __name__ == "__main__":
    main()