#Count of prime numbers in array
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

count = 0

for i in arr:
    if is_prime(i):
        count += 1

print("Number of prime elements:", count)