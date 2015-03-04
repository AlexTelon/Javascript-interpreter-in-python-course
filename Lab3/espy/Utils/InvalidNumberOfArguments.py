import Utils

class InvalidNumberOfArguments(BaseException):
  def __init__(self):
    super().__init__("Invalid number of arguments")