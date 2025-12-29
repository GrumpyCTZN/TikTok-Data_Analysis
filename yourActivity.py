import directory as dir

def shareHistoryOutput(data):
    shareData=dir.getDeepValue(data,('Your Activity','Share History','ShareHistoryList'))
    with open('shareHistory.txt','w',encoding='utf-8') as file:
        file.write(f"Share History\n\n")
        for shares in shareData:
            file.write(f"{shares['Date'][:10]}\t{shares['Link']}\n")
            
def searchHistroyOutput(data):
    searchData=dir.getDeepValue(data,('Your Activity','Searches','SearchList'))
    print(searchData[-1])
    with open('searchHistory.txt','w',encoding='utf-8') as file:
        file.write(f"Search History\n\n")
        for search in searchData:
            file.write(f"{search['Date'][:10]}\t{search['SearchTerm']}\n")  
            
def watchHistoryOutput(data):
    watchData=dir.getDeepValue(data,('Your Activity','Watch History','VideoList'))
    print(watchData[-1])
    with open('watchHistory.txt','w',encoding='utf-8') as file:
        file.write(f"Watch History\n\n")
        for watch in watchData:
            file.write(f"{watch['Date'][:10]}\t{watch['Link']}\n")  