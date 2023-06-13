import matplotlib.pyplot as plt 
import numpy as np 

tpoints = np.linspace(0, 2*np.pi, 100)
def x(t):
    return((1 + np.sin(tpoints))*(np.cos(tpoints)))
def y(t):
    return(1 + (2*np.sin(tpoints))*(np.sin(tpoints)))
 
plt.plot(tpoints, x(tpoints),'-', linewidth = 2, color = 'b', markersize =10)
plt.plot(tpoints, y(tpoints),'D--g', linewidth = 2, markersize =10)
plt.title('$ x(t)=(1+sin(t))*cos(t) $\n$    y(t)=(1+2sin(t))(sin(t))$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.show() 