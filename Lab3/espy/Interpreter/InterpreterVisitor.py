import antlr4
import Utils
from Interpreter.ControlExceptions import BreakException, ContinueException, ReturnException

from ECMAScriptParser import ECMAScriptVisitor

from Interpreter.Console import Console
from Interpreter.Math import MathModule
from Interpreter.Environment import Environment
from Interpreter.Object import Object, ObjectModule

def printCtx(ctx, level=4, tab="", path="ctx"):
    if (True):
        #print(tab, "Entering ctx")
        print(tab,"list with of ", ctx.getChildCount(), " elements")
        num = -1;
        if (ctx.children != None):
            for c in ctx.children:
                num = num + 1
                path_ = path + ".children[" + str(num) + "]"
                if(isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)):
                    print(tab, path_, " is ", c.symbol.text)
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
    


class InterpreterVisitor(ECMAScriptVisitor):

    def __init__(self, environment = Environment(), input=None):
      self.environment = environment
      self.environment.defineVariable("console", Console())
      self.environment.defineVariable("Math", MathModule())
      self.environment.defineVariable("Object", ObjectModule())

    def visitTerminal(self, node):
        #        print("Test in visitTerminal: ", node.symbol.text);
        return node.symbol.text

    # Visit a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx):
        return ctx.children[0].symbol.type


    # Visit a parse tree produced by ECMAScriptParser#eos.
    def visitEos(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#program.
    def visitProgram(self, ctx):
        self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#argumentList.
    def visitArgumentList(self, ctx):
      args = []
      for c in ctx.children:
        if(not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)): # Skip ","
          args.append(c.accept(self))
        return args


    # Visit a parse tree produced by ECMAScriptParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx):
        func = ctx.children[0].accept(self)
        args = ctx.children[1].accept(self)
        if(args == None): args = []
        return func(None, *args)


    # Visit a parse tree produced by ECMAScriptParser#ThisExpression.
    def visitThisExpression(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#identifierName.
    def visitIdentifierName(self, ctx):
        return ctx.children[0].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#BinaryExpression.
    def visitBinaryExpression(self, ctx):
        # numeric returns
        if(ctx.children[1].symbol.type == 17): # +
            return ctx.children[0].accept(self) + ctx.children[2].accept(self) + 0.0
        if(ctx.children[1].symbol.type == 18): # -
            return ctx.children[0].accept(self) - ctx.children[2].accept(self) + 0.0
        if(ctx.children[1].symbol.type == 21): # *
            return ctx.children[0].accept(self) * ctx.children[2].accept(self) + 0.0
        if(ctx.children[1].symbol.type == 22): # /
            # divide by 0?
            return ctx.children[0].accept(self) / ctx.children[2].accept(self) + 0.0
        if(ctx.children[1].symbol.type == 23): # *
            return ctx.children[0].accept(self) % ctx.children[2].accept(self) + 0.0

        # boolean returns
        # TODO - ask if stuff will crash if we dont check for types in === and such
        if(ctx.children[1].symbol.type == 24): # >>
            return float(int(ctx.children[0].accept(self)) >> int(ctx.children[2].accept(self)))
        if(ctx.children[1].symbol.type == 25): # <<
            return float(int(ctx.children[0].accept(self)) << int(ctx.children[2].accept(self)))
        if(ctx.children[1].symbol.type == 26): # >>>
            val = int(ctx.children[0].accept(self))
            n = int(ctx.children[2].accept(self))
            return float(val>>n if val >= 0 else (val+0x100000000)>>n)

        if(ctx.children[1].symbol.type == 27): # <
            return ctx.children[0].accept(self) < ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 28): # >
            return ctx.children[0].accept(self) > ctx.children[2].accept(self)

        if(ctx.children[1].symbol.type == 29): # <=
            return ctx.children[0].accept(self) <= ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 30): # >=
            return ctx.children[0].accept(self) >= ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 33 or ctx.children[1].symbol.type == 31): # === or ==
            return ctx.children[0].accept(self) == ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 34 or ctx.children[1].symbol.type == 32 ): # !== or !=
            return ctx.children[0].accept(self) != ctx.children[2].accept(self)



        if(ctx.children[1].symbol.type == 35): # &
            return ctx.children[0].accept(self) & ctx.children[2].accept(self) + 0.0
        if(ctx.children[1].symbol.type == 36): # ^
            return ctx.children[0].accept(self) ^ ctx.children[2].accept(self) + 0.0
        if(ctx.children[1].symbol.type == 37): # |
            return ctx.children[0].accept(self) | ctx.children[2].accept(self) + 0.0
        if(ctx.children[1].symbol.type == 38): # &&
            return ctx.children[0].accept(self) and ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 39): # ||
            return ctx.children[0].accept(self) or ctx.children[2].accept(self)


        # TODO ADD MORE LATER


    # Visit a parse tree produced by ECMAScriptParser#futureReservedWord.
    def visitFutureReservedWord(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#initialiser.
    def visitInitialiser(self, ctx):
        # a = 10 (I think)
        #print("initialiser skipping", ctx.children[0].symbol.text)
        return ctx.children[1].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#statementList.
    def visitStatementList(self, ctx):
        # a bunch of statements with ; between like:
        # var a = 10;
        # var b = 20; and so on...
        args = []
        for c in ctx.children:
            if(not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)): # Skip ","
                args.append(c.accept(self))
        return args


    # Visit a parse tree produced by ECMAScriptParser#PropertyGetter.
    def visitPropertyGetter(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#block.
    def visitBlock(self, ctx):
        # { stuff }, so ignore children[0] and children[2]
        return ctx.children[1].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx):
      self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#keyword.
    def visitKeyword(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#elementList.
    def visitElementList(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx):
        if(isinstance(ctx.children[0], antlr4.tree.Tree.TerminalNodeImpl)): # Skip ","
            if(ctx.children[0].symbol.type == 56):
                return float(eval(ctx.children[0].symbol.text))
            if(ctx.children[0].symbol.type == 57):
                return float(eval(ctx.children[0].symbol.text))
            if(ctx.children[0].symbol.type == 55):
                return float(eval(ctx.children[0].symbol.text))

        return ctx.children[0].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#ForInStatement.
    def visitForInStatement(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx):
        pass

    # Visit a parse tree produced by ECMAScriptParser#labelledStatement.
    def visitLabelledStatement(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#PropertySetter.
    def visitPropertySetter(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#NewExpression.
    def visitNewExpression(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx):
      obj    = ctx.children[0].accept(self)
      member = ctx.children[2].accept(self)
      return getattr(obj, member)


    # Visit a parse tree produced by ECMAScriptParser#withStatement.
    def visitWithStatement(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#incrementOperator.
    def visitIncrementOperator(self, ctx):
        return ctx.children[0].symbol.type

    # Visit a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx):
        #print("AssignmentOperatorExpression")
        # a = 1 for example, where = and 1 are lists
        type = ctx.children[1].accept(self)
        name = ctx.children[0].accept(self)
        value = ctx.children[2].accept(self)
        oldVal = self.environment.value(name)
        
        if(type == 11): # =
            self.environment.setVariable(name, value)
            # JavaScript returns the value of an assignment
            return value
        if(type == 43): # +=
            newVal = oldVal+value
            self.environment.setVariable(name, newVal)
            return newVal
        if(type == 44): # -=
            newVal = oldVal-value
            self.environment.setVariable(name, newVal)
            return newVal
        if(type == 40): # *=
            newVal = oldVal*value
            self.environment.setVariable(name, newVal)
            return newVal
        if(type == 41): # /=
            newVal = oldVal/value
            self.environment.setVariable(name, newVal)
            return newVal
            
            


    # Visit a parse tree produced by ECMAScriptParser#PostUnaryAssignmentExpression.
    def visitPostUnaryAssignmentExpression(self, ctx):
        #name first
        name = ctx.children[0].symbol.text
        value = self.environment.value(name)
        type = ctx.children[1].accept(self);
        if(type == 15): # ++
            self.environment.setVariable(name, value+1)
            return value;
        if(type == 16): # --
            self.environment.setVariable(name, value-1)
            return value;

    # Visit a parse tree produced by ECMAScriptParser#TernaryExpression.
    def visitTernaryExpression(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#tryStatement.
    def visitTryStatement(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#DoStatement.
    def visitDoStatement(self, ctx):
        #printCtx(ctx)
        # [0] = do, [1] = block, [2] = while, [3] = (, [4] = condition, [5] = )
        ctx.children[1].accept(self)

        while ctx.children[4].accept(self):
            ctx.children[1].accept(self)

        


    # Visit a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#arrayLiteral.
    def visitArrayLiteral(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#elision.
    def visitElision(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#statements.
    def visitStatements(self, ctx):
        self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#UnaryExpression.
    def visitUnaryExpression(self, ctx):
        if(ctx.children[0].symbol.type == 18): # -
            return -ctx.children[1].accept(self)
        if(ctx.children[0].symbol.type == 17): # +
            return ctx.children[1].accept(self)
        if(ctx.children[0].symbol.type == 19): # ~
            #print("hest")
            #return "felfelfel"
            return float(~int(ctx.children[1].accept(self)))
        if(ctx.children[0].symbol.type == 20): # !
            return not(ctx.children[1].accept(self))

    # Visit a parse tree produced by ECMAScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx):
        # [0] = while, (, condition, ), [4] = block

        while ctx.children[2].accept(self):
            try:
                ctx.children[4].accept(self)
            except BreakException:
                break
            except ContinueException:
                continue


    # Visit a parse tree produced by ECMAScriptParser#returnStatement.
    def visitReturnStatement(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#switchStatement.
    def visitSwitchStatement(self, ctx):
        sPrintCtx(ctx)
        raise Utils.UnimplementedVisitorException(ctx)

    # Visit a parse tree produced by ECMAScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#literal.
    def visitLiteral(self, ctx):
        child = ctx.children[0]
        if(isinstance(ctx.children[0], antlr4.tree.Tree.TerminalNodeImpl)):
            #            print("value: ", ctx.children[0].symbol.text)
            #print("type of child:", child.symbol.type)
            if(child.symbol.text == "true"):
                return True
            if(child.symbol.text == "false"):
                return False
            if(child.symbol.type == 101):
                tmp = child.symbol.text[1:-1]
                return tmp
            if(child.symbol.type == 53):
                return None
            # TODO - fix for regularExpressionLiteral=1
        return child.accept(self)


    # Visit a parse tree produced by ECMAScriptParser#variableStatement.
    def visitVariableStatement(self, ctx):
        # var a = 10; for example
        # ctx.children[0] is var
        # ctx.children[1] is a = 10
        # ctx.children[2] is ;
        return ctx.children[1].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#defaultClause.
    def visitDefaultClause(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#statement.
    def visitStatement(self, ctx):
      self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForStatement.
    def visitForStatement(self, ctx):
        #printCtx(ctx)
        #sPrintCtx(ctx)
        # [0] = for, [1] = (, [2] = assignment/starting value, [3] = ;, 
        # [4] = end condition, [5] = ; , [6] = change of var or whatever
        # [7] = ), [8] = block
        # The above is if the for loop is full, it could be for (;;) {...}
        # as well, so the code below is made to make sure it works no matter what
        child = 2
        
        if ctx.children[child].accept(self) == "var":
            child = child + 1
        if ctx.children[child].accept(self) != ";":
            child = child + 1
        child = child + 1

        condition = ctx.children[child].accept(self)
        if condition == ";":
            condition = True
        else: # if condition is valid, we want to save the "pointer" to it
            condition = ctx.children[child]
            child = child + 1
        child = child + 1

        if isinstance(ctx.children[child], antlr4.tree.Tree.TerminalNodeImpl):
            varChange = None
            child = child + 1
        else:
            # "pointer"
            varChange = ctx.children[child]
            child = child + 2
            

        #saving the "pointer" to the block
        block = ctx.children[child]
        if condition == True:
            while True:
                try:
                    block.accept(self)
                except BreakException:
                    break
                except ContinueException:
                    pass
                varChange.accept(self)                    
        else:
            while condition.accept(self):
                try:
                    block.accept(self)
                except BreakException:
                    break
                except ContinueException:
                    pass
                varChange.accept(self)                    



    # Visit a parse tree produced by ECMAScriptParser#caseBlock.
    def visitCaseBlock(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx):
        # the syntax is: ( thing ), so do accept on the thing
        return ctx.children[1].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#objectLiteral.
    def visitObjectLiteral(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#throwStatement.
    def visitThrowStatement(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#breakStatement.
    def visitBreakStatement(self, ctx):
        raise BreakException()


    # Visit a parse tree produced by ECMAScriptParser#ifStatement.
    def visitIfStatement(self, ctx):
        # ctx.children[0] = "if", ctx.children[1] = "(", ctx.children[3] = ")", ctx.children[4] = stuff to run
        #if there is an else it is in [5] and what is to be run in [6]
        if ctx.children[2].accept(self):
            return ctx.children[4].accept(self)
        if ctx.getChildCount() >= 7:
            return ctx.children[6].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#reservedWord.
    def visitReservedWord(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx):
        #print("visitVariableDeclaration, skipping ", ctx.children[0].symbol.text)
        if (ctx.getChildCount() == 1):
            self.environment.defineVariable(ctx.children[0].symbol.text)
        else:
            # dont retun the value since JavaScript does not return in this case
            self.environment.defineVariable(ctx.children[0].symbol.text, ctx.children[1].accept(self))


    # Visit a parse tree produced by ECMAScriptParser#finallyProduction.
    def visitFinallyProduction(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx):
      return self.environment.value(ctx.children[0].accept(self))


    # Visit a parse tree produced by ECMAScriptParser#propertyName.
    def visitPropertyName(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#catchProduction.
    def visitCatchProduction(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#continueStatement.
    def visitContinueStatement(self, ctx):
        raise ContinueException()


    # Visit a parse tree produced by ECMAScriptParser#caseClause.
    def visitCaseClause(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#arguments.
    def visitArguments(self, ctx):
      return ctx.children[1].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx):
        #print("variableDeclarationList: ")
        # stuff like a = 10, b = 20
        #        printCtx(ctx)
        for c in ctx.children:
            if(not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)): # Skip ","
                #print("variableDeclartionList")
                c.accept(self)
                #raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#functionBody.
    def visitFunctionBody(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#eof.
    def visitEof(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#UnaryAssignmentExpression.
    def visitUnaryAssignmentExpression(self, ctx):
        #operator first
        name = ctx.children[1].symbol.text
        value = self.environment.value(name)
        type = ctx.children[0].accept(self);
        if(type == 15): # ++
            value = value + 1
            self.environment.setVariable(name, value)
            return value;
        if(type == 16): # --
            value = value - 1
            self.environment.setVariable(name, value)
            return value;
