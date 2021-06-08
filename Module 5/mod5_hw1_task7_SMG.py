#####
# banking
#
# Sean Gregor
#
# desc: an app for banking
#####
import math

def banking():
    print("PYTHON BANK\n")
    availableBalance = eval(input("What is your available balance? $"))
    withdrawAmount = eval(input("Amount Required: $"))
    balanceCheck = availableBalance - withdrawAmount
    if  balanceCheck ==  abs(balanceCheck):#absolute value to check if positive
        print("Transaction sucessful.")
        runReceipt = input("Do you need the receipt? (Y/N)  :  ")
        if runReceipt == 'y' or 'Y': #'or' avoids "incorect input" bug if the user would forget to capitalize
           print("======================================")
           print("             PYTHON BANK             ")
           print("======================================\n")
           print("Welcome to PYTHON BANK!\n")
           print("Available Balance = $ "+ "{:1,.2f}".format(availableBalance))#by using {:1,.2f} it adds ".00" to the end of it and a coma every three charaters
           print(("{0:>22}{1:1,.2f}".format("Withdrawn = $ ", withdrawAmount)))
           print("{0:>22}{1:1,.2f}".format("Current Balance = $ ", balanceCheck))
           print("\n======================================")
           print("  THANK YOU FOR USING PYTHON BANKING")
           print("======================================")
        elif runReceipt == 'n' or 'N':
            print("Balance updated. Thank You!")
        else:
           print("Incorect input! Asuming No to a reciept.\nBalance has been Updated. Thank You!")
    else:
        print("Transaction Failed.")
        print("The amount required exceeded the availabe balance.")

if __name__ == "__main__":
    banking()