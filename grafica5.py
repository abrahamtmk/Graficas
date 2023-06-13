import matplotlib.pyplot as plt 
import numpy as np 
from numpy import sin, cos 
import math 

w = 4*math.pi
x = np.linspace(0, w)   
sx = cos(2*x) + sin(2*x)
vx = -2*sin(2*x) + 3*cos(3*x) 
plt.plot(x, sx,'-', linewidth = 2, color = 'b', markersize =10)
plt.title('h(t) = $sin(2t)exp^{-0,1t}$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show() 
 


