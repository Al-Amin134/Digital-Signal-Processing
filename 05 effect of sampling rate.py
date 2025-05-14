import numpy as np
import matplotlib.pyplot as plt

# Define analog signal
def xa(t):
    return 3*np.cos(200*np.pi*t) + 5*np.sin(600*np.pi*t) + 10*np.cos(1200*np.pi*t)

# Continuous-time signal
t_cont = np.linspace(0, 0.01, 1000)
x_cont = xa(t_cont)

# Sampling at 1500 Hz
fs1 = 1500
Ts1 = 1 / fs1
t_samp1 = np.arange(0, 0.01, Ts1)
x_samp1 = xa(t_samp1)

# Sampling at 1000 Hz
fs2 = 1000
Ts2 = 1 / fs2
t_samp2 = np.arange(0, 0.01, Ts2)
x_samp2 = xa(t_samp2)

# Sampling at 800 Hz
fs3 = 800
Ts3 = 1 / fs3
t_samp3 = np.arange(0, 0.01, Ts3)
x_samp3 = xa(t_samp3)

# Plotting
plt.figure(figsize=(12, 9))

# 1500 Hz
plt.subplot(3, 1, 1)
plt.title("Sampling at 1500 Hz (No Aliasing)")
plt.plot(t_cont, x_cont, color="lightgray", label="Original Signal")
plt.stem(t_samp1, x_samp1, linefmt='r-', markerfmt='ro', basefmt=' ', label="Sampled Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# 1000 Hz
plt.subplot(3, 1, 2)
plt.title("Sampling at 1000 Hz (Small Aliasing)")
plt.plot(t_cont, x_cont, color="lightgray", label="Original Signal")
plt.stem(t_samp2, x_samp2, linefmt='b-', markerfmt='bo', basefmt=' ', label="Sampled Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# 800 Hz
plt.subplot(3, 1, 3)
plt.title("Sampling at 800 Hz (Much Aliasing)")
plt.plot(t_cont, x_cont, color="lightgray", label="Original Signal")
plt.stem(t_samp3, x_samp3, linefmt='g-', markerfmt='go', basefmt=' ', label="Sampled Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
