#two sum walktrhough questions: are the pairs distinct(2,2) valid?, negative integers?, 

list=[2,7,11,15]
target=9


#best with dictionaries AKA hashmap 
#complexity = O(n)
def twoSumBest(list,target):
   dict={}
   for i in range(len(list)):
       compliment=target - list[i]
       if compliment in dict:
           return [dict[compliment],i]
       
       dict[list[i]]=i

print("twosum2",twoSumBest(list,target))

print("twosumBest2",twoSumBest([3,2,4],6))

print("twosumBest2",twoSumBest([3,2,4,6],8))


#can use sliding window

def twoSum(list,target):
    start=0

    while start < len(list)-1:
        end=start+1
        
        while end<len(list):
            if list[start]+list[end]==target:
                return [start,end]
    
            end+=1

        start+=1

print("twosum",twoSum(list,target))

print("twosum",twoSum([3,2,4],6))

print("twosum",twoSum([3,2,4,6],8))


#second sol
def twoSum2(list,target):
   for i in range(len(list)):
       for j in range(i+1, len(list)):
           if list[i]+list[j]==target:
               return [i,j]

print("twosum2",twoSum(list,target))

print("twosum2",twoSum([3,2,4],6))

print("twosum2",twoSum([3,2,4,6],8))

