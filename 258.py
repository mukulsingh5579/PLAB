#Fetching Data from an API
import requests

def get_bored_suggestion():
    # A public API that suggests activities
    response = requests.get("https://www.boredapi.com/api/activity")
    if response.status_code == 200:
        data = response.json()
        return f"Try this: {data['activity']}"
    return "Could not find an activity."

# print(get_bored_suggestion())