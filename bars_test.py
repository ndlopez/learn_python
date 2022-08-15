# bar plots
import numpy as np
import matplotlib.pyplot as plt

labels = ["Physics","Mathematics","Literature","Economics"]
foo_data = [3,6,10,4]
bar_data = [8,6,3,2]
'''
bar_width = 0.5
xloc = np.array(range(len(foo_data))) + bar_width
plt.bar(xloc,foo_data, width=bar_width)
plt.yticks(range(0,12))
plt.xticks(xloc+bar_width/2,labels)
plt.xlim(0,xloc[-1]+bar_width*2)
plt.title("Prizes?")
plt.gca().get_xaxis().tick_bottom()
plt.gca().get_yaxis().tick_left()
plt.gcf().set_size_inches((8,4))
plt.savefig('bars_custom.svg')
'''
#2 sets of data plotted in vertical bars
fig,ax = plt.subplots(figsize=(8,4))
bar_width = 0.4
xlocs = np.arange(len(bar_data)) #=ylocs
'''
ax.bar(xlocs-bar_width,foo_data,bar_width,color='r',label='Men')
ax.bar(xlocs,bar_data,bar_width,color='g',label='Women')
# ticks, labels, grids, and title
ax.set_yticks(range(12))
ax.set_xticks(ticks=range(len(foo_data)))
ax.set_xticklabels(labels)
ax.yaxis.grid(True)
ax.legend(loc='best')
ax.set_ylabel('Number of partners')
fig.suptitle('Partners per subject')
fig.tight_layout(pad=2)
fig.savefig('bartchart.png',dpi=200)
'''
ylocs = xlocs
ax.barh(ylocs-bar_width,foo_data, bar_width,color='b',label='Men')
ax.barh(ylocs,bar_data,bar_width,color='g',label='Women')
ax.set_xticks(range(12))
ax.set_yticks(ticks=range(len(foo_data)))
ax.set_yticklabels(labels)
ax.xaxis.grid(True)
ax.legend(loc='best')
ax.set_xlabel('Number of prizes')
plt.show()
