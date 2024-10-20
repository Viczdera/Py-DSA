# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]


#list comprhension
def middle(lst):
    return [lst[i] for i in range(len(lst)) if i>0 and i<(len(lst)-1)]

print(middle(myList))

#anther shorter
def middle(lst):
    return lst[1:-1]

print(middle(myList))