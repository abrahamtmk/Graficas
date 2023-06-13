import matplotlib.pyplot as plt 
import numpy as np 

tpoints = np.linspace(0, 4*np.pi, 100)
def f(t):
    return(np.sin(3*tpoints)*np.cos(2*tpoints))
def g(t):
    return((0.5*np.cos(tpoints))+(2.5*np.cos(5*tpoints)))
 
plt.plot(tpoints, f(tpoints),'-', linewidth = 2, color = 'b', markersize =10)
plt.plot(tpoints, g(tpoints),'D--g', linewidth = 2, markersize =10)
plt.title('$ sin(3t)cos(2t) $'+'$    1/2 cos(t)+5/2 cos(5t) $')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show() 
 
