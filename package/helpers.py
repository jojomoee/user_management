import json 

def toString(obj):
    jsonString = json.dumps(obj.__dict__)
    return jsonString
    
    # dumps to return a String dump to return normal.

def getList(jsonFile):
    fileData = open(jsonFile, "r",encoding="utf-8")
    dataList = json.loads(fileData.read())
    return dataList
    
    # "r" means read, encoding ensures also non ascii characters.
    # Loads not load because i want to load a String.

    # File open alternative:
    #
    # with(fileNam) as f:
    #  data = json.loads(f.read())

def saveList(dataList,jsonFile):
    outFile = open(jsonFile, "w",encoding="utf-8")
    json.dump(dataList, outFile,indent=4)
    outFile.close()

    # "w" means open the file to write
    # Uses dump  without s because i want to save a json Obj, setting indent to have a typically structured json
 
def addPerson(string,jsonFile): 
    personList = getList(jsonFile)
    personList.append(string)
    return personList
    
    #append String to personList (str) uses getList()

