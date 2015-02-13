# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from ECMAScriptParser.ECMAScriptVisitor import ECMAScriptVisitor
import Utils

# This class defines a complete generic visitor for a parse tree produced by ECMAScriptParser.

class PrintVisitor(ECMAScriptVisitor):

  indenting = ""
  
  def visitContext(self, ctx):
    Utils.prettyprint(ctx, self.indenting)
    previous_indenting = self.indenting
    self.indenting += " "
    self.visitChildren(ctx)
    self.indenting = previous_indenting
    
  def visitTerminal(self, node):
    Utils.prettyprint(node, self.indenting)


  # Visit a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
  def visitPropertyExpressionAssignment(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#getter.
  def visitGetter(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#assignmentOperator.
  def visitAssignmentOperator(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#eos.
  def visitEos(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#sourceElements.
  def visitSourceElements(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#program.
  def visitProgram(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#MemberDotAssignmentExpression.
  def visitMemberDotAssignmentExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#argumentList.
  def visitArgumentList(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ArgumentsExpression.
  def visitArgumentsExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ThisExpression.
  def visitThisExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#identifierName.
  def visitIdentifierName(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#BinaryExpression.
  def visitBinaryExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#futureReservedWord.
  def visitFutureReservedWord(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#initialiser.
  def visitInitialiser(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#statementList.
  def visitStatementList(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#PropertyGetter.
  def visitPropertyGetter(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#block.
  def visitBlock(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
  def visitExpressionStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#keyword.
  def visitKeyword(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#elementList.
  def visitElementList(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#numericLiteral.
  def visitNumericLiteral(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ForInStatement.
  def visitForInStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#emptyStatement.
  def visitEmptyStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#labelledStatement.
  def visitLabelledStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#PropertySetter.
  def visitPropertySetter(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#NewExpression.
  def visitNewExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
  def visitLiteralExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
  def visitArrayLiteralExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#MemberDotExpression.
  def visitMemberDotExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#withStatement.
  def visitWithStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#MemberIndexExpression.
  def visitMemberIndexExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#formalParameterList.
  def visitFormalParameterList(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#propertySetParameterList.
  def visitPropertySetParameterList(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
  def visitAssignmentOperatorExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#TernaryExpression.
  def visitTernaryExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#tryStatement.
  def visitTryStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#debuggerStatement.
  def visitDebuggerStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#DoStatement.
  def visitDoStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
  def visitObjectLiteralExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#arrayLiteral.
  def visitArrayLiteral(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#elision.
  def visitElision(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#UnaryExpression.
  def visitUnaryExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#WhileStatement.
  def visitWhileStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#returnStatement.
  def visitReturnStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#switchStatement.
  def visitSwitchStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#expressionSequence.
  def visitExpressionSequence(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#literal.
  def visitLiteral(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#variableStatement.
  def visitVariableStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#FunctionExpression.
  def visitFunctionExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#defaultClause.
  def visitDefaultClause(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#AssignmentExpression.
  def visitAssignmentExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#statement.
  def visitStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ForStatement.
  def visitForStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#caseBlock.
  def visitCaseBlock(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
  def visitParenthesizedExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#propertyNameAndValueList.
  def visitPropertyNameAndValueList(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#objectLiteral.
  def visitObjectLiteral(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#throwStatement.
  def visitThrowStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#sourceElement.
  def visitSourceElement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#breakStatement.
  def visitBreakStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#ifStatement.
  def visitIfStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#reservedWord.
  def visitReservedWord(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#variableDeclaration.
  def visitVariableDeclaration(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#finallyProduction.
  def visitFinallyProduction(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
  def visitIdentifierExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#PostUnaryExpression.
  def visitPostUnaryExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#propertyName.
  def visitPropertyName(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#MemberIndexAssignmentExpression.
  def visitMemberIndexAssignmentExpression(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#catchProduction.
  def visitCatchProduction(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#continueStatement.
  def visitContinueStatement(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#caseClause.
  def visitCaseClause(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#arguments.
  def visitArguments(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#variableDeclarationList.
  def visitVariableDeclarationList(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#functionBody.
  def visitFunctionBody(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#setter.
  def visitSetter(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#functionDeclaration.
  def visitFunctionDeclaration(self, ctx):
    self.visitContext(ctx)


  # Visit a parse tree produced by ECMAScriptParser#eof.
  def visitEof(self, ctx):
    self.visitContext(ctx)

