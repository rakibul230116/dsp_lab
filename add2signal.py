
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6 * np.pi, 1000)

# User input
A1 = float(input("Enter amplitude of signal 1: "))
f1 = float(input("Enter frequency of signal 1: "))

A2 = float(input("Enter amplitude of signal 2: "))
f2 = float(input("Enter frequency of signal 2: "))

# Generate signals
x1 = A1 * np.sin(2 * np.pi * f1 * t)
x2 = A2 * np.sin(2 * np.pi * f2 * t)

# Addition
y = x1 + x2

# One figure with two parts
plt.figure(figsize=(10, 7))

# First part: Two signals
plt.subplot(2, 1, 1)
plt.plot(t, x1, label="Signal 1")
plt.plot(t, x2, label="Signal 2")
plt.title("Two Harmonics")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Second part: Addition signal
plt.subplot(2, 1, 2)
plt.plot(t, y, color="deeppink", label="Addition Signal")
plt.title("Adding Two Harmonics")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print("Addition result:", np.round(y[:10], 4))
