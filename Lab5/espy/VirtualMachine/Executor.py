from Interpreter.Environment    import Environment
from Interpreter.Object         import Object
from Interpreter.Function       import Function
from Interpreter.Property       import Property

from VirtualMachine.OpCode      import OpCode
from VirtualMachine.Code        import Code
from VirtualMachine.Instruction import Instruction
from VirtualMachine.Stack       import Stack

from Interpreter.ControlExceptions import ReturnException
from Interpreter.ESException       import ESException



class Executor:
  '''
  Execute the code of a program or function
  '''
  def __init__(self, environment = Environment()):
    self.environment = environment
    self.stack  = Stack()
    self.current_index = 0;
    
    # The following code acts as a switch statements for OpCodes
    self.opmaps  = {}
    # Stack
    self.opmaps[OpCode.PUSH] = Executor.execute_push
    self.opmaps[OpCode.POP] = Executor.execute_pop    
    self.opmaps[OpCode.DUP] = Executor.execute_dup
    self.opmaps[OpCode.SWAP] = Executor.execute_swap

    # Environment and objects manipulation
    self.opmaps[OpCode.LOAD] = Executor.execute_load
    self.opmaps[OpCode.STORE] = Executor.execute_store
    self.opmaps[OpCode.DCL] = Executor.execute_dcl
    self.opmaps[OpCode.LOAD_MEMBER] = Executor.execute_load_member
    self.opmaps[OpCode.STORE_MEMBER] = Executor.execute_store_member
    self.opmaps[OpCode.LOAD_INDEX] = Executor.execute_load_index
    self.opmaps[OpCode.STORE_INDEX] = Executor.execute_store_index

    # Control
    self.opmaps[OpCode.JMP] = Executor.execute_jmp
    self.opmaps[OpCode.IFJMP] = Executor.execute_ifjmp
    self.opmaps[OpCode.UNLESSJMP] = Executor.execute_unlessjmp
    self.opmaps[OpCode.CALL] = Executor.execute_call
    # self.opmaps[OpCode.NEW] = Executor.execute_new
    # self.opmaps[OpCode.RET] = Executor.execute_ret
    # self.opmaps[OpCode.SWITCH] = Executor.execute_switch

    # Exceptions
    # Array and Objects creation
    # Binary arithmetic operation
    # Binary bolean operation
    # Unary operations
   
    
  
  def execute(self, program):
    '''
    Execute the program given in argument
    '''
    
    # You might have to modify this later.
    # for inst in program.instructions:
    #   inst = program.instructions[self.current_index]
    #   f = self.opmaps[inst.opcode]

    #   f(self, *inst.params)
    #   self.current_index = self.current_index + 1
    #for inst in program.instructions:
    while self.current_index < len(program.instructions):
      inst = program.instructions[self.current_index]
      f = self.opmaps[inst.opcode]

      f(self, *inst.params)
      self.current_index = self.current_index + 1

  def execute_push(self, value):
    '''
    Execute the PUSH instruction
    '''
    self.stack.push(value)
  
  def execute_pop(self, count):
    '''
    Execute the POP instruction
    '''
    for i in range(0, count):
      self.stack.pop()

  def execute_dup(self):
    '''
    Execute the DUP instruction
    '''
    self.stack.dup()

  def execute_swap(self):
    '''
    Execute the SWAP instruction
    '''
    self.stack.swap()

  def execute_load(self, varname):
    '''
    Execute the LOAD instruction
    '''
    self.stack.push(self.environment.value(varname))

  def execute_store(self, varname):
    '''
    Execute the STORE instruction
    '''
    self.stack.dup() # make sure we still have a copy of the top element after the pop below
    self.environment.defineVariable(varname, self.stack.pop())

  def execute_dcl(self, varname):
    '''
    Execute the DCL instruction
    '''
    self.environment.defineVariable(varname)

  def execute_load_member(self, varname):
    '''
    Execute the LOAD_MEMBER instruction
    '''
    # self.stack.dup() # make sure we still have a copy of the top element after the pop below
    # print("derp: ", self.stack.pop().a)
    top_obj = self.stack.pop()
    try:
      if varname is "length":
        # if length we only return length of the array
        self.stack.push(len(top_obj))
      else:
        self.stack.push(getattr(top_obj, varname))
    except:
      self.stack.push(top_obj[varname])

  def execute_store_member(self, varname):
    '''
    Execute the STORE_MEMBER instruction
    '''
    obj = self.stack.pop()
    self.stack.dup()
    member = self.stack.pop()
    if isinstance(varname, (int, float)):
      index = int(varname)
      obj[index] = member
    else:
      setattr(obj,varname,member)

  def execute_load_index(self):
    '''
    Execute the LOAD_INDEX instruction
    '''
    index = self.stack.pop()
    obj = self.stack.pop()
    if isinstance(index, (int, float)):
      number = int(index)
      self.stack.push(obj[index])
    else:
      if index is "length":
        # if length we only return length of the array
        self.stack.push(len(obj))
      else:
        self.stack.push(getattr(obj,index))

  def execute_store_index(self):
    '''
    Execute the STORE_INDEX instruction
    '''
    index = self.stack.pop()
    obj = self.stack.pop()
    self.stack.dup()
    value = self.stack.pop()

    if isinstance(index, (int, float)):
      number = int(index)
      obj[index] = value
    else:
      setattr(obj,index,value)

  def execute_jmp(self, idx):
    '''
    Execute the JMP instruction
    '''
    self.current_index = idx - 1

  def execute_ifjmp(self, idx):
    '''
    Execute the IFJMP instruction
    '''

    bool = self.stack.pop()
    if bool:
      self.current_index = idx - 1

  def execute_unlessjmp(self, idx):
    '''
    Execute the UNLESS instruction
    '''
    bool = self.stack.pop()
    if not bool:
      self.current_index = idx - 1

  def execute_call(self, args):
    '''
    Execute the CALL instruction
    '''
    func = self.stack.pop()
    params = []
    for i in range(0,args):
      params.append(self.stack.pop())
    print("params: ", params)
    func(self, *params)    
