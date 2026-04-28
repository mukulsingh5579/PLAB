#Working with Dates and Times
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current Date and Time: {formatted_date}")