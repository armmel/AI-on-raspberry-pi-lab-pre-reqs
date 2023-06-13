class BankAccount:
  def __init__(self, account_number, balance=0):
    self.account_number = account_number 
    self.balance = balance 

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Deposited {amount} into the account")
    else:
      print("Amount is invalid")

  def withdraw(self, amount):
    if amount >0:
      self.balance -= amount
      print(f"Withdrew {amount} from the account")
    else:
      print("Amount is invalid")

  def get_balance(self):
    return self.balance
