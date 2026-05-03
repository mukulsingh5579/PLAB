#Using zip() for Parallel Iteration
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Bonus: zip(*zipped_list) can "unzip" the data back!