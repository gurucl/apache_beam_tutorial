from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [1,2,3,4,5]
y = [2,6,4,10,8]

x1 = [3,5,7,9]
y1 = [6,9,12,8]

plt.plot(x,y,'g',label='lineOne',linewidth=3)
plt.plot(x1,y1,'r', label='linetwo', linewidth=3)

plt.xlabel("Number Of Chips")
plt.ylabel("Production Cost")
plt.title("Info Table")

plt.grid(True,color='k')
plt.legend()

plt.show()