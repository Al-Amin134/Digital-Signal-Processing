import numpy as np
import matplotlib.pyplot as plt

def u(n):
    return 1 if n>=0 else 0
def h(n):
    return u(n)-u(n-5)
def x(n):
    return u(n)


def convolution(x_func, h_func,n_min, n_max):
    y = []
    for n in range(n_min, n_max+1):
        sum = 0
        for k in range (n_min,n+1):
            sum+=h_func(k)*x_func(n-k)
        y.append(sum)
    return y
n_min = 0
n_max = 20
n = np.arange(0,n_max+1,1)
y1 = convolution(x,h,n_min,n_max)
print(y1)
plt.stem(n,y1)
plt.show()