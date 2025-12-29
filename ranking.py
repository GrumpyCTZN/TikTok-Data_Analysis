import loadJsonFile as ld
import directory as dir
import matplotlib.pyplot as plt

def giveTotalChat(data):
    deepVal=dir.getDeepValue(data,('Direct Message','Direct Messages','ChatHistory'))
    countDict={}
    for people in deepVal:
        chatCount=0
        for message in deepVal[people]:
            chatCount+=1
        countDict[people.replace(":","").split()[-1]]=chatCount
    return countDict

jsonData=ld.loadFromFile()
chatDict=giveTotalChat(jsonData)

temp=sorted(chatDict.items(),key=lambda item: item[1],reverse=True)
sortedChatDict=dict(temp)
total=0
newDict={}
newtotal=0
for count,i in enumerate(sortedChatDict):
    print(f"{count+1}.\t{i}: \t{sortedChatDict[i]}")
    total+=sortedChatDict[i]
    if sortedChatDict[i]>=400:
        newDict[i]=sortedChatDict[i]
    else:
        newtotal+=sortedChatDict[i]
    

newDict['Others']=newtotal        
print(f"\nTotal:\t\t\t{total}")




labels=list(newDict.keys())
sizes=list(newDict.values())

plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('TikTok Chat Distribution')
#plt.savefig('TikTokChatPieChart_beastmaster6420.png', dpi=300, bbox_inches='tight')

plt.show()


