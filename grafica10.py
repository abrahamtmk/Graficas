import matplotlib.pyplot as plt 
import numpy as np 
import math 

xpoints = np.linspace(-2*np.pi, 2*np.pi ,100)

def f(x):
    return(x + 2*np.sin(2*x))
def y(x):
    return(x + 2*np.cos(5*x))   

plt.plot(xpoints, f(xpoints),'-', linewidth = 2, color = 'm', markersize =10)
plt.plot(xpoints, y(xpoints),'+--c', linewidth = 2, markersize =10)
plt.title('$ x=t + 2sin(2t) $ \n $ y=t + 2cos(5t) $')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.show() 
