import antlr4
from ECMAScriptParser.ECMAScriptLexer import ECMAScriptLexer

class Lexer(ECMAScriptLexer):

  def __init__(self, input=None):
    super().__init__(input)

  # A flag indicating if the lexer should operate in strict mode.
  # When set to true, FutureReservedWords are tokenized, when false,
  # an octal literal can be tokenized.
  strictMode = True;

  # The most recently produced token.
  lastToken = None;

    
  # Returns {@code true} iff the lexer operates in strict mode.
  #
  # @return {@code true} iff the lexer operates in strict mode.
  #
  def getStrictMode(self):
    return self.strictMode;

    
  # Sets whether the lexer operates in strict mode or not.
  #
  # @param strictMode
  #         the flag indicating the lexer operates in strict mode or not.
  #
  def setStrictMode(self, strictMode):
    self.strictMode = strictMode;

  # Return the next token from the character stream and records this last
  # token in case it resides on the default channel. This recorded token
  # is used to determine when the lexer could possibly match a regex
  # literal.
  #
  # @return the next token from the character stream.
  #
  def nextToken(self):    
    # Get the next token.
    nextToken = super(Lexer, self).nextToken();
    
    if (nextToken.channel == antlr4.Token.DEFAULT_CHANNEL):
        # Keep track of the last token on the default channel.                                              
        self.lastToken = nextToken;
    
    return nextToken;

  # Returns {@code true} iff the lexer can match a regex literal.
  #
  # @return {@code true} iff the lexer can match a regex literal.
  #
  def isRegexPossible(self):
                                       
    if (self.lastToken == None):
      # No token has been produced yet: at the start of the input,
      # no division is possible, so a regex literal _is_ possible.
      return True;
    
    t = self.lastToken.type
    if(t ==  Lexer.Identifier
       or t == Lexer.NullLiteral
       or t == Lexer.BooleanLiteral
       or t == Lexer.This
       or t == Lexer.CloseBracket
       or t == Lexer.CloseParen
       or t == Lexer.OctalIntegerLiteral
       or t == Lexer.DecimalLiteral
       or t == Lexer.HexIntegerLiteral
       or t == Lexer.StringLiteral):
      # After any of the tokens above, no regex literal can follow.
      return False;
    else:
      # In all other cases, a regex literal _is_ possible.
      return True;
