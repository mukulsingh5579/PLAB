#World Clock (Datetime & Timezones)
from datetime import datetime, timedelta

# Get current UTC time
now_utc = datetime.utcnow()
# Manual offset for Tokyo (UTC+9)
tokyo_time = now_utc + timedelta(hours=9)

print(f"UTC Time: {now_utc.strftime('%H:%M:%S')}")
print(f"Tokyo Time: {tokyo_time.strftime('%H:%M:%S')}")