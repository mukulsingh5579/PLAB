#Create a frequency array (count occurrences)
def frequency_array(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Example
A = [1, 2, 2, 3, 3, 3]
print("Frequency array:", frequency_array(A))