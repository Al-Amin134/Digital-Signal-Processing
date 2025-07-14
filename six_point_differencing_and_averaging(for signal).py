import numpy as np
import matplotlib.pyplot as plt



def six_point_averaging(x):
    len_x = len(x)
    y = np.zeros_like(x, dtype=float)
    # y = []
    for n in range (len_x):
        sum = 0
        for i in range(6):
            if(n-i>=0):
                sum+=x[n-i]
        y[n]=sum/6
        # y.append(sum/6)
    return y
def six_point_differencing(x):
    len_x = len(x)
    y = np.zeros_like(x,dtype=float)
    for n in range(5,len_x):
        y[n] = (x[n]-x[n-1]+x[n-2]-x[n-3]+x[n-4]-x[n-5])/6
    return y

np.random.seed(0)
n = np.linspace(0,1,500)
x = np.sin(2*np.pi*5*n)+ 0.5*np.random.randn(len(n))
avg1 = six_point_averaging(x)
diff = six_point_differencing(x)
print("six point averaging",[round(float(val),2) for val in avg1])
print("six point differencing",[round(float(val),2) for val in diff])

plt.subplot(3,1,1)
plt.title("Main Signal")
plt.plot(n,x,label="main",color="r")
plt.xlabel("---->Time")
plt.ylabel("---->Amplitude")
plt.grid(True)
plt.legend()

plt.subplot(3,1,2)
plt.title("Six Point Differencing")
plt.plot(n,diff,label="diff",color="y")
plt.xlabel("---->Time")
plt.ylabel("---->Amplitude")
plt.grid(True)
plt.legend()

plt.subplot(3,1,3)
plt.title("Six Point Averaging")
plt.plot(n,avg1,label="avg",color="g")
plt.xlabel("---->Time")
plt.ylabel("---->Amplitude")
plt.grid(True)
plt.legend()



plt.show()