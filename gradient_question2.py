def gradient(x):
    return 6 * (3 * x + 5)

cur_x = 3
rate = 0.01
precision = 0.0000001
max_iters = 10000
iters = 0
prev_x = cur_x

while iters < max_iters:
    cur_x = cur_x - rate * gradient(prev_x)
    difference = abs(cur_x - prev_x)
    
    if difference < precision:
        break
    
    prev_x = cur_x
    iters += 1
    
    cur_y = (3 * cur_x + 5) ** 2
    grad_value = gradient(cur_x)

    print(f"Iteration {iters}: (x, y) = ({cur_x:.4f}, {cur_y:.4f}), Gradient = {grad_value:.4f}, Difference = {difference:.10f}")

print("Local minimum occurs at:", cur_x)