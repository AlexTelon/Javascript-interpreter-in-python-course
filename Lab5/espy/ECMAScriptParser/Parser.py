import antlr4
from ECMAScriptParser.ECMAScriptParser import ECMAScriptParser

class Parser(ECMAScriptParser):
  def __init__(self, input:antlr4.TokenStream):
    super().__init__(input)

  #
  # Returns {@code true} iff on the current index of the parser's
  # token stream a token of the given {@code type} exists on the
  # {@code HIDDEN} channel.
  #
  # @param type
  #         the type of the token on the {@code HIDDEN} channel
  #         to check.
  #
  # @return {@code true} iff on the current index of the parser's
  # token stream a token of the given {@code type} exists on the
  # {@code HIDDEN} channel.
  #
  def here(self, type):
    # Get the token ahead of the current index.
    possibleIndexEosToken = self.getCurrentToken().tokenIndex - 1;
    ahead = self._input.get(possibleIndexEosToken);
    
    # Check if the token resides on the HIDDEN channel and if it's of the provided type.
    return (ahead.channel == antlr4.Lexer.HIDDEN) and (ahead.type == type);
      
  #
  # Returns {@code true} iff on the current index of the parser's
  # token stream a token exists on the {@code HIDDEN} channel which
  # either is a line terminator, or is a multi line comment that
  # contains a line terminator.
  #
  # @return {@code true} iff on the current index of the parser's
  # token stream a token exists on the {@code HIDDEN} channel which
  # either is a line terminator, or is a multi line comment that
  # contains a line terminator.
  #
  def lineTerminatorAhead(self):

      # Get the token ahead of the current index.
      possibleIndexEosToken = self.getCurrentToken().tokenIndex - 1;
      ahead = self._input.get(possibleIndexEosToken);

      if (ahead.channel != antlr4.Lexer.HIDDEN):
          # We're only interested in tokens on the HIDDEN channel.
          return False;

      # Get the token's text and type.
      text = ahead.text;
      type = ahead.type;

      # Check if the token is, or contains a line terminator.
      return (type == self.MultiLineComment and (text.contains("\r") or text.contains("\n"))) or (type == self.LineTerminator);
