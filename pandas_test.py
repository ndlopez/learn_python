# series into dataframes
import pandas as pd
import numpy as np
s = pd.Series(np.arange(4))
print(s)
s= pd.Series([1.0,2.0,3.0],index=['x','y','z'])
print(s)
s= pd.Series({'a':1,'b':2,'c':3,'d':4})
print(s)

s=pd.Series([1,2,3,4],['t','x','y','z'])
print(np.sqrt(s))
#concat 2 series
names=pd.Series(['Einstein','Marie Curie'],name='name')
categ=pd.Series(['Physics','Chemistry'],name='category')
df = pd.concat([names,categ],axis=1)
print(df.head())

#creating a panel of dataframes
df1= pd.DataFrame({'foo':[1,2,3],'bar':['x','y','z']})
df2= pd.DataFrame({'dat':[7,9,8,2],'shi':['i','j','k','l']})
#pn = pd.Panel({'item1':df1, 'item2':df2})
#print(pn)
''' The following error outputs:
pandas_test.py:22: FutureWarning: The Panel class is removed from pandas.
Accessing it from the top-level namespace will also be removed in the next
version.
  pn = pd.Panel({'item1':df1, 'item2':df2})
Traceback (most recent call last):
  File "pandas_test.py", line 22, in <module>
    pn = pd.Panel({'item1':df1, 'item2':df2})
TypeError: Panel() takes no arguments
'''
