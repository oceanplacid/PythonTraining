class Budget():
    def __init__(self, cat_list = {"food":0, "clothing":0, "entertainment":0}):
        
        self.cat_list = cat_list
             
        
    def deposit(self, dep_amount, category):
        self.dep_amount = dep_amount
        self.category = category
                
        self.cat_list[category] = self.cat_list[category] + dep_amount
        
    
    def withdraw(self, withdraw_amount, withdraw_cat):
        self.withdraw_amount = withdraw_amount
        self.withdraw_cat = withdraw_cat

        self.cat_list[withdraw_cat] = self.cat_list[withdraw_cat] - withdraw_amount
        
        
    def transfer(self, amount, source_funds, destination_funds):
        self.amount = amount
        self.source_funds = source_funds
        self.destination_funds = destination_funds

        self.cat_list[destination_funds] = self.cat_list[destination_funds] + amount
        self.cat_list[source_funds] = self.cat_list[source_funds] - amount


    def budget_balance(self):
        print ("Current Balances")
        for key, value in self.cat_list.items():
            print (f"{key} : {value}")
        
        


print ("Create A Budget for the Below Categories \nFood, Clothing, Entertainment")

first_name = str(input ("First Name: "))
last_name = str(input ("Last Name: "))


username = first_name + "_" + last_name
print ("Enter budget allocations below")
food_budget = float(input ("Food: "))
cloth_budget = float(input ("Clothing: "))
ent_budget = float(input ("Entertainment: "))

username = Budget({"food":food_budget, "clothing":cloth_budget, "entertainment":ent_budget})

print("")
print ("Budget Successfully Created")
print (f"Name: {first_name} {last_name}")

print("")
username.budget_balance()
print("")

print ("Press 1 for more options \nPress 2 to exit\n")
option = int(input(": "))


if (option == 1):
    print ("1 - Deposit\n2 - Withdraw\n3 - Transfer Between Budgets\n4 - Check Balances")
    activity = int(input(": "))
    if (activity == 1):
        deposit_amount = float(input("Amount: "))
        deposit_category = str(input("Category: ")).casefold()
        username.deposit(deposit_amount, deposit_category)
        print (f"${deposit_amount} Successfully Deposited into {deposit_category} Budget")
        print (f"Available Balance for {deposit_category} is: {username.cat_list[deposit_category]}")      
        
    elif (activity == 2):
        withdraw_amount = float(input("Amount: "))
        withdraw_category = str(input("Category: ")).casefold()
        if (withdraw_amount <= username.cat_list[withdraw_category]):
            username.withdraw(withdraw_amount, withdraw_category)
            print (f"${withdraw_amount} Successfully Withdrawn from {withdraw_category} Budget")
            print (f"Available Balance for {withdraw_category} is: {username.cat_list[withdraw_category]}")
        else:
            print ("Insufficient Funds in %s Budget" %withdraw_category)
            exit()
        
    elif (activity == 3):
        transfer_amount = float(input("Amount: "))
        transfer_count = 0
        source_category = str(input("Source Budget: ")).casefold()
        dest_category = str(input("Destination Budget: ")).casefold()
        trans_count = 0
        
        if (transfer_amount <= username.cat_list[source_category]):
        
            username.transfer(transfer_amount, source_category, dest_category)
            print (f"${transfer_amount} Successfully Transferred From {source_category} Budget Into {dest_category} Budget")
            username.budget_balance()
        else:
            print ("Insufficient Funds in Source Budget")
            exit()
        
    elif (activity == 4):
        username.budget_balance()
elif (option == 2):
    exit()
else:
    print ("Invalid Input")
    exit()






