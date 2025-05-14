import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 10)

# Define signals with different omegas
omega1 = np.pi / 2
x1 = np.cos(omega1 * n)

omega2 = np.pi / 4
x2 = np.cos(omega2 * n)

omega3 = np.pi
x3 = np.cos(omega3 * n)

# Plotting
plt.figure(figsize=(8, 6))

plt.subplot(3, 1, 1)
plt.stem(n, x1)
plt.title("x[n] = cos(pi/2 * n)")
plt.ylim([-1.2, 1.2])
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, x2)
plt.title("x[n] = cos(pi/4 * n)")
plt.ylim([-1.2, 1.2])
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, x3)
plt.title("x[n] = cos(pi * n)")
plt.ylim([-1.2, 1.2])
plt.grid(True)

plt.tight_layout()
plt.show()
