# scatter plots
import numpy as np
import matplotlib.pyplot as plt

num_points = 100
gradient = 0.5
x = np.array(range(num_points))
y = np.random.randn(num_points)*10+x*gradient
fig, ax = plt.subplots(figsize=(8,4))
'''
colors = np.random.rand(num_points)
size = (2+np.random.rand(num_points)*8)**2
ax.scatter(x,y,s=size,c=colors,alpha=0.5)
fig.suptitle('Scatterplot with color and size specified')
plt.show()
'''
ax.scatter(x,y)
m, c = np.polyfit(x,y,1) #1D regression method
ax.plot(x,m*x+c, color='r') #regression function
fig.suptitle('Scatterplot with regression')
plt.show()
