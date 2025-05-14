import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10,10,1)

unit = np.where(n>=0,1,0)


ramp = np.where(n>=0,n,0)


A = 1
b = 0.5
t = np.linspace(0,10,50)
exponetial1 = A*np.exp(b*t)



plt.subplot(6,1,1)
plt.stem(n,unit, label="Unit Sequence")
plt.title("Unit Step Sequence")
plt.xlabel("n")
plt.ylabel("value")
plt.grid("True")
plt.legend("Best")

plt.subplot(6,1,3)
plt.stem(n,ramp, label="ramp Sequence")
plt.title("Ramp Sequence")
plt.grid("True")
plt.xlabel("n")
plt.ylabel("value")
plt.legend("Best")

plt.subplot(6,1,5)
plt.stem(t,exponetial1,label="exponential form")
plt.title("Exponential Sequence")
plt.grid("True")
plt.legend("Best")
plt.xlabel("n")
plt.ylabel("value")
plt.show()
