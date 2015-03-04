import math
import random

class MathModule:
  def min(self, this, *args):
    return min(args)
  def max(self, this, *args):
    return max(args)
  def random(self, this):
    return random.random()
  def log(self, this, x):
    return math.log(x)
  def exp(self, this, x):
    return math.exp(x)
  def abs(self, this, x):
    return math.fabs(x)
  def cos(self, this, x):
    return math.cos(x)
  def acos(self, this, x):
    return math.acos(x)
  def sin(self, this, x):
    return math.sin(x)
  def asin(self, this, x):
    return math.asin(x)
  def tan(self, this, x):
    return math.tan(x)
  def atan(self, this, x):
    return math.atan(x)
  def round(self, this, x):
    return float(round(x))
  def ceil(self, this, x):
    return float(math.ceil(x))
  def floor(self, this, x):
    return float(math.floor(x))
  def pow(self, this, x, y):
    return pow(x, y)
  def sqrt(self, this, x):
    return math.sqrt(x)

