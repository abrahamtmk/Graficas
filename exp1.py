import matplotlib.pyplot as plt 
import numpy as np 

i = np.arange(0, 2*np.pi, 0.01)

r = 2 - 2*np.sin(i) + np.sin(i) * np.sqrt(np.abs(np.cos(i))/np.sin(i) + 1.4) 

x = r * np.cos(i)
y = r * np.sin(i)

fig = plt.figure(facecolor='green')

plt.fill_between(x, y, color='blue')

plt.axis('equal')
plt.axis('off')

plt.show()