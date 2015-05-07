# Change bound_checking_decorator to handle function with multiple arguments

def bound_checking_decorator(*args):
  # *args is (-1 1 -2 2 -3 3)
  def make_decorator(func):
    # *x is (a b c)
    def decorator(*x):
      i = 0
      for param in x:
        # get the min and max value for this param from args
        min = args[i]
        i = i + 1    
        max = args[i]
        i = i + 1
        #print("min:", min, " max:", max, " value:", param)
        if(param < min or param > max):
          raise Exception()
      # if no Exception has been raised we can safely return
      return func(*x)
    return decorator
  return make_decorator
