import json
import loadJsonFile as ld
import algorithms as alg

jsonData=ld.loadFromFile()
dateData=alg.pinpointDate(jsonData)


specificDate=input("Date: ")
if f"{specificDate}" in dateData:
    chatter=input("Username? ")
    if f"{chatter}" in dateData[f"{specificDate}"]:
        print(f"\n\nChat with {chatter} on {specificDate}: \n")
        for i in dateData[f"{specificDate}"][f"{chatter}"]:
            print(f"{i["From"]}: {i["Content"]}\n\t\t\t\t\t\t\t\t\t\t\t{i["Date"][11:]}")
    else: print("Invalid Username")
else: print("Invalid Date")