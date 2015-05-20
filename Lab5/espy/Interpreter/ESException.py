class ESException(Exception):
  '''
  This exception can be use to implement an ECMAScript exception.
  '''
  def __init__(self, value):
    self.value = value