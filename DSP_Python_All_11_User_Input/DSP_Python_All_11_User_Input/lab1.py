# Problem 01: Convert a continuous-time signal to a discrete-time signal
# The computer samples x(t) at t = n/Fs.
import numpy as np
import matplotlib.pyplot as plt

A = float(input("Enter amplitude A: "))
f = float(input("Enter signal frequency f (Hz): "))
Fs = float(input("Enter sampling frequency Fs (Hz): "))
duration = float(input("Enter duration (seconds): "))

if f < 0 or Fs <= 0 or duration <= 0:
    raise ValueError("Frequency must be non-negative; Fs and duration must be positive.")

t = np.arange(0, duration, 1 / Fs)
x = A * np.sin(2 * np.pi * f * t)

plt.stem(t, x)
plt.title("Discrete-Time Samples of x(t) = A sin(2 pi f t)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

print("Sample times:", np.round(t, 4))
print("Discrete signal samples:", np.round(x, 4))
