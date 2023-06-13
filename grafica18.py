import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
xmesh,ymesh = np.meshgrid(x,y)
zmesh = np.sqrt(np.absolute(np.cos(xmesh) + np.sin(ymesh))) 
ax.plot_surface(xmesh,ymesh, zmesh)

plt.show()