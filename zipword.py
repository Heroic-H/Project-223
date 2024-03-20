import zipfile
import time
folderPath=input("path to file: ")
zipf=zipfile.ZipFile(folderPath)
global result
result=0
global tried
tried=0
c=0
if not zipf:
    print("the zipped file/folder has no password so you can open it")
else:
    startTime=time.time()
    wordListFile=open("wordList.txt","r",errors="ignore")
    body=wordListFile.read().lower()
    words=body.split("\n")
    for i in range(len(words)):
        word=words[i]
        password=word.encode("utf8").strip()
        c=c+1
        #print(f"trying to decode password by {word}")
        try:
            with zipfile.ZipFile(folderPath,"r")as zf:
                zf.extractall(pwd=password)
                print(f"success: the password is {word}")
                result=1
                endTime=time.time()
                print(f"time taken: {startTime-endTime}")
            break
        except:
            pass