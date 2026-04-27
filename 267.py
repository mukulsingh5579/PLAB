#Dictionary-Based "Switch" Case
def get_mood(color):
    modes = {
        "red": "Energetic or Angry",
        "blue": "Calm and Relaxed",
        "green": "Natural and Balanced",
        "yellow": "Happy and Bright"
    }
    return modes.get(color.lower(), "Unknown mood color")

user_color = input("Enter a color (Red/Blue/Green/Yellow): ")
print(f"The mood is: {get_mood(user_color)}")