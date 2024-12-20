# implement inheritance and polymorphism cncepts by extending the bank account system . create differenr types of acount (saving,checking)that inherit from a base bankaccount class . implement polymorphic methods and demonstarate their usage.

class bank_account:
        def __init__(self,account_number,account_holder,balance):
            self.account_number=account_number
            self.account_holder=account_holder
            self.balance=balance
            

        def deposit(self,amount):
            if amount>=0:
                self.balance += amount

            else:
                print("invalid amount")
        
        def withdraw(self,amount):
            if amount>self.balance:
                return"insuficiant balance"
            elif amount<=0:
                return"invalid amount"
            else:
                self.balance-=amount
                return f"Rs.{amount} debited from your account"

        def checkbalance(self):
            print (f'''Total balance:{self.balance}''')
        
        def getaccinfo(self):
            print (f'''account_number:{self.account_number}''')

        def account_info(self,account_number,balance,name):
            self.account_number=account_number
            self.balance=balance
            self.name=name

            #main code
# if __name__=='__main__':
#     name=input("enter the name")
#     account_number=10023456789526
#     ac = bank_account(account_number,name,balance=1000)
#     while True:
#         print('''menu
              
# 1.Deposit
# 2. Withdraw
# 3.Check balance
# 4.account info
# 5. Exit
#               ''')
#         choice =int(input('enter the choice 1/2/3/4/5'))
#         if choice ==5:
#             break
#         elif choice==4:
#             print(ac.getaccinfo())
#         elif choice==3:
#             print(ac.checkbalance())
#         elif choice==2:
#             amt =int(input("Enter amount: "))
#             print(ac.withdraw(amt))
#         elif choice==1:
#             amt =int(input("Enter amount: "))
#             print(ac.deposit(amt))

class savingsaccount(bank_account):
        def __init__ (self,account_number,account_holder,balance=0, interest_rate=0.02):
            super().__init__(account_number , account_holder,balance)
            self.interest_rate = interest_rate

        def add_interest(self):
            interest  = self.balance*self.interest_rate
            self.balance += interest
            print(f"interest added:{interest}, New balance:{self.balance}")

class checkingaccount(bank_account):
        def __init__(self,account_number,account_holder,balance=0,overdraft_limit=100):
            super().__init__(account_number,account_holder,balance)
            self.overdraft_limit=overdraft_limit
        def withdraw(self, amount):
            if amount<=(self.balance+self.overdraft_limit):
                self.balance-=amount
                print(f"withdraw {amount} ,new balance{self.balance}")
            else:
                print("insufficient funds! overdraft limit reached")

if __name__=='__main__':
    saving_account=savingsaccount(account_number=123,account_holder='ravi',balance=1000)
    checking_account=checkingaccount(account_number=456,account_holder='kisan',balance=500,overdraft_limit=200)

    # depsit ans display balance for both account
    saving_account.deposit(200) 
    saving_account.checkbalance()


    checking_account.deposit(100)
    checking_account.checkbalance()

    # withdraw and dispaly balance fro both account

    saving_account.withdraw(50)
    saving_account.checkbalance()

    checking_account.withdraw(300)
    checking_account.checkbalance()

    # add interest to the saving acccount
    saving_account.add_interest()
    saving_account.checkbalance()




    
