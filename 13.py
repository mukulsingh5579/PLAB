#Custom Sorting with Lambda
players = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 70}
]

# Sort by the 'score' key in descending order
players.sort(key=lambda x: x['score'], reverse=True)

print(players[0]) 
# Output: {'name': 'Bob', 'score': 95}