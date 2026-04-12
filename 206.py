#Multiplication Table (10×10 Grid)
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end=" ")  # formatted spacing
    print()