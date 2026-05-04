#Dictionary Merging (The Pipe Operator)
user_info = {"name": "Alex", "age": 25}
user_settings = {"theme": "dark", "notifications": True}

# The | operator merges them
profile = user_info | user_settings

print(profile)