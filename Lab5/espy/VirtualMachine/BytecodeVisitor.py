# Generated from java-escape by ANTLR 4.4
from antlr4 import *
import Utils

from ECMAScriptParser import ECMAScriptVisitor

# This class defines a complete generic visitor for a parse tree produced by ECMAScriptParser.

class BytecodeVisitor(ECMAScriptVisitor):
  def __init__(self, program):
    self.program    = program

  def add_instruction(self, opcode, *arguments):
    inst = Instruction(opcode, *arguments)
    self.program.add_instruction(inst)
    return inst

  AV_IDENTIFIER = 0
  AV_MEMBERDOT  = 1
  AV_INDICE     = 2
  
  
  
  
  
  
   # Visit a parse tree produced by ECMAScriptParser#ArgumentsExpression.
  def visitArgumentsExpression(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)
  
  
  # Visit a parse tree produced by ECMAScriptParser#elementList.
  def visitElementList(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)
  
  # Visit a parse tree produced by ECMAScriptParser#ForInStatement.
  def visitForInStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#emptyStatement.
  def visitEmptyStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)
# Visit a parse tree produced by ECMAScriptParser#NewExpression.
  def visitNewExpression(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  # Visit a parse tree produced by ECMAScriptParser#MemberDotExpression.
  def visitMemberDotExpression(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)
      
    # Visit a parse tree produced by ECMAScriptParser#tryStatement.
  def visitTryStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  # Visit a parse tree produced by ECMAScriptParser#DoStatement.
  def visitDoStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  # Visit a parse tree produced by ECMAScriptParser#WhileStatement.
  def visitWhileStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#returnStatement.
  def visitReturnStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#switchStatement.
  def visitSwitchStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)
  
    # Visit a parse tree produced by ECMAScriptParser#FunctionExpression.
  def visitFunctionExpression(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  # Visit a parse tree produced by ECMAScriptParser#defaultClause.
  def visitDefaultClause(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  # Visit a parse tree produced by ECMAScriptParser#ForStatement.
  def visitForStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#caseBlock.
  def visitCaseBlock(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  # Visit a parse tree produced by ECMAScriptParser#objectLiteral.
  def visitObjectLiteral(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#throwStatement.
  def visitThrowStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#breakStatement.
  def visitBreakStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ifStatement.
  def visitIfStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  # Visit a parse tree produced by ECMAScriptParser#variableDeclaration.
  def visitVariableDeclaration(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#catchProduction.
  def visitCatchProduction(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#continueStatement.
  def visitContinueStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#caseClause.
  def visitCaseClause(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

      
  
  
  def gen_setter(self, a, idx, b):
    if(isinstance(a, list)):
      a[int(idx)] = b
    else:
      if(isinstance(idx, float)):
        idx = "__float__" + str(idx)
      if(isinstance(b, Function)):
        b = (a, b)
      if(hasattr(a, idx)):
        val = getattr(a, idx)
        if(isinstance(val, Property)):
          val.set(b)
        else:
          setattr(a, idx, b)
      else:
        setattr(a, idx, b)

  def gen_getter(self, a, idx):
    if(isinstance(a, list)):
      if(idx == 'length'):
        return float(len(a))
      elif(idx == 'append'):
        return lambda this, value: a.append(value)
      return a[int(idx)]
    else:
      if(isinstance(idx, float)):
        idx = "__float__" + str(idx)
      val = getattr(a, idx)
      if(isinstance(val, Property)):
        return val.get()
      else:
        return val

  def gen_setter_dot(self, a, idx):
    a.accept(self)
    self.add_instruction(OpCode.STORE_MEMBER, idx)
    
  def gen_getter_dot(self, a, idx):
    a.accept(self)
    self.add_instruction(OpCode.LOAD_MEMBER, idx)
    
  def gen_setter_indice(self, a, idx):
    a.accept(self)
    idx.accept(self)
    self.add_instruction(OpCode.STORE_INDEX)
    
  def gen_getter_indice(self, a, idx):
    a.accept(self)
    idx.accept(self)
    self.add_instruction(OpCode.LOAD_INDEX)
    
  def assignmentVariable(self, array, index, typ):
    if(typ == self.AV_IDENTIFIER):
      variable_setter = lambda: self.add_instruction(OpCode.STORE, array[index].symbol.text)
      variable_getter = lambda: self.add_instruction(OpCode.LOAD, array[index].symbol.text)
    elif(typ == self.AV_MEMBERDOT):
      variable_setter = lambda: self.gen_setter_dot(array[index], array[index + 2].accept(self))
      variable_getter = lambda: self.gen_getter_dot(array[index], array[index + 2].accept(self))
    elif(typ == self.AV_INDICE):
      variable_setter = lambda: self.gen_setter_indice(array[index], array[index + 2])
      variable_getter = lambda: self.gen_getter_indice(array[index], array[index + 2])
    else:
      raise Utils.UnimplementedVisitorException(array)
    return (variable_setter, variable_getter)

  # Visit a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
  def visitPropertyExpressionAssignment(self, ctx):
    ctx.children[2].accept(self)
    name = ctx.children[0].accept(self)
    if(name != None):
      self.add_instruction(OpCode.PUSH, name)


  # Visit a parse tree produced by ECMAScriptParser#assignmentOperator.
  def visitAssignmentOperator(self, ctx):
    return ctx.children[0].symbol.text


  # Visit a parse tree produced by ECMAScriptParser#eos.
  def visitEos(self, ctx):
    pass


  # Visit a parse tree produced by ECMAScriptParser#program.
  def visitProgram(self, ctx):
    args = []
    for c in ctx.children:
      if(not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)): # Skip ","
        args.append(c.accept(self))
    return args


  # Visit a parse tree produced by ECMAScriptParser#argumentList.
  def visitArgumentList(self, ctx):
    count = 0
    for c in ctx.children:
      if(not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)): # Skip ","
        c.accept(self)
        count += 1
    return count


 


  # Visit a parse tree produced by ECMAScriptParser#ThisExpression.
  def visitThisExpression(self, ctx):
    self.add_instruction(OpCode.LOAD, "this")


  # Visit a parse tree produced by ECMAScriptParser#identifierName.
  def visitIdentifierName(self, ctx):
    return ctx.children[0].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#BinaryExpression.
  def visitBinaryExpression(self, ctx):
    op  = ctx.children[1].accept(self)
    
    ctx.children[0].accept(self)
    ctx.children[2].accept(self)
    if(op == '+'):
      self.add_instruction(OpCode.ADD)
    elif(op == '-'):
      self.add_instruction(OpCode.SUB)
    elif(op == '*'):
      self.add_instruction(OpCode.MUL)
    elif(op == '/'):
      self.add_instruction(OpCode.DIV)
    elif(op == '%'):
      self.add_instruction(OpCode.MOD)
    elif(op == '<<'):
      self.add_instruction(OpCode.LEFT_SHIFT)
    elif(op == '>>'):
      self.add_instruction(OpCode.RIGHT_SHIFT)
    elif(op == '>>>'):
      self.add_instruction(OpCode.UNSIGNED_RIGHT_SHIFT)
    elif(op == '>'):
      self.add_instruction(OpCode.SUPPERIOR)
    elif(op == '>='):
      self.add_instruction(OpCode.SUPPERIOR_EQUAL)
    elif(op == '<'):
      self.add_instruction(OpCode.INFERIOR)
    elif(op == '<='):
      self.add_instruction(OpCode.INFERIOR_EQUAL)
    elif(op == '==' or op == '==='):
      self.add_instruction(OpCode.EQUAL)
    elif(op == '!=' or op == '!=='):
      self.add_instruction(OpCode.DIFFERENT)
    elif(op == '&&'):
      self.add_instruction(OpCode.AND)
    elif(op == '||'):
      self.add_instruction(OpCode.OR)
    else:
      raise Utils.UnknownOperator(op)


  # Visit a parse tree produced by ECMAScriptParser#futureReservedWord.
  def visitFutureReservedWord(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#initialiser.
  def visitInitialiser(self, ctx):
    ctx.children[1].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#statementList.
  def visitStatementList(self, ctx):
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#PropertyGetter.
  def visitPropertyGetter(self, ctx):
    func_code     = VirtualMachine.Code()
    bv = BytecodeVisitor(func_code)
    ctx.children[5].accept(bv)
    self.add_instruction(OpCode.PUSH, [])
    self.add_instruction(OpCode.PUSH, func_code)
    self.add_instruction(OpCode.MAKE_FUNC)
    self.add_instruction(OpCode.PUSH, ctx.children[1].accept(self))
    self.add_instruction(OpCode.MAKE_GETTER)


  # Visit a parse tree produced by ECMAScriptParser#block.
  def visitBlock(self, ctx):
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
  def visitExpressionStatement(self, ctx):
    self.visitChildren(ctx)
    self.add_instruction(OpCode.POP, 1)


  # Visit a parse tree produced by ECMAScriptParser#keyword.
  def visitKeyword(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  


  # Visit a parse tree produced by ECMAScriptParser#numericLiteral.
  def visitNumericLiteral(self, ctx):
    self.add_instruction(OpCode.PUSH, float(eval(ctx.children[0].symbol.text)))


  

  # Visit a parse tree produced by ECMAScriptParser#labelledStatement.
  def visitLabelledStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#PropertySetter.
  def visitPropertySetter(self, ctx):
    func_code     = VirtualMachine.Code()
    bv = BytecodeVisitor(func_code)
    ctx.children[6].accept(bv)
    self.add_instruction(OpCode.PUSH, [ctx.children[3].accept(self)])
    self.add_instruction(OpCode.PUSH, func_code)
    self.add_instruction(OpCode.MAKE_FUNC)
    self.add_instruction(OpCode.PUSH, ctx.children[1].accept(self))
    self.add_instruction(OpCode.MAKE_SETTER)


  

  # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
  def visitLiteralExpression(self, ctx):
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
  def visitArrayLiteralExpression(self, ctx):
    return ctx.children[0].accept(self)

  


  # Visit a parse tree produced by ECMAScriptParser#withStatement.
  def visitWithStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#MemberIndexExpression.
  def visitMemberIndexExpression(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#formalParameterList.
  def visitFormalParameterList(self, ctx):
    args = []
    for c in ctx.children:
      if(c.symbol.type == ECMAScriptParser.Lexer.Identifier):
        args.append(c.symbol.text)
    return args


  # Visit a parse tree produced by ECMAScriptParser#incrementOperator.
  def visitIncrementOperator(self, ctx):
    return ctx.children[0].symbol.text


  # Visit a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
  def visitAssignmentOperatorExpression(self, ctx):
    if(len(ctx.children) == 3):
      (variable_setter, variable_getter) = self.assignmentVariable(ctx.children, 0, self.AV_IDENTIFIER)
      operator = ctx.children[1]
      value    = ctx.children[2]
    elif(len(ctx.children) == 5):
      (variable_setter, variable_getter) = self.assignmentVariable(ctx.children, 0, self.AV_MEMBERDOT)
      operator = ctx.children[3]
      value    = ctx.children[4]
    elif(len(ctx.children) == 6):
      (variable_setter, variable_getter) = self.assignmentVariable(ctx.children, 0, self.AV_INDICE)
      operator = ctx.children[4]
      value    = ctx.children[5]
    else:
      raise Utils.UnimplementedVisitorException(ctx)

    operator = operator.accept(self)
    value.accept(self)
    if(operator == "="):
      variable_setter()
    elif(operator == "+="):
      variable_getter()
      self.add_instruction(OpCode.ADD)
      variable_setter()
    elif(operator == "-="):
      variable_getter()
      self.add_instruction(OpCode.SWAP)
      self.add_instruction(OpCode.SUB)
      variable_setter()
    elif(operator == "*="):
      variable_getter()
      self.add_instruction(OpCode.MUL)
      variable_setter()
    elif(operator == "/="):
      variable_getter()
      self.add_instruction(OpCode.SWAP)
      self.add_instruction(OpCode.DIV)
      variable_setter()
    else:
      raise Utils.UnknownOperator(operator)


  # Visit a parse tree produced by ECMAScriptParser#PostUnaryAssignmentExpression.
  def visitPostUnaryAssignmentExpression(self, ctx):
    if(len(ctx.children) == 2):
      (variable_setter, variable_getter) = self.assignmentVariable(ctx.children, 0, self.AV_IDENTIFIER)
      operator = ctx.children[1]
    elif(len(ctx.children) == 4):
      (variable_setter, variable_getter) = self.assignmentVariable(ctx.children, 0, self.AV_MEMBERDOT)
      operator = ctx.children[3]
    elif(len(ctx.children) == 5):
      (variable_setter, variable_getter) = self.assignmentVariable(ctx.children, 0, self.AV_INDICE)
      operator = ctx.children[4]
    else:
      raise Utils.UnimplementedVisitorException(ctx)
    
    operator = operator.accept(self)
    variable_getter()
    self.add_instruction(OpCode.DUP)
    self.add_instruction(OpCode.PUSH, 1)
    if(operator == "++"):
      self.add_instruction(OpCode.ADD)
    elif(operator == "--"):
      self.add_instruction(OpCode.SUB)
    else:
      raise Utils.UnimplementedVisitorException(ctx)
    variable_setter()
    self.add_instruction(OpCode.POP, 1)


  # Visit a parse tree produced by ECMAScriptParser#TernaryExpression.
  def visitTernaryExpression(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  # Visit a parse tree produced by ECMAScriptParser#debuggerStatement.
  def visitDebuggerStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
  def visitObjectLiteralExpression(self, ctx):
    ctx.children[0].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#arrayLiteral.
  def visitArrayLiteral(self, ctx):
    ctx.children[1].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#elision.
  def visitElision(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#statements.
  def visitStatements(self, ctx):
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#UnaryExpression.
  def visitUnaryExpression(self, ctx):
    op  = ctx.children[0].symbol.text
    ctx.children[1].accept(self)
    
    if(op == '-'):
      self.add_instruction(OpCode.NEG)
    elif(op == '+'):
      pass
    elif(op == '~'):
      self.add_instruction(OpCode.TILDE)
    elif(op == '!'):
      self.add_instruction(OpCode.NOT)
    else:
      raise Utils.UnknownOperator(op)



  # Visit a parse tree produced by ECMAScriptParser#expressionSequence.
  def visitExpressionSequence(self, ctx):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#literal.
  def visitLiteral(self, ctx):
    child = ctx.children[0]
    if(isinstance(child, antlr4.tree.Tree.TerminalNodeImpl)):
      if(child.symbol.text == 'true'):
        self.add_instruction(OpCode.PUSH, True)
      elif(child.symbol.text == 'false'):
        self.add_instruction(OpCode.PUSH, False)
      else:
        self.add_instruction(OpCode.PUSH, eval(child.symbol.text))
    else:
      child.accept(self)


  # Visit a parse tree produced by ECMAScriptParser#variableStatement.
  def visitVariableStatement(self, ctx):
    self.visitChildren(ctx)




  # Visit a parse tree produced by ECMAScriptParser#statement.
  def visitStatement(self, ctx):
    self.visitChildren(ctx)



  # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
  def visitParenthesizedExpression(self, ctx):
    ctx.children[1].accept(self)

  
  # Visit a parse tree produced by ECMAScriptParser#reservedWord.
  def visitReservedWord(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)
      
  

  # Visit a parse tree produced by ECMAScriptParser#finallyProduction.
  def visitFinallyProduction(self, ctx):
    ctx.children[1].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
  def visitIdentifierExpression(self, ctx):
    self.add_instruction(OpCode.LOAD, ctx.children[0].accept(self))


  # Visit a parse tree produced by ECMAScriptParser#propertyName.
  def visitPropertyName(self, ctx):
    child = ctx.children[0]
    
    if(isinstance(child, antlr4.tree.Tree.TerminalNodeImpl)):
      if(child.symbol.type == ECMAScriptParser.Lexer.StringLiteral):
        self.add_instruction(OpCode.PUSH, eval(child.symbol.text))
        return

    r = child.accept(self)
    if(r != None):
      self.add_instruction(OpCode.PUSH, r)
  


  # Visit a parse tree produced by ECMAScriptParser#arguments.
  def visitArguments(self, ctx):
    if(len(ctx.children) == 3):
      return ctx.children[1].accept(self)
    elif(len(ctx.children) == 2):
      return 0
    else:
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#variableDeclarationList.
  def visitVariableDeclarationList(self, ctx):
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#functionBody.
  def visitFunctionBody(self, ctx):
    ctx.children[0].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#eof.
  def visitEof(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#UnaryAssignmentExpression.
  def visitUnaryAssignmentExpression(self, ctx):
    operator = ctx.children[0]
    if(len(ctx.children) == 2):
      (variable_setter, variable_getter) = self.assignmentVariable(ctx.children, 1, self.AV_IDENTIFIER)
    elif(len(ctx.children) == 4):
      (variable_setter, variable_getter) = self.assignmentVariable(ctx.children, 1, self.AV_MEMBERDOT)
    elif(len(ctx.children) == 5):
      (variable_setter, variable_getter) = self.assignmentVariable(ctx.children, 1, self.AV_INDICE)
    else:
      raise Utils.UnimplementedVisitorException(ctx)
    
    operator = operator.accept(self)
    variable_getter()
    if(operator == "++"):
      self.add_instruction(OpCode.PUSH, 1)
      self.add_instruction(OpCode.ADD)
    elif(operator == "--"):
      self.add_instruction(OpCode.PUSH, 1)
      self.add_instruction(OpCode.SUB)
    else:
      raise Utils.UnimplementedVisitorException(ctx)
    variable_setter()
