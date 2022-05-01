from matplotlib import pyplot as plt
from matplotlib import style

hours = [3,2,8,3,8]
activities = ['eating', 'walking', 'working', 'playing', 'sleeping']
colors = ['m', 'r', 'c', 'k', 'g']

plt.pie(hours,
        labels=activities,
        colors=colors,
        startangle=90,
        explode=(0, 0.1, 0, 0, 0),
        autopct='%1.1f%%',
        shadow=False)

plt.legend()
plt.title("My Activities")

plt.show()