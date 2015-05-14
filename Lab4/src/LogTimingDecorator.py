import time

class Logger:
  '''
  Logger class. It should contains an array of objects containing the information about function calls
  '''
  function_calls = [] # includes tons of fib calls

  class Func_call_obj:
    def __init__(self, name, args, result, start, end):
      self.func_name = name
      self.func_args = args
      self.func_result = result
      self.start = start
      self.end = end

  def __init__(self):
    function_calls = [] # New set for each logger
    
  def log_function_call(self, func_name, func_args, func_result, start, end):
    '''
    Call this function after the function has finished been executed
    func_name: name of the function
    func_args: list of arguments of the function
    func_result: return value from the function call
    start: time when the function was started
    end:   time when the function has finish execution
    '''
    func_call_obj = self.Func_call_obj(func_name, func_args, func_result, start, end)
    self.function_calls.append(func_call_obj)

def logtiming(logger):
  '''
  Decorator that will add an entry in logger after a function call
  '''
  #print("logger: ", logger)
  def make_decorator(func):
    #print("func: ", func)
    def decorator(*x):
      #print("*x: ", *x)
      start = time.time()
      func_ret = func(*x)
      end   = time.time()
      logger.log_function_call(func.__name__, x, func_ret, start, end)
      return func_ret
    return decorator
  return make_decorator
