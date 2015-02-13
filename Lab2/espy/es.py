#!/usr/bin/env python3

import sys

import antlr4
import ECMAScriptParser 
import Interpreter

def main(argv):
  input = antlr4.FileStream(argv[1])
  lexer = ECMAScriptParser.Lexer(input)
  stream = antlr4.CommonTokenStream(lexer)
  parser = ECMAScriptParser.Parser(stream)
  tree = parser.program()
  
  interpreter = Interpreter.InterpreterVisitor()
  tree.accept(interpreter)
 
if __name__ == '__main__':
  main(sys.argv)

