class UnknownVariable(Exception):
  def __init__(self, variable):
    super().__init__("Unknown variable '{}'".format(variable))