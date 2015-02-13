import Utils

class ReadOnlyException(Exception):
  '''
  Exception thrown when accessing a read only property
  '''
  def __init__(self):
    pass

class WriteOnlyException(Exception):
  '''
  Exception thrown when accessing a write only property
  '''
  def __init__(self):
    pass

class Property:
  '''
  Define an ECMAScript style property. This should contains three members:
  * getter a Function that is called when accessing the value
  * setter a Function that is called when setting the value
  * this the object to which this property belongs
  '''
  def __init__(self):
    pass

  def get(self):
    '''
    Get the value or raise WriteOnlyException
    '''
    pass
    
  def set(self, value):
    '''
    Set the value or raise ReadOnlyException
    '''
    pass
 
  def merge(self, other):
    '''
    Merge two properties.
    '''
    pass
  def clone(self):
    '''
    Clone a property (useful when creating new objects).
    '''
    pass