######
#space begone
#
# Sean Gregor
#
#desc: takes a string and removes the space
######

def SpaceBegone():
    userString = input("Please enter a string with a space: ").split(" ")
    userEndString = ""
    for i in userString:
        userEndString += i.title() #adds the strings from the split input together for each "string" in the "string list"
    
    print("Your string without space: ",userEndString)
    
if __name__ == "__main__":
    SpaceBegone()