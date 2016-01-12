account_balance = 1000
 
withdrawal = 50

new_balance = account_balance - withdrawal

while new_balance >= 0:
        print("Ok, your withdrawal has been made.")
        print("Your balance is now $" + str(new_balance) + ".")
        new_balance = new_balance - withdrawal

