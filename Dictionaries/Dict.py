
myDict=dict()

myDictFull=dict(name="dera",address="churchgate")
print("mydict",myDict)
print("mydictfull",myDictFull)

def traverseDict(dict):
    for i in dict:
        print(i,dict[i])
    
traverseDict(myDictFull)

#delete
removedElem=myDictFull.pop("name")
removedElemWithPopItem=myDictFull.popitem()

print("removedValue",removedElem)