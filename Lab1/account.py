class AccountError(Exception):
  def __init__(self, value):
    self.value = value
  def str(self):
    return repr(self.value)
 
def make_account(balance, interest):
  lastTime = 0;
  def withdraw(amount, time):
    nonlocal balance, lastTime
    balance = get_balance(time);
    lastTime = time
    if balance >= amount:
      balance = balance - amount
    else:
      raise AccountError("Account balance too low")
      
  def deposit(amount, time):
    nonlocal balance, lastTime
    balance = get_balance(time) + amount
    lastTime = time
  
  def get_value(time):
    nonlocal lastTime
    tmp = get_balance(time)
    lastTime = time
    return tmp

  #lazy implementation
  def get_balance(time):
    nonlocal balance
    balance = balance+balance*(time-lastTime)*interest
    return balance
  
  public_methods = {'withdraw' : withdraw, 'deposit' : deposit, 'get_value' : get_value}
  return public_methods
