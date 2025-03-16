import numpy as np

sampling_rate = 0.1

x_samples = np.linspace(-20, 20, int(40 / sampling_rate))
y_samples = np.linspace(-20, 20, int(40 / sampling_rate))

samples = []

for x in x_samples:
    for y in y_samples:
        samples.append((x, y, (np.sin(x) - np.sin(2*x)/2 + np.sin(3*x)/3 - np.sin(4*x)/4) * (x**2 / (x + 1)) * (2 + np.cos(y) + np.cos(2*y - 1/2)/2)))

total_samples = len(samples)

first_five_samples = samples[:5]

print("Total number of samples:", total_samples)
print("First five samples:", first_five_samples)