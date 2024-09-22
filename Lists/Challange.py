myList=list()
print('Type "done" to proceed')
while (True):
    inp=input("Enter a number: ")
    if inp=="done":break
    value=float(inp)
    myList.append(value)

total=sum(myList)

print("Average is :",total/len(myList))