


def pair_sum(myList, sum):
    res=[]
    comp={}
    
    for i in range(len(myList)):
        compliment=sum - myList[i]
        if compliment in comp:
             resStr=f"{comp[compliment]}+{myList[i]}"
             res.append(resStr)
             
        comp[myList[i]]=myList[i]
    return res


print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))