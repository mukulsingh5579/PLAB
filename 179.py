#Frequency of each distinct element
arr = list(map(int, input("Enter elements: ").split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequencies:")
for key in freq:
    print(key, ":", freq[key])