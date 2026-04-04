#Print elements appearing more than once
def duplicates(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    for key, value in freq.items():
        if value > 1:
            print(key, end=" ")

# Example
A = [1, 2, 2, 3, 4, 4, 5]
print("Duplicate elements:", end=" ")
duplicates(A)