import Utils

class ReadOnlyException(Exception):
  '''
  Exception thrown when accessing a read only property
  '''
  def __init__(self):
    super().__init__("U has no getter, stupid!")

class WriteOnlyException(Exception):
  '''
  Exception thrown when accessing a write only property
  '''
  def __init__(self):
    super().__init__("U has no setter fool!")

class Property:
  '''
  Define an ECMAScript style property. This should contains three members:
  * getter a Function that is called when accessing the value
  * setter a Function that is called when setting the value
  * this the object to which this property belongs
  '''
  def __init__(self, this):
    self.getter = None;
    self.setter = None;
    self.this = this;

  def get(self):
    '''
    Get the value or raise WriteOnlyException
    '''
    if (self.getter == None):
      raise WriteOnlyException()
    else:
      return self.getter(self.this);
    
  def set(self, value):
    '''
    Set the value or raise ReadOnlyException
    '''
    if (self.setter == None):
      raise ReadOnlyException()
    else:
     return self.setter(self.this, value)
 
  def merge(self, other):
    '''
    Merge two properties.
    '''
    if (other.setter != None):
      self.setter = other.setter
    if (other.getter != None):
      self.getter = other.getter
    
  def clone(self):
    '''
    Clone a property (useful when creating new objects).
    '''
    newProp = Property(self.this)
    newProp.getter = self.getter
    newProp.setter = self.setter
    return newProp
