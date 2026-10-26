# Problem 09: Circular convolution using matrix method
import numpy as np
import matplotlib.pyplot as plt

N = int(input("Enter common length N of both signals: "))
if N <= 0:
    raise ValueError("N must be positive.")

x = np.array([float(v) for v in input(f"Enter {N} samples of x: ").split()])
h = np.array([float(v) for v in input(f"Enter {N} samples of h: ").split()])
if len(x) != N or len(h) != N:
    raise ValueError("Both signals must contain exactly N samples.")

X = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        X[i, j] = x[(i - j) % N]

y = X @ h
print("Circulant matrix X =")
print(X)
print("Circular convolution (matrix method) =", y)

plt.stem(np.arange(N), y)
plt.title("Circular Convolution - Matrix Method")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
