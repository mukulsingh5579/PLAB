#The Progress Bar (Without Libraries)
import time

def progress_bar(iteration, total, length=40):
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled = int(length * iteration // total)
    bar = '█' * filled + '-' * (length - filled)
    print(f'\rProgress: |{bar}| {percent}% Complete', end='\r')

# Usage
items = range(0, 50)
for i, item in enumerate(items):
    time.sleep(0.1)  # Simulating work
    progress_bar(i + 1, len(items))