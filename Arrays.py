import array

my_array=array.array('i',[1,2,3,4,5,6,8])
my_array.insert(100,7)

my_array.remove(8)

def traverseArr(arr):
    for i in arr:
        print(i)

def accessElement(i,arr):
    if i<0 or i>= len(arr):
        print("No element in this index")
        return
    print("accessed element",arr[i]) # 0(1)

def linearSearch(target,arr): #0(n)
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
traverseArr(my_array)
accessElement(-100,my_array)
print("find 3 index",linearSearch(3,my_array))








#using numpy..more feature rich,with wide range of numerical operations and functions

import numpy as np
np_array0=np.array([],dtype=int) # 0(1)
np_array=np.array([1,2,3,4]) # 0(n)
print(np_array)