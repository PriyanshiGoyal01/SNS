import numpy as np
import matplotlib.pyplot as plt
data= np.genfromtxt('data.csv',delimiter=',')[1:]
print(data.shape)
x_n = data[:,0]
y_n = data[:,1]

plt.plot(y_n)
plt.plot(x_n)
plt.show()
