from matplotlib import pyplot as plt
from matplotlib import style

x = [1,2,3,4,5]
y = [2,4,6,8,4]

plt.scatter(x,y, label = 'Scatter points', color = 'g')

plt.title("Scatter Plot Graph")
plt.xlabel("Quantity")
plt.ylabel("Value")

plt.legend()

# plt.grid(True, color = 'b')

plt.show()