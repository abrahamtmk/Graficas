import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 5, 200)
fx = 2*x**2 - 8*x - 11
plt.plot(x, fx, '<', linewidth=3, color='g', markersize =10)
plt.title('$F(x) = 2x2 - 8x - 11$')
plt.xlabel('Eje x', fontsize = 14)
#a = plt.gca()
#a.set_axis_bgcolor('k')
plt.grid(True)
#plt.savefig('Graficala.png')
plt.show()