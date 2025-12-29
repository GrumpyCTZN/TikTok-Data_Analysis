import loadJsonFile as ld
import directory as dir
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


jsonData=ld.loadFromFile()
chatData=dir.getDeepValue(jsonData,('Direct Message','Direct Messages','ChatHistory'))

for people in chatData:
    name=people.replace(':','').split()[-1]
    frequencyList=[]
    for message in chatData[people]:
        frequencyList.append(message['Date'][:10])
    frequencyList.sort()
    npFrequencyList=np.array(frequencyList)
    
    uniqueFreqList,count=np.unique(npFrequencyList,return_counts=True)
    #print(f"For {name} \nMax: {uniqueFreqList[count.argmax()]}\t{count.max()}\nMinimum: {uniqueFreqList[count.argmin()]}\t{count.min()}\n\n")
    fig,ax=plt.subplots(figsize=(15,7))

    ax.hist(npFrequencyList,bins=len(uniqueFreqList),color='red',edgecolor='black')
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=9 if len(uniqueFreqList)>9 else len(uniqueFreqList)))
    
    plt.xlabel('Dates')
    plt.ylabel('Frequency')
    plt.title(f'Chat Frequency with {name}')
    plt.savefig(f'HistogramIndividualChat/{name}_Histogram.png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    npFrequencyList=None
    uniqueFreqList=None

    
    
    