import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-10, 10, 40)
Y = np.linspace(-10, 10, 40)
x, y = np.meshgrid(X, Y)
u = y / (x**2 + y**2)
v = -x / (x**2 + y**2)
tot_vel = np.sqrt(u**2 + v**2)

plot = plt.quiver(x, y, u, v, tot_vel, cmap=plt.cm.jet)
plt.colorbar(plot, cmap=plt.cm.jet)
plt.show()