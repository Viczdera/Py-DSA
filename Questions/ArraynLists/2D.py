# Given 2D list calculate the sum of diagonal elements.

# Example

# myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
# diagonal_sum(myList2D) # 15

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
def diagonal_sum(matrix):
    # TODO
    length=len(matrix)
    sumItems=0
    for i in range(length):
        sumItems+=matrix[i][i]
    
    return sumItems

print("2d",diagonal_sum(myList2D))