# Problem 08: Circular convolution using circle/circular-shifting method
import numpy as np
import matplotlib.pyplot as plt

N = int(input("Enter common length N of both signals: "))
if N <= 0:
    raise ValueError("N must be positive.")

x = np.array([float(v) for v in input(f"Enter {N} samples of x: ").split()])
h = np.array([float(v) for v in input(f"Enter {N} samples of h: ").split()])
if len(x) != N or len(h) != N:
    raise ValueError("Both signals must contain exactly N samples.")

y = np.zeros(N)
for n in range(N):
    for k in range(N):
        y[n] += x[k] * h[(n - k) % N]

print("Circular convolution (circle method) =", y)

plt.stem(np.arange(N), y)
plt.title("Circular Convolution - Circle Method")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
