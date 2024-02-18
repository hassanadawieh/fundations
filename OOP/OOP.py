"""
Create an app to create and manage bank accounts
and transfers

#Account number / Balance
"""
### Procedural programming


def create_bank_account(account_number , balance = 0):
    return {'account_number' : account_number , 'balance' : balance}

def deposit(account , amount):
    account['balance'] += amount

def withdraw(account , amount):
     if account['balance'] < amount:
       raise ValueError("Insufficient funds to withdraw")
     account['balance'] -= amount

def transfer_money(sender , recipient , amount):
    if sender['balance'] < amount:
        #Exceptions
        raise ValueError('Insufficient funds')
    sender['balance'] -=amount
    recipient['balance'] +=amount
    return [sender , recipient]



### Solution version 2 : OOP

class BankAccount:  # Real world object representation
    # Abstraction

    # Constructor
    def __init__(self , owner_name , account_number , balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance  #properties  | attributes

    def get_account_data(self):
        print(self.owner_name , self.account_number , self.balance)

    def withdraw(self ,  amount):
        if self.balance < amount:
            raise ValueError("insufficient balance to withdraw")
        self.balance -= amount

    def deposit(self , amount):
        self.balance += amount

    def transfer(self , recipient , amount):
        if self.balance < amount:
            raise ValueError("insufficient balance to transfer")
        self.withdraw(amount)
        recipient.deposit(amount)



account1 = BankAccount("hassan" , "hs43" , 1000)
account2 = BankAccount("ismail" , "hs76" , 2000)

account1.get_account_data() 
account2.get_account_data()

print("////////////////////////////////////////////////////////////////")

account1.withdraw(200)
account1.deposit(100)
account1.transfer(account2 , 200)

print(account1.balance , account2.balance)




    