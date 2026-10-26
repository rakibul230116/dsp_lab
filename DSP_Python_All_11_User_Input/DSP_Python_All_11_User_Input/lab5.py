# Problem 05: Find even and odd components of a signal
# Input samples must be ordered from n=-M to n=0 to n=+M (odd N).
import numpy as np
import matplotlib.pyplot as plt

N = int(input("Enter an odd number of samples (e.g. 5, 7, 9): "))
if N <= 0 or N % 2 == 0:
    raise ValueError("N must be a positive odd number.")

x = np.array([float(v) for v in input(f"Enter {N} samples from n=-M to n=+M: ").split()])
if len(x) != N:
    raise ValueError("Please enter exactly N samples.")

x_reverse = x[::-1]
xe = (x + x_reverse) / 2
xo = (x - x_reverse) / 2
n = np.arange(-(N // 2), N // 2 + 1)

print("Even component x_e[n] =", xe)
print("Odd component x_o[n] =", xo)

plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.title("Original Signal")
plt.grid(True)
plt.subplot(3, 1, 2)
plt.stem(n, xe)
plt.title("Even Component")
plt.grid(True)
plt.subplot(3, 1, 3)
plt.stem(n, xo)
plt.title("Odd Component")
plt.grid(True)
plt.tight_layout()
plt.show()
