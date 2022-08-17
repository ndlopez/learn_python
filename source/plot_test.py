#Visualizing data with Matplotlib
#Matplotlib config
#import matplotlib as mpl
#mpl.rcParams['lines.linewidth'] = 2
#mpl.rcParams['lines.color'] = 'r'
#plt.rcParams['figure.figsize'] = (8,4)
#plt.gcf().set_size_inches(8,4)

#example 1
import numpy as np
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

hoy = date.today()
x = pd.period_range(hoy,periods=200,freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200,3).cumsum(0)

#three plots in one figure
'''
plots = plt.plot(x,y)
plt.legend(plots,('foo','bar','mongo'),loc='best',
           framealpha=0.25,prop={'size':'small','family':'monospace'})
plt.gcf().set_size_inches(8,4)
plt.title('Random Trends')
plt.xlabel('Date')
plt.ylabel('Cummulative sum')
plt.grid(True)
plt.figtext(0.995,0.01,'\u00a9 Acme designs 2020',ha='right',va='bottom')
plt.tight_layout()
plt.savefig('mpl_3lines_custom.svg')
'''
# a plot insert with figure.axes
'''
fig = plt.figure(figsize=(8,4))
#Main axes
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_title('Main axes with insert child axes')
ax.plot(x,y[:,0])#selects the 1st col of numpy rand y-data
ax.set_xlabel('Date')
ax.set_ylabel('Cummulative Sum')
# inserted axes
ax = fig.add_axes([0.15,0.15,0.3,0.3])
ax.plot(x,y[:,1],color='g')
ax.set_xticks([]);#removes the xticks of subplot
plt.savefig('subplots.png')
'''
# another subplot
fig, axes = plt.subplots(nrows=3,ncols=1,sharex=True,sharey=True,figsize=(8,8))
labelled_data = zip(y.transpose(),('foo','bar','mongo'),('b','g','r'))
fig.suptitle('3 random trends',fontsize=16)
for i, ld in enumerate(labelled_data):
    ax = axes[i]
    ax.plot(x, ld[0], label=ld[1], color=ld[2])
    ax.set_ylabel('Cummulative sum')
    ax.legend(loc='upper left',framealpha=0.5,prop={'size':'small'})
    ax.grid(True)

axes[-1].set_xlabel('Date')
fig.text(0.995,0.01,'\u00a9 Acme designs 2020',ha='right',va='bottom')
fig.tight_layout()
print('Today is',hoy)
plt.savefig('3rand_subplots.png')

