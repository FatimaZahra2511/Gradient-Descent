import numpy as np

def gradient_multidimensional(x, y):
    grad_x = (np.cos(x) - np.cos(2*x) + np.cos(3*x) - np.cos(4*x)) * ((x**2 - 2*x**3) / (x + 1)) + (-2*x**3 + 3*x**2 - x + 1) * ((np.sin(y) - np.sin(2*y + 1/2)) / 2 + np.sin(y) + np.cos(2*y - 1/2) / 2)
    grad_y = (-np.sin(y) - np.sin((2*y - 1)/2)/2)
    return grad_x, grad_y

cur_x = 0
cur_y = 0
rate = 0.01
precision = 0.0000001
max_iters = 10000
iters = 0

while iters < max_iters:
    prev_x = cur_x
    prev_y = cur_y
    grad_x, grad_y = gradient_multidimensional(prev_x, prev_y)
    cur_x = prev_x - rate * grad_x
    cur_y = prev_y - rate * grad_y
    iters += 1

    if abs(cur_x - prev_x) < precision and abs(cur_y - prev_y) < precision:
        print(f"Reached precision at iteration {iters}.")
        break

    print(f"Iteration {iters}: (x, y) = ({cur_x:.4f}, {cur_y:.4f})")

print("Local minimum occurs at:", cur_x, cur_y)
