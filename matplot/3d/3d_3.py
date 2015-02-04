
import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

xs = np.arange(-5, 5, 0.25)
ys = np.arange(-5, 5, 0.25)
#X, Y = np.meshgrid(xs, ys)
#R = np.sqrt(X**2 + Y**2)



Z = np.random.rand(len(X))

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.savefig('3d_3.png', dpi = 600)
