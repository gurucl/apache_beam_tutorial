from matplotlib import pyplot as plt
from matplotlib import style

# style.use('ggplot')

x = [1,2,3,4,5]
y = [2,4,6,8,10]

x1 = [1,3,4,5,6]
y1 = [1,2,3,4,5]

plt.bar(x, y, width = 0.5, bottom = None, align = 'center', label = 'lineOne')
plt.bar(x1, y1, width = 0.5, align = 'center', color = 'g', label = 'lineTwo')

plt.title("Bar Chart")
plt.xlabel("Number of Computer Chips")
plt.ylabel("Production Cost in Million $")

plt.legend()
# plt.grid(True, color = 'k')

plt.show()