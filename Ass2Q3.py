""" Write a menu based program to manage BankAccounts using class concept (develop your own logic) with the following features.
a. account number - data(instance)
b. account balance - data(instance)
c. account type -data(instance)
d. number of accounts-data(class)
e. account holder name-data(instance)
f. account holder address-data(instance)
g. methods for deposit,withdraw,setting and getting account & account holder details.
(Note: you may create a dict of bank account instances with 'account no' as key in your program)"""

ac_all={
    "Cust01": {
        "ac_no":"Cust01",
        "ac_name":"Deepak",
        "ac_balance":500.00,
        "ac_address":"Vadodara",
        "ac_type":"saving"
    },
    "Cust02": {
        "ac_no":"Cust02",
        "ac_name":"Deepak",
        "ac_balance":500.00,
        "ac_address":"df",
        "ac_type":"saving"
    }
}

class concept:   
    def __init__(self,acnumber):
        self.acnumber=acnumber

    def view_ac_func(self):
        print("==========================")
        print("Account number:",ac_all[str(self.acnumber)]['ac_no'])
        print("Account Name:",ac_all[str(self.acnumber)]['ac_name'])
        print("Account Balance:",ac_all[str(self.acnumber)]['ac_balance'])
        print("Account Address:",ac_all[str(self.acnumber)]['ac_address'])
        print("Account Type:",ac_all[str(self.acnumber)]['ac_type'])
        print("==========================\n")
    
    def ac_withd(self):
        w1=ac_all[str(self.acnumber)]['ac_balance']
        print("\n==========================")
        print("Account Balance:",w1)
        wm=float(input("Please Enter Withdraw Amount: "))
        print("Withdrawal amount: ")
        w1=w1-wm
        print("After withrawal Balance: ",w1)
        print("==========================\n")
        return w1
    def ac_dep(self):
        d1=ac_all[str(self.acnumber)]['ac_balance']
        print("\n==========================")
        print("Account Balance:",d1)
        dm=float(input("Please Enter Withdraw Amount: "))
        print("Withdrawal amount: ")
        d1=d1+dm
        print("After withrawal Balance: ",d1)
        print("==========================\n")
        return d1
        
        

choice=0
while choice<3:
    print("\n==========================")
    print("1. View Account Detail")
    print("2. Withdrawing Account")
    print("3. Deposit Account")
    print("4. Quit/EXIT")
    print("==========================\n")
    ch=input("Input Choice : ")
    if (ch=="1"):
        get_view=input("Enter Account Number:")
        view_ac=concept(get_view)
        view_ac.view_ac_func()
    elif (ch=="2"):
        get_withdraw=input("Enter Withdraw Account Number: ")
        withdraw=concept(get_withdraw)
        ac_all[get_withdraw]['ac_balance']=withdraw.ac_withd()
    elif (ch=="3"):
        get_dep=input("Enter Withdraw Account Number: ")
        deposit_ac=concept(get_dep)
        ac_all[get_dep]['ac_balance']=deposit_ac.ac_dep()
    elif (ch=="4"):
        print("Quit")
        break
    else:
        choice=0
        print("\nPlease Enter Valid Choice")