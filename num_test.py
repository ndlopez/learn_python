import numpy as np
a=np.array([1,2,3,4,5,6,7,8])
def array_details(a):
  print('Dimensions: %d, shape: %s, dtype:%s',(a.ndim, a.shape, a.dtype))
print(a)
array_details(a)
print(a[::-1])
a=a.reshape([2,4])
array_details(a)
print('a*2',a*2)
#creates an array of evenly spaced numbers over an interval
b=np.linspace(2,10,5)# 4 numbers between 2 and 10
print('using linspace',b)
b=np.arange(2,10,2) # from 2 to 10 with step-size 2
print('using arange',b)

pi=np.pi
a=np.array([pi,pi/2,pi/4,pi/6])

print('convert rad to deg',np.degrees(a))
sin_a=np.sin(a)
print('get sin(a)',np.round(sin_a,7))#round to 7 decimals
a=np.arange(8).reshape((2,4))
print('2x4 array',a)
print('cumulative sum',np.cumsum(a,axis=1))

#calc moving avg of an array
def moving_avg(a,n=3):
  ret=np.cumsum(a,dtype=float)
  ret[n:]=ret[n:] - ret[:-n]
  return ret[n -1:]/n
a=np.arange(12)
print('Moving avg of a 1D array\n',moving_avg(a,4))

a=np.arange(20).reshape(5,4)
print(a)
print('w/no axis',np.argmax(a))
print('w/axis=1 each row',np.argmax(a,axis=1))
print('w/axis=0 each column',np.argmax(a,axis=0))

array=np.array([[3,7,1],[10,3,2],[5,6,7]])
print(array)
print('sort the array',np.sort(array,axis=None))
print('sort along each row', np.sort(array,axis=1))
print('sort along each col', np.sort(array,axis=0))

array=np.array([28,13,45,12,4,8,0])
print(array)
print('sort indices',np.argsort(array))

list=[
  np.array([3,2,8,9]),
  np.array([4,12,34,25,78]),
  np.array([23,12,67])]
result=[]
for i in range(len(list)):
  result.append(np.mean(list[i]))
print(result)
array=np.array([
  [3,2,8],[4,12,33],[23,12,67]
])
print(array)
newRow=np.array([2,4,8])
newArray=np.vstack((array,newRow))
print('adding a row',newArray)
newCol=np.array([2,1,8])
newArray=np.column_stack((array,newCol))
print('adding a col',newArray)
#print a checker pattern of 1, 0s
n=8
mat=np.zeros((n,n),dtype=int)
#fill 1 with alt rows 0 and cols
mat[::2,1::2]=1
mat[1::2,::2]=1
#print the checker pattern
for i in range(n):
  for j in range(n):
    print(mat[i][j],end=" ")
  print()

