# Problem 11: Implement Discrete Fourier Transform (DFT)
# Computes X[k] = sum(n=0..N-1) x[n] exp(-j*2*pi*k*n/N).
import numpy as np
import matplotlib.pyplot as plt

N = int(input("Enter number of samples N: "))
if N <= 0:
    raise ValueError("N must be positive.")

x = np.array([float(v) for v in input(f"Enter {N} real-valued samples: ").split()])
if len(x) != N:
    raise ValueError("Please enter exactly N samples.")

X = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

print("DFT values X[k] =")
for k, value in enumerate(X):
    print(f"X[{k}] = {value.real:.4f} {value.imag:+.4f}j")

magnitude = np.abs(X)
print("Magnitude |X[k]| =", np.round(magnitude, 4))

plt.stem(np.arange(N), magnitude)
plt.title("Magnitude of Discrete Fourier Transform")
plt.xlabel("Frequency index k")
plt.ylabel("|X[k]|")
plt.grid(True)
plt.show()
