import math
import matplotlib.pyplot as plt
import numpy as np


def get_velocity(strength, xs, ys, x, y):
    u = (strength / (2 * np.pi) * (x - xs) / ((x - xs)**2 + (y - ys)**2))
    v = strength / (2 * np.pi) * (y - ys) / ((x - xs)**2 + (y - ys)**2)
    return u, v


def get_stream_function(strength, xs, ys, x, y):
    psi = strength / (2 * np.pi) * np.arctan2((y - ys), (x - xs))
    return psi


def vector_field_plot(x, y, u_abs, v_abs):
    # Plot streamlines
    arrow_len = np.sqrt(u_abs ** 2 + v_abs ** 2)
    u_norm = u / arrow_len
    v_norm = v / arrow_len
    color = arrow_len
    plot = plt.quiver(x, y, u_norm, v_norm, color, headwidth=1.5, headlength=3, cmap=plt.cm.jet)
    plt.colorbar(plot, cmap=plt.cm.jet)


def streamlines_plot(x, y, u_abs, v_abs):
    plt.streamplot(x, y, u_abs, v_abs, density=2, linewidth=1, arrowsize=1, arrowstyle='->')


def scatter_plot(x, y):
    # Plot scatter
    plt.scatter(x, y, s=5, color='red')


# Generates a meshgrid
n = 50
x_start, x_end = -4.0, 4.0
y_start, y_end = -2.0, 2.0
x = np.linspace(x_start, x_end, n)
y = np.linspace(y_start, y_end, n)
X, Y = np.meshgrid(x, y)

# Ambient Conditions
sigma_source = 20
sigma_sink = -20
x_source, y_source = -1, 0
x_sink, y_sink = 1, 0
u_sorc, v_sorc = get_velocity(sigma_source, x_source, y_source, X, Y)
u_sink, v_sink = get_velocity(sigma_sink, x_sink, y_sink, X, Y)
u_free, v_free = 0, 0
u, v = u_sorc + u_free + u_sink, v_sorc + v_free + v_sink

# Plot streamlines
vector_field_plot(X, Y, u, v)

# Plot scatter
scatter_plot(x_source, y_source)
scatter_plot(x_sink, y_sink)

# General Plot configs
plt.xlim(x_start - 1, x_end + 1)
plt.ylim(y_start - 1, y_end + 1)
plt.show()
