######
# String counter
#
# Sean Gregor
#
#desc: count the number of occurances in a string of characters for a specific character
######

def stringCounter():
    userString = input("Please enter a string: ")
    searchChar = input('Enter a charater of this string to know its position: ')
    charCount = userString.count(searchChar) #counts the number of occurances
    charPos = userString.find(searchChar) #finds the first position of character
    print('Number of',"'",searchChar,"'",'in the string',"'",userString,"'",':',charCount)
    print('It first occurs at position',charPos+1)
if __name__=="__main__":
    stringCounter()