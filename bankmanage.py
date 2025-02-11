# ### *5. Banking System*
# *Description*: A console-based banking system to manage accounts and transactions.
#
# #### Features:
# - *Account Management*:
#   - Create, update, and delete accounts.
#   - View account details.
# - *Transactions*:
#   - Deposit and withdraw money.
#   - Transfer funds between accounts.]-
# - *Reports*:
#   - View account statements for a specific period.
#   - Calculate total funds in the bank.
#
# #### Database Tables:
# - accounts: Store account details.
# - transactions: Record deposit, withdrawal, and transfer transactions.
#
# ---
from datetime import datetime
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Bankmanagement']
db2 = client['Transactions']

collection = db['Customer']
collection2 = db2['transaction']

# Insert a document
# document = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
# collection.insert_one(document)

# Find a document
# result = collection.find_one({'name': 'John Doe'})
# print(result)
class Bank:
    def __init__(self,bank_id,bank_name,bank_branch,bank_address,number_of_customer):
        self.__bank_id=bank_id
        self.__bank_name=bank_name
        self.__bank_branch=bank_branch
        self.__bank_address=bank_address
        self.__number_of_customer=number_of_customer
    def __str__(self):
        print(f"bank_id:={self.__bank_id} \tbank_name:={self.__bank_name}\t bank_branch:={self.__bank_branch}\t bank_name:={self.__bank_address}\t number_of_customer:={self.__number_of_customer}")

class Account:
    def __init__(self):
        i=1
        account_no=i
        self.account_no=account_no
        self.account_branch="BOB"
        self.ifsc_code="qwerty"
        self.bank_name="BOB"
        i+=1

    def __str__(self):
        print(f"account_no:={self.account_no}\t account_branch:=BOB\t ifsc_code:={self.ifsc_code}\t bank_name:={self.bank_name}")

class Customer:
    def __init__(self,customer_name,account_no,customer_mode,customer_amount,customer_address,customer_mobileno):
        self.customer_name=customer_name
        self.customer_mode=customer_mode
        self.customer_amount=customer_amount
        self.customer_address=customer_address
        self.customer_mobileno=customer_mobileno
        self.account_no = account_no
        self.account_branch = "BOB"
        self.ifsc_code = "qwerty"
        self.bank_name = "BOB"

        document = {'customer_name':self.customer_name, 'account_no':self.account_no, 'account_branch':self.account_branch,'ifsc_code':self.ifsc_code,'bank_name':'BOB','customer_mode':self.customer_mode,'customer_amount':self.customer_amount,'customer_address':customer_address,'customer_mobileno':customer_mobileno}
        collection.insert_one(document)
    def __str__(self):
        print(f"customer_name:={self.customer_name}\t account_no:={self.account_no}\t account_branch:=BOB\t ifsc_code:={self.ifsc_code}\t bank_name:={self.bank_name}  \tcustomer_mode:={self.customer_mode}\t customer_amount:={self.customer_amount}\t customer_mobileno:={self.customer_mobileno} \t customer_address:={self.customer_address}")

class Transaction:
    def __init__(self,getid,getid2,amount,select):
        self.getid=getid
        self.getid2=getid2
        self.amount=amount
        self.select=select
    def deposite(self):
        document=collection.find_one({'account_no':self.getid})
        balance=document['customer_amount']
        new_balance=balance+self.amount
        collection.update_one({'account_no':self.getid},{'$set': {'customer_amount': new_balance}})
        if self.select!=3:
            transactions={'account_no':self.getid, 'method':'Deposite', 'amount':self.amount, 'Date':datetime.now()}
            collection2.insert_one(transactions)

    def withdrawl(self):
        document=collection.find_one({'account_no':self.getid})
        balance=document['customer_amount']
        if balance>=self.amount:
            new_balance=balance-self.amount
            collection.update_one({'account_no':self.getid},{'$set': {'customer_amount': new_balance}})
            if self.select!=3:
                transactions = {'account_no': self.getid, 'method': 'Withdrawl', 'amount': self.amount,
                                'Date': datetime.now()}
                collection2.insert_one(transactions)
        else :
            print("you dont have enough amount to withdrawl")

    @classmethod
    def transfer(self):
        tran1 = Transaction(getid, 0, amount, select3)
        tran1.withdrawl()
        tran2 = Transaction(getid2, 0, amount, select3)
        tran2.deposite()

        transactions = {'fromaccount_no': getid,'toaccount_no': getid2, 'method': 'Transfer', 'amount': amount,
                        'Date': datetime.now()}
        collection2.insert_one(transactions)

while(True):
    select1=int (input("\n<1> Account Management \n<2> Transactions \n<3> Reports \n<4> Exit"))
    if select1 ==1:
        select2 = int(input("\n<1> Add customer\n<2> Update customer\n<3> Delete customer \n<4> View customer"))
        if select2 ==1:
           create_customer=Customer(input("\nEnter the name of Customer: "),int(input("Enter the account_no: ")),input("Enter the customer_mode: "), int(input("Enter the customer_amount: ")),input("Enter the address: "),int(input("Enter the customer mobileno: ")))
           create_customer.__str__()
        if select2==2:
            documents = collection.find()
            print()
            for doc in documents:
                print(doc['customer_name'])
            update_customer=input("Select the customer name in which you want to update: ")
            customer_name=update_customer
            toupdate1= collection.find_one({'customer_name':update_customer})
            print(toupdate1)
            update_customer_field=input("Select the customer filed in which you want to update: ")
            update_customer_value=input("Select the customer filed value you want to update: ")
            argu1=toupdate1[update_customer_field]
            update_data = {"$set": {update_customer_field:update_customer_value}}
            toupdate2=collection.update_one({update_customer_field:argu1},update_data)
        if select2==3:
            documents = collection.find()
            print()
            for doc in documents:
                print(doc['customer_name'])
            update_customer = input("Select the customer name you want to delete: ")
            customer_name = update_customer
            toupdate1 = collection.find_one({'customer_name': update_customer})
            collection.delete_one(toupdate1)
        if select2==4:
            documents = collection.find()
            print()
            for doc in documents:
                print(doc)


    elif select1==2:
        select3=int(input("\n<1> Deposit money \n<2> Withdraw money \n<3> Transfer funds between accounts"))

        if select3==1:
            getid = int(input("Enter the account_no in which you want to deposite"))
            amount=int(input("Enter the amount you want to Deposite"))
            tran=Transaction(getid,0,amount,select3)
            tran.deposite()
        if select3==2:
            getid = int(input("Enter the account_no in which you want to deposite"))
            amount = int(input("Enter the amount you want to Deposite"))
            tran = Transaction(getid,0,amount,select3)
            tran.withdrawl()
        if select3==3:
            getid=int(input("Enter the account_no from which you want to transer money"))
            getid2=int(input("Enter the account_no in which you want to transer money"))
            amount=int(input("Enter the amount you want to transer"))
            tran = Transaction(getid,getid2, amount, select3)
            tran.transfer()
    elif select1==3 :
        select4=int(input("<1> Calculate total funds in the bank \n<2> View account statements for a specific period"))
        if select4==1:
            doc=collection.find()
            totalbalnce=0
            for x in doc:
                totalbalnce+=x['customer_amount']
            print("Total funds in the bank is ",totalbalnce)
        elif select4==2:
            startdatestr=input("Enter the startdate in the format yyyy-mm-dd:")
            startdate = datetime.strptime(startdatestr, "%Y-%m-%d")
            enddatestr=input("Enter the enddate in the  format yyyy-mm-dd :")
            enddate = datetime.strptime(enddatestr, "%Y-%m-%d")

            print(enddate,startdate)
            transactions = collection2.find({
                'Date': {
                    '$gte': startdate,
                    '$lt': enddate
                }
            })
            for x in transactions:
                print(transactions)

    if select1==4:
        break






