import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib import style

x = [5,15,21,25,22,29,18,30,45,68,89,71,91,99,101,115]

bucket = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(x, bins= bucket, histtype='bar', label='age_group', color = 'g', rwidth=0.5)

plt.title("Age Survey")
plt.xlabel('Age Bucket')
plt.ylabel('Number of People')

plt.legend()

# plt.grid(True, color='b')

plt.show()