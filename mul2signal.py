
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 6)

# First signal input
A1 = float(input("Enter amplitude of signal 1: "))
f1 = float(input("Enter frequency of signal 1: "))

# Second signal input
A2 = float(input("Enter amplitude of signal 2: "))
f2 = float(input("Enter frequency of signal 2: "))

# Generate signals
x1 = A1 * np.sin(2 * np.pi * f1 * n)
x2 = A2 * np.cos(2 * np.pi * f2 * n)

# Multiplication of signals
y = x1 * x2

# One figure with two parts
plt.figure(figsize=(10, 7))

# First part: Two signals
plt.subplot(2, 1, 1)
plt.plot(n, x1, marker='o', label="Signal 1")
plt.plot(n, x2, marker='o', label="Signal 2")
plt.title("Two Input Signals")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Second part: Multiplication result
plt.subplot(2, 1, 2)
plt.plot(n, y, marker='o', color="deeppink")
plt.title("Multiplication of Signals")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()

print("Signal 1:", np.round(x1, 4))
print("Signal 2:", np.round(x2, 4))
print("Multiplication result:", np.round(y, 4))
