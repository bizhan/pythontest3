class BankAccount:
  def __init__(self,name):
    self._name = name
    self._balance = 0.0

  def deposit(self, amount):
    self._balance += amount
    return self._balance
  
  def withdraw(self, amount):
    self._balance -= amount
    return self._balance

jim = BankAccount('JIM')
mich = BankAccount('Mich')




