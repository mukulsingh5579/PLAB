#The Instant Progress Bar
import time

def progress_bar(iteration, total, length=40):
    percent = f"{100 * (iteration / float(total)):.11f}"
    filled = int(length * iteration // total)
    bar = "█" * filled + "-" * (length - filled)
    print(f"\r|{bar}| {percent}% Complete", end="\r")

# Usage
items = range(100)
for i, item in enumerate(items):
    time.sleep(0.05)  # Simulating work
    progress_bar(i + 1, len(items))