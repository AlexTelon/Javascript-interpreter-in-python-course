class BreakException(Exception):
  def __init__(self):
    pass


class ContinueException(Exception):
  def __init__(self):
    pass


class ReturnException(Exception):
  '''
  This an exception that can be used to represent a return statement
  '''
  def __init__(self, value):
    self.value = value

class ThrowException(Exception):
  '''
  If U throw then U thow this
  '''
  def __init__(self,msg):
    self.msg = msg
