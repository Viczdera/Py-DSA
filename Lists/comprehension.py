#offers shorter syntax for creatin a new list 
myStr="Algorithm"
myStrList=[i for i in myStr ]

print(myStrList)

sentence="My name is dera"

def isConsonant(letter):
    vowels="aeiou"
    return letter.isalpha() and letter.lower() not in vowels

myNameConsonants=[i for i in sentence if isConsonant(i)]
print("My name consonants: ",myNameConsonants)

#//
prevList=[1,-1,3,-4,5,2,-424,0,4]
newList=[number for number in prevList if number>0]
newListNegative=[number*number for number in prevList if number<0]
print("Positive nums",newList)
print ("negative square",newListNegative)


