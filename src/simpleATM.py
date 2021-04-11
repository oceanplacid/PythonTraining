
import datetime


curdate = datetime.datetime.now()
currentBalance = 0
validPIN = 1234


PIN = int(input("Please enter your PIN\n:"))
if PIN == validPIN:
    print ("WELCOME!")
    
    print (curdate.strftime("%Y-%b-%d %H:%M\n"))

    print ("Please Select An Option")

    print ("1 - Withdrawal")
    print ("2 - Deposit")
    print ("3 - Complaint")

    option = int(input(": "))


    if option == 1:
        int(input("How much would you like to withdraw\n:"))
        print ("Take your cash")
    elif option == 2:
        deposit = int(input ("How much would you like to deposit?\n: "))
        currentBalance = currentBalance + deposit
        print ("Current Balance: ", currentBalance)
    elif option == 3:
        complaint = int(input("What issue will you like to report?\n: "))
        print ("Thank you for contacting us")
    else:
        print ("Invalid Selection")
        print ("Please Try Again")
else:
    print ("Invalid PIN")
    print ("Please Try Again")
    

