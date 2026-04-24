#Smart Dictionary Merging (Python 3.9+)
user_profile = {"name": "Alex", "level": 10}
session_data = {"level": 11, "last_login": "2026-04-24"}

# The | operator merges them. If keys overlap, the second dict wins.
updated_profile = user_profile | session_data

print(updated_profile)
# Output: {'name': 'Alex', 'level': 11, 'last_login': '2026-04-24'}