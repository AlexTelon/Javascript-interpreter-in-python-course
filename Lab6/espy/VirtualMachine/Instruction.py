from VirtualMachine.OpCode import OpCode

class Instruction:
  '''
  Represent a single instruction with its given OpCode and its parameters
  '''
  def __init__(self, opcode: OpCode, *params):
    self.opcode = opcode
    self.params = list(params)
  