class UnknownOperator(Exception):
  def __init__(self, op):
    super().__init__("Unknown operator '{}'".format(op))