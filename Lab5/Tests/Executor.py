#!/usr/bin/env python3

import unittest
from Interpreter.Environment    import Environment
from Interpreter.Object         import Object
from Interpreter.Function       import Function
from Interpreter.Property       import Property
import Utils
from VirtualMachine.OpCode      import OpCode
from VirtualMachine.Code        import Code
from VirtualMachine.Instruction import Instruction
from VirtualMachine.Executor    import Executor
from Interpreter.ControlExceptions import ReturnException
from Interpreter.ESException import ESException
  

class TestExecutor(unittest.TestCase):

  def run_test_executor(self, instructions, final_stack, initial_environment, final_environment):
    code     = Code()
    
    for inst in instructions:
      code.add_instruction(Instruction(inst[0], *tuple(inst[1:len(inst)])))
    env      = Environment()

    for key, value in initial_environment.items():
      env.defineVariable(key, value)
    
    executor = Executor(env)
    executor.execute(code)
    self.assertEqual(len(final_stack), len(executor.stack.stack))
    
    for i in range(0, len(final_stack)):
      f_elt = final_stack[i]
      a_elt = executor.stack.stack[i]
      if(isinstance(f_elt, Object) or isinstance(f_elt, Function)):
        self.assertEqual(f_elt.__class__, a_elt.__class__)
      else:
        self.assertEqual(f_elt, a_elt)
    
    for key, value in final_environment.items():
      self.assertEqual(env.value(key), value)
      
    return (executor.stack.stack, env)
    
  def test_001_push(self):
    self.run_test_executor( 
      [[OpCode.PUSH, 1.0], [OpCode.PUSH, -1.0]],
      [1.0, -1.0],
      {}, {})
  def test_002_pop(self):
    self.run_test_executor( 
      [[OpCode.PUSH, 1.0], [OpCode.PUSH, -1.0], [OpCode.PUSH, 0.0], [OpCode.POP, 2]],
      [1.0],
      {}, {})
  def test_003_dup(self):
    self.run_test_executor( 
      [[OpCode.PUSH, 1.0], [OpCode.DUP]],
      [1.0, 1.0],
      {}, {})
  def test_004_swap(self):
    self.run_test_executor( 
      [[OpCode.PUSH, 1.0], [OpCode.PUSH, -1.0], [OpCode.SWAP]],
      [-1.0, 1.0],
      {}, {})
  def test_010_load(self):
    self.run_test_executor( 
      [[OpCode.LOAD, 'a']],
      [1.0],
      { 'a': 1.0 }, { 'a': 1.0 })
  def test_011_store(self):
    self.run_test_executor( 
      [[OpCode.PUSH, -1.0], [OpCode.STORE, 'a']],
      [-1.0],
      { 'a': 1.0 }, { 'a': -1.0 })
  def test_012_dcl(self):
    self.run_test_executor( 
      [[OpCode.DCL, 'a'], [OpCode.PUSH, -1.0], [OpCode.STORE, 'a']],
      [-1.0],
      { }, { 'a': -1.0 })
  def test_013_load_member(self):
    obj = Object()
    setattr(obj, 'a', -1.0)
    self.run_test_executor( 
      [[OpCode.PUSH, obj ], [OpCode.LOAD_MEMBER, 'a']],
      [-1.0],
      { }, { })
    arr = [1.0, 2.0, 4.0]
    self.run_test_executor( 
      [[OpCode.PUSH, arr ], [OpCode.LOAD_MEMBER, 1]],
      [2.0],
      { }, { })
    self.run_test_executor( 
      [[OpCode.PUSH, arr ], [OpCode.LOAD_MEMBER, 'length' ]],
      [3.0],
      { }, { })
  def test_014_store_member(self):
    obj = Object()
    setattr(obj, 'a', -1.0)
    self.run_test_executor( 
      [[OpCode.PUSH, 1.0 ], [OpCode.PUSH, obj ], [OpCode.STORE_MEMBER, 'a']],
      [1.0],
      { }, { })
    self.assertEqual(obj.a, 1.0)
    arr = [1.0, 2.0, 4.0]
    self.run_test_executor( 
      [[OpCode.PUSH, -1.0 ], [OpCode.PUSH, arr ], [OpCode.STORE_MEMBER, 1]],
      [-1.0],
      { }, { })
    self.assertEqual(arr,[1.0, -1.0, 4.0])
  def test_015_load_index(self):
    obj = Object()
    setattr(obj, 'a', -1.0)
    self.run_test_executor( 
      [[OpCode.PUSH, obj ], [OpCode.PUSH, 'a' ], [OpCode.LOAD_INDEX]],
      [-1.0],
      { }, { })
    arr = [1.0, 2.0, 4.0]
    self.run_test_executor( 
      [[OpCode.PUSH, arr ], [OpCode.PUSH, 1 ], [OpCode.LOAD_INDEX]],
      [2.0],
      { }, { })
    self.run_test_executor( 
      [[OpCode.PUSH, arr ], [OpCode.PUSH, 'length' ], [OpCode.LOAD_INDEX]],
      [3.0],
      { }, { })
  def test_016_store_index(self):
    obj = Object()
    setattr(obj, 'a', -1.0)
    self.run_test_executor( 
      [[OpCode.PUSH, 1.0 ], [OpCode.PUSH, obj ], [OpCode.PUSH, 'a' ], [OpCode.STORE_INDEX ]],
      [1.0],
      { }, { })
    self.assertEqual(obj.a, 1.0)
    arr = [1.0, 2.0, 4.0]
    self.run_test_executor( 
      [[OpCode.PUSH, -1.0 ], [OpCode.PUSH, arr ], [OpCode.PUSH, 1 ], [OpCode.STORE_INDEX ]],
      [-1.0],
      { }, { })
    self.assertEqual(arr,[1.0, -1.0, 4.0])

  def test_020_jmp(self):
    self.run_test_executor( 
      [[OpCode.JMP, 2], [OpCode.PUSH, 1.0 ], [OpCode.PUSH, -1.0 ] ],
      [-1.0],
      { }, { })

  def test_021_ifjmp(self):
    self.run_test_executor( 
      [[OpCode.PUSH, True], [OpCode.IFJMP, 3], [OpCode.PUSH, 1.0 ], [OpCode.PUSH, -1.0 ] ],
      [-1.0],
      { }, { })
    self.run_test_executor( 
      [[OpCode.PUSH, False], [OpCode.IFJMP, 3], [OpCode.PUSH, 1.0 ], [OpCode.PUSH, -1.0 ] ],
      [1.0, -1.0],
      { }, { })

  def test_022_unlessjmp(self):
    self.run_test_executor( 
      [[OpCode.PUSH, True], [OpCode.UNLESSJMP, 3], [OpCode.PUSH, 1.0 ], [OpCode.PUSH, -1.0 ] ],
      [1.0, -1.0],
      { }, { })
    self.run_test_executor( 
      [[OpCode.PUSH, False], [OpCode.UNLESSJMP, 3], [OpCode.PUSH, 1.0 ], [OpCode.PUSH, -1.0 ] ],
      [-1.0],
      { }, { })
  
  def test_023_call(self):
    global test_014_called
    test_014_called = False
    def func_body(env):
      global  test_014_called
      test_014_called = True
    f = Function([], Environment(), func_body)
    self.run_test_executor( 
      [[OpCode.PUSH, f], [OpCode.CALL, 0] ],
      [None],
      { }, { })
    self.assertTrue(test_014_called)

    def func_body_params(env):
      self.assertEqual(env.value('a'), 1.0)
      self.assertEqual(env.value('b'), 2.0)
    f = Function(['a', 'b'], Environment(), func_body)
    self.run_test_executor( 
      [[OpCode.PUSH, 1.0], [OpCode.PUSH, 2.0], [OpCode.PUSH, f], [OpCode.CALL, 2] ],
      [None],
      { }, { })
  
  def test_024_new(self):
    def func_new(env):
      self.assertTrue(env.value("this"), Object)
      self.assertEqual(env.value('a'), 1.0)
      self.assertEqual(env.value('b'), 2.0)
    f = Function(['a', 'b'], Environment(), func_new)
    self.run_test_executor(
      [[OpCode.PUSH, 1.0], [OpCode.PUSH, 2.0], [OpCode.PUSH, f], [OpCode.NEW, 2] ],
      [Object()],
      { }, { })
  
  def test_025_ret(self):
    self.assertRaises(ReturnException, self.run_test_executor, [[OpCode.PUSH, 1.0], [OpCode.RET]], [], {}, {})
  
  def test_026_switch(self):
    self.run_test_executor(
      [[OpCode.PUSH, 1], [OpCode.PUSH, {1: 3, -1: 4, 0: 5}], [OpCode.SWITCH, 6],  [OpCode.PUSH, 2.0], [OpCode.PUSH, 3.0], [OpCode.PUSH, 4.0] ],
      [2.0, 3.0, 4.0],
      { }, { })
    self.run_test_executor(
      [[OpCode.PUSH, 10], [OpCode.PUSH, {1: 3, -1: 4, 0: 5}], [OpCode.SWITCH, 6],  [OpCode.PUSH, 2.0], [OpCode.PUSH, 3.0], [OpCode.PUSH, 4.0] ],
      [],
      { }, { })
  
  def test_030_exception(self):
    self.run_test_executor([[ OpCode.TRY_PUSH, 5], [OpCode.PUSH, 1.0], [OpCode.THROW], [OpCode.PUSH, 3.0], [OpCode.TRY_POP]  ], [1.0], {}, {})
  
    self.assertRaises(ESException, self.run_test_executor, [[OpCode.PUSH, 1.0], [OpCode.THROW] ], [], {}, {})
    self.assertRaises(ESException, self.run_test_executor, [[ OpCode.TRY_PUSH, 5], [OpCode.PUSH, 1.0], [OpCode.PUSH, 3.0], [OpCode.TRY_POP], [OpCode.THROW]], [], {}, {})
  
  def test_040_make_array(self):
    self.run_test_executor( [[OpCode.PUSH, 1.0], [OpCode.PUSH, 2.0], [OpCode.MAKE_ARRAY, 2]], [[1.0, 2.0]], {}, {})
  
  def test_041_make_object(self):
    (stack, env) = self.run_test_executor( [[OpCode.PUSH, 1.0], [OpCode.PUSH, 'a'], [OpCode.PUSH, 2.0], [OpCode.PUSH, 'b'], [OpCode.MAKE_OBJECT, 2]], [Object()], {}, {})
    self.assertEqual(stack[0].a, 1.0)
    self.assertEqual(stack[0].b, 2.0)
  
  def test_042_make_function(self):
    args = ['a', 'b']
    code = Code()
    (stack, env) = self.run_test_executor( [[OpCode.PUSH, args], [OpCode.PUSH, code], [OpCode.MAKE_FUNC]], [Function(None, None, None)], {}, {})
    self.assertEqual(stack[0].args, args)
    code.add_instruction(Instruction(OpCode.PUSH, 1.0))
    code.add_instruction(Instruction(OpCode.RET))
    self.run_test_executor( [[OpCode.PUSH, []], [OpCode.PUSH, code], [OpCode.MAKE_FUNC], [OpCode.CALL, 0] ], [1.0], {}, {})
  
  def test_043_make_getter(self):
    f = Function(None, None, None)
    obj = Object()
    self.run_test_executor( [[OpCode.PUSH, obj], [OpCode.PUSH, f], [OpCode.PUSH, 'test'], [OpCode.MAKE_GETTER] ], [obj], {}, {})
    self.assertTrue(isinstance(obj.test, Property))
    self.assertEqual(obj.test.getter, f)
    self.assertEqual(obj.test.setter, None)
  
  def test_044_make_setter(self):
    f = Function(None, None, None)
    obj = Object()
    self.run_test_executor( [[OpCode.PUSH, obj], [OpCode.PUSH, f], [OpCode.PUSH, 'test'], [OpCode.MAKE_SETTER] ], [obj], {}, {})
    self.assertTrue(isinstance(obj.test, Property))
    self.assertEqual(obj.test.setter, f)
    self.assertEqual(obj.test.getter, None)
    f2 = Function(None, None, None)
    self.run_test_executor( [[OpCode.PUSH, obj], [OpCode.PUSH, f2], [OpCode.PUSH, 'test'], [OpCode.MAKE_GETTER] ], [obj], {}, {})
    self.assertEqual(obj.test.setter, f)
    self.assertEqual(obj.test.getter, f2)
  
  def run_test_binary(self, opcode, arg1, arg2, result):
    self.run_test_executor([[OpCode.PUSH, arg1], [OpCode.PUSH, arg2], [opcode]], [result], {}, {})
  
  def test_050_add(self):
    self.run_test_binary(OpCode.ADD, 1.0, 2.0, 3.0)

  def test_051_sub(self):
    self.run_test_binary(OpCode.SUB, 1.0, 2.0,-1.0)
  
  def test_052_div(self):
    self.run_test_binary(OpCode.DIV, 1.0, 2.0, 0.5)
  
  def test_053_mul(self):
    self.run_test_binary(OpCode.MUL, 3.0, 2.0, 6.0)
  
  def test_054_mod(self):
    self.run_test_binary(OpCode.MOD, 7.0, 2.0, 1.0)
  
  def test_055_left_shift(self):
    self.run_test_binary(OpCode.LEFT_SHIFT, 10.0, 2.0, 40.0)
    
  def test_056_right_shift(self):
    self.run_test_binary(OpCode.RIGHT_SHIFT, 10.0, 2.0, 2.0)
    
  def test_057_unsigned_right_shift(self):
    self.run_test_binary(OpCode.UNSIGNED_RIGHT_SHIFT, -8.0, 2.0, 1073741822.0)
    
  def test_060_supperior(self):
    self.run_test_binary(OpCode.SUPPERIOR, -8.0, 2.0, False)
    self.run_test_binary(OpCode.SUPPERIOR,  8.0, 2.0, True)
    self.run_test_binary(OpCode.SUPPERIOR,  2.0, 2.0, False)
  
  def test_061_supperior_equal(self):
    self.run_test_binary(OpCode.SUPPERIOR_EQUAL, -8.0, 2.0, False)
    self.run_test_binary(OpCode.SUPPERIOR_EQUAL,  8.0, 2.0, True)
    self.run_test_binary(OpCode.SUPPERIOR_EQUAL,  2.0, 2.0, True)
  
  def test_062_inferior(self):
    self.run_test_binary(OpCode.INFERIOR, -8.0, 2.0, True)
    self.run_test_binary(OpCode.INFERIOR,  8.0, 2.0, False)
    self.run_test_binary(OpCode.INFERIOR,  2.0, 2.0, False)
  
  def test_063_inferior_equal(self):
    self.run_test_binary(OpCode.INFERIOR_EQUAL, -8.0, 2.0, True)
    self.run_test_binary(OpCode.INFERIOR_EQUAL,  8.0, 2.0, False)
    self.run_test_binary(OpCode.INFERIOR_EQUAL,  2.0, 2.0, True)
  
  def test_064_equal(self):
    self.run_test_binary(OpCode.EQUAL, -8.0, 2.0, False)
    self.run_test_binary(OpCode.EQUAL,  8.0, 2.0, False)
    self.run_test_binary(OpCode.EQUAL,  2.0, 2.0, True)
  
  def test_065_different(self):
    self.run_test_binary(OpCode.DIFFERENT, -8.0, 2.0, True)
    self.run_test_binary(OpCode.DIFFERENT,  8.0, 2.0, True)
    self.run_test_binary(OpCode.DIFFERENT,  2.0, 2.0, False)
  
  def test_066_and(self):
    self.run_test_binary(OpCode.AND, True, True, True)
    self.run_test_binary(OpCode.AND, True, False, False)
    self.run_test_binary(OpCode.AND, False, True, False)
    self.run_test_binary(OpCode.AND, False, False, False)
  
  def test_067_and(self):
    self.run_test_binary(OpCode.OR, True, True, True)
    self.run_test_binary(OpCode.OR, True, False, True)
    self.run_test_binary(OpCode.OR, False, True, True)
    self.run_test_binary(OpCode.OR, False, False, False)
  
  def run_test_unary(self, opcode, arg, result):
    self.run_test_executor([[OpCode.PUSH, arg], [opcode]], [result], {}, {})
  
  def test_070_neg(self):
    self.run_test_unary(OpCode.NEG, 1.0, -1.0)
  
  def test_071_tilde(self):
    self.run_test_unary(OpCode.TILDE, 10.0,-11.0)
  
  def test_072_not(self):
    self.run_test_unary(OpCode.NOT, True, False)
    self.run_test_unary(OpCode.NOT, False, True)
  
if __name__ == '__main__':
  unittest.main(failfast=True)  # Only test until first failure
