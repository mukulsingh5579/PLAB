#Find all pairs of same characters (nested loop)
s = "programming"

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            print(f"Pair found: {s[i]} at positions {i} and {j}")