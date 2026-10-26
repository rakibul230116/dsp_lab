# Problem 07: Deconvolution by polynomial long division
# Assumes y is the convolution of x and h, and h[0] is non-zero.
import numpy as np
import matplotlib.pyplot as plt

ny = int(input("Enter number of samples in convolution result y: "))
if ny <= 0:
    raise ValueError("Length must be positive.")
y = np.array([float(v) for v in input(f"Enter {ny} samples of y: ").split()], dtype=float)
if len(y) != ny:
    raise ValueError("Please enter exactly ny samples.")

nh = int(input("Enter number of samples in known signal h: "))
if nh <= 0 or nh > ny:
    raise ValueError("h length must be positive and no greater than y length.")
h = np.array([float(v) for v in input(f"Enter {nh} samples of h: ").split()], dtype=float)
if len(h) != nh:
    raise ValueError("Please enter exactly nh samples.")
if abs(h[0]) < 1e-12:
    raise ValueError("h[0] must be non-zero for this deconvolution method.")

work = y.copy()
nx = ny - nh + 1
x = np.zeros(nx)

for i in range(nx):
    x[i] = work[i] / h[0]
    for j in range(nh):
        work[i + j] -= x[i] * h[j]

print("Recovered signal x[n] =", np.round(x, 8))
print("Remainder (should be near zero) =", np.round(work, 8))

plt.stem(np.arange(len(x)), x)
plt.title("Recovered Signal by Deconvolution")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
