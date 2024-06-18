# Write code below 💖

# bank_accounts.py

class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self,money):
    self.balance += money
  
  def withdraw(self,money):
    self.balance -= money
  
  def display_balance(self):
    print(f"{self.first_name} possui R${self.balance} na conta {self.account_type}.")

daniel = BankAccount('Daniel','Dmitry',214312,'corrente',2407,200.00)

daniel.deposit(96)
daniel.withdraw(25)
daniel.display_balance()