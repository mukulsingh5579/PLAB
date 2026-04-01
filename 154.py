#Replace all even numbers with 1 and all odd with 0
arr = [3, -1, 4, 7, -5, 10]

even_odd_replaced = [1 if x % 2 == 0 else 0 for x in arr]

print("Even -> 1, Odd -> 0:", even_odd_replaced)