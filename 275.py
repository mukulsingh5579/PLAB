#Merging Dictionaries (The | Operator)
defaults = {"theme": "light", "notifications": True}
user_settings = {"theme": "dark"}

# The right-hand side takes priority
final_config = defaults | user_settings

print(final_config)
# Output: {'theme': 'dark', 'notifications': True}