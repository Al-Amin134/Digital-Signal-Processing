import numpy as np
import matplotlib.pyplot as plt
def six_point_averaging(x):
    y=[]
    length = len(x)
    for n in range(length):
        sum = 0
        for i in range(6):
            if(n-i>=0):
                sum+=x[n-i]
        sum/=6
        y.append(sum)
    return y

def six_point_deferencing(x):

    y = []
    x_len = len(x)
    for n in range(x_len):
       if(n-6>=0):
         y.append(x[n]-x[n-6])
       else:
          y.append(0)
    return y


x = [1,3,-2,4,5,-1,6,8,2,-3]
v = six_point_averaging(x)
print("mainx x(n) : ",x)
print("6-point averaging", [round(val,2)for val in v])

d = six_point_deferencing(x)
print("6-point differencing",[round(val,2) for val in d])
plt.subplot(3,2,1)
a = np.arange(0,len(x))
plt.stem(a,x)
plt.title("main x(n)")

plt.subplot(3,2,2)
plt.stem(a,v)
plt.title("6-point averaging")

plt.subplot(3,2,3)
plt.stem(a,d)
plt.title("6-point differencing")
plt.show()