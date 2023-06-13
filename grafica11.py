import matplotlib.pyplot as plt 
import numpy as np 
import math  

w = 2*np.pi 
xpoints  = np.linspace(-w , w)

def f(x):
    return(np.sin(3*xpoints)) 
def y(x):
    return(np.cos(4*xpoints))

plt.plot(xpoints, f(xpoints),'-', linewidth = 2, color = 'm', markersize =10)
plt.plot(xpoints, y(xpoints),'+--c', linewidth = 2, markersize = 10)
plt.title('$ x = sin(3t) $ \n $ x = sen(4t) $')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show() 
