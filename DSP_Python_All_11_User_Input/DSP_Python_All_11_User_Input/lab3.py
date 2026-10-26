# Problem 03: Multiplication of two discrete-time signals
import numpy as np
import matplotlib.pyplot as plt

N = int(input("Enter number of samples in each signal: "))
if N <= 0:
    raise ValueError("Number of samples must be positive.")

x1 = np.array([float(v) for v in input(f"Enter {N} samples of x1 separated by spaces: ").split()])
x2 = np.array([float(v) for v in input(f"Enter {N} samples of x2 separated by spaces: ").split()])
if len(x1) != N or len(x2) != N:
    raise ValueError("Please enter exactly N samples for each signal.")

y = x1 * x2
print("Multiplication result y[n] =", y)

plt.stem(np.arange(N), y)
plt.title("Multiplication of Signals: y[n] = x1[n] x2[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
