import datetime
class bank:
    bank_name="federal"
    def __init__(self,accno,cust_name,phno,balance):
        self.accno=accno
        self.cust_name=cust_name
        self.phno=phno
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("your",bank.bank_name,"with account_number",+self.accno,"is credited with ",amount,"on",datetime.datetime.now(),"and your available balance is",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("your transaction failed")
        else:
            self.balance-=amount
            print("your",bank.bank_name,"with account_number",self.accno,"is debited with",amount,"on",datetime.datetime.now(),"and your available balance is",self.balance)
    def balance_enquiry(self):
        print("your available balance is",self.balance)

obj=bank(1000,"merlin",123456789,10000)
obj.deposit(2000)
obj.withdraw(5000)
