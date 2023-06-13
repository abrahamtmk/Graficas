import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import axes3d 

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.arange(-10,10,0.5)
y = np.arange(-10,10,0.5)
xmesh,ymesh = np.meshgrid(x,y)
zmesh = np.sin(np.absolute(xmesh) - np.absolute(ymesh))
ax.plot_surface(xmesh,ymesh, zmesh)

ax.set_aspect('equal')
plt.show()