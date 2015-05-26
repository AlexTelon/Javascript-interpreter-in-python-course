#!/usr/bin/env python3

import sys

import antlr4
import ECMAScriptParser 
import VirtualMachine

def main(argv):
  input = antlr4.FileStream(argv[1])
  lexer = ECMAScriptParser.Lexer(input)
  stream = antlr4.CommonTokenStream(lexer)
  parser = ECMAScriptParser.Parser(stream)
  tree = parser.program()
  
  program  = VirtualMachine.Code()
  bytecode = VirtualMachine.BytecodeVisitor(program)
  tree.accept(bytecode)
  #program.print() # Uncomment to print the bytecode
  executor = VirtualMachine.Executor()
  executor.execute(program)
 
if __name__ == '__main__':
  main(sys.argv)

