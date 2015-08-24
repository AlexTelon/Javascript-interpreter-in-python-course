from enum import Enum

class OpCode(Enum):
  # Stack Manipulation
  NOP             = 0   # Do nothing
  PUSH            = 1   # PUSH [arg] Push a constant [arg] on the stack - CHECK
  POP             = 2   # POP [arg] Remove [arg] elements from the stack - CHECK
  DUP             = 3   # Duplicate the top value on the stack
  SWAP            = 4   # Swap the top two members of the stack
  
  # Environment and objects manipulation
  LOAD            = 10  # LOAD [varname] Load a variable from the environment
  STORE           = 11  # STORE [varname] Take a number from the stack and store it in the environment
  DCL             = 12  # DCL [varname] Declare a new variable
  LOAD_MEMBER     = 13 # LOAD_MEMBER [varname] Load a member from the first object in the stack
  STORE_MEMBER    = 14 # STORE_MEMBER [varname] Store the second object of the stack as the [varname] member of the first stack element
  LOAD_INDEX      = 15 # LOAD_INDEX Load a member from the second object in the stack using the index at the first position in the stck
  STORE_INDEX     = 16 # STORE_INDEX Store the third object of the stack of the second stack element using the first as stack index
  
  # Control
  JMP             = 20  # JMP [idx] Jump to a specific index
  IFJMP           = 21  # IFJMP [idx] Jump to a specific index if true
  UNLESSJMP       = 22  # UNLESSJMP [idx] Jump to a specific index if false
  CALL            = 23  # CALL [args] Call a function with the given number of arguments
  NEW             = 24  # NEW [args] Create an object and call the constructor with the given number of arguments
  RET             = 25  # Return from a function call
  SWITCH          = 26  # SWITCHTO [default] Jump to the index specified as the first element in the stack from a map of index, if the value is not in the map, jump to [default]  

  # Exceptions
  TRY_PUSH        = 30  # TRY_PUSH [idx]. Push index/address to jump to if an exception is thrown.
  TRY_POP         = 31  # TRY_POP. Pop address.
  THROW           = 32  # THROW an exception, with the first object of the stack
  
  # Array and Objects creation
  MAKE_ARRAY      = 40  # MAKE_ARRAY [count] make an array with the [count] elements from the stack
  MAKE_OBJECT     = 41  # MAKE_OBJECT [count]
  MAKE_FUNC       = 42  # MAKE_FUNC make a function top of the stack is the Code for the body, second is the argument list
  MAKE_GETTER     = 43  # MAKE_GETTER makes a getter property for an object, top of the stack is the property name, second is the function, third is the object, after the instruction the object is pushed backed on the stack
  MAKE_SETTER     = 44  # MAKE_SETTER makes a setter property for an object, top of the stack is the property name, second is the function, third is the object, after the instruction the object is pushed backed on the stack
  
  # Binary arithmetic operation
  ADD             = 50  # Takes two numbers from the stack and pushes the sum of them to stack.
  MUL             = 51  # Similar for multiplication
  SUB             = 52  # Similar for subtraction
  DIV             = 53  # Similar for division
  MOD             = 54  # Similar for modulus (remainder)
  LEFT_SHIFT      = 55  # Similar for left shift.
  RIGHT_SHIFT     = 56  # See above.
  UNSIGNED_RIGHT_SHIFT  = 57 # See above. Cf Utils.
  
  # Binary bolean operation
  SUPPERIOR       = 60  # Takes two elements from the stack and pushes the result of a greater-comparison.
  SUPPERIOR_EQUAL = 61  # Same as above, but with greater-or-equal.
  INFERIOR        = 62
  INFERIOR_EQUAL  = 63
  EQUAL           = 64
  DIFFERENT       = 65
  AND             = 66
  OR              = 67

  # Unary operations
  NEG             = 70 # Push the unary negation of the top element.
  TILDE           = 71  
  NOT             = 72 

  #wololo
  DEBUG           = 1337
  STACKDUMP           = 1373



