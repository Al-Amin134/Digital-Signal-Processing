import numpy as np
import matplotlib.pyplot as plt

x = [1,3,-2,4]
y = [2,3,-1,3]
z = np.array([2,-1,4,-2])

def correlation(x,y):
    x_len = len(x)
    y_len = len(y)
    result = []
    for n in range(-y_len+1,x_len):
        sum = 0
        for k in range(x_len):
            if(n+k>=0 and n+k<y_len):
                sum+=x[k]*y[n+k]
        result.append(sum)
    return result 
y1 = correlation(x,y)
y3 = y1[::-1]
y2 = np.correlate(x,y,mode="full")
print(y3)
print(y2)