#Data viz with Seaborn

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

num_points=100
gradient=0.5
x = np.array(range(num_points))
y = np.random.randn(num_points)*10+x*gradient
data = pd.DataFrame({'dummy x':x,'dummy y':y})
sns.lmplot('dummy x','dummy y',data,height=4,aspect=2,
           scatter_kws={"color":"slategray"},
           line_kws={"linewidth":2,"linestyle":'--',"color":"seagreen"},
           markers='D', #D=diamonds
           ci=68) #confidence interval=68%
plt.tight_layout()
plt.show()
