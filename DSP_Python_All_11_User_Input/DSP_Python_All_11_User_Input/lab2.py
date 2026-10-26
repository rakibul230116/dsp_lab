
# Problem 02: Addition of Two Discrete-Time Signals

import numpy as np
import matplotlib.pyplot as plt

# User input
N = int(input("Enter number of samples in each signal: "))

if N <= 0:
    raise ValueError("Number of samples must be positive.")

x1 = np.array([
    float(v) for v in
    input(f"Enter {N} samples of x1 separated by spaces: ").split()
])

x2 = np.array([
    float(v) for v in
    input(f"Enter {N} samples of x2 separated by spaces: ").split()
])

if len(x1) != N or len(x2) != N:
    raise ValueError("Please enter exactly N samples for each signal.")

# Signal addition
n = np.arange(N)
y = x1 + x2

# Print results in terminal
print("\n========== RESULTS ==========")
print("Sample indices n =", n)
print("First signal x1[n] =", x1)
print("Second signal x2[n] =", x2)
print("Addition y[n] = x1[n] + x2[n] =", y)
print("Rounded result =", np.round(y, 4))
print("=============================")

# Plot three graphs
plt.figure(figsize=(9, 10))

plt.subplot(3, 1, 1)
plt.stem(n, x1)
plt.title("Graph 1: First Signal x1[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, x2)
plt.title("Graph 2: Second Signal x2[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, y)
plt.title("Graph 3: Addition y[n] = x1[n] + x2[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
