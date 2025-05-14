import numpy as np
import matplotlib.pyplot as plt

def ax(t):
    return 3 * np.cos(100 * np.pi * t)  # 50 Hz cosine signal

# Continuous (original) signal
t_cont = np.linspace(0, 0.1, 1000)
x_cont = ax(t_cont)

# Sampling above Nyquist (fs = 200 Hz)
f1 = 200
ts1 = np.arange(0, 0.1, 1/f1)
fs1 = ax(ts1)

# Sampling below Nyquist (fs = 75 Hz)
f2 = 75
ts2 = np.arange(0, 0.1, 1/f2)
fs2 = ax(ts2)

# Plotting
plt.figure(figsize=(10, 6))

# No Aliasing
plt.subplot(3, 1, 1)
plt.title("fs ≥ Nyquist Rate (200 Hz): No Aliasing")
plt.plot(t_cont, x_cont, color="lightgray", label="Original Signal")
plt.stem(ts1, fs1, linefmt='b-', markerfmt='bo', basefmt=' ', label="Sampled at 200 Hz")
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend(loc="best")
plt.grid(True)

# With Aliasing
plt.subplot(3, 1, 3)
plt.title("fs < Nyquist Rate (75 Hz): Aliasing")
plt.plot(t_cont, x_cont, color="lightgray", label="Original Signal")
plt.stem(ts2, fs2, linefmt='r-', markerfmt='ro', basefmt=' ', label="Sampled at 75 Hz")
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend(loc="best")
plt.grid(True)

plt.tight_layout()
plt.show()
