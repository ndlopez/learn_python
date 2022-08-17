#python::pandas...
import pandas as pd
df2 = pd.DataFrame({'name':['zoe','aliyah','bibi','melissa','brianna','lena'],'score':[4,3,2,5,4,6]})
df2.sort_values(['name','score'],ascending=[1,0])
'''
[out]
      name  score
1   aliyah      3
2     bibi      2
4  brianna      4
5     lena      6
3  melissa      5
0      zoe      4
'''
