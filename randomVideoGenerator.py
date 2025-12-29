import loadJsonFile as ld
import directory as dir
from numpy import random as rnd

jsonData=ld.loadFromFile()
watchData=dir.getDeepValue(jsonData,('Your Activity','Watch History','VideoList'))
rndNum=rnd.randint(len(watchData))
rndmVdo=watchData[len(watchData)-1]
print(rndNum)
print(rndmVdo['Link'])