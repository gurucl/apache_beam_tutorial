from matplotlib import pyplot as plt
from matplotlib import style

days = [1,2,3,4,5]

eating = [1,2,1,2,1]
working = [8,7,9,8,7]
sleeping = [6,7,6,7,8]
playing = [1,2,1,2,2]

plt.plot([], [], color = 'm', label = 'eating')
plt.plot([], [], color = 'r', label = 'working')
plt.plot([], [], color = 'c', label = 'sleeping')
plt.plot([], [], color = 'k', label = 'playing')

plt.stackplot(days, eating, working, sleeping, playing, colors=['m','r','c', 'k'])

plt.legend()
# plt.grid(True, color = 'g')

plt.title("Area Chart")
plt.xlabel("Number of Days")
plt.ylabel("Hours Spent")
plt.show()