import loadJsonFile as ld
import directory as dir

jsonData=ld.loadFromFile()

deepData=dir.getDeepValue(jsonData,('Comment','Comments','CommentsList'))
deepData.reverse()
with open('commentData.txt','w',encoding='utf-8') as file:
    file.write(f"Comments list\n\n")
    for comment in deepData:
        file.write(f"{comment['date'][:10]}\t{comment['comment']}\n")