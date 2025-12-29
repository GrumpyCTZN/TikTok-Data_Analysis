import directory as dir
import loadJsonFile as ld
from pathlib import Path
import algorithms as alg

jsonData=ld.loadFromFile()
dateData=alg.pinpointDate(jsonData)
username=dir.getDeepValue(jsonData,("Profile","Profile Info", "ProfileMap","userName"))



for item in dateData:
    for unit in dateData[item]:
        folder=Path(f'{username}_Videos')
        file_path=folder / f"videoDataWith_{unit}.txt"

        folder.mkdir(parents=True,exist_ok=True)
        with file_path.open('a',encoding='utf-8') as file:
            if dateData[item][unit]: file.write(f"{item}\n")
            for small in dateData[item][unit]:
                if "https://www.tiktokv.com/share/video" in small["Content"]:
                    file.write(f"{small["From"]}: {small["Content"]}\n")
            if dateData[item][unit]: file.write(f"\n")
   
