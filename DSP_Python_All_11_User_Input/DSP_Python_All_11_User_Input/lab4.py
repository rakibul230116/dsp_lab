# Problem 04: Amplitude scaling of a discrete-time signal
import numpy as np
import matplotlib.pyplot as plt

N = int(input("Enter number of samples: "))
if N <= 0:
    raise ValueError("Number of samples must be positive.")
A = float(input("Enter scaling factor A: "))
x = np.array([float(v) for v in input(f"Enter {N} samples of x separated by spaces: ").split()])
if len(x) != N:
    raise ValueError("Please enter exactly N samples.")

y = A * x
print("Scaled signal y[n] =", y)

plt.stem(np.arange(N), y)
plt.title(f"Amplitude Scaling: y[n] = {A} x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
