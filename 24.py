#Basic Data Plotting
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker='o')
plt.title("Simple Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square")
plt.show()