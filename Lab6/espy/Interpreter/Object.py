from Interpreter.Property import Property

class Object:
  def __init__(self):
    pass

class ObjectModule:
  def __init__(self):
    self.prototype = Object()
  
  def __call__(self, this, *args):
    pass
  def create(self, this, prototype):
    obj = Object()
    for attr in dir(prototype):
      val = getattr(prototype, attr)
      if(not callable(val) and not attr.startswith("__")):
        if(isinstance(val, tuple)):
          val = list(val)
          val[0] = obj
          val = (val[0], val[1])
        setattr(obj, attr, val)
    return obj
  
  def defineProperty(self, this, obj, name, param):

    prop = ObjectModule()

    if(hasattr(param, 'get')):
      tmp = getattr(param, 'get')
      setattr(prop,"get",tmp)
      
    if(hasattr(param, 'set')):
      tmp = getattr(param, 'set')
      setattr(prop,"set",tmp)
    setattr(obj, name, prop)
