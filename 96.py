#Numbers from 1–n whose binary has even number of 1s
n = int(input("Enter n: "))

for i in range(1, n + 1):
    binary = bin(i)[2:]   # convert to binary
    count = binary.count('1')
    
    if count % 2 == 0:
        print(i, "->", binary)