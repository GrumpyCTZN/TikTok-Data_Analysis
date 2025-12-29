import loadJsonFile as ld
import directory as dir
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

jsonData=ld.loadFromFile()
watchData=dir.getDeepValue(jsonData,('Your Activity','Watch History','VideoList'))

dateList=[]

for video in watchData:
    dateList.append(video['Date'][:10])
dateList.sort()
npArray=np.array(dateList)

dateArray=np.unique(npArray)
fig,ax=plt.subplots(figsize=(15,7))

ax.hist(npArray,bins=len(dateArray),color='lightgreen',edgecolor='green',label='Hello')
ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=7))

plt.xlabel('Dates')
plt.ylabel('Frequency')
plt.title('TitTok Watch Frequency')
plt.savefig('Tiktok_Watch_History_Histogram.png', dpi=300, bbox_inches='tight')
plt.show()


