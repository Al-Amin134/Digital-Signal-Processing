//Jodi convolution diyei krte chai:
import numpy as np
import matplotlib.pyplot as plt

def correlation(x,y):
    y = y[::-1]
    len_x = len(x)
    len_y = len(y)
    len_res = len(x)+len(y)-1
    res = np.zeros(len_res)
    for n in range(len_res):
        sum = 0
        for k in range(len_y):
            if 0<=n-k<len_x:
                sum+=(y[k]*x[n-k])
        res[n]=sum 
    return res 


def normalized(x,y):
    x = np.array(x)
    y = np.array(y)
    numerator = np.sum(x*y)
    denominator = np.sqrt(np.sum(x*x))*np.sqrt(np.sum(y*y))
    return numerator/denominator

x = [1,2,3,4,5]
y = [7,8,9,10,13]
z = [1,1,1,1,0]

y1 = correlation(x,y)
y2 =np.correlate(x,y,mode='full')

y3 = normalized(y,z) 

print([round(float(val),2)for val in y1])
print([round(float(val),2)for val in y2])

print(y3)





// Shudhu correlation alada kre
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

