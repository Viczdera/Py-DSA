myLists=[1,2,3,4,5,6,7]
def linearSearch(listItems,target): #O(n)
    for i,value in enumerate(listItems): #O(n)
        if value==target: #O(1)
            return i
    return -1

target=4
print("index is",linearSearch(myLists,target))

#concatenating lists
a=[1,4]
a=a*4 # multiplies items in list
print(a)

#max
print(max(a))

#min
print(min(a))
#sum
print(sum(a))

#number
print(len(a))

#average
print("average number",sum(a)/len(a))

#split
mystr="a boy is coming"
myStrList=mystr.split(" ")
print(myStrList)

a=[1,2,3,4,5]
print(a[3:0:-1])

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ")

#quiz
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)

#quiz
a=[1,2,3,4,5,6,7,8,9]
print(a[::2])
#quiz
arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())


#quiz...points doesnt copy,hence answer is 22
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)