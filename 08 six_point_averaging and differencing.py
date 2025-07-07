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


x = [1,3,-2,4,5,-1,6,8,2,-3]
avg1 = six_point_averaging(x)
diff = six_point_differencing(x)
print("six point averaging",[round(float(val),2) for val in avg1])
print("six point differencing",[round(float(val),2) for val in diff])
