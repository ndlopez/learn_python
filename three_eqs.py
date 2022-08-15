'''
 Calculate the distance between 2 points
 dist=\sqrt{[(x_1-x_0)^2-(y_1-y_0)^2]}
 x_0,y_0: start point
 x_1,y_1: end point
'''
import pandas as pd
import numpy as np

point = np.array([[5,3],[3,-4],[-2,-4],[-3,5]])
print point
d = [(point[I,0]**2+point[I,1]**2)**0.5
        for I in range(4)]
re = np.c_[point, d]
re1 = pd.DataFrame(re)
re1.columns = ['x','y','dist']
re1.index = ['b','g','r','k']
print(re1)

'''Output
  x    y    dist
b 5.0  3.0  5.830952
g 3.0  -4.0 5.0
r -2   -4   4.472136
...
'''

############
# another code
import numpy.linalg as la
la.norm([[5.0],[3.0]])
a = np.array([[3][7]])
a_norm = la.norm(a)
a_unit = a/a_norm
print(a_unit)
