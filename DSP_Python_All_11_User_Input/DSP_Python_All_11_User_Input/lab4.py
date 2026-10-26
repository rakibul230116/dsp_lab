
# Problem 04: Amplitude Scaling of a Discrete-Time Signal

import numpy as np
import matplotlib.pyplot as plt

# User input
N = int(input("Enter number of samples: "))

if N <= 0:
    raise ValueError("Number of samples must be positive.")

A = float(input("Enter scaling factor A: "))

x = np.array([
    float(v)
    for v in input(f"Enter {N} samples of x separated by spaces: ").split()
])

if len(x) != N:
    raise ValueError("Please enter exactly N samples.")

# Amplitude scaling
n = np.arange(N)
y = A * x

# Print results
print("\n----- Results -----")
print("Sample index n =", n)
print("Original signal x[n] =", x)
print("Scaling factor A =", A)
print("Scaled signal y[n] = A * x[n] =", y)

# Plot using subplots
plt.figure(figsize=(10, 7))

plt.subplot(2, 1, 1)
plt.stem(n, x)
plt.title("Original Signal x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(n, y)
plt.title(f"Amplitude Scaled Signal y[n] = {A} x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
