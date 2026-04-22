#Simple Log Analyzer (Counts Errors in File)
error_count = 0

with open("log.txt", "r") as file:
    for line in file:
        if "error" in line.lower():
            error_count += 1

print("Total errors found:", error_count)