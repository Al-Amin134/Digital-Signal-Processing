# frequency domain a multiplication = time domain a convolution
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [5,3,4,2,1]
x = np.array(x)
y = np.array(y)
xt = np.convolve(x,y)
N = len(x)+len(y)-1
X1 = np.fft.fft(x,N)
Y1 = np.fft.fft(y,N) 
xn = np.fft.ifft(X1*Y1).real
print([round(float(val),2) for val in xt])
print([round(float(val),2) for val in xn])

plt.plot(range(N),xt,label="Time domain convolution",color="r")
plt.plot(range(N),xn,label="Frequency domain multiplication",color="g")
plt.legend()
plt.grid(True)
plt.show()