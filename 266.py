# Simulating data returned from a Web API
api_response = {
    "status": "success",
    "data": {
        "user_id": 101,
        "username": "coder_pro",
        "skills": ["Python", "HTML", "SQL"]
    }
}

# Accessing nested data safely
if api_response["status"] == "success":
    print(f"User: {api_response['data']['username']}")
    print(f"Top Skill: {api_response['data']['skills'][0]}")