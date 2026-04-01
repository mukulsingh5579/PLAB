#Replace every negative number with 0
arr = [3, -1, 4, 7, -5, 10]

no_negatives = [x if x >= 0 else 0 for x in arr]

print("No negatives:", no_negatives)