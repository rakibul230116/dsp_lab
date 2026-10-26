# Problem 06: Linear convolution of two discrete-time signals
import numpy as np
import matplotlib.pyplot as plt

nx = int(input("Enter number of samples in x: "))
if nx <= 0:
    raise ValueError("Signal length must be positive.")
x = np.array([float(v) for v in input(f"Enter {nx} samples of x: ").split()])
if len(x) != nx:
    raise ValueError("Please enter exactly nx samples.")

nh = int(input("Enter number of samples in h: "))
if nh <= 0:
    raise ValueError("Signal length must be positive.")
h = np.array([float(v) for v in input(f"Enter {nh} samples of h: ").split()])
if len(h) != nh:
    raise ValueError("Please enter exactly nh samples.")

y = np.convolve(x, h)
print("Linear convolution y[n] =", y)
print("Output length =", len(y), "= nx + nh - 1")

plt.stem(np.arange(len(y)), y)
plt.title("Linear Convolution")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
