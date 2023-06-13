import matplotlib.pyplot as plt 
import numpy as np 
from numpy import sin ,cos
import math 

w = 2*math.pi 
t = np.linspace(0 , w)

r = (2 - 2*np.sin(t)) + (np.sin(t) * np.sqrt(np.abs(np.cos(t)))/(np.sin(t) + 1.4)) 

x = r * np.cos(t)
y = r * np.sin(t)

fig = plt.figure(facecolor='m')

plt.fill_between(x, y, color='red')
plt.axis('equal')
plt.axis('off')

plt.show()