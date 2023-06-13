import matplotlib.pyplot as plt
import numpy as np 
import math 

xpoints = np.linspace(0 ,2*np.pi, 100)

def f(x):
    return(np.cos(xpoints)**3)
def g(y):
    return(np.sin(xpoints)**3)
 
plt.plot(xpoints, f(xpoints),'-', linewidth = 2, color = 'm', markersize =10)
plt.plot(xpoints, g(xpoints),'D--c', linewidth = 2, markersize =10)
plt.title('$ x=cos^{3}(t) $ \n $ y=sin^{3}(t) $')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.show() 