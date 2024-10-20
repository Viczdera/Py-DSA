


list=[3,2,4,5,6,7,7,3,5,3,8,9,6,7,5,4,32,5]


# product of two max numbers is max product

def maxProduct(arr):
    max1,max2=0,0
    for num in arr:
        if num>max1 :
            max2=max1
            max1=num
        elif num>max2:max2=num
    return max1*max2

print("maxprod",maxProduct(list))

def maxProductBrute(arr):
    max=0
    
    for i in range(len(arr)):
        for j in range (i+1,len(arr)):
            product=arr[i]*arr[j]
            if product>max: max=product
    
    return max

print("maxprodbrute",maxProductBrute(list))