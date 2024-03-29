import antlr4
import Utils
from Interpreter.ControlExceptions import BreakException, ContinueException, ReturnException, ThrowException

from ECMAScriptParser import ECMAScriptVisitor

from Interpreter.Console import Console
from Interpreter.Math import MathModule
from Interpreter.Environment import Environment
from Interpreter.Function import Function
from Interpreter.Object import Object, ObjectModule
from Interpreter.Property import Property

def printCtx(ctx, level=14, tab="", path="ctx"):
    if False:
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

def dprint(string):
    if False:
        print(string)
    
class InterpreterVisitor(ECMAScriptVisitor):

    def __init__(self, environment = Environment(), input=None):
      self.environment = environment
      self.environment.defineVariable("console", Console())
      self.environment.defineVariable("Math", MathModule())
      self.environment.defineVariable("Object", ObjectModule())

    def visitTerminal(self, node):
        return node.symbol.text

    # Visit a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx):
        dprint("visitPropertyExpressionAssignment")
        #printCtx(ctx,3)
        #tmp = [ctx.children[0].accept(self), ctx.children[2].accept(self)]
        name = ctx.children[0].accept(self)
        #print("NameIs: ", name)
        if isinstance(name, str) and name[0] == "\"":
            name = name[1:-1]
        tmp = {"name": name, "value": ctx.children[2].accept(self), "function": False, "setter": False}
        return tmp


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
        dprint("VisitArgumentList")
        args = []
        for c in ctx.children:
            if(not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)): # Skip ","
                args.append(c.accept(self))
        #print("Visit ArgumentList args: ", args)
        return args


    # Visit a parse tree produced by ECMAScriptParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx):
        dprint("visitArgumentsExpression")
        printCtx(ctx)
        func = ctx.children[0].accept(self)
        #print("func argumentsExpression: ", func)
        args = ctx.children[1].accept(self)
        #print("args argumentsExpression: ", args)
        this = ctx.children[0].children[0].accept(self)
        #print("this argumentsExpression: ", this)

        if args is None:
            args = []
        
        if hasattr(func, "__name__") and func.__name__ == "append":
            this.append(*args)
            return args[0]
        return func(this, *args)


    # Visit a parse tree produced by ECMAScriptParser#ThisExpression.
    def visitThisExpression(self, ctx):
        dprint("visitThisExpression")
        return self.environment.value("this")


    # Visit a parse tree produced by ECMAScriptParser#identifierName.
    def visitIdentifierName(self, ctx):
        return ctx.children[0].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#BinaryExpression.
    def visitBinaryExpression(self, ctx):
        # numeric returns
        if(ctx.children[1].symbol.type == 17): # +
            return ctx.children[0].accept(self) + ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 18): # -
            return ctx.children[0].accept(self) - ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 21): # *
            return ctx.children[0].accept(self) * ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 22): # /
            # divide by 0?
            return ctx.children[0].accept(self) / ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 23): # *
            return ctx.children[0].accept(self) % ctx.children[2].accept(self)

        # boolean returns
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
            return ctx.children[0].accept(self) & ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 36): # ^
            return ctx.children[0].accept(self) ^ ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 37): # |
            return ctx.children[0].accept(self) | ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 38): # &&
            return ctx.children[0].accept(self) and ctx.children[2].accept(self)
        if(ctx.children[1].symbol.type == 39): # ||
            return ctx.children[0].accept(self) or ctx.children[2].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#futureReservedWord.
    def visitFutureReservedWord(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#initialiser.
    def visitInitialiser(self, ctx):
        #  = stuff 
        dprint("VisitInitialiser")
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
        dprint("visitPropertyGetter")
        name = ctx.children[1].accept(self)
        body = ctx.children[5]
        def runBodyFunction(env):
            origEnv = self.environment
            self.environment = env
            retVal = body.accept(self)
            self.environment = origEnv
            return retVal

        retFunc =  Function(None, self.environment, runBodyFunction)
        tmp = {"name": name, "value": retFunc, "function" : True, "setter": False}
        return tmp


    # Visit a parse tree produced by ECMAScriptParser#block.
    def visitBlock(self, ctx):
        # { stuff }, so ignore children[0] and children[2]
        return ctx.children[1].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx):
        dprint("visitExpressionStatement")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#keyword.
    def visitKeyword(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#elementList.
    def visitElementList(self, ctx):
        array = []
        i = 0
        for child in ctx.children:
            value = child.accept(self)
            if not value == ",":
                array.append(child.accept(self))
            i = i + 1
        return array


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
        dprint("visitPropertySetter")
        name = ctx.children[1].accept(self)
        params = ctx.children[3].accept(self)
        body = ctx.children[6]

        def runBodyFunction(env):
            origEnv = self.environment
            self.environment = env
            retVal = body.accept(self)
            self.environment = origEnv
            return retVal

        retFunc =  Function([params], self.environment, runBodyFunction)
        tmp = {"name": name, "value": retFunc, "function": True, "setter": True}
        return tmp
        
    # Visit a parse tree produced by ECMAScriptParser#NewExpression.
    def visitNewExpression(self, ctx):
        dprint("visitNewExpression")
        this = ObjectModule()

        func = ctx.children[1].accept(self) #Object
        if hasattr(func, "prototype"):
            prototype = getattr(func, "prototype")
            for attr in dir(prototype):
                val = getattr(prototype, attr)
                if( not attr.startswith("__") and not attr == "prototype"):
                    if(isinstance(val, tuple)):
                        val = list(val)
                        val[0] = this
                        val = (val[0], val[1])
                    setattr(this, attr, val)
        parameters = ctx.children[2].accept(self) #()

        if parameters != None:
            func(this, *parameters)
        return this

    # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx):
        return ctx.children[0].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx):
        dprint("visitMemberDotExpression")
        obj    = ctx.children[0].accept(self)
        member = ctx.children[2].accept(self)

        if member == "length":
            return float(len(obj))

        if member == "prototype":
            if not hasattr(obj, "prototype"):
                # We want to save the prototype thing somehow
                # Either we create .nantionality here and now to person
                # or to a new prototype object.
                # if we save to prototype we need to always check in both person
                # and person.prototype for properies which can be bad
                # this  function and visitAssignmentOperatorExpression is key to this problem
                # maybe also the place where we create functions, so we can create prototype for all
                # functions at creation just like JS does for real anyways.
                newObj = ObjectModule();
                setattr(obj, "prototype", newObj)
                return newObj
        getSetObj = getattr(obj, member)
        if isinstance(getSetObj, ObjectModule):
            if hasattr(getSetObj, "get"):
                getter = getattr(getSetObj, "get")
                ret = getter(ctx.children[0].accept(self))
                return ret

        return getattr(obj, member)


    # Visit a parse tree produced by ECMAScriptParser#withStatement.
    def visitWithStatement(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)


    # Visit a parse tree produced by ECMAScriptParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx):
        # Should return a[1], a value from array
        # a [ list ]

        #dprint("visitMemberIndexExpression")
        name = ctx.children[0].accept(self)
        index = ctx.children[2].accept(self)
        
        if isinstance(name,ObjectModule):
            if isinstance(index, str):
                return getattr(name, index)
            else:
                return getattr(name, "int_"+str(int(index)))

        return name[int(index)]
        

    # Visit a parse tree produced by ECMAScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx):
        #print("visitFormalParameterList")
        #sPrintCtx(ctx)
        array = []
        i = 0
        for child in ctx.children:
            value = child.accept(self)
            if not value == ",":
                array.append(child.accept(self))
            i = i + 1
        return array



    # Visit a parse tree produced by ECMAScriptParser#incrementOperator.
    def visitIncrementOperator(self, ctx):
        return ctx.children[0].symbol.type

    # Visit a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx):
        # a = 1 for example, where = and 1 are lists
        dprint("visitAssignmentOperatorExpression")
        if ctx.getChildCount() == 3: # a = 3
            type = ctx.children[1].accept(self)
            name = ctx.children[0].accept(self)
            value = ctx.children[2].accept(self)
            oldVal = self.environment.value(name)
        elif ctx.getChildCount() == 6: # a[1] = 3
            name = ctx.children[0].accept(self) # a
            type = ctx.children[4].accept(self) # =
            index = ctx.children[2].accept(self) # 1
            value = ctx.children[5].accept(self) 

            # if assignment then we dont need keep track of old values
            # also an old value might not exist
            if type != 11:
                if isinstance(name,ObjectModule):
                    if isinstance(index, str):
                        oldVal = getattr(name, index)
                    else:
                        oldVal = getattr(name, "int_"+str(int(index)))
                else:
                    oldVal = name[int(index)]
        elif ctx.getChildCount() == 5: # a.b = 3
            type = ctx.children[3].accept(self) # =
            obj = ctx.children[0].accept(self) # a
            value = ctx.children[4].accept(self) # 3
            member = ctx.children[2].accept(self) # b

            # if assignment then we dont need keep track of old values
            # also an old value might not exist
            if type != 11:
                oldVal = getattr(obj, member)
        else:
            raise Utils.UnimplementedVisitorException(ctx)

        # JavaScript returns the value of an assignment
        if(type == 11): # =
            newVal = value
        if(type == 43): # +=
            newVal = oldVal+value
        if(type == 44): # -=
            newVal = oldVal-value
        if(type == 40): # *=
            newVal = oldVal*value
        if(type == 41): # /=
            newVal = oldVal/value

        if ctx.getChildCount() == 3:
            self.environment.setVariable(name, newVal)            
            return newVal
        elif ctx.getChildCount() == 6:
            if isinstance(name,ObjectModule):
                if isinstance(index, str):
                    setattr(name, index, newVal)
                else:
                    setattr(name, "int_"+str(int(index)), newVal)
            else:
                name[int(index)] = newVal
            return newVal
        elif ctx.getChildCount() == 5:

            # this is done to get setter from object, cannot get it directly from ctx 
            if hasattr(obj, member):
                getSetObj = getattr(obj, member)
                if hasattr(getSetObj, "set"):
                    member = getSetObj
                    setter = getattr(member, "set")
                    this = obj
                    ret = setter(this, newVal)
                    return ret

            setattr(obj, member, newVal)


    # Visit a parse tree produced by ECMAScriptParser#PostUnaryAssignmentExpression.
    def visitPostUnaryAssignmentExpression(self, ctx):
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
        dprint("visitTryStatement")
        try:
            ctx.children[1].accept(self) # code to run
        except ThrowException as e:
            msg = str(e)
            catchBlock = ctx.children[2]
            self.environment.defineVariable(catchBlock.children[2].accept(self), msg)
            catchBlock.accept(self) # catch
        
        # finally
        if ctx.getChildCount() == 4:
            finallyBlock = ctx.children[3]
            finallyBlock.accept(self)


    # Visit a parse tree produced by ECMAScriptParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)

    # Visit a parse tree produced by ECMAScriptParser#DoStatement.
    def visitDoStatement(self, ctx):
        # [0] = do, [1] = block, [2] = while, [3] = (, [4] = condition, [5] = )
        ctx.children[1].accept(self)
        while ctx.children[4].accept(self):
            ctx.children[1].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx):
        return ctx.children[0].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#arrayLiteral.
    def visitArrayLiteral(self, ctx):
        # The below structure creates an python array and we just return it upwards
        return ctx.children[1].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#elision.
    def visitElision(self, ctx):
        raise Utils.UnimplementedVisitorException(ctx)

    # Visit a parse tree produced by ECMAScriptParser#statements.
    def visitStatements(self, ctx):
        dprint("visitStatements")
        try:
            return self.visitChildren(ctx)
        except ReturnException as e:
            return e.value

    # Visit a parse tree produced by ECMAScriptParser#UnaryExpression.
    def visitUnaryExpression(self, ctx):
        if(ctx.children[0].symbol.type == 18): # -
            return -ctx.children[1].accept(self)
        if(ctx.children[0].symbol.type == 17): # +
            return ctx.children[1].accept(self)
        if(ctx.children[0].symbol.type == 19): # ~
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
        # print("VisitReturnStatement")
        # Return val ;
        returnVal = ctx.children[1].accept(self)
        raise ReturnException(returnVal)

    # Visit a parse tree produced by ECMAScriptParser#switchStatement.
    def visitSwitchStatement(self, ctx):
        variable = ctx.children[2].accept(self)
        ctx.children[4].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx):
        dprint("visitExpressionSequence")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#literal.
    def visitLiteral(self, ctx):
        child = ctx.children[0]
        if(isinstance(ctx.children[0], antlr4.tree.Tree.TerminalNodeImpl)):
            if(child.symbol.text == "true"):
                return True
            if(child.symbol.text == "false"):
                return False
            if(child.symbol.type == 101):
                tmp = child.symbol.text[1:-1]
                return tmp
            if(child.symbol.type == 53):
                return None
        return child.accept(self)


    # Visit a parse tree produced by ECMAScriptParser#variableStatement.
    def visitVariableStatement(self, ctx):
        # var a = 10; for example
        # ctx.children[0] is var
        # ctx.children[1] is a = 10
        # ctx.children[2] is ;
        dprint("VisitVariableStatement")
        return ctx.children[1].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx):
        dprint("visitFunctionExpression")
        isLambda = False
        
        if(isinstance(ctx.children[2], antlr4.tree.Tree.TerminalNodeImpl) and isinstance(ctx.children[3], antlr4.tree.Tree.TerminalNodeImpl)):
            # haz no parameters
            if ctx.getChildCount() == 7:
                # Normal function, so we have a name
                functionName = ctx.children[1].accept(self)
                params = []
                body =  ctx.children[5]
            elif ctx.getChildCount() == 6:
                # Lambda function, return function only
                # setup the function bits
                isLambda = True
                params =  []
                body =  ctx.children[4]
        
        else:
            if ctx.getChildCount() == 8:
                # Normal function, so we have a name
                functionName = ctx.children[1].accept(self)
                # setup the function bits
                params =  ctx.children[3].accept(self)
                body =  ctx.children[6]
            elif ctx.getChildCount() == 7:
                # Lambda function, return function only
                # setup the function bits
                isLambda = True
                params =  ctx.children[2].accept(self)
                body =  ctx.children[5]

        #always run this
        def runBodyFunction(env):
            origEnv = self.environment
            self.environment = env
            retVal = body.accept(self)
            self.environment = origEnv
            return retVal

        if isLambda:
            return Function(params, self.environment, runBodyFunction)
        else:
            self.environment.defineVariable(functionName, Function(params, self.environment, runBodyFunction))


    # Visit a parse tree produced by ECMAScriptParser#defaultClause.
    def visitDefaultClause(self, ctx):
        ctx.children[2].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#statement.
    def visitStatement(self, ctx):
        dprint("visitStatement")
        children = ctx.getChildren()
        if children is None:
            rjhjujyjuy #should crash here ;) thihi
        contexts = []
        for child in children:
            contexts.append(child)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForStatement.
    def visitForStatement(self, ctx):
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
        switchVar = ctx.parentCtx.children[2].accept(self)
        continueUntilBreak = False
        defaultCase = False
        try:
            for child in ctx.children:
                if(not isinstance(child, antlr4.tree.Tree.TerminalNodeImpl)): # Skip "{ and }"            
                    # when the syntax is "case 0: block" then [1] is the nr. if "default : block" then [1] is :
                    caseVal = child.children[1].accept(self)
                    if caseVal == ":": #Default
                        #There is a default case, save it in case we need it
                        defaultCase = child
                    else:
                        if caseVal == switchVar or continueUntilBreak: 
                            # we have found a matching case, now run everything unless we break out from here
                            continueUntilBreak = True
                            child.accept(self)

            # If we did not find a matching case and there was a default case, run that default case.
            if continueUntilBreak == False and not defaultCase == False:
                defaultCase.accept(self)

        except BreakException:
            pass
        


    # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx):
        # the syntax is: ( thing ), so do accept on the thing
        return ctx.children[1].accept(self)

    # Visit a parse tree produced by ECMAScriptParser#objectLiteral.
    def visitObjectLiteral(self, ctx):
        dprint("visitObjectLiteral")
        this = ObjectModule()
        prop = Property(this)

        for c in ctx.children:
            if(not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)): # Skip ", or { or }"
                pair = c.accept(self) 
                # pair format is: 
                #{"name": ctx.children[0].accept(self), "value": ctx.children[2].accept(self), "function" : False}

                if pair["function"]:
                    newObj = ObjectModule()
                    name = "get"
                    if pair["setter"]:
                        name = "set"
                    
                    #print("saving ", name, ", with value ", pair["value"], ", to ", newObj)
                    setattr(newObj, name, pair["value"])
                    #print("Now saving ", pair['name'], ", with value ", newObj, ", to ", this)
                    setattr(this, pair["name"], newObj)
                else:
                    #print("result: ", pair["name"], " value: ",  pair["value"])
                    if isinstance(pair["name"], str):
                        setattr(this, pair["name"], pair["value"])
                    else:
                        setattr(this, "int_"+str(int(pair["name"])), pair["value"])
        return this

    # Visit a parse tree produced by ECMAScriptParser#throwStatement.
    def visitThrowStatement(self, ctx):
        dprint("visitThrowStatement")
        msg = ctx.children[1].accept(self)
        # Any kind of exception that will (hopefully) be caught further up
        raise ThrowException(msg)

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
        dprint("visitVariableDeclaration")
        if (ctx.getChildCount() == 1):
            self.environment.defineVariable(ctx.children[0].symbol.text)
        else:
            # dont retun the value since JavaScript does not return in this case
            self.environment.defineVariable(ctx.children[0].symbol.text, ctx.children[1].accept(self))

    # Visit a parse tree produced by ECMAScriptParser#finallyProduction.
    def visitFinallyProduction(self, ctx):
        ctx.children[1].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx):
        dprint("visitIdentifierExpression")
        return self.environment.value(ctx.children[0].accept(self))


    # Visit a parse tree produced by ECMAScriptParser#propertyName.
    def visitPropertyName(self, ctx):
        dprint("visitPropertyName")
        return ctx.children[0].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#catchProduction.
    def visitCatchProduction(self, ctx):
        ctx.children[4].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#continueStatement.
    def visitContinueStatement(self, ctx):
        raise ContinueException()


    # Visit a parse tree produced by ECMAScriptParser#caseClause.
    def visitCaseClause(self, ctx):
        value = ctx.children[1].accept(self)
        ctx.children[3].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#arguments.
    def visitArguments(self, ctx):
        dprint("visitArguments")
        if ctx.getChildCount() == 2: # ( )
            return None
        else:
            return ctx.children[1].accept(self)


    # Visit a parse tree produced by ECMAScriptParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx):
        dprint("variableDeclarationList")
        # stuff like a = 10, b = 20
        for c in ctx.children:
            if(not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)): # Skip ","
                c.accept(self)

    # Visit a parse tree produced by ECMAScriptParser#functionBody.
    def visitFunctionBody(self, ctx):
        dprint("visitFunctionBody")
        tmp = ctx.children[0].accept(self)
        return tmp
        
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
