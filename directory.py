#data is the main json Data and path is a list

def getDeepValue(data,path):
    current=data
    for key in path:
        if isinstance(current,dict) and key in current:
            current=current[key]
        else:
            return None
    return current
