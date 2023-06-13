import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import axes3d 

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.arange(-2,2,0.2)
y = np.arange(-2,2,0.2)
xmesh,ymesh = np.meshgrid(x,y)
zmesh = xmesh*np.exp(-xmesh**2-ymesh**2)
ax.plot_surface(xmesh,ymesh, zmesh)

plt.show()