import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-1, 5, 200)
def f(t):
    return (t* np.exp(-2*t))
plt.plot(t, f(t), '<', linewidth=2, color='g', markersize =10)
plt.title('$F(t) = t.exp^(-2t)$')
plt.xlabel('Eje t', fontsize = 14)
#a = plt.gca()
#a.set_axis_bgcolor('k')
plt.grid(True)
#plt.savefig('Graficala.png')
plt.show()