#####
# Formated Data Table 
#
#Sean Gregor
#
#desc: program that uploads data from the provided datatable.csv
#  and prints it out with column headers with it being in proper
#  right justifed
######
#added a space in the datatable file after "Price"
def dataTableP():
    dataTable = open("datatable.csv",'r')
    print("~<>~-----------------±%(SMG)%±-----------------~<>~",end=" ")
    print()
    for line in dataTable:
        for i in range(0,1): #second for loop is for the iterable to make the line below work nicer
            #     Line   +   (" Space " * 9 - length of(word[i]) )+ "||" + (another space) Etc...                        Line2                                                                                      Line3                 
            print(" • " + line.split(",")[i] + (" " * (9-len(line.split(",")[i])) + " >< ") +(  line.split(",")[i+1] + ((" " * (20-len(line.split(",")[i+1]))) + " >< "  )  )  + (" " * (10-len(line.split(",")[i+2])) )+( line.split(",")[i+2]),end=" ")
            #big line of code I know, I wanted it to print out the list as the lines came in from the first for loop. But I needed spaceing imbetween so i made spacing based on len of the words
            print("   ~~--------<>----------------------<>-------~~")   
    print("~<>~----------------+%(ʕ •ᴥ•ʔ)%+---------------~<>~")
if __name__ == "__main__":
    dataTableP() 