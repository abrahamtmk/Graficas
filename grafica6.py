import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0, 2, 100)

fc = x*np.exp(-3*x)
fd = 1 - 3*np.exp(-3*x)

plt.plot(x, fc,'-', linewidth = 2, color = 'b', markersize =10)
plt.plot(x, fd,'-', linewidth = 2, color = 'g', markersize =10)
plt.title('$fd = 1 - 3e^{-3x}\n fc= xe^(-3x) $')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.grid(True)
plt.show() 
 



