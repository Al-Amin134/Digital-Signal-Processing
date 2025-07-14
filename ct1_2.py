import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0,1,100)
x = np.sin(2*np.pi*500*n)+np.random.randn(len(n))
alpha = [0.2,0.3,0.5,0.7]

res = {}
for a in alpha:
    y=np.zeros(len(n))
    for i in range(1,len(n)):
        y[i]=(1-a)*y[i-1]+a*x[i]
    res[a]=y
for a in alpha:
    plt.plot(n,res[a],label=a)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
plt.show()
