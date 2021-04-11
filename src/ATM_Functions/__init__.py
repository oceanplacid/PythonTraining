
import datetime
import random
#from django.template.defaultfilters import last

curdate = datetime.datetime.now()
currentBalance = 0
print (curdate.strftime("%Y-%b-%d %H:%M\n"))

accDB = {"HDadzie": ["Hanif", "Dadzie","PassHanif", "somemail@gmaii.com", 3546758868934]}

welcome_count = 0


def login():
    login_counter = 0
    userID = str(input("UserID: "))
    password = str(input("Password: "))
    
    while (userID not in accDB and login_counter < 2):
        login_counter += 1
        print ("Incorrect Username or Password")
        userID = str(input("UserID: "))        
        password = str(input("Password: "))
    
    if (userID in accDB and password == accDB[userID][2]):
        transaction()
    
    
    
def transaction():
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

    
    
def register():
    
    first_name = str(input("First Name: "))
    last_name = str(input("Last Name: "))
    email = str(input("Email Address: "))
    new_pass = str(input("Password: "))
    
    accNum = random.randrange(1111111111111, 9999999999999)
    
    accDB[first_name[0]+last_name] = [first_name, last_name, new_pass, email, accNum]
    
    print ("Registration Successful \nPlease Login")
    print ("")
    
    print ("Please find details below")
    print ("Account Number: ", accNum)
    print ("UserID: ", first_name[0]+last_name)
    
    login()
    


print ("1 - Log In")
print ("2 - Create New Account")
    
    
opt = int(input("Selection An Option: \n"))
while ((welcome_count <2) & (opt > 2)):
    opt =int(input("Enter A Valid Number: "))
    welcome_count +=1
    
   
    
if (opt == 1):
    login()
elif (opt == 2): 
    register()
else:
    pass
    
    
