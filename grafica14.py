import matplotlib.pyplot as plt 
import numpy as np 
from numpy import sin , cos
import math 

w = 2*math.pi
t = np.arange(0 , w , 0.015)
r = -250*np.sin(5*t)*np.cos(4*t)
z = t + np.sin(r/100)
x = 320 + r*np.cos(z)
y = -240 - r*np.sin(z)

plt.plot(x , y , linewidth = 5, color = 'k')
plt.fill_between(x , y , color ='m')
plt.axis('equal')
plt.axis('off')

plt.show()