import json 

def toString(obj):
    jsonString = json.dumps(obj.__dict__)
    return jsonString

def getList(fileName):
    fileData = open(fileName, "r",encoding="utf-8")
    dataList = json.loads(fileData.read())
    return dataList

    #with(fileNam) as f:
    #  data = json.loads(f.read())

def saveList(dataList,fileName):
    outFile = open(fileName, "w",encoding="utf-8")
    json.dump(dataList, outFile,indent=4)
    outFile.close()
 
def addPerson(string,fileName): 
    personList = getList(fileName)
    personList.append(string)
    return personList
