
class Code:
  '''
  This class hold the instructions for a program or a function.
  '''
  def __init__(self):
    self.instructions = []

  def add_instruction(self, instruction):
    '''
    Convenience function to add an instruction to the program
    '''
    self.instructions.append(instruction)

  def modify_instruction_arg(self, lineno, *arg):
    '''
    Convenience function to modify an instruction to the program
    '''
    #print("changed arg to: ", list(arg))
    self.instructions[lineno].params = list(arg)

  def get_instruction_arg(self, lineno):
    '''
    Convenience function to modify an instruction to the program
    '''
    return self.instructions[lineno].params


  def current_index(self):
    '''
    Return the current index, for use in jump instructions, for instnace.
    '''
    return len(self.instructions)



  def print(self):
    '''
    Print the list of instruction with their index, operands and parameters
    '''
    for i in range(0, len(self.instructions)):
      inst = self.instructions[i]
      print(i, ": ", inst.opcode, inst.params)
      
