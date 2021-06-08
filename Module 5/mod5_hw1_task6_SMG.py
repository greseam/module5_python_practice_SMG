#####
# encoder
#
# Sean Gregor
#
# desc: using graphics a program that encrypts a typed in message using a digit from the value of pi multiplied by the ord val
#####
from graphics import*
import math
center = Point(250,250)#easy edit
userStringBox = Entry(center, 30)
Pi = [3,1,4,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4] #first 23 digits of Pi
def SpaceBegone(userString): #ord doesnt like spaces
    try: 
        userString = userStringBox.getText().split(' ')
        userEndString = ""
        for i in userString:
            userEndString += i.title() 
        return userEndString
    except:
        return userString
def encoder():
    win = GraphWin('Encode me',1000,400)
    win.setCoords(0,0,500,500)#makes the center value actualy centered
    win.setBackground('pink')
    descriptionText = Text(Point(250,200),"Enter a String to encode \n\nThen click anywhere")
    descriptionText.draw(win)
    userStringBox.draw(win)
    win.getMouse()
    ranVal = "• "
    string2List = str(SpaceBegone(userStringBox.getText()))
    for i in range(1,len(string2List)+1):
        userNumVal = ord(string2List[i-1:i])
        encodedString = userNumVal * Pi[i-1]
        ranVal = ranVal + str(encodedString) +" • "
    descriptionText.undraw()
    userStringBox.undraw()
    encodedMessage = Text(Point(250,215),"~---Here is your encoded message---~\n\n" + ranVal + "\n\n~--Click anywhere to Exit--~")
    encodedMessage.draw(win)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    encoder()   