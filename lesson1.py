import math
import numpy as np
from matplotlib import pyplot as plt

# Create grid
point_number = 20
x_start, x_end = -2, 2
y_start, y_end = -1, 1
x_grid = np.linspace(x_start, x_end, point_number)
y_grid = np.linspace(y_start, y_end, point_number)
X, Y = np.meshgrid(x_grid, y_grid)

# Source and Sink parameters
x_source = -1
y_source = 0
x_sink = 1
y_sink = 0
strength_source = 5
strength_sink = -5
u_source = (strength_source / (2 * math.pi) * (X - x_source) / ((X - x_source)**2 + (Y - y_source)**2))
v_source = (strength_source / (2 * math.pi) * (Y - y_source) / ((X - x_source)**2 + (Y - y_source)**2))
u_sink = (strength_sink / (2 * math.pi) * (X - x_sink) / ((X - x_sink)**2 + (Y - y_sink)**2))
v_sink = (strength_sink / (2 * math.pi) * (Y - y_sink) / ((X - x_sink)**2 + (Y - y_sink)**2))

# Velocity fields
u_res = u_source + u_sink
v_res = v_source + v_sink
total_velocity = np.sqrt(u_res**2 + v_res**2)


plt.xlabel('x')
plt.ylabel('y')
# plt.scatter(x_source, y_source, color='red')
# plt.scatter(x_sink, y_sink, color='orange')
plt.streamplot(X, Y, u_res, v_res, density=2)
cp = plt.contourf(X, Y, total_velocity)
plt.colorbar(cp)
plt.show()
