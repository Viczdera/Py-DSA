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