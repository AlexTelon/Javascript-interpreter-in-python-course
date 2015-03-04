import inspect

def prettyprintstr(obj, indenting = ""):
  str = "{}{}\n".format(indenting, type(obj))
  
  for (k, v) in inspect.getmembers(obj):
    if(not k.startswith("__") and not inspect.ismethod(v)):
      str += "{}  {} = {}\n".format(indenting, k, v)
  
  return str

def prettyprint(obj, indenting = ""):
  print(prettyprintstr(obj, indenting))

def prettyprintall(objs, indenting = ""):
  for obj in objs:
    print(prettyprintstr(obj, indenting))

