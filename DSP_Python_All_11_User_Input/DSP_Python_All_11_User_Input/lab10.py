# Problem 10: Implement Fourier Series
# Uses standard Fourier-series approximations for square, sawtooth, or triangle waves.
import numpy as np
import matplotlib.pyplot as plt

wave = input("Choose waveform (square / sawtooth / triangle): ").strip().lower()
T = float(input("Enter period T (> 0): "))
K = int(input("Enter number of harmonics (> 0): "))
points = int(input("Enter number of time points (at least 100 recommended): "))

if wave not in {"square", "sawtooth", "triangle"}:
    raise ValueError("Choose square, sawtooth, or triangle.")
if T <= 0 or K <= 0 or points < 2:
    raise ValueError("T and harmonics must be positive; points must be at least 2.")

t = np.linspace(-T, T, points)
w0 = 2 * np.pi / T
y = np.zeros_like(t)

if wave == "square":
    # x(t) = (4/pi) * [sin(w0t) + sin(3w0t)/3 + ...]
    for k in range(1, K + 1):
        harmonic = 2 * k - 1
        y += (4 / np.pi) * np.sin(harmonic * w0 * t) / harmonic
elif wave == "sawtooth":
    # x(t) = (2/pi) * sum((-1)^(k+1) sin(k*w0*t)/k)
    for k in range(1, K + 1):
        y += (2 / np.pi) * ((-1) ** (k + 1)) * np.sin(k * w0 * t) / k
else:
    # Triangle wave: odd cosine harmonics, alternating signs, 1/harmonic^2.
    for k in range(K):
        harmonic = 2 * k + 1
        y += (8 / np.pi**2) * ((-1) ** k) * np.cos(harmonic * w0 * t) / (harmonic**2)

print(f"Fourier series approximation for {wave} wave generated with {K} harmonics.")
plt.plot(t, y)
plt.title(f"Fourier Series Approximation: {wave.title()} Wave")
plt.xlabel("Time t")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
