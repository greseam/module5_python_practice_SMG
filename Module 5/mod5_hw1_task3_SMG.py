######
# Wow, thats your month?
#
# Sean Gregor
#
#desc: print the alphabetic representation month of an entered number between 0-11
######
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def monthByNum():
    userNumMon = eval(input("Enter your month of birth (in number): "))
    print("Wow!! You're the Ruler of",months[userNumMon-1],"!")#the -1 is because user will most likely not enter 0
if __name__ == "__main__":
    monthByNum()