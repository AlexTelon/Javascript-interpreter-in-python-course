#Generated from java-escape by ANTLR 4.4
import antlr4
import Utils

from VirtualMachine.OpCode      import OpCode
from VirtualMachine.Code        import Code
from VirtualMachine.Instruction import Instruction
from VirtualMachine.Stack       import Stack

from ECMAScriptParser import ECMAScriptVisitor

from Interpreter.Console import Console
from Interpreter.Math import MathModule
from Interpreter.Environment import Environment
from Interpreter.Function import Function
from Interpreter.Object import Object, ObjectModule
from Interpreter.Property import Property


def printCtx(ctx, level=14, tab="", path="ctx"):
    if 1==1:
        print(tab,"list of ", ctx.getChildCount(), "")
        num = -1;
        if (ctx.children != None):
            for c in ctx.children:
                num = num + 1
                path_ = path + " " + str(num) +" -"# ".children[" + str(num) + "]"
                if(isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)):
                    print(tab, path_, " is         ", c.symbol.text)
                else:
                    print(tab, path_, " is list ->")
                    if (level > 0):
                        printCtx(c, level-1, tab + "   ", path_)
                    else:
                        print(tab, "children: ", c)
        print("")
            

def sPrintCtx(ctx):
    num = -1;
    if (ctx.children != None):
            for c in ctx.children:
                num = num + 1
                path_ = "ctx.children[" + str(num) + "]"
                if(isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)):
                    print(path_, " is ", c.symbol.text)
                else:
                    print(path_, " is ", c)
    print("")

def dprint(*string):
    if 1==1:
        for s in string:
            print(s, end="")
            print(" ", end="")
        print("")

# def console(value):
#     print(value)

# This class defines a complete generic visitor for a parse tree produced by ECMAScriptParser.
class BytecodeVisitor(ECMAScriptVisitor):
  def __init__(self, program):
    self.program    = program
    self.lineno = 0
  def add_instruction(self, opcode, *arguments):
    inst = Instruction(opcode, *arguments)
    dprint("add_instruction:", self.lineno, ":", opcode, arguments)
    self.lineno = self.lineno + 1
    self.program.add_instruction(inst)
    return inst

  AV_IDENTIFIER = 0
  AV_MEMBERDOT  = 1
  AV_INDICE     = 2
  
  
  def visitTerminal(self, node):
      txt = "visitTerminal " + node.symbol.text
      dprint(txt)
      return node.symbol.text

  
  # Visit a parse tree produced by ECMAScriptParser#ArgumentsExpression.
  def visitArgumentsExpression(self, ctx):
    dprint("visitArugmentsExpression")
    #printCtx(ctx)
    #ordering is important!
    #many accepts do stuff on the stack for you!
    args = ctx.children[1].accept(self)
    #print("args argumentsExpression: ", args)

    func = ctx.children[0].accept(self)
    #print("func argumentsExpression: ", func)

    if args is None:
      args = []
        
    self.add_instruction(OpCode.CALL, args)
     
  
  # Visit a parse tree produced by ECMAScriptParser#elementList.
  def visitElementList(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)
  
  # Visit a parse tree produced by ECMAScriptParser#ForInStatement.
  def visitForInStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#emptyStatement.
  def visitEmptyStatement(self, ctx):
      dprint("visitEmptyStatement")
      pass

  # Visit a parse tree produced by ECMAScriptParser#NewExpression.
  def visitNewExpression(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  # Visit a parse tree produced by ECMAScriptParser#MemberDotExpression.
  def visitMemberDotExpression(self, ctx):
      dprint("visitMemberDotExpression")
      #printCtx(ctx)
      obj    = ctx.children[0].accept(self)
      #print("obj: ", obj)

      member = ctx.children[2].accept(self)
      #print("member: ", member)
      
      # on top of stack we have obj
      self.add_instruction(OpCode.LOAD_MEMBER, member)
      
    # Visit a parse tree produced by ECMAScriptParser#tryStatement.
  def visitTryStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  # Visit a parse tree produced by ECMAScriptParser#DoStatement.
  def visitDoStatement(self, ctx):
      dprint("visitDoStatement")
      printCtx(ctx)
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
      dprint("visitIfStatement")
      
      ctx.children[2].accept(self) # True/False value pused to stack 
      placeHolderIFPosition = self.program.current_index()
      self.add_instruction(OpCode.UNLESSJMP, 1337)
      ctx.children[4].accept(self)

      #if we have an else statement we need to jump over it
      if ctx.getChildCount() >= 7:
           placeHolderELSEPosition = self.program.current_index()
           self.add_instruction(OpCode.JMP, 1337)

      #make sure the IFJUMP jumps over the if-true part of the statements
      afterIF = self.program.current_index()
      self.program.instructions[placeHolderIFPosition] = Instruction(OpCode.UNLESSJMP, afterIF)

      if (ctx.getChildCount() >= 7):
          ctx.children[6].accept(self)
          #change the jump in the if-statement to jump over the else part
          afterELSE = self.program.current_index()
          self.program.instructions[placeHolderELSEPosition] = Instruction(OpCode.JMP, afterELSE)


  # Visit a parse tree produced by ECMAScriptParser#variableDeclaration.
  def visitVariableDeclaration(self, ctx):
      dprint("visitVariableDeclaration")
      printCtx(ctx)

      if (ctx.getChildCount() == 1):
          varname = ctx.children[0].accept(self)
          self.add_instruction(OpCode.DCL, varname)
          
      else:
          varname = ctx.children[0].accept(self)
          ctx.children[1].accept(self)
          self.add_instruction(OpCode.STORE, varname)

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
    dprint("gen_setter, 3 args")

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
    dprint("gen_getter, 2 args")
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
    dprint("gen_stter_dot")
    a.accept(self)
    self.add_instruction(OpCode.STORE_MEMBER, idx)
    
  def gen_getter_dot(self, a, idx):
    dprint("gen_getter_dot")
    a.accept(self)
    self.add_instruction(OpCode.LOAD_MEMBER, idx)
    
  def gen_setter_indice(self, a, idx):
    dprint("gen_setter_indice")
    a.accept(self)
    idx.accept(self)
    self.add_instruction(OpCode.STORE_INDEX)
    
  def gen_getter_indice(self, a, idx):
    dprint("gen_getter_indice")
    a.accept(self)
    idx.accept(self)
    self.add_instruction(OpCode.LOAD_INDEX)
    
  def assignmentVariable(self, array, index, typ):
    dprint("assignmentVariable")
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
    dprint("visitPropertyExpressionAssignment")
    ctx.children[2].accept(self)
    name = ctx.children[0].accept(self)
    if(name != None):
      self.add_instruction(OpCode.PUSH, name)


  # Visit a parse tree produced by ECMAScriptParser#assignmentOperator.
  def visitAssignmentOperator(self, ctx):
    dprint("visitAssignmentOperator")
    return ctx.children[0].symbol.text


  # Visit a parse tree produced by ECMAScriptParser#eos.
  def visitEos(self, ctx):
    dprint("visitEos")
    pass


  # Visit a parse tree produced by ECMAScriptParser#program.
  def visitProgram(self, ctx):
    dprint("visitProgram")
    args = []
    for c in ctx.children:
      if(not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)): # Skip ","
        args.append(c.accept(self))
    return args


  # Visit a parse tree produced by ECMAScriptParser#argumentList.
  def visitArgumentList(self, ctx):
    dprint("visitArgumentList")
    count = 0
    for c in ctx.children:
      if(not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)): # Skip ","
        c.accept(self)
        count += 1
    return count


 


  # Visit a parse tree produced by ECMAScriptParser#ThisExpression.
  def visitThisExpression(self, ctx):
    dprint("visitThisExpression")
    self.add_instruction(OpCode.LOAD, "this")


  # Visit a parse tree produced by ECMAScriptParser#identifierName.  
  def visitIdentifierName(self, ctx):
    dprint("visitIdentifierName")
    #printCtx(ctx)
    return ctx.children[0].accept(self)
    


  # Visit a parse tree produced by ECMAScriptParser#BinaryExpression.
  def visitBinaryExpression(self, ctx):
    dprint("visitBinaryExpression")
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
    dprint("visitInitialiser")
    ctx.children[1].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#statementList.
  def visitStatementList(self, ctx):
    dprint("visitStatementList")
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#PropertyGetter.
  def visitPropertyGetter(self, ctx):
    dprint("visitPropertyGetter")
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
    dprint("visitBlock")
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
  def visitExpressionStatement(self, ctx):
    dprint("visitExpressionStatement")
    self.visitChildren(ctx)
    self.add_instruction(OpCode.POP, 1)


  # Visit a parse tree produced by ECMAScriptParser#keyword.
  def visitKeyword(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)

  
  # Visit a parse tree produced by ECMAScriptParser#numericLiteral.
  def visitNumericLiteral(self, ctx):
    txt = "visitNumericLiteral " + str(float(eval(ctx.children[0].symbol.text)))
    dprint(txt)
    self.add_instruction(OpCode.PUSH, float(eval(ctx.children[0].symbol.text)))
  

  # Visit a parse tree produced by ECMAScriptParser#labelledStatement.
  def visitLabelledStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#PropertySetter.
  def visitPropertySetter(self, ctx):
    dprint("visitPropertySetter")
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
    dprint("visitLiteralExpression")
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
  def visitArrayLiteralExpression(self, ctx):
    dprint("visitArrayLiteralExpression")
    return ctx.children[0].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#withStatement.
  def visitWithStatement(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#MemberIndexExpression.
  def visitMemberIndexExpression(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#formalParameterList.
  def visitFormalParameterList(self, ctx):
    dprint("visitFormalParameterList")
    args = []
    for c in ctx.children:
      if(c.symbol.type == ECMAScriptParser.Lexer.Identifier):
        args.append(c.symbol.text)
    return args


  # Visit a parse tree produced by ECMAScriptParser#incrementOperator.
  def visitIncrementOperator(self, ctx):
    dprint("visitIncrementOperator")
    return ctx.children[0].symbol.text


  # Visit a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
  def visitAssignmentOperatorExpression(self, ctx):
    dprint("visitAssignmentOperatorExpression")
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
    dprint("visitPostUnaryAssignmentExpression")
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
    dprint("visitObjectLiteralExpression")
    ctx.children[0].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#arrayLiteral.
  def visitArrayLiteral(self, ctx):
    dprint("visitArrayLiteral")
    ctx.children[1].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#elision.
  def visitElision(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#statements.
  def visitStatements(self, ctx):
    dprint("visitStatements")
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#UnaryExpression.
  def visitUnaryExpression(self, ctx):
    dprint("visitUnaryExpression")
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
    dprint("visitExpressionSequence")
    return self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#literal.
  def visitLiteral(self, ctx):
    dprint("visitLiteral")
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
    dprint("visitVariableStatement")
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#statement.
  def visitStatement(self, ctx):
    dprint("visitStatement")
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
  def visitParenthesizedExpression(self, ctx):
    dprint("visitParenthesizedExpression")
    ctx.children[1].accept(self)

  
  # Visit a parse tree produced by ECMAScriptParser#reservedWord.
  def visitReservedWord(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)
      
  

  # Visit a parse tree produced by ECMAScriptParser#finallyProduction.
  def visitFinallyProduction(self, ctx):
    dprint("visitFinallyProduction")
    ctx.children[1].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
  def visitIdentifierExpression(self, ctx):
    dprint("visitIdentifierExpression")
    self.add_instruction(OpCode.LOAD, ctx.children[0].accept(self))


  # Visit a parse tree produced by ECMAScriptParser#propertyName.
  def visitPropertyName(self, ctx):
    dprint("visitPropertyName")
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
    dprint("visitArguments")
    if(len(ctx.children) == 3):
      return ctx.children[1].accept(self)
    elif(len(ctx.children) == 2):
      return 0
    else:
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#variableDeclarationList.
  def visitVariableDeclarationList(self, ctx):
    dprint("visitVariableDeclarationList")
    self.visitChildren(ctx)


  # Visit a parse tree produced by ECMAScriptParser#functionBody.
  def visitFunctionBody(self, ctx):
    dprint("visitFunctionBody")
    ctx.children[0].accept(self)


  # Visit a parse tree produced by ECMAScriptParser#eof.
  def visitEof(self, ctx):
      raise Utils.UnimplementedVisitorException(ctx)


  # Visit a parse tree produced by ECMAScriptParser#UnaryAssignmentExpression.
  def visitUnaryAssignmentExpression(self, ctx):
    dprint("visitUnaryAssignmentExpression")
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
