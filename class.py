class Student:
    def __init__(self, name, age, student_no, course):
        self.name = name
        self.age = age
        self.student_no = student_no
        self.course = course

    def study(self,unit):
        print(f"{self.name} studies {unit}")

    def study(self,football):
        print(f"{self.name} studies {football}")

    def study(self,enrolled):
        print(f"{self.name} studies {enrolled}")
    
    def display_info(self):
        print("User details")
        print(f"Name:{self.name} - Student No:{self.student_no} - Course:{self.course}")
        print("--------------------------------")

#object 1
student1 = Student("Jack",19,"100101","Finance")
print(type(student1))
print(student1)
student1.display_info()
student1.study("unit")
student1.play("football")
student1.get_enrolled("enrolled")


#object 2
student2 = Student("Mary",21,"100102","Data Science")
print(type(student2))
print(student2)
student2.display_info()
student2.study("unit")
student2.play("football")
student2.get_enrolled("enrolled")

from datetime import date
class BankAccount:
    def __init__(self, owner_name,account_number, balance, date_opened=date.today()):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance
        self.date_opened = date_opened

    def deposit(self,amount):
        if amount<=0 :
            print("Deposit amount must be grater than 0")
            return
        self.balance+=amount
        print(f"Deposit: Ksh. {amount}. New balance: Ksh.{self.balance} ")

    def withdraw(self,amount):
        if amount<=0 :
            print("Withdrawal amount must be grater than 0")
        if amount > balance:
            print("Insufficient balance. Current balance: Ksh. {self.balance}")
        self.balance-=amount
        print(f"Withdrawn: Ksh. {amount}. Current balance: Ksh.{self.balance}")

    def check_balance(self):
        print(f"{self.owner_name}'s balance is {self.balance}")

    def display_info(self):
        print("Account owner's details:")
        print(f"""
              ------------------------------------
              Name:{self.owner_name}  
              Account No:{self.account_number} 
              Balance:Ksh. {self.balance} 
              Date opened:{self.date_opened} 
              ------------------------------------""")
    
    def close_account(self):
        self.balance=0
        print(f"Account {self.account_number} has been closed. Balace set to Ksh. 0.00")

account1= BankAccount("Logan", 11045687, 8000.00 )
print(type(account1))
print(account1)
account1.display_info()
account1.deposit(20000)
account1.withdraw(2500)
account1.check_balance()
account1.close_account()

account2= BankAccount("Chelsea", 10120896, 12500.00)
print(type(account2))
print(account2)
account2.display_info()
account2.deposit(5000)
account2.withdraw(1800)
account2.check_balance()
account2.close_account()