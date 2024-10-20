#missing number
list=[1,2,3,4,5,6,7,9,10]
n=10

#first sol
def missingNumber(list,n):
    for i in range(n):
        if i+1 != list[i]:return i+1

print ("missing number",missingNumber(list,n))

#second sol
def missingNumber2(list,n):
    #using sum of n natural numbers equation n *n=1/2
    sumToN= n * (n+1)/2
    sumInArray=sum(list)

    return sumToN-sumInArray
print("missing2",missingNumber2(list,n))
    