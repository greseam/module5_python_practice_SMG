######
#every third word begin
#
# Sean Gregor
#
#desc: takes a string and only prints every thrid word
######

def SpaceBegone():
    userString = input("Enter in a sentence at least 3 words long: ").split(" ")
    userEndString = len(userString)
    for i in range (2, userEndString, 3):#the range is set to grab the third word starting at position 2 in the list and then every three words
        decode = userString[i]
        print(decode, end=" ")

if __name__ == "__main__":
    SpaceBegone()