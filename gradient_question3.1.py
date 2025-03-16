import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the functions g(x) and h(y)
def g(x):
    return (np.sin(x) - np.sin(2*x)/2 + np.sin(3*x)/3 - np.sin(4*x)/4) * (x**2 / (x + 1))

def h(y):
    return 2 + np.cos(y) + np.cos(2*y - 1/2)/2

# Generate grid points for x and y
x = np.linspace(-20, 20, 400)
y = np.linspace(-20, 20, 400)
X, Y = np.meshgrid(x, y)

# Calculate Z = f(x, y) = g(x) * h(y)
Z = g(X) * h(Y)

# Plot the function f(x, y) in 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')
plt.title('3D plot of the function f(x,y)')
plt.colorbar(surf, label='f(x, y)')
plt.show()
