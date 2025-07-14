import numpy as np
import matplotlib.pyplot as plt
x = [1,2,2,10,2,2,1]
alpha = [0.1,0.2,0.5,0.7,0.9]

n = len(x)

y1 ={}
for a in alpha:
    y = np.zeros(n)
    for i in range(1,len(x)):
      y[i] = (1-a)*y[i-1]+(a*x[i])
    y1[a]=y

for i in alpha:
    plt.plot(range(n),y1[i],label=i)
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
plt.show()