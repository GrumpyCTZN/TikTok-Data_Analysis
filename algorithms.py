import directory as dir


def pinpointDate(data):
    deepValue=dir.getDeepValue(data,("Direct Message","Direct Messages","ChatHistory"))
    dateList=[]
    for key in deepValue:
        #key-key and deepValue[key] is the value [list]
        for entry in deepValue[key]:
            dateList.append(entry["Date"][:10])
    clearDateList=list(set(dateList))
    clearDateList.sort()
    ndateDict={}
    for date in clearDateList:
        deepValueList=[]
        deepValueDict={}
        
        for key in deepValue:   
            for entry in deepValue[key]:
                if date in entry["Date"]:
                    deepValueList.append(entry)
            deepValueList.reverse()
            #if deepValueList:
            deepValueDict[key.replace(":","").split()[-1]]=deepValueList
            deepValueList=[]
            
        ndateDict[date]=deepValueDict
        deepValueDict={}
    return ndateDict

'''
To access the new list,
the structure will be as followes
ChatHistory
|_Dates(dict of dates)
|   |_friendsontiktok
|   |   |_[List Items](every single message)
|   |   |   |_Date
|   |   |   |_From
|   |   |   |_Content
'''