from Interpreter.Environment    import Environment
from Interpreter.Object         import Object, ObjectModule
from Interpreter.Function       import Function
from Interpreter.Property       import Property
from VirtualMachine.OpCode      import OpCode
from VirtualMachine.Code        import Code
from VirtualMachine.Instruction import Instruction
from VirtualMachine.Stack       import Stack

from Interpreter.Console import Console
from Interpreter.Math import MathModule

from Interpreter.ControlExceptions import ReturnException
from Interpreter.ESException       import ESException
from Utils.UnsignedShiftRight      import unsignedShiftRight


class Executor:
  '''
  Execute the code of a program or function
  '''
  def __init__(self, environment = Environment()):
    self.environment = environment

    self.environment.defineVariable("console", Console())
    self.environment.defineVariable("Math", MathModule())
    self.environment.defineVariable("Object", ObjectModule())

    self.stack  = Stack()
    self.current_index = 0;
    self.exceptionStack = Stack();

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
    self.opmaps[OpCode.NEW] = Executor.execute_new
    self.opmaps[OpCode.RET] = Executor.execute_ret
    self.opmaps[OpCode.SWITCH] = Executor.execute_switch

    # Exceptions
    self.opmaps[OpCode.TRY_PUSH] = Executor.execute_try_push
    self.opmaps[OpCode.TRY_POP] = Executor.execute_try_pop
    self.opmaps[OpCode.THROW] = Executor.execute_throw

    # Array and Objects creation
    self.opmaps[OpCode.MAKE_ARRAY] = Executor.execute_make_array
    self.opmaps[OpCode.MAKE_OBJECT] = Executor.execute_make_object
    self.opmaps[OpCode.MAKE_FUNC] = Executor.execute_make_func
    self.opmaps[OpCode.MAKE_GETTER] = Executor.execute_make_getter
    self.opmaps[OpCode.MAKE_SETTER] = Executor.execute_make_setter

    # Binary arithmetic operation
    self.opmaps[OpCode.ADD] = Executor.execute_add
    self.opmaps[OpCode.MUL] = Executor.execute_mul
    self.opmaps[OpCode.SUB] = Executor.execute_sub
    self.opmaps[OpCode.DIV] = Executor.execute_div
    self.opmaps[OpCode.MOD] = Executor.execute_mod
    self.opmaps[OpCode.LEFT_SHIFT] = Executor.execute_left_shift
    self.opmaps[OpCode.RIGHT_SHIFT] = Executor.execute_right_shift
    self.opmaps[OpCode.UNSIGNED_RIGHT_SHIFT] = Executor.execute_unsigned_right_shift

    # Binary bolean operation
    self.opmaps[OpCode.SUPPERIOR] = Executor.execute_supperior
    self.opmaps[OpCode.SUPPERIOR_EQUAL] = Executor.execute_supperior_equal
    self.opmaps[OpCode.INFERIOR] = Executor.execute_inferior
    self.opmaps[OpCode.INFERIOR_EQUAL] = Executor.execute_inferior_equal
    self.opmaps[OpCode.EQUAL] = Executor.execute_equal
    self.opmaps[OpCode.DIFFERENT] = Executor.execute_different
    self.opmaps[OpCode.AND] = Executor.execute_and
    self.opmaps[OpCode.OR] = Executor.execute_or

    # Unary operations
    self.opmaps[OpCode.NEG] = Executor.execute_neg
    self.opmaps[OpCode.TILDE] = Executor.execute_tilde
    self.opmaps[OpCode.NOT] = Executor.execute_not
    
  
  def execute(self, program):
    '''
    Execute the program given in argument
    '''
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

    try:
      ret = func(self, *params)
    except ReturnException as e:
      ret = e.value

    self.stack.push(ret)

  def execute_new(self, args):
    '''
    Execute the NEW instruction
    '''
    func = self.stack.pop()
    params = []
    for i in range(0,args):
      params.insert(0, self.stack.pop())
    
    ret = func(self, *params)
    self.stack.push(Object())

  def execute_ret(self):
    '''
    Execute the RET instruction
    '''
    ret = self.stack.pop()
    raise ReturnException(ret)

  def execute_switch(self, default):
    '''
    Execute the SWITCH instruction
    '''
    values = self.stack.pop()
    key = self.stack.pop()

    try:
      self.current_index = values[key] -1 
    except:
      self.current_index = default - 1 

  def execute_try_push(self, idx):
    '''
    Execute the TRY_PUSH instruction
    '''
    self.exceptionStack.push(idx)

  def execute_throw(self):
    '''
    Execute the THROW instruction
    '''
    if self.exceptionStack.size() > 0:
      exceptionAddress = self.exceptionStack.pop()
      self.current_index = exceptionAddress - 1
    else:
      topStack = self.stack.pop()
      raise ESException(topStack)


  def execute_try_pop(self):
    '''
    Execute the TRY_POP instruction
    '''
    self.exceptionStack.pop()

  def execute_make_array(self, count):
    '''
    Execute the MAKE_ARRAY instruction
    '''
    array = []
    for i in range(0,count):
      array.insert(0, self.stack.pop())
    self.stack.push(array)

  def execute_make_object(self, count):
    '''
    Execute the MAKE_OBJECT instruction
    '''
    Obj = Object()
    key = ""
    count = count * 2
    for i in range(0,count):
      if i % 2 == 0:
        # we have an value
        key = self.stack.pop()
      else:
        # we have an key
        value = self.stack.pop()
        setattr(Obj, key, value)
    self.stack.push(Obj)

  def execute_make_func(self):
    '''
    Execute the MAKE_FUNC instruction
    '''
    code = self.stack.pop()
    args = self.stack.pop()
    def body(env):
      exe = Executor(Environment(env))
      exe.execute(code)
             
    f = Function(args, self.environment, body)
    self.stack.push(f)

  def execute_make_getter(self):
    '''
    Execute the MAKE_GETTER instruction
    '''
    name = self.stack.pop()
    func = self.stack.pop()
    obj = self.stack.pop()
    
    if(hasattr(obj,name) and isinstance(getattr(obj,name), Property )):
       prop = getattr(obj,name)
    else:
       prop = Property(obj)
    prop.getter = func
    setattr(obj, name, prop)
       
    self.stack.push(obj)

  def execute_make_setter(self):
    '''
    Execute the MAKE_SETTER instruction
    '''
    name = self.stack.pop()
    func = self.stack.pop()
    obj = self.stack.pop()
    
    if(hasattr(obj,name) and isinstance(getattr(obj,name), Property)):
       prop = getattr(obj,name)
    else:
       prop = Property(obj)
    prop.setter = func
    setattr(obj, name, prop)
       
    self.stack.push(obj)

  def execute_add(self):
    '''
    Execute the ADD instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = a+b
    self.stack.push(val)

  def execute_mul(self):
    '''
    Execute the MUL instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = a*b
    self.stack.push(val)

  def execute_sub(self):
    '''
    Execute the SUB instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = b-a
    self.stack.push(val)

  def execute_div(self):
    '''
    Execute the DIV instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = b/a
    self.stack.push(val)

  def execute_mod(self):
    '''
    Execute the MOD instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = b % a
    self.stack.push(val)

  def execute_left_shift(self):
    '''
    Execute the LEFT_SHIFT instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    a = int(a)
    b = int(b)
    val = b << a
    val = float(val)
    self.stack.push(val)

  def execute_right_shift(self):
    '''
    Execute the RIGHT_SHIFT instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    a = int(a)
    b = int(b)
    val = b >> a
    val = float(val)
    self.stack.push(val)

  def execute_unsigned_right_shift(self):
    '''
    Execute the UNSIGNED_RIGHT_SHIFT instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    a = int(a)
    b = int(b)
    val = unsignedShiftRight(b,a)
    val = float(val)
    self.stack.push(val)

  def execute_supperior(self):
    '''
    Execute the SUPPERIOR instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = b > a
    self.stack.push(val)

  def execute_supperior_equal(self):
    '''
    Execute the SUPPERIOR_EQUAL instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = b >= a
    self.stack.push(val)

  def execute_inferior(self):
    '''
    Execute the INFERIOR instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = b < a
    self.stack.push(val)

  def execute_inferior_equal(self):
    '''
    Execute the INFERIOR_EQUAL instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = b <= a
    self.stack.push(val)

  def execute_equal(self):
    '''
    Execute the EQUAL instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = b == a
    self.stack.push(val)

  def execute_different(self):
    '''
    Execute the DIFFERENT instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = not (b == a)
    self.stack.push(val)

  def execute_and(self):
    '''
    Execute the AND instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = b and a
    self.stack.push(val)

  def execute_or(self):
    '''
    Execute the OR instruction
    '''
    a = self.stack.pop()
    b = self.stack.pop()
    val = b or a
    self.stack.push(val)


  def execute_neg(self):
    '''
    Execute the NEG instruction
    '''
    a = self.stack.pop()
    val = -a
    self.stack.push(val)


  def execute_tilde(self):
    '''
    Execute the TILDE instruction
    '''
    a = self.stack.pop()
    a = int(a)
    val = ~a
    val = float(val)
    self.stack.push(val)


  def execute_not(self):
    '''
    Execute the NOT instruction
    '''
    a = self.stack.pop()
    val = not a
    self.stack.push(val)
